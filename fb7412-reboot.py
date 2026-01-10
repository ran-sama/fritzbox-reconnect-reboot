#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib, requests, base64
import xml.etree.ElementTree as ET
from datetime import datetime

def main():
    # define your IP and credentials
    url = "http://10.0.0.4/login_sid.lua"
    username = ""
    password = "fox1234"

    # legacy MD5 SID request for FritzOS 6.xx
    r = requests.get(url)
    xml = ET.fromstring(r.content)
    challenge = xml.find("Challenge").text
    response = challenge + "-" + password

    # utf_16_le encoding is required
    response = response.encode("utf_16_le")
    md5_sum = hashlib.md5()
    md5_sum.update(response)
    challenge_response = challenge + "-" + md5_sum.hexdigest()
    post_data = {"username": username, "response": challenge_response}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(url, headers=headers, data=post_data)
    xml = ET.fromstring(r.content)
    sid = xml.find("SID").text
    print(sid)

    # wireshark magic and millisecond unix timestamp plus SID
    url1 = "http://10.0.0.4:80/data.lua"
    url2 = "http://10.0.0.4:80/data.lua"
    url3 = "http://10.0.0.4:80/reboot.lua?sid=" + sid + "&ajax=1&no_sidrenew=1&xhr=1&t" + str(int(datetime.utcnow().timestamp()*1e3)) + "=nocache"
    data1 = "xhr=1&sid=" + sid + "&reboot=1&lang=de&page=reboot"
    data2 = "xhr=1&sid=" + sid + "&page=rootReboot"
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    boxdata1 = requests.post(url=url1,data=data1,headers=headers).content.decode('utf-8')
    boxdata2 = requests.post(url=url2,data=data2,headers=headers).content.decode('utf-8')
    boxdata3 = requests.get(url3).content.decode('utf-8')
    print(boxdata1)
    print(boxdata2)
    print(boxdata3)

main()
