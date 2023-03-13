#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, hashlib, requests, subprocess
import xml.etree.ElementTree as ET

def main():
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} IP username password")
        exit(1)
    url = "http://" + sys.argv[1] + "/login_sid.lua?version=2"
    user = sys.argv[2]
    pwd = sys.argv[3]
    my_task = sys.argv[4]
    get_xml = requests.get(url).content
    clean_xml = ET.fromstring(get_xml)
    challenge = clean_xml.find("Challenge").text
    tokens = challenge.split("$")
    iterations_1 = int(tokens[1])
    salt_1 = bytes.fromhex(tokens[2])
    iterations_2 = int(tokens[3])
    salt_2 = bytes.fromhex(tokens[4])
    hash_1 = hashlib.pbkdf2_hmac("sha256", pwd.encode(), salt_1, iterations_1)
    hash_2 = hashlib.pbkdf2_hmac("sha256", hash_1, salt_2, iterations_2)
    response = f"{tokens[4]}${hash_2.hex()}"
    data = {"username": user, "response": response}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    auth_response = requests.post(url,data,headers).content
    get_xml = ET.fromstring(auth_response)
    sid = get_xml.find("SID").text
    print(sid)
    print(my_task + " starting")
    if my_task == "reboot":
        output = subprocess.call(["bash","/home/ran/fb_reboot.sh",sid])
    elif my_task == "reconnect":
        output = subprocess.call(["bash","/home/ran/fb_reconnect.sh",sid])
    else:
        print("unknown command " + my_task + ", use reboot or reconnect")
        exit(1)
    print(output)

if __name__ == "__main__":
    main()
