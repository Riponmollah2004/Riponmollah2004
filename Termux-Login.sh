#!/user/bin/bash
#Author : Mohammad Ripon
setup_system(){
	trap ' ' 2 15 20
	clear
	printf "\033[0;92m"
	figlet "`cat $PREFIX/bin/owner.db`"
	read -p "`printf \"\033[0;96m ~ \033[0;97m\$ Setup Security Name: \"`"  name
	read -p "`printf \"\033[0;96m ~ \033[0;97m\$ Setup Password: \"`"  password
	echo "$name">$PREFIX/bin/owner.db
	echo "$password">$PREFIX/bin/passw.db
	clear
	login_system
	trap - 2 15 20
}
done_login(){
clear
printf "\033[0;92m"
figlet "`cat $PREFIX/bin/owner.db`"
printf "\033[0m"
cd /sdcard/
}
login_system(){
trap ' ' 2 15 20
clear
printf "\033[0;92m"
figlet "`cat $PREFIX/bin/owner.db`"
read -p "`printf \"\033[0;96m ~ \033[0;97m\$ Enter Password: \"`" passw
if [ "$passw" = "`cat $PREFIX/bin/passw.db`" ]
then
    touch "$PREFIX/tmp/login"
    done_login
else
    login_system
fi
trap - 2 15 20
}
FILE="$PREFIX/bin/owner.db"
if [ -f "$FILE" ]; then
    clear
else
    setup_system
fi

FILE="$PREFIX/tmp/login"
if [ -f "$FILE" ]; then
    done_login
else
    login_system
fi
