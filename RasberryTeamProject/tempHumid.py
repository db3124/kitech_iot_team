import logging
import datetime
import time

import Adafruit_DHT
#############################################################
# 온습도 센서 감지 log 남기기
date = str(datetime.date.today())

logger = logging.getLogger('temperaturelog')
hand = logging.FileHandler('tempHumid-'+date+'.log')


#                              생성시간,   로그레벨 ,       프로세스ID,   메시지
formatter = logging.Formatter('%(asctime)s %(levelname)s %(process)d %(message)s')

# 파일핸들러에 문자열 포메터를 등록
hand.setFormatter(formatter)

logger.addHandler(hand)

logger.setLevel(logging.INFO)

# 온습도 가져오기
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    
    if humidity is not None and temperature is not None:

        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        logger.info("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))

    else:
        print("Sensor failure. Check wiring.")

    time.sleep(3)