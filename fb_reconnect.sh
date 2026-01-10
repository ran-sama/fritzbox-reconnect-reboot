#!/usr/bin/env sh
MYSID=$1
myboxurl="http://10.0.0.1:80"
curl https://ipv4.icanhazip.com/
curl --insecure -s -X POST -d "xhr=1&sid=$MYSID&lang=de&page=netMoni&xhrId=reconnect&disconnect=true&useajax=1&nosidrenew=" "$myboxurl/data.lua"
sleep 12
curl https://ipv4.icanhazip.com/
exit 0
