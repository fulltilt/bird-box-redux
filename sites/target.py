try:
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP
except:
    from Cryptodome.PublicKey import RSA
    from Cryptodome.Cipher import PKCS1_OAEP
from base64 import b64encode
from utils import send_webhook
import requests, time, lxml.html, json, sys, settings

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common import exceptions


class BestBuy:
    def __init__(
        self,
        task_id,
        status_signal,
        image_signal,
        product,
        profile,
        proxy,
        monitor_delay,
        error_delay,
    ):
        (
            self.status_signal,
            self.image_signal,
            self.product,
            self.profile,
            self.monitor_delay,
            self.error_delay,
        ) = (
            status_signal,
            image_signal,
            product,
            profile,
            float(monitor_delay),
            float(error_delay),
        )
        self.session = requests.Session()
        if proxy != False:
            self.session.proxies.update(proxy)
        self.status_signal.emit({"msg": "Starting", "status": "normal"})
        # self.product_image, offer_id = self.monitor()
        self.monitor()

    def monitor(self):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "cache-control": "no-cache",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.69 Safari/537.36",
        }
        image_found = False
        sproduct_image = ""
        try:
            r = self.session.get(self.product, headers=headers)
            print(r)
        except Exception as e:
            self.status_signal.emit(
                {
                    "msg": "Error Loading Product Page (line {} {} {})".format(
                        sys.exc_info()[-1].tb_lineno, type(e).__name__, e
                    ),
                    "status": "error",
                }
            )


      # https://www.target.com/p/airheads-assorted-mini-bars-14oz/-/A-50326050#lnk=sametab