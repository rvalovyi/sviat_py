#!/bin/sh

ssh pi@raspberry "sudo pkill python3"
#ssh raspberry "ps -ef | grep 'sudo python3 /home/pi/Adeept_AWR/sviat/$1' | grep root | awk '{print $2}' | xargs sudo kill"
