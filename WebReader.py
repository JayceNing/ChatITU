import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import re

class ChromeDriver:
    def __init__(self):
        print('Initializing Chrome WebDriver...')
        # 设置 ChromeOptions 以便在无头模式下运行 Chrome 浏览器
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # 初始化 Chrome WebDriver
        # 创建 ChromeDriver 服务
        chrome_driver_path = "D:/anaconda3/envs/swin/chromedriver.exe"  # 将此路径替换为 ChromeDriver 的实际路径
        service = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)
        # self.driver = webdriver.Chrome(options=chrome_options)
        print('Chrome WebDriver initialized')

    def get_viewstate(self, url):
        # 使用 Selenium 打开浏览器
        self.driver.get(url)

        # 提取必要的字段值
        viewstate = self.driver.find_element(By.NAME, '__VIEWSTATE').get_attribute('value')
        print(viewstate)

        return viewstate

    def close(self):
        # 关闭浏览器
        self.driver.quit()

# def get_viewstate(url):
#     # 设置 ChromeOptions 以便在无头模式下运行 Chrome 浏览器
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")

#     # 初始化 Chrome WebDriver
#     #service = Service('/usr/bin/chromedriver')  # 确保 ChromeDriver 在这个路径下，或者使用实际路径
#     driver = webdriver.Chrome(options=chrome_options)

#     # 假设找到了正确的AJAX请求URL和必要的参数
#     #url = 'https://www.itu.int/ITU-T/workprog/wp_search.aspx?isn_sp=-1&isn_status=-1,8,1,3,7,2&title=AI&details=0&field=acdefghijo'

#     # 使用 Selenium 打开浏览器
#     #driver = webdriver.Chrome()
#     driver.get(url)

#     # 提取必要的字段值
#     viewstate = driver.find_element(By.NAME, '__VIEWSTATE').get_attribute('value')
#     #eventvalidation = driver.find_element(By.NAME, '__EVENTVALIDATION').get_attribute('value')
#     print(viewstate)

#     # 关闭浏览器
#     driver.quit()
#     return viewstate

def post_request(url, data):

    # 假设这是你的会话和Cookies信息
    session = requests.Session()
    # 假设你已经通过某种方式（如登录）获取了这些Cookies
    #session.cookies.set('cookie_name', 'cookie_value')

    # 假设找到了正确的AJAX请求URL和必要的参数
    # url = 'https://www.itu.int/ITU-T/workprog/wp_search.aspx?isn_sp=-1&isn_status=-1,8,1,3,7,2&title=AI&details=0&field=acdefghijo'
    # 构造POST请求参数
    
    # 构造请求头信息
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        #'Cookie': 
        'Host': 'www.itu.int',
        'Origin': 'https://www.itu.int',
        'Referer': 'https://www.itu.int/ITU-T/workprog/wp_search.aspx?isn_sp=-1&isn_status=-1,8,1,3,7,2&title=AI&details=0&field=acdefghijo',
        'Sec-Ch-Ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
        'X-Microsoftajax': 'Delta=true',
        'X-Requested-With': 'XMLHttpRequest'
    }

    # 发送POST请求，模拟AJAX请求
    response = session.post(url, headers=headers, data=data)

    return response

def get_work_item_list(chrome_driver, key_words):
    url = f'https://www.itu.int/ITU-T/workprog/wp_search.aspx?isn_sp=-1&isn_status=-1,8,1,3,7,2&title={key_words}&details=0&field=acdefghijo'
    # 获取ViewState
    viewstate = chrome_driver.get_viewstate(url)

    data = {
        'ctl00$ContentPlaceHolder1$ScriptManager': 'ctl00$ContentPlaceHolder1$TabContainer1$tab_list_view$update_panel_list_view|ctl00$ContentPlaceHolder1$TabContainer1$tab_list_view$gd_wp',
        'ctl00_ContentPlaceHolder1_TabContainer1_ClientState': '{"ActiveTabIndex":0,"TabEnabledState":[true,true,true],"TabWasLoadedOnceState":[true,false,false]}',
        'ctl00$ContentPlaceHolder1$hidden_page_title': 'ITU-T WP',
        'ctl00$ContentPlaceHolder1$ddl_study_period': '-1',
        'ctl00$ContentPlaceHolder1$ddl_gsi': '-1',
        'ctl00$ContentPlaceHolder1$chk_lst_status$0': 'on',
        'ctl00$ContentPlaceHolder1$chk_lst_status$1': 'on',
        'ctl00$ContentPlaceHolder1$chk_lst_status$2': 'on',
        'ctl00$ContentPlaceHolder1$chk_lst_status$3': 'on',
        'ctl00$ContentPlaceHolder1$chk_lst_status$4': 'on',
        'ctl00$ContentPlaceHolder1$ddl_registered': '0',
        'ctl00$ContentPlaceHolder1$txt_consent_date_from': '',
        'ctl00$ContentPlaceHolder1$txt_consent_date_to': '',
        'ctl00$ContentPlaceHolder1$txt_approval_date_from': '',
        'ctl00$ContentPlaceHolder1$txt_approval_date_to': '',
        'ctl00$ContentPlaceHolder1$txt_acronym': '',
        'ctl00$ContentPlaceHolder1$txt_title': 'ds',
        'ctl00$ContentPlaceHolder1$txt_summary': '',
        'ctl00$ContentPlaceHolder1$txt_base_text': '',
        'ctl00$ContentPlaceHolder1$txt_editor': '',
        'ctl00$ContentPlaceHolder1$ddl_page_size': '100',
        'ctl00$ContentPlaceHolder1$hidden_active_page_index': '0',
        'ctl00$ContentPlaceHolder1$TabContainer1$tab_customized_view$hidden_field_displayed': 'acdefghijo',
        'ctl00$ContentPlaceHolder1$TabContainer1$tab_customized_view$hidlstCustomSel': '',
        '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$TabContainer1$tab_list_view$gd_wp',
        '__EVENTARGUMENT': 'Page$1',
        '__LASTFOCUS': '',
        '__VIEWSTATE': viewstate,
        '__VIEWSTATEGENERATOR': '12B937D7',
        '__ASYNCPOST': 'true'
    }

    response = post_request(url, data)
    def has_isn_in_href(tag):
        return tag.has_attr('href') and 'http://www.itu.int/itu-t/workprog/wp_item.aspx?isn=' in tag['href']

    # 检查请求是否成功
    if response.status_code == 200:
        print(response)
        print(response.text)
        # 使用BeautifulSoup解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')

        a_tags = soup.find_all(has_isn_in_href)
        print(len(a_tags))
        # 正则表达式匹配<a>标签中的href属性和文本内容
        pattern = r'<a href="([^"]+)"[^>]*>([^<]+)</a>'
        urls = []
        work_items = []
        questions = []
        titles = []
        timings = []
        study_groups = []
        study_periods = []


        for tag in a_tags:
            print(tag)  # <a href="http://www.itu.int/itu-t/workprog/wp_item.aspx?isn=4053" title="See more details">E.161</a>
            # 使用search方法查找匹配项
            match = re.search(pattern, str(tag))
            url, text = match.groups()  # 提取匹配的URL和文本
            urls.append(url)
            # texts.append(text)

        
        # 查找 id 包含 'ctl00_ContentPlaceHolder1_TabContainer1_tab_list_view_gd_wp_ct' 的所有 <span> 标签
        spans = soup.find_all('span', id=lambda x: x and 'ctl00_ContentPlaceHolder1_TabContainer1_tab_list_view_gd_wp_ct' in x)
        print(len(spans))

        # 每 6 个元素为一组进行处理
        for i in range(0, len(spans), 6):
            group = spans[i:i+6]
            work_items.append(group[0].get_text(strip=True))
            questions.append(group[1].get_text(strip=True))
            titles.append(group[2].get_text(strip=True))
            timings.append(group[3].get_text(strip=True))
            study_groups.append(group[4].get_text(strip=True))
            study_periods.append(group[5].get_text(strip=True))

        return urls, work_items, questions, titles, timings, study_groups, study_periods

    else:
        print(response)
        print('Failed to retrieve the page')

