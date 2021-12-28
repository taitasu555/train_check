import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import os
from os.path import join, dirname



load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


# LINE Notifyと連携するためのtoken
line_notify_token = os.environ.get("LINE_NOTIFY") 
line_notify_api = 'https://notify-api.line.me/api/notify'  # LINE Notifyへの通知URL

# LINENotifyにメッセージを送付


def delay_information_send(message):
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    requests.post(line_notify_api, data=payload, headers=headers)

# スクレイピングして運行状況ページの抽出


def Extract_delay_information():
    url = 'https://transit.yahoo.co.jp/diainfo/46/46'
    r = requests.get(url)
    Soup = BeautifulSoup(r.text, 'html.parser')
    # .findでtroubleクラスのddタグを探す
    trouble_info = Soup.find('dd', class_='trouble')
    # 運行状況ページに'trouble'があるかで条件を分岐する
    if trouble_info:
        delay_information_send("\n" + "京浜東北線は" + trouble_info.text + "です。")
    else:
        pass


if __name__ == "__main__":
    Extract_delay_information()
