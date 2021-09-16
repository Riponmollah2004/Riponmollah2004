#!/user/bin/bash
#Author : Mohammad Ripon
done_login(){
clear
printf "\033[0;92m"
figlet "REALME"
printf "\033[0m"
cd /sdcard/
}
login_system(){
trap ' ' 2 15 20
clear
printf "\033[0;92m"
figlet "REALME"
read -p "`printf \"\033[0;96m ~ \033[0;97m\$ Enter Password: \"`" passw
if [ "$passw" = "772233" ]
then
    touch "$PREFIX/tmp/login"
    done_login
else
    login_system
fi
trap - 2 15 20
}

FILE="$PREFIX/tmp/login"
if [ -f "$FILE" ]; then
    done_login
else
    login_system
fi
