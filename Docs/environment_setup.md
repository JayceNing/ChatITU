# Environment Setup
This is the tutorial for environment setup on Ubuntu system.
## Python Environment
```bash
pip install -r requirements.txt
```
## Google Chrome
### Install Chrome
Install Chrome.
```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
```
Check Chrome version.
```bash
google-chrome --version
# Google Chrome 128.0.6613.84
```
Install Chrome Driver.
```bash
# Make sure Driver's version matches Chrome version
# This link is not available.
# wget https://chromedriver.storage.googleapis.com/128.0.6613.84/chromedriver_linux64.zip
# The latest version
wget https://storage.googleapis.com/chrome-for-testing-public/128.0.6613.84/linux64/chromedriver-linux64.zip
unzip chromedriver-linux64.zip
sudo mv -f chromedriver-linux64/chromedriver /usr/local/share/chromedriver 
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver 
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```
Check Chrome Driver version.
```bash
chromedriver --version
```

**Note:** Make sure the path of Chrome Drive is correct in ```../WebReader.py``` line 19. If you configurate Chrome following above toturial, you don't have to make any change.

## VUE
Install packages.
```bash
cd ./vue
npm install
```
Start service.
```bash
npm run dev
```