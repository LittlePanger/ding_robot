# -*- coding: utf-8 -*-
import logging
from config import global_config

# 日志配置
logging.basicConfig(level=logging.DEBUG,
                    filename=global_config.get('config', 'log_path'),
                    filemode='a',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
