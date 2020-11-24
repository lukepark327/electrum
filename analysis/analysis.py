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
    remove_first_N = 1

    network_times, verify_times = [], []

    """block height | download headers | verify headers | where"""
    with open('download_verify.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if remove_first_N != 0:
                remove_first_N -= 1
                continue

            _, network_time, verify_time, _ = line.split()

            network_times.append(float(network_time))
            verify_times.append(float(verify_time))

    """print"""
    # print(total_block, total_network_time, total_verify_time)

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