def read_programme_page(url):
    # 发送HTTP GET请求
    response = requests.get(url)
    # 确保请求成功
    if response.status_code == 200:
        # 使用BeautifulSoup解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')
        #print(response.text)

        ##############################################
        # 提取年份和工作组的信息
        path_info = soup.find('span', id='ctl00_ContentPlaceHolder1_rpt_main_ctl00_lbl_full_path').get_text()

        associated_work_info = ''
        # 提取patent和associated work信息
        patent_info = soup.find('span', id='ctl00_ContentPlaceHolder1_rpt_main_ctl00_lbl_ipr').get_text()
        try:
            associated_work_info = soup.find('span', id='ctl00_ContentPlaceHolder1_rpt_main_ctl00_lbl_related_work').find('a').get_text()
        except AttributeError:
            pass

        # 提取Publication信息
        publication_span = soup.find('span', id='ctl00_ContentPlaceHolder1_rpt_main_ctl00_Label2')
        publication_text = publication_span.get_text(strip=True)
        if len(publication_text) > 0:
            publication_link = publication_span.find('a')['href']
            print(f'{publication_text} ({publication_link})')

        # 输出提取的信息
        print(path_info.strip())
        print(f'[{patent_info.strip()}] - [{associated_work_info.strip()}]')
        ##############################################
        # 提取各个字段的信息
        data = {
            "year_group_question": path_info.strip() if len(path_info.strip()) > 0 else '',
            "publication_link": publication_link if len(publication_text) > 0 else '',
            "Work_item": soup.find('span', id='ctl00_ContentPlaceHolder1_rpt_main_ctl00_lbl_status').get_text(strip=True),
            "Subject_title": soup.find('span', id='ctl00_ContentPlaceHolder1_rpt_main_ctl00_lbl_subject').get_text(strip=True),
            "Status": soup.find('span', id='ctl00_ContentPlaceHolder1_rpt_main_ctl00_Label4').get_text(strip=True),
            "Approval_process": soup.find('span', id='ctl00_ContentPlaceHolder1_rpt_main_ctl00_lbl_approval_process').get_text(strip=True),
            "Type_of_work_item": soup.find('span', id='ctl00_ContentPlaceHolder1_rpt_main_ctl00_lbl_type_of_work_item').get_text(strip=True),
            "Version": soup.find('span', id='ctl00_ContentPlaceHolder1_rpt_main_ctl00_Label1').get_text(strip=True),
            "Equivalent_number": soup.find('span', id='ctl00_ContentPlaceHolder1_rpt_main_ctl00_lbl_iso_number').get_text(strip=True),
            "Timing": soup.find('span', id='ctl00_ContentPlaceHolder1_rpt_main_ctl00_lbl_timing').get_text(strip=True),
            "Liaison": soup.find('span', id='ctl00_ContentPlaceHolder1_rpt_main_ctl00_Label3').get_text(strip=True),
            "Supporting_members": soup.find('span', id='ctl00_ContentPlaceHolder1_rpt_main_ctl00_Label6').get_text(strip=True),
            "Summary": soup.find('span', id='ctl00_ContentPlaceHolder1_rpt_main_ctl00_lbl_summary').get_text(strip=True),
            "Comment": soup.find('span', id='ctl00_ContentPlaceHolder1_rpt_main_ctl00_lbl_comment').get_text(strip=True),
            "References": [ref.get_text(strip=True) for ref in soup.find_all('span', id=lambda x: x and x.startswith('ctl00_ContentPlaceHolder1_rpt_main_ctl00_gd_base_text_active'))],
            "References_link": [ref.find('a')['href'] if ref.find('a') else '' for ref in soup.find_all('span', id=lambda x: x and x.startswith('ctl00_ContentPlaceHolder1_rpt_main_ctl00_gd_base_text_active'))],
            "Contact(s)": [contact.get_text(strip=True) for contact in soup.find_all('span', id=lambda x: x and x.startswith('ctl00_ContentPlaceHolder1_rpt_main_ctl00_gd_editor'))],
            "First_registration_in_the_WP": soup.find('span', id='ctl00_ContentPlaceHolder1_rpt_main_ctl00_lbl_first_registration_date').get_text(strip=True),
            "Last_update": soup.find('span', id='ctl00_ContentPlaceHolder1_rpt_main_ctl00_Label5').get_text(strip=True),
        }

        # 输出提取的信息
        for key, value in data.items():
            print(f'{key}: {value}')

        return data

        
    else:
        print(f'Failed to retrieve the webpage. Status code: {response.status_code}')