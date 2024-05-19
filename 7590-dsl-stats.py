#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib, requests, json
import xml.etree.ElementTree as ET
from datetime import datetime

def main():
    # define your IP and credentials
    url = "http://10.0.0.1/login_sid.lua?version=2"
    username = "fritz1234"
    password = "fox789"

    r = requests.get(url)
    xml = ET.fromstring(r.content)
    challenge = xml.find("Challenge").text
    challenge_parts = challenge.split("$")
    iter1 = int(challenge_parts[1])
    salt1 = bytes.fromhex(challenge_parts[2])
    iter2 = int(challenge_parts[3])
    salt2 = bytes.fromhex(challenge_parts[4])
    hash1 = hashlib.pbkdf2_hmac("sha256", password.encode(), salt1, iter1)
    hash2 = hashlib.pbkdf2_hmac("sha256", hash1, salt2, iter2)
    challenge_response = "{}${}".format(challenge_parts[4], hash2.hex())
    post_data = {"username": username, "response": challenge_response}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(url, headers=headers, data=post_data)
    xml = ET.fromstring(r.content) 
    sid = xml.find("SID").text
    print(sid)

    # wireshark magic plus SID
    url1 = "http://10.0.0.1:80/data.lua"
    data1 = "xhr=1&sid=" + sid + "&lang=de&page=dslStat&xhrId=refresh&useajax=1&no_sidrenew="
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    boxdata1 = requests.post(url=url1,data=data1,headers=headers).content.decode('utf-8')
    json_data = json.loads(boxdata1)
    json_data = json.dumps(json_data, indent=4)
    print(json_data)

main()
