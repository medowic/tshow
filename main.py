#!/usr/bin/env python3
import sys
import os.path

human_read = ["-h", "--human-readable"]

def help():
    print("\nUsage: tshow [OPTIONS]")
    print("Show CPU's temperature in machine- and human-readable format\n")
    print("Options:")
    print("    -h, --human-readable    print temperature in human-readable format (e.g.: 50.0C)")
    print("    --help                  display this help and exit")
    print("    --version               display version information and exit")
    return ""

def version():
    print("\ntshow v1.0, 2024")
    print("GitHub repository: github.com/medowic/tshow\n")
    print("Contributed under MIT License, github.com/medowic/tshow/LICENSE")
    return ""

def temperature(human_readable=False):
    if os.path.exists("/sys/devices/virtual/thermal/thermal_zone0/temp"):
        thermal_zone_file = "/sys/devices/virtual/thermal/thermal_zone0/temp" # usually used for an Intel CPU
    elif os.path.exists("/sys/class/hwmon/hwmon/temp1_input"):
        thermal_zone_file = "/sys/class/hwmon/hwmon/temp1_input" # for an AMD CPU
    else:
        raise FileNotFoundError("Error: couldn't find thermal zone file.\nBe sure you're not running this program in VM and you has latest BIOS version")
    
    with open(thermal_zone_file, "r") as file:
        temp = int(file.read())

    if human_readable:
        return str(float(temp) / 1000) + str("C")
    else:
        return temp

def main():
    try:
        if sys.argv[1] in human_read:
            print(temperature(True))
            sys.exit(0)
        elif sys.argv[1] == "--help":
            print(help())
            sys.exit(0)
        elif sys.argv[1] == "--version":
            print(version())
            sys.exit(0)
        else:
            print("Error: couldn't resolve any flag")
            sys.exit(1)
    except IndexError:
        try:
            print(temperature())
            sys.exit(0)
        except FileNotFoundError as Exception:
            print(Exception)
            sys.exit(2)

if __name__ == "__main__":
    main()
