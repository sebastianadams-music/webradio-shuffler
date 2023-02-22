from pyradios import RadioBrowser
import socket
rb = RadioBrowser()
#!/bin/env python
import socket
import random
import urllib
import urllib.request
import json

def get_radiobrowser_base_urls():
    """
    Get all base urls of all currently available radiobrowser servers

    Returns: 
    list: a list of strings

    """
    hosts = []
    # get all hosts from DNS
    ips = socket.getaddrinfo('all.api.radio-browser.info',
                             80, 0, 0, socket.IPPROTO_TCP)
    for ip_tupple in ips:
        ip = ip_tupple[4][0]

        # do a reverse lookup on every one of the ips to have a nice name for it
        host_addr = socket.gethostbyaddr(ip)
        # add the name to a list if not already in there
        if host_addr[0] not in hosts:
            hosts.append(host_addr[0])

    # sort list of names
    hosts.sort()
    # add "https://" in front to make it an url
    return list(map(lambda x: "https://" + x, hosts))

def downloadUri(uri, param):
    """
    Download file with the correct headers set

    Returns: 
    a string result

    """
    paramEncoded = None
    if param != None:
        paramEncoded = json.dumps(param)
        print('Request to ' + uri + ' Params: ' + ','.join(param))
    else:
        print('Request to ' + uri)

    req = urllib.request.Request(uri, paramEncoded)
    #TODO: change the user agent to name your app and version
    req.add_header('User-Agent', 'MyApp/0.0.1')
    req.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(req)
    data=response.read()

    response.close()
    return data

def downloadRadiobrowser(path, param):
    """
    Download file with relative url from a random api server.
    Retry with other api servers if failed.

    Returns: 
    a string result

    """
    servers = get_radiobrowser_base_urls()
    random.shuffle(servers)
    i = 0
    for server_base in servers:
        print('Random server: ' + server_base + ' Try: ' + str(i))
        uri = server_base + path

        try:
            data = downloadUri(uri, param)
            return data
        except Exception as e:
            print("Unable to download from api url: " + uri, e)
            pass
        i += 1
    return {}

def downloadRadiobrowserStats():
    stats = downloadRadiobrowser("/json/stats", None)
    return json.loads(stats)

def downloadRadiobrowserStationsByCountry(countrycode):
    stations = downloadRadiobrowser("/json/stations/bycountrycodeexact/" + countrycode, None)
    return json.loads(stations)

def downloadRadiobrowserStationsByName(name):
    stations = downloadRadiobrowser("/json/stations/search", {"name":name})
    return json.loads(stations)

# print list of names
print("All available urls")
print("------------------")
for host in get_radiobrowser_base_urls():
    print(host)
print("")

print("Stats")
print("------------")
print(json.dumps(downloadRadiobrowserStats(), indent=4))

country_codes = ["FR", "IR"]

