import os


def median(A: list):
    len_ = len(A)
    if len_ % 2 == 0:
        tmp_A = sorted(A)
        return (tmp_A[len_ // 2 - 1] + tmp_A[len_ // 2]) / 2
    else:
        return sorted(A)[len_ // 2]


def ninety_nine(A: list):
    len_ = len(A)
    return sorted(A)[int(len_ * 0.99)]


if __name__ == "__main__":
    """hyperparams"""
    remove_first_N = 0

    network_timess, verify_timess = [], []
    per_server = dict()

    """read files"""
    BASE_PATH = './res'
    files = os.listdir(BASE_PATH)
    for file_ in files:
        
        N = remove_first_N

        network_times, verify_times = [], []
        # block height | download headers | verify headers | where
        with open(BASE_PATH + '/' + file_, 'r') as f:
            lines = f.readlines()
            for line in lines:

                if N != 0:
                    N -= 1
                    continue

                _, network_time, verify_time, server = line.split()

                network_times.append(float(network_time))
                verify_times.append(float(verify_time))
                
                if server in per_server:
                    per_server[server].append((network_time, verify_time))
                else:
                    per_server[server] = [(network_time, verify_time)]
        
        network_timess.append(network_times)
        verify_timess.append(verify_times)

    # from pprint import pprint
    # pprint(per_server)
    # print(len(per_server.items()))
    # exit()

    """print"""
    network_times, verify_times = sum(network_timess, []), sum(verify_timess, [])

    # Avg.
    print("=========================")
    print("Avg\tnetwork_time\t: ", end='')
    print(sum(network_times) / len(network_times))
    print("Avg\tverify_time\t: ", end='')
    print(sum(verify_times) / len(verify_times))
    print("Avg\ttot_spent_time\t: ", end='')
    print((sum(network_times) + sum(verify_times)) / len(network_times))

    # Median
    print("=========================")
    print("Med\tnetwork_time\t: ", end='')
    print(median(network_times))
    print("Med\tverify_time\t: ", end='')
    print(median(verify_times))
    print("Med\ttot_spent_time\t: ", end='')
    print(median(network_times) + median(verify_times))

    # Min
    print("=========================")
    print("Min\tnetwork_time\t: ", end='')
    print(min(network_times))
    print("Min\tverify_time\t: ", end='')
    print(min(verify_times))
    print("Min\ttot_spent_time\t: ", end='')
    print(min(network_times) + min(verify_times))

    # Max
    print("=========================")
    print("Max\tnetwork_time\t: ", end='')
    print(max(network_times))
    print("Max\tverify_time\t: ", end='')
    print(max(verify_times))
    print("Max\ttot_spent_time\t: ", end='')
    print(max(network_times) + max(verify_times))

    # 99%
    print("=========================")
    print("99%\tnetwork_time\t: ", end='')
    print(ninety_nine(network_times))
    print("99%\tverify_time\t: ", end='')
    print(ninety_nine(verify_times))
    print("99%\ttot_spent_time\t: ", end='')
    print(ninety_nine(network_times) + ninety_nine(verify_times))

    print("=========================")
