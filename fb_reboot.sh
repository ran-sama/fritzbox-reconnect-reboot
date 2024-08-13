#!/usr/bin/env sh
MYSID=$1
myboxurl="http://10.0.0.1:80"
curl --insecure -s -X POST -d "xhr=1&sid=$MYSID&reboot=1&lang=de&page=reboot" "$myboxurl/data.lua"
curl --insecure -s -X POST -d "xhr=1&sid=$MYSID&page=rootReboot" "$myboxurl/data.lua"
curl --insecure -s -X POST -d "ajax=1&sid=$MYSID&no_sidrenew=1&xhr=1&useajax=1" "$myboxurl/reboot.lua"
exit 0
