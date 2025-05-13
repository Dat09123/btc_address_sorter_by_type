import os
import multiprocessing
from pyfiglet import Figlet
from colorama import Fore, Style, init
from tqdm import tqdm

init(autoreset=True)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def title():
    f = Figlet(font='slant')
    print(Fore.CYAN + f.renderText("BitMorphX") + Style.RESET_ALL)
    print(Fore.YELLOW + "  BTC ADDRESS SORTER — OPTIMIZED WITH MULTIPROCESSING\n")
    print(Fore.GREEN + "  Supported Bitcoin Address Formats:" + Style.RESET_ALL)
    print(Fore.GREEN + "  • Legacy (P2PKH)         → Base58  → Starts with '1'")
    print(Fore.GREEN + "  • Nested SegWit (P2SH)   → Base58  → Starts with '3'")
    print(Fore.GREEN + "  • Native SegWit (P2WPKH) → Bech32  → Starts with 'bc1'\n" + Style.RESET_ALL)

def classify_address(address):
    if address.startswith('1'):
        return '1'
    elif address.startswith('3'):
        return '3'
    elif address.startswith('bc1'):
        return 'bc'
    return None

def worker(queue, result_dict, lock):
    local_counts = {'1': [], '3': [], 'bc': []}
    while True:
        line = queue.get()
        if line == "STOP":
            break
        line = line.strip()
        if not line:
            continue
        key = classify_address(line)
        if key:
            local_counts[key].append(line)
    with lock:
        for k in local_counts:
            result_dict[k].extend(local_counts[k])

def write_output(address_types):
    if address_types['1']:
        with open('1xxxx.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(address_types['1']))
    if address_types['3']:
        with open('3xxxx.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(address_types['3']))
    if address_types['bc']:
        with open('bcxxxx.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(address_types['bc']))

def main():
    clear_terminal()
    title()

    input_file = input(Fore.YELLOW + "Enter input file name [default: btc_address.txt]: " + Style.RESET_ALL).strip()
    if not input_file:
        input_file = 'btc_address.txt'
    if not os.path.exists(input_file):
        print(Fore.RED + f"File '{input_file}' not found.\n" + Style.RESET_ALL)
        return

    try:
        cpu_cores = multiprocessing.cpu_count()
        threads = int(input(Fore.YELLOW + f"Enter number of CPU threads (1-{cpu_cores}) [default: {cpu_cores}]: " + Style.RESET_ALL) or cpu_cores)
        threads = max(1, min(threads, cpu_cores))
    except ValueError:
        threads = cpu_cores

    manager = multiprocessing.Manager()
    queue = manager.Queue(maxsize=10000)
    result_dict = manager.dict({'1': manager.list(), '3': manager.list(), 'bc': manager.list()})
    lock = manager.Lock()

    print(Fore.CYAN + f"\nCounting total lines in '{input_file}'..." + Style.RESET_ALL)
    with open(input_file, 'r', encoding='utf-8') as f:
        total_lines = sum(1 for _ in f)

    print(Fore.GREEN + f"Processing {total_lines:,} addresses using {threads} thread(s)...\n" + Style.RESET_ALL)

    workers = []
    for _ in range(threads):
        p = multiprocessing.Process(target=worker, args=(queue, result_dict, lock))
        p.start()
        workers.append(p)

    with open(input_file, 'r', encoding='utf-8') as f, tqdm(total=total_lines, desc="Sorting", colour="green") as pbar:
        for line in f:
            queue.put(line)
            pbar.update(1)

    # Stop workers
    for _ in workers:
        queue.put("STOP")
    for p in workers:
        p.join()

    # Convert back to dict of lists
    final_results = {k: list(v) for k, v in result_dict.items()}
    write_output(final_results)

    print(Fore.LIGHTGREEN_EX + "\n✔ Done! Output saved as 1xxxx.txt, 3xxxx.txt, bcxxxx.txt\n" + Style.RESET_ALL)

if __name__ == '__main__':
    main()
