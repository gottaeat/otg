#!/usr/bin/python3
# pylint: disable=C0103,C0114,C0116,R1710

import os
import platform
import time


def module_mem():
    with open("/proc/meminfo", "r", encoding="utf-8") as f:
        for line in f.readlines():
            if "MemAvailable" in line:
                return f"{int(int(line.split()[1]) / 1024)}m"


def module_date():
    return time.strftime("%a %d %H:%M:%S")


def module_loadavg():
    return f"{os.getloadavg()[0]:.2f}"


if __name__ == "__main__":
    msg = f"#[fg=white bg=black] {module_date()} #[default] #[fg=white bg=black] {module_loadavg()}"
    if platform.system() == "Linux":
        msg += f" {module_mem()}"
    print(msg)
