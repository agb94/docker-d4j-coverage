# usage: ./extract.sh <pid>
pid=$1
cat $pid.tar.bz2* | tar -xjvf -
rm $pid.tar.bz2*
