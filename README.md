# fritzbox-reconnect-reboot
Python 3 and bash based tool to login and perform web-interface commands. Tested on 7590 (v7.57) and 7412 (v06.88) supporting the two methods of SID generation and different reboot commands.

## Why?
Because I was tired of my scripts breaking each FB update. I wish they would stop making their interface less power user friendly already.

## Usage and operations
```
./fb_helper.py 10.0.0.1 username password reboot
./fb_helper.py 10.0.0.1 username password reconnect
```
I don't like the default IP and the limited DNS of the FB, so I refuse their fritz.box placebo. An own unbound recursive DNS resolver is superior in any regard. Also the usage of urllib over requests in the reference implementation was atrocious.

## How do I find the default username?
```
http://10.0.0.1/login_sid.lua?version=1
http://10.0.0.1/login_sid.lua?version=2
```

## I need more commands!
Grab wireshark and record packages. Your mind is the limit.

## Docs  
https://avm.de/fileadmin/user_upload/Global/Service/Schnittstellen/AVM%20Technical%20Note%20-%20Session%20ID_englisch.pdf  

## License
Licensed under the WTFPL license.
