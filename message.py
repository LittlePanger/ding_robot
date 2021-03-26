# -*- coding: utf-8 -*-
import requests
import json
from sign import build_sign
from config import global_config
from weather import get_weather
from fund import get_fund

class Msg:
    def __init__(self):
        # 钉钉url
        self._access_token = global_config.get('config', 'access_token')
        self._timestamp, self._sign = build_sign()
        self.url = 'https://oapi.dingtalk.com/robot/send?access_token=%s&timestamp=%s&sign=%s' % (
            self._access_token, self._timestamp, self._sign)
        self.headers = {"Content-Type": "application/json ;charset=utf-8"}
        self.expression = global_config.get('config', 'expression')
        self.content = ""

    def send_msg(self):
        msg = {
            "msgtype": "text",
            "text": {
                "content": self.content
            }
        }
        msg_json = json.dumps(msg)
        requests.post(url=self.url, data=msg_json, headers=self.headers)

    def send_markdown(self, title, use_img=False):
        if use_img:
            img = global_config.get('config', 'img')
            if img:
                self.content += "\n![](%s)" % img
        msg = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": self.content
            }
        }
        msg_json = json.dumps(msg)
        requests.post(url=self.url, data=msg_json, headers=self.headers)

    def drink(self):
        self.content += f"#### 喝口水吧 {self.expression}\n"

    def weather(self):
        weather = get_weather()
        if weather:
            self.content += f"""
> 未来一小时 {weather['text']}\n
> {weather['windDir']} {weather['windScale']}级\n
> 降水概率: {weather['pop']}%\n
"""
            if weather.get('precip_text'):
                self.content += f"> 降雨量{weather['precip']} {weather['precip_text']}\n"

    def mao_tai(self):
        self.content += f"距离抢购茅台还有3分钟 {self.expression}"

    def buy_fund(self, code):
        self.content += get_fund(code)
