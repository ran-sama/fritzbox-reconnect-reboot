#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, hashlib, requests, subprocess
import xml.etree.ElementTree as ET

def main():
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} IP username password task")
        exit(1)
    url = "http://" + sys.argv[1] + "/login_sid.lua?version=2"
    username = sys.argv[2]
    password = sys.argv[3]
    my_task = sys.argv[4]
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
