# init
sh stop.sh
sh clean.sh
mkdir res

# loops
for n in `seq 1 1 100`; do
        echo \#$n

        # sh run.sh
        ./run_electrum daemon -d
        sleep 10.
        ./run_electrum getinfo

        sleep 300.

        # sh stop.sh
        ./run_electrum getinfo
        ./run_electrum stop
        sleep 10.

        mv download_verify.txt ./res/$n

        # sh clean.sh
        rm -rf ~/.electrum
        rm -f download_verify.txt
        sleep 10.
done