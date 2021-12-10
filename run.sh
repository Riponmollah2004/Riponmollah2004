file="$1";
cp "$file" "$HOME/$file"
path=`pwd`;
cd ~
gcc "$file" -o .temp.c
rm -rf "$file"
./.temp.c
cd "$path"
