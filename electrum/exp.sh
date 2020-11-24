# init
sh stop.sh
sh clean.sh
mkdir res

# loops
for n in `seq 1 1 100`; do
        echo \#$n
        sh run.sh
        sleep 180.
        mv download_verify.txt ./res/$n
        sh stop.sh
        sh clean.sh
done