# -*- coding: utf-8 -*-
import requests
import re


def get_fund(code):
    url = "http://hq.sinajs.cn/list=%s" % code
    res = requests.get(url).text
    str_com = re.compile(r'\"(.*)\"')
    result = str_com.findall(res)[0].split(',')
    yesterday_closing = float(result[2])
    now = float(result[3])
    # 根据现价和昨日收盘价格判断
    closing_diff = round(now - yesterday_closing, 2)
    closing_diff_percent = round(closing_diff / yesterday_closing * 100, 2)
    color = '#ff0000' if closing_diff > 0 else '#006d21'
    content = f'现价：{round(now, 2)}，幅度：<font color={color}>{closing_diff_percent}%</font>，'
    if closing_diff_percent <= -1:
        if 3600 > now > 3400:
            multiple = '单倍'
        elif 3400 > now > 3200:
            multiple = '双倍'
        else:
            multiple = '三倍'
        content += f'{multiple}定投'
    return content

