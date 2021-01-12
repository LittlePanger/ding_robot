# -*- coding: utf-8 -*-
import requests
import json
import time

from logger import logging
from config import global_config


def get_weather():
    url = "https://devapi.heweather.net/v7/weather/24h"
    key = global_config.get('config', 'key')
    location = global_config.get('config', 'location')

    # 失败重试5次
    count = 0
    while count < 5:
        try:
            count += 1
            result = requests.get(url=url, params={'location': location, 'key': key}, timeout=(3, 1))
            if result:
                return get_result(result)
        except Exception as e:
            logging.error(f'retry,{count}, {e}')
            time.sleep(1)


def get_result(result):
    result = json.loads(result.text)["hourly"][0]
    logging.info(result)
    if float(result['precip']) > 0:
        precip = float(result['precip'])
        if precip < 10:
            precip_text = '小雨'
        elif precip < 25:
            precip_text = '中雨'
        elif precip < 50:
            precip_text = '大雨'
        elif precip < 100:
            precip_text = '暴雨'
        elif precip < 250:
            precip_text = '大暴雨'
        else:
            precip_text = '特大暴雨'
        result['precip_text'] = precip_text
    return result