# country_codes = [
#     "AF",
# "AL",
# "DZ",
# "AS",
# "AD",
# "AO",
# "AI",
# "AQ",
# "AG",
# "AR",
# "AM",
# "AW",
# "AU",
# "AT",
# "AZ",
# "BS",
# "BH",
# "BD",
# "BB",
# "BY",
# "BE",
# "BZ",
# "BJ",
# "BM",
# "BT",
# "BO",
# "BQ",
# "BA",
# "BW",
# "BV",
# "BR",
# "IO",
# "BN",
# "BG",
# "BF",
# "BI",
# "CV",
# "KH",
# "CM",
# "CA",
# "KY",
# "CF",
# "TD",
# "CL",
# "CN",
# "CX",
# "CC",
# "CO",
# "KM",
# "CD",
# "CG",
# "CK",
# "CR",
# "HR",
# "CU",
# "CW",
# "CY",
# "CZ",
# "CI",
# "DK",
# "DJ",
# "DM",
# "DO",
# "EC",
# "EG",
# "SV"	,
# "GQ"	,
# "ER"	,
# "EE"	,
# "SZ"	,
# "ET"	,
# "FK"	,
# "FO"	,
# "FJ"	,
# "FI"	,
# "FR"	,
# "GF"	,
# "PF"	,
# "TF"	,
# "GA"	,
# "GM"	,
# "GE"	,
# "DE"	,
# "GH"	,
# "GI"	,
# "GR"	,
# "GL"	,
# "GD"	,
# "GP"	,
# "GU"	,
# "GT"	,
# "GG"	,
# "GN"	,
# "GW"	,
# "GY"	,
# "HT"	,
# "HM"	,
# "VA"	,
# "HN"	,
# "HK"	,
# "HU"	,
# "IS"	,
# "IN"	,
# "ID"	,
# "IR"	,
# "IQ"	,
# "IE"	,
# "IM"	,
# "IL"	,
# "IT"	,
# "JM"	,
# "JP"	,
# "JE"	,
# "JO"	,
# "KZ"	,
# "KE"	,
# "KI"	,
# "KP"	,
# "KR"	,
# "KW"	,
# "KG"	,
# "LA"	,
# "LV"	,
# "LB"	,
# "LS"	,
# "LR"	,
# "LY"	,
# "LI"	,
# "LT"	,
# "LU"	,
# "MO"	,
# "MG"	,
# "MW"	,
# "MY"	,
# "MV"	,
# "ML"	,
# "MT"	,
# "MH"	,
# "MQ"	,
# "MR"	,
# "MU"	,
# "YT"	,
# "MX"	,
# "FM"	,
# "MD"	,
# "MC"	,
# "MN"	,
# "ME"	,
# "MS"	,
# "MA"	,
# "MZ"	,
# "MM"	,
# "NA"	,
# "NR"	,
# "NP"	,
# "NL"	,
# "NC"	,
# "NZ"	,
# "NI"	,
# "NE"	,
# "NG"	,
# "NU"	,
# "NF"	,
# "MP"	,
# "NO"	,
# "OM"	,
# "PK"	,
# "PW"	,
# "PS"	,
# "PA"	,
# "PG"	,
# "PY"	,
# "PE"	,
# "PH"	,
# "PN"	,
# "PL"	,
# "PT"	,
# "PR"	,
# "QA"	,
# "MK"	,
# "RO"	,
# "RU"	,
# "RW"	,
# "RE"	,
# "BL"	,
# "SH"	,
# "KN"	,
# "LC"	,
# "MF"	,
# "PM"	,
# "VC"	,
# "WS"	,
# "SM"	,
# "ST"	,
# "SA"	,
# "SN"	,
# "RS"	,
# "SC"	,
# "SL"	,
# "SG"	,
# "SX"	,
# "SK"	,
# "SI"	,
# "SB"	,
# "SO"	,
# "ZA"	,
# "GS"	,
# "SS"	,
# "ES"	,
# "LK"	,
# "SD"	,
# "SR"	,
# "SJ"	,
# "SE"	,
# "CH"	,
# "SY"	,
# "TW"	,
# "TJ"	,
# "TZ"	,
# "TH"	,
# "TL"	,
# "TG"	,
# "TK"	,
# "TO"	,
# "TT"	,
# "TN"	,
# "TR"	,
# "TM"	,
# "TC"	,
# "TV"	,
# "UG"	,
# "UA"	,
# "AE"	,
# "GB"	,
# "UM"	,
# "US"	,
# "UY"	,
# "UZ"	,
# "VU"	,
# "VE"	,
# "VN"	,
# "VG"	,
# "VI"	,
# "WF"	,
# "EH"	,
# "YE"	,
# "ZM"	,
# "ZW"	,
# "AX"	,
# ]
textfile = open("stationlist.txt", 'a+')

for code in country_codes: 
    country_stations = downloadRadiobrowserStationsByCountry(code)
    print(country_stations)
    print("_________---_____---_____EEEE")
    for station in country_stations:
        url = station['url']
        print(url)
        print("----")    
        textfile.write('"' + url + '", ')
