# ding_robot

钉钉群聊自定义机器人

功能

1. 提醒喝水, 天气
2. 提醒抢茅台



配置

1. 安装Python3

2. `pip install -r requirements.txt`

3. 添加钉钉群聊机器人

4. 配置config.ini
   - access_token = 群聊机器人Webhook中URL中的access_token参数
   - secret = 群聊机器人安全设置为加签产生的密钥
   - log_path = 日志文件名, 默认为send.log
   - key = 和风天气应用key
   - location = 和风天气区域代码, 默认为北京朝阳, 即101010300
   - expression = 消息中的颜文字, 默认为ฅ’ω’ฅ
   
5. 配置定时任务(Linux)

   终端输入`crontab -e`  输入下面内容

   ```
   # ding_robot drink 工作日10点-12点,14点-19点执行喝水天气提醒
   0 10-12,14-19 * * 1-5 /opt/allenv/ding_robot/bin/python /opt/ding_robot/drink.py
   
   # ding_robot maotai 每天晚上19:57 执行茅台提醒
   57 19 * * * /opt/allenv/ding_robot/bin/python /opt/ding_robot/maotai.py
   ```

   


