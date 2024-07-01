import csv
import sys
import ipaddress

def ip_to_number(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        if ip_obj.version == 4:
            # Convert IPv4 to IPv6-mapped IPv4 address
            ip_obj = ipaddress.IPv6Address(f"::ffff:{ip}")
        return int(ip_obj)
    except ValueError:
        raise ValueError(f"Invalid IP address: {ip}")

def lookup_ip(csv_file, ip):
    ip_num = ip_to_number(ip)
    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            ip_from = int(row[0])
            ip_to = int(row[1])
            if ip_from <= ip_num <= ip_to:
                return {
                    "ip": ip,
                    "country_code": row[2],
                    "country_name": row[3],
                    "region": row[4],
                    "city": row[5]
                }
    return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ip2location.py <ip2location_csv_file> <IP>")
        sys.exit(1)

    csv_file = sys.argv[1]
    ip = sys.argv[2]

    try:
        result = lookup_ip(csv_file, ip)
        if result:
            print(f'"{result["ip"]}", "{result["country_code"]}", "{result["country_name"]}", "{result["region"]}", "{result["city"]}"')
        else:
            print(f'"{ip}", "-", "-", "-", "-"')
    except ValueError as e:
        print(e)

