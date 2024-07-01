# IP to Location
I am not associated to https://lite.ip2location.com/ but I found their Geo IP database to be quite handy and yet free (although they have a more accurate paid package).

Here is how to find out the location of a given IP using Unix power tools.

## Preconditions
- You should look at the latest and greated IP-COUNTRY-REGION-CITY data from https://lite.ip2location.com/database-download
- Put the file in the directory of this project

## Find the location of one IP
```
python ip2location.py IP2LOCATION-LITE-DB3.IPV6.CSV 192.148.209.120
```

## Find the location of a list of IPs in a file (one IP per line)
```
python process_ips.py IP2LOCATION-LITE-DB3.IPV6.CSV iplist.txt    
```
