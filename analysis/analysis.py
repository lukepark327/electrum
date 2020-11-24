"""
server  : electrum3.hodlister.co
format  : block height | download headers | verify headers
"""

if __name__ == "__main__":
    total_network_time = 0.
    total_verify_time = 0.
    total_block = 0

    with open('download_verify.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            block, network_time, verify_time = line.split()

            block = int(block)
            network_time = float(network_time)
            verify_time = float(verify_time)

            total_block += 1
            total_network_time += network_time
            total_verify_time += verify_time

    print(total_block, total_network_time, total_verify_time)
    print("Avg network_time:\t", end='')
    print(total_network_time / total_block)
    print("Avg verify_time:\t", end='')
    print(total_verify_time / total_block)
    print("Avg total_spent_time:\t", end='')
    print((total_network_time + total_verify_time) / total_block)
