import uvicorn
from fastapi import Body, FastAPI, WebSocket, WebSocketDisconnect, Response
from fastapi.middleware.cors import CORSMiddleware

from WebReader import get_work_item_list, read_programme_page, ChromeDriver
from LLM import SparkApi, SparkWS

import pandas as pd
import io
from typing import List

chrome_driver = ChromeDriver()

def get_work_item_list_api(
        key_words: str = Body(..., description="", example=""),
        x: str = Body(None, description="", example="")
    ):
    urls, work_items, questions, titles, timings, study_groups, study_periods = get_work_item_list(chrome_driver, key_words)
    return {"urls": urls, "work_items": work_items, "questions": questions, "titles": titles, "timings": timings, "study_groups": study_groups, "study_periods": study_periods}

def read_programme_page_api(
        url: str = Body(..., description="", example=""),
        x: str = Body(None, description="", example="")
    ):
    print(url)
    if url is None:
        url = 'https://www.itu.int/itu-t/workprog/wp_item.aspx?isn=4053'
    return {"data": read_programme_page(url)}

def create_excel(url_list):
    data_list = []
    for url in url_list:
        data = read_programme_page(url)
        data_list.append(data)
    df = pd.DataFrame(data_list)
    excel_buffer = io.BytesIO()
    df.to_excel(excel_buffer, index=False)
    excel_buffer.seek(0)
    return excel_buffer

async def download_excel(
    urls: List[str] = Body(..., description="", example=""),
    x: str = Body(None, description="", example="")
):
    excel_buffer = create_excel(urls)
    headers = {'Content-Disposition': 'attachment; filename=data.xlsx'}
    return Response(content=excel_buffer.read(), headers=headers, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

async def chat_spark_ws(websocket: WebSocket):
    await websocket.accept()
    query = websocket.query_params.get("query")
    SparkApi.websocket_clients.append(websocket)  # 使用append而不是直接赋值

    try:
        while True:
            question = [{'role': 'user', 'content': query}]
            await SparkApi.main(SparkWS.appid, SparkWS.api_key, SparkWS.api_secret, SparkWS.Spark_url, SparkWS.domain, question)
            await asyncio.sleep(1)  # 模拟等待时间或其他逻辑
    except WebSocketDisconnect:
        print("WebSocket disconnected")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await websocket.close()
        SparkApi.websocket_clients.remove(websocket)  # 确保从客户端列表中移除



if __name__ == '__main__':

    app = FastAPI()
    app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
    )
    app.post("/v1/get_work_item_list", response_model="")(get_work_item_list_api)
    app.post("/v1/read_programme_page", response_model="")(read_programme_page_api)
    app.post("/v1/download_excel", response_model="")(download_excel)

    # LLM
    app.websocket("/ws")(SparkWS.websocket_endpoint)
    app.websocket("/ws/chat_spark")(chat_spark_ws)

    uvicorn.run(app, host="0.0.0.0", port=8008)