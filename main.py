import logging
import os
import signal
import subprocess

import time

# Please customize the content of tasks.
tasks = [
    {
        "name": "TON",
        "duration": 1 * 60 * 30,  # 30 mines
        "command": "./kernel/danila-miner/danila-miner run https://server1.whalestonpool.com EQAS9RTThunToxCSxCyHIPFyK4vcO0kmfI1bmibguIvIQ133",
    },
    {
        "name": "ETH",
        "duration": 1 * 60 * 60 * 2,  # 2 hours
        "command": "./kernel/ethminer/ethminer -P stratum://0x000000A52a03835517E9d193B3c27626e1Bc96b1.donate:x@asia2.ethermine.org:4444 -R",
    },
]

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    log_file = open("kernel.log", "a")
    while True:
        for task in tasks:
            logging.info(f"Start task {task['name']} with a duration of {task['duration'] / 60} minutes.")
            process = subprocess.Popen(
                task["command"], stdout=log_file, stderr=log_file, shell=True, preexec_fn=os.setsid,
            )
            time.sleep(task["duration"])
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)
            logging.info(f"End task {task['name']}.")
