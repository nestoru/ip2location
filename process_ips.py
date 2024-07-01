import sys
import subprocess

if len(sys.argv) != 3:
    print("Usage: process_ips.py <ip2location_csv_file> <ClientIPAddressFile>")
    sys.exit(1)

csv_file = sys.argv[1]
ip_file = sys.argv[2]

with open(ip_file, 'r') as f:
    ips = f.read().splitlines()

for ip in ips:
    result = subprocess.run([sys.executable, 'ip2location.py', csv_file, ip], capture_output=True, text=True)
    print(result.stdout.strip())

