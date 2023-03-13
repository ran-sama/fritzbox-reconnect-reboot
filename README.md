# fritzbox-reconnect-reboot
Python 3 and bash based tool to login and perform web-interface commands.

## Why?
Because I was tired of my scripts breaking each FB update.

## Usage and operations
```
./fb_helper.py 10.0.0.1 username password reboot
./fb_helper.py 10.0.0.1 username password reconnect
```
I don't like the default IP and the limited DNS of the FB, so I refuse their fritz.box placebo. An own unbound recursive DNS resolver is superior in any regard.

## How do I find the default username?
```
http://10.0.0.1/login_sid.lua?version=1
http://10.0.0.1/login_sid.lua?version=2
```

## I need more commands!
Grab wireshark and record packages. Your mind is the limit.

## License
Licensed under the WTFPL license.
