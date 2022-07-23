# MADE BY PR0T0N!!! Working on adding AI Solver 
# Telegram link: https://t.me/+Tvbz-xGh_5pjYzVh
# New Discord Server: https://discord.gg/FSqsR2HEJR
from http import cookies
from re import M
from utils import TokenUtils
import colorama
from colorama import init, Fore
from structures import ProxyPool
import threading
import json
from invisifox import InvisiFox
import time
import random
import os
import requests
import string
import http.client
import base64
import ctypes
from twocaptcha import TwoCaptcha
from capmonster_python import HCaptchaTask
from anticaptchaofficial.hcaptchaproxyless import *
# ^^ Library's being used


# Sends request to get amount of users using this software
def get_users():
    check_users = "https://WeeReflectingWaterfall.crypticsserver.repl.co/users"
    response2 = requests.get(check_users)
    data2 = response2.text
    data2 = "{:,}".format(int(data2))
    return data2

# Checks to see if you have latest version of Gen
def check_up_to_date():
    url = "https://WeeReflectingWaterfall.crypticsserver.repl.co"
    response = requests.get(url)
    data = response.text
    data2 = get_users()
    print(Fore.WHITE + f"Total Users: {data2}")
    if Version in data:
        print(Fore.LIGHTGREEN_EX + "Generator Up to Date!")
    else:
        print(Fore.RED + "Generator Out of date please update for new features!\nLink: https://github.com/Pr0t0ns/Discord-Token-Generator/releases")
    return

# Opening Configuration file and fetching Data like API keys
with open("data/config.json") as config:
    config = json.load(config)
    anticaptcha_API = config["anticaptcha_api_key"]
    capmonster_API = config["capmonster_api_key"]
    twocaptcha_API = config['2captcha_API_key']
    InvisiFox_api_key = config['invisiFox_API_key']
    x_super_prop = config['x-super-properties']
    user_agent = config['user-agent']
    if x_super_prop == "" and user_agent == "":
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.33 Safari/537.36"
        x_super_prop = "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjUwNjAuMzMgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMy4wLjUwNjAuMzMiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwODMyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
    use_InvisiFox = config['use_InvisiFox']
    use_2captcha = config['use_2captcha']
    use_capmonster = config["use_capmonster"]
    if use_2captcha == True and use_capmonster == True or use_2captcha == True and use_InvisiFox == True or use_capmonster == True and use_InvisiFox == True:
        print("You can only use 1 Captcha Provider please modify your config.json file!")
        time.sleep(10)
        exit(0)
    threadss = config['threads']
    password = config['password']
    birthday = config['Date_of_birth']
    show_proxy_errors = config['Display_proxy_errors']
    join_server = config['Join_Server_On_Creation']
    invite_link = config['Server_Invite']
    use_proxies_for_capmonster = config['capmonster_use_proxies']
    if_ip_auth = config['user:pass@ip:port format']
    hotmailbox_API_key = config['hotmailbox_API']
    use_hotmailbox = config['use_hotmailbox']
    gen_passwords = config['generate_password']
    fivesim_API = config["5sim_API"]
    use_5sim = config['use_5sim']
    country = config['5sim_country']
    operator = config['5sim_op']
    use_custom_usernames = config['custom_usernames']
    custom_username_file = config['username_file']
    fivesim_product = 'discord'
    del config # Deleting Variable for more mem

# Discord Host Details For Auth Proxies 
host_details = {
    "url" : "discord.com",
    "port" : 443 
}

# Variables being set
blacklisted_IPS = []
IPS_in_use = []
auth_proxies = []
char_symbols = ["!", "@", "#", "$", "^", "(", "&", "%"]
total_auth_proxies = 0
index_pos = 0
Version = "V1.9"
domains = ["@gmail.com", "@yahoo.com", "@outlook.com", "@hotmail.com", "@protonmail.com"]

# Initilazing stuff like Solver API's and colorama
bot = InvisiFox()
bot.apiKey = InvisiFox_api_key
proxy_recycle_message_sent = False
init(convert=True)
colorama.init(autoreset=True)

# Site key's
site_key = "4c672d35-0701-42b2-88c3-78380b0db560"
email_site_key = "f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"

#Clear Screen
def clear_screen():
    os.system("clear")
    os.system("cls")
    return

# Checking Type of tokens being generated to put in Title
if use_5sim == True and use_hotmailbox == True:
    token_type = "Email & Phone Verified Tokens"
elif use_5sim == True and use_hotmailbox == False:
    token_type = "Phone Verified Tokens"
elif use_5sim == False and use_hotmailbox == True:
    token_type = "Email Verified Tokens"
else:
    token_type = "Unverified Tokens"

# Attempting to set console title
try:
	ctypes.windll.kernel32.SetConsoleTitleW(f"[FREE] Pr0t0n Generator | {Version} | Threads: {threadss} | Token Type: {token_type}")
except Exception as error:
    print(f"Cannot Set Title!\nError Thrown: {error}")

# Purchasing Hotmail Email using hotmailbox API
def purchase_email():
    url = f"https://api.hotmailbox.me/mail/buy?apikey={hotmailbox_API_key}&mailcode=HOTMAIL&quantity=1"
    r = requests.get(url)
    data = r.json()
    email = data['Data']['Emails'][0]['Email']
    email_password = data['Data']['Emails'][0]['Password']
    return email, email_password

# Parsing username:password@ip:port proxies to 4 variables one for the ip_address another for the Ip Port another for the ip username and another for the ip password
def parse_auth_proxy(proxy):
    proxy = proxy.replace("@", ":")
    colons_hit = 0
    IP_username = ""
    IP_password = ""
    IP_Address = ""
    IP_port = ""
    for character in proxy:
        if character == ":":
            colons_hit = colons_hit + 1
        else:
            if colons_hit == 0:
                IP_username += character
            elif colons_hit == 1:
                IP_password += character
            elif colons_hit == 2:
                IP_Address += character
            elif colons_hit == 3:
                IP_port += character
    
    return IP_username, IP_password, IP_Address, IP_port


# Parsing ip:port Proxy to Get 2 variables one for IP Address and the other one for the IP Port
def parse_ip_port_proxy(proxy): 
    IP_Address = proxy.split(":")[0].replace('\n', '')
    IP_Port = proxy.split(":")[1].replace('\n', '')
    return IP_Address, IP_Port

# Function to send request with auth proxies (proxies using username:pass@ip:port format)
def auth_proxy_request(url, port, username, password, method, route, payload, headers): 
    conn = http.client.HTTPSConnection(url, port)
    auth = '%s:%s' % (username, password)
    headers['Proxy-Authorization'] = 'Basic ' + str(base64.b64encode(auth.encode())).replace("b'", "").replace("'", "")
    conn.set_tunnel(host_details['url'], host_details['port'], headers)
    conn.request(method, route, payload, headers)
    return conn

# Fetching Proxies and Adding them to list
with open("data/proxies.txt") as proxy: 
    if if_ip_auth == False:
        proxies = ProxyPool(proxy.read().splitlines())
    else:
        proxies = proxy.read().splitlines()
        for proxy in proxies:
            auth_proxies.append(proxy)
            total_auth_proxies += 1

# Captcha Solvers function to solve captchas depending on provider choosen
def solve_captcha(site_key, proxy=None):
    if capmonster_API != "" and use_capmonster == True: # Checking if user is using Capmonster
        if use_proxies_for_capmonster == True and proxy != None: # Checking to see if user want's to use proxies with capmonster
            if if_ip_auth == False: # Checking to see if user is using auth proxies
                ip, port = parse_ip_port_proxy(proxy)
                print("|>" + Fore.YELLOW + " Solving Captcha")
                capmonster = HCaptchaTask(capmonster_API)
                try:
                    capmonster.set_proxy("http", ip, port)
                    task_id = capmonster.create_task("https://discord.com", site_key)
                    result = capmonster.join_task_result(task_id)
                    g_response = result.get("gRecaptchaResponse")
                    return g_response
                except Exception:
                    print("This proxy Does not work with capmonster")
                    return ""
            else: # is user is using ip:port proxies
                ip_username, ip_password, ip_ip, ip_port = parse_auth_proxy(proxy)
                print("|>" + Fore.YELLOW + " Solving Captcha")
                capmonster = HCaptchaTask(capmonster_API)
                try:
                    capmonster.set_proxy("http", ip_ip, ip_port, ip_username, ip_password)
                    task_id = capmonster.create_task("https://discord.com", site_key)
                    result = capmonster.join_task_result(task_id)
                    g_response = result.get("gRecaptchaResponse")
                    return g_response
                except Exception:
                    print("this proxy does not work with capmonster!")
                    return ""
        else: # if user wants to solve capmonster captcha proxyless
            print("|>" + Fore.YELLOW + " Solving Captcha")
            capmonster = HCaptchaTask(capmonster_API)
            task_id = capmonster.create_task("https://discord.com", site_key)
            result = capmonster.join_task_result(task_id)
            g_response = result.get("gRecaptchaResponse")
            return g_response
    elif use_2captcha == True: # Checks if user wants to use 2captcha
        print("|>" + Fore.YELLOW + " Solving Captcha")
        solver = TwoCaptcha(twocaptcha_API)
        try:
            result = solver.hcaptcha(
                sitekey=site_key,
                url='https://discord.com',
            )
        except Exception as e:
            print(e)
            print("|>" + Fore.LIGHTRED_EX + " Error Solving Captcha!")
            return ""
        else:
            print("|>" + Fore.GREEN + " Solved Captcha")
            result = result.get("code")
            return result
    elif use_InvisiFox == True and proxy == None: # Checks to see if user has proxies for InvisiFox Solver
        print("To use InvisiFox as your Captcha provider you are required to pass in a proxy!")
        return "Error"
    elif use_InvisiFox == True and proxy != None: # Checking to see if user wants to use InvisiFox as their provider
        print("|>" + Fore.YELLOW + " Solving Captcha")
        if if_ip_auth == True: # Checking for auth proxies to solve InvisiFox captcha
            try:
                solution = bot.solveHCaptcha(site_key, 'https://discord.com', f'http://{proxy}')
            except Exception as error:
                print("There was an error trying to solve captcha using InvisiFox!")
                time.sleep(0.1)
                return "error"
            print("|>" + Fore.GREEN + " Solved Captcha")
            return solution
        else: # Checking for ip:port proxies to solve InvisiFox captcha
            try:
                solution = bot.solveHCaptcha(site_key, 'https://discord.com', proxy)
            except Exception as error:
                print(f"There was an error trying to solve captcha using InvisiFox! {error}")
                time.sleep(0.1)
                return "error"
            print("|>" + Fore.GREEN + " Solved Captcha")
            return solution
    else: # Checking to see if user is using anticaptcha as their solving provider
        print("|>" + Fore.YELLOW + " Solving Captcha")
        solver = hCaptchaProxyless()
        solver.set_verbose(1)
        solver.set_key(anticaptcha_API)
        solver.set_website_url("https://discord.com")
        solver.set_website_key(site_key)
        g_response = solver.solve_and_return_solution()
        if g_response != 0:
            print("|>" + Fore.GREEN + " Solved Captcha")
            return g_response
        else:
            print("|>" + Fore.RED +" Error Solving Captcha!")
            return ""

# Generates Random Email Address for Signup
def generate_email(length):
    return ''.join(random.choice(string.ascii_letters) for x in range(int(length))) + random.choice(domains)

# Generates Random Password for Signup
def generate_passwords(length):
    return ''.join(random.choice(string.ascii_letters) for x in range(int(length))) + random.choice(char_symbols)

# Generates Random Username for Signup
def generate_username(length):
    return ''.join(random.choice(string.ascii_letters) for x in range(length))

# Fetches dcfduid and sdcfduid cookies 
def fetch_cookies(proxy):
    if if_ip_auth == False:
        ip, port = parse_ip_port_proxy(proxy)
        session = requests.Session()
        session.proxies = {
            'http': f'http://{ip}:{port}',
            'https': f'http://{ip}:{port}',
        }
        data = session.get('https://discord.com')
        cookiess = session.cookies.get_dict()
        dcfduid = cookiess.get("__dcfduid")
        sdcfduid = cookiess.get("__sdcfduid")
        session.close()
        return dcfduid, sdcfduid
    else:
        ip_username, ip_password, ip_ip, ip_port = parse_auth_proxy(proxy)
        session = requests.Session()
        session.proxies = {
            'http': f"http://{ip_username}:{ip_password}@{ip_ip}:{ip_port}",
            'https': f'http://{ip_username}:{ip_password}@{ip_ip}:{ip_port}',
        }
        data = session.get('https://discord.com')
        cookiess = session.cookies.get_dict()
        dcfduid = cookiess.get("__dcfduid")
        sdcfduid = cookiess.get("__sdcfduid")
        session.close()
        return dcfduid, sdcfduid


# Fetches Fingerprint
def get_fingerprint(proxy, dcfduid, sdcfduid):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "cookie": f"__dcfduid={dcfduid}; __sdcfduid={sdcfduid};",
        "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": user_agent
    }
    if if_ip_auth == False:
        ip, port = parse_ip_port_proxy(proxy)
        session = requests.Session()
        session.proxies = {
            'http': f'http://{ip}:{port}',
            'https': f'http://{ip}:{port}',
        }
        session.headers = headers
        data = session.get('https://discord.com/api/v9/experiments')
        data = data.text
        fingerprint = json.loads(data)
        fingerprint = fingerprint['fingerprint']
        session.close()
        return fingerprint
    else:
        ip_username, ip_password, ip_ip, ip_port = parse_auth_proxy(proxy)
        session = requests.Session()
        session.proxies = {
            'http': f"http://{ip_username}:{ip_password}@{ip_ip}:{ip_port}",
            'https': f'http://{ip_username}:{ip_password}@{ip_ip}:{ip_port}',
        }
        session.headers = headers
        data = session.get('https://discord.com/api/v9/experiments')
        data = data.text
        fingerprint = json.loads(data)
        fingerprint = fingerprint['fingerprint']
        session.close()
        return fingerprint

# Verifys Phone Number Using 5sim
def verify_phone(proxy, discord_token, discord_password, dcfduid_cookie, sdcfduid_cookie):
    if use_5sim == True:
        
        headers = {
            'Authorization': 'Bearer ' + fivesim_API,
            'Accept': 'application/json',
        }
        response = requests.get('https://5sim.net/v1/user/buy/activation/' + country + '/' + operator + '/' + fivesim_product, headers=headers)
        try:
            phone_number = response.json()['phone']
        except Exception as error:
            print("Looks like the token, country or operator is invalid for phone verification!!")
            time.sleep(10)
            exit(0)
        phone_id = response.json()['id']
        try:
            phone_id_str = str(phone_id)
        except Exception as error:
            print(error)
        captcha_key = solve_captcha(email_site_key)
        if if_ip_auth == False:
            headers = {
                "authorization": discord_token,
                "content-type": "application/json",
                "cookie": f"__dcfduid={dcfduid_cookie}; __sdcfduid={sdcfduid_cookie}",
                "user-agent": user_agent,
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-US",
                "x-super-properties": x_super_prop
            }
            payload = {
                "captcha_key": captcha_key,
                "change_phone_reason": "user_action_required",
                "phone": phone_number
            }
            payload = json.dumps(payload)
            conn = proxy.get_connection("discord.com")
            conn.request("POST", "/api/v9/users/@me/phone", payload, headers)
            response = conn.getresponse()
            if int(response.status) == 204:
                print("|>" + Fore.LIGHTYELLOW_EX + " Sent Verification Code to Phone Number")
            else:
                print("|>" + Fore.LIGHTRED_EX + " Could not send verification code to number!")
                return
            result = ""
            headers = {
                'Authorization': 'Bearer ' + fivesim_API,
                'Accept': 'application/json',
            }
            Retrys = 0
            while result != "NULL":
                response = requests.get('https://5sim.net/v1/user/check/' + phone_id_str, headers=headers)
                data = response.json()
                result = data['status']
                try:
                    code = data['sms'][0]['code']
                    break
                except Exception as error:
                    Retrys += 1
                    if Retrys > 375:
                        print("|>" + Fore.RED + " Could not find Verification Code from discord!")
                        return
            headers = {
                "authorization": discord_token,
                "content-type": "application/json",
                "cookie": f"__dcfduid={dcfduid_cookie}; __sdcfduid={sdcfduid_cookie}",
                "user-agent": user_agent,
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-US",
                "x-super-properties": x_super_prop
            }
            payload = {
                "code": code,
                "phone": phone_number
            }
            payload = json.dumps(payload)

        else:
            ip_username, ip_password, ip_ip, ip_port = parse_auth_proxy(proxy)
            proxy_details = {
                "url" : ip_ip, 
                "port" : ip_port, 
                "username" : ip_username, 
                "password" : ip_password 
            }
            headers = {
                "authorization": discord_token,
                "content-type": "application/json",
                "cookie": f"__dcfduid={dcfduid_cookie}; __sdcfduid={sdcfduid_cookie}",
                "user-agent": user_agent,
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-US",
                "x-super-properties": x_super_prop
            }
            payload = {
                "captcha_key": captcha_key,
                "change_phone_reason": "user_action_required",
                "phone": phone_number
            }
            payload = json.dumps(payload)
            conn = auth_proxy_request(proxy_details['url'], proxy_details['port'], proxy_details['username'], proxy_details['password'], "POST", "/api/v9/users/@me/phone", payload, headers)
            response = conn.getresponse()
            if int(response.status) == 204:
                print("|>" + Fore.LIGHTYELLOW_EX + " Sent Verification Code to Phone Number")
            else:
                print("|>" + Fore.LIGHTRED_EX + " Could not send verification code to number!")
                return
            result = ""
            headers = {
                'Authorization': 'Bearer ' + fivesim_API,
                'Accept': 'application/json',
            }
            Retrys = 0
            while result != "NULL":
                response = requests.get('https://5sim.net/v1/user/check/' + phone_id_str, headers=headers)
                data = response.json()
                result = data['status']
                try:
                    code = data['sms'][0]['code']
                    break
                except Exception as error:
                    Retrys += 1
                    if Retrys > 375:
                        print("|>" + Fore.RED + " Could not find Verification Code from discord!")
                        return
            headers = {
                "authorization": discord_token,
                "content-type": "application/json",
                "cookie": f"__dcfduid={dcfduid_cookie}; __sdcfduid={sdcfduid_cookie}",
                "user-agent": user_agent,
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-US",
                "x-super-properties": x_super_prop
            }
            payload = {
                "code": code,
                "phone": phone_number
            }
            payload = json.dumps(payload)
            conn = auth_proxy_request(proxy_details['url'], proxy_details['port'], proxy_details['username'], proxy_details['password'], "POST", "/api/v9/phone-verifications/verify", payload, headers)
            response = conn.getresponse()
            if int(response.status) == 200:
                pass
            else:
                print("|>" + Fore.RED +" Invalid Verification Code!")
                return
            response = response.read()
            verify_url_token = json.loads(response)
            verify_url_token = verify_url_token['token']
            headers = {
                "authorization": discord_token,
                "content-type": "application/json",
                "cookie": f"__dcfduid={dcfduid_cookie}; __sdcfduid={sdcfduid_cookie}",
                "user-agent": user_agent,
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-US",
                "x-super-properties": x_super_prop
            }
            payload = {
                "change_phone_reason": "user_action_required",
                "password": discord_password,
                "phone_token": verify_url_token
            }
            payload = json.dumps(payload)
            conn = auth_proxy_request(proxy_details['url'], proxy_details['port'], proxy_details['username'], proxy_details['password'], "POST", "/api/v9/users/@me/phone", payload, headers)
            response = conn.getresponse()
            if int(response.status) == 204:
                print("|>" + Fore.LIGHTGREEN_EX + f" Phone Verified {discord_token}")
                return
            else:
                print("|>" + Fore.RED + " Issue Verifying Response Code!")
                return
        return


# Verifys Email using HotmailBox API
def verify_email(token, username, password, proxy, mail_fingerprint, dcfduid_cookie, sdcfduid_cookie):
    url = f'https://getcode.hotmailbox.me/discord?email={username}&password={password}&timeout=50'
    data = requests.get(url)
    data = data.json()
    Verfication_Link = data['VerificationCode']
    Verfication_Link = Verfication_Link.replace("https://click.discord.com", "")
    if if_ip_auth == False:
        conn = proxy.get_connection("click.discord.com")
        headers = {}
        payload = {}
        Verfication_Link = Verfication_Link.replace("\r\n\r\n", "")
        Verfication_Link = Verfication_Link.replace("\r", "")
        conn.request("GET", Verfication_Link, payload, headers)
        response = conn.getresponse()
        headers = response.getheaders()
        ans = [val for key, val in headers if key == 'Location'][0]
        str_ans = str(ans)
        url_token = str_ans.replace("https://discord.com/verify#token=", "")
        ans = ans[19:]
        captcha_key = solve_captcha(email_site_key, proxy)
        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "cookie": f"__dcfduid={dcfduid_cookie}; __sdcfduid={sdcfduid_cookie}; locale=en-US",
            "origin": "https://discord.com",
            "referer": "https://discord.com/verify",
            "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": user_agent,
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-fingerprint": mail_fingerprint,
            "x-super-properties": x_super_prop
        }
        payload = {
            "captcha_key": captcha_key,
            "token": url_token
        }
        payload = json.dumps(payload)
        conn = proxy.get_connection("discord.com")
        conn.request("POST", "/api/v9/auth/verify", payload, headers)
        r1 = conn.getresponse()
        if int(r1.status) == 200:
            print("|>" + Fore.LIGHTGREEN_EX + f" Email Verified {token}")
            return
        else:
            print("|>" + Fore.RED + " Issue Verifying Email!")
            return

    else:
        ip_username, ip_password, ip_ip, ip_port = parse_auth_proxy(proxy)
        proxy_details = {
            "url" : ip_ip, 
            "port" : ip_port, 
            "username" : ip_username, 
            "password" : ip_password 
        }

        headers = {}
        payload = {}
        conn = auth_proxy_request(proxy_details['url'], proxy_details['port'], proxy_details['username'], proxy_details['password'], "GET", Verfication_Link, payload, headers)
        response = conn.getresponse()
        response = response.getheaders()
        ans = [val for key, val in response if key == 'Location'][0]
        str_ans = str(ans)
        url_token = str_ans.replace("https://discord.com/verify#token=", "")
        ans = ans[19:]
        captcha_key = solve_captcha(email_site_key, proxy)

        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "cookie": f"__dcfduid={dcfduid_cookie}; __sdcfduid={sdcfduid_cookie}; locale=en-US",
            "origin": "https://discord.com",
            "referer": "https://discord.com/verify",
            "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": user_agent,
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-fingerprint": mail_fingerprint,
            "x-super-properties": x_super_prop
        }
        payload = {
            "captcha_key": captcha_key,
            "token": url_token
        }
        payload = json.dumps(payload)
        conn = auth_proxy_request(proxy_details['url'], proxy_details['port'], proxy_details['username'], proxy_details['password'], "POST", "/api/v9/auth/verify", payload, headers)
        r1 = conn.getresponse()
        if int(r1.status) == 200:
            print("|>" + Fore.LIGHTGREEN_EX + f" Email Verified {token}")
            return
        else:
            print("|>" + Fore.RED + " Issue Verifying Email!")
            return

# Function that actually creates the account
def create_account(proxy, username=None):
    if proxy in IPS_in_use:
        return
    IPS_in_use.append(proxy)
    if if_ip_auth == True:
        ip_username, ip_password, ip_ip, ip_port = parse_auth_proxy(proxy)
    if gen_passwords == True:
        password = generate_passwords(random.randint(15, 19))
    dcfduid, sdcfduid = fetch_cookies(proxy)
    fingerprint = get_fingerprint(proxy, dcfduid, sdcfduid)
    if username == None:
        username = generate_username(random.randint(8, 12))
    email = generate_email(random.randint(9, 13))
    Captcha = solve_captcha(site_key, proxy)
    #Captcha = "P0_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiMXRuVTR6UDgyaTZwOTdiVXNQZXgrV1pCRHUvbWpxSGNLOXpkRlhXUzluVmpheXIzVFNvTzF4aHVrc0JuSlg2Vk83MkN1cXpwTTlvaWUvS2FUWUtHKzFrRGpXQ2xJSjNwK2pPVWpNNXZhMW5yS3h5SGFLU2lNdlNpR2dLcEw4ZTZoYThmMjBnUHlFbkwvYTdqb21sTHNpYzhVc3BRUllCUjhWQUFvbUI1bHRMbFBoT1J3ak81UzBoV05CMk5pb1J3RmlEdU8ybnhudGcra2VzSVhBR0VSUWJEekNsdW01dFRZdUczSUNRYjM4ZjV0Yk90NHlNazl1WnhZMldnOEJGTjdja1E4SDdSOGtMT282WVdEQk4waXdibEZaQXVKU0x3NGN3ZjJMbUQ5dmZDY29HQTcvZEg3NFF3MEpTN2JJOFBkcThmeUJsNW5BZTJBZ2REMWcwbHJybXMyeGJvQWdxa1BOSnNKc08wcE9PdGpNNVhYQjJZdEhQSUlJdTNEMWowRDFCNmc3cGNlTFlaNlR5ZEN0cDMxbFlJOGlzUHVlWGNOeTM4ZDZpZU9EWVJZcVV0YmNqOEFRQ2tRclk2cS9yaE5jY3Q5Zk9XR093VGtVdktlVTViZGtTM3FwOHBnbG5mVkVVQnZHanFJRTF3RFdaazRZRXU3WGc0Zm1nQXlrVk0wOXRQbnYyQ3hiY3Ivb0lFd1BuOXdTeGNlVE8zd2c3d3ZjSTNjSi83aGxPVUliNWlXSTFPZlozeXcwTDk3U2RETUhOMXlVVS94RmJZQzJBVUdzaW1KbGNub3p1WW1mMjI1aVpxbDdNbzVvblBZUkpjNENsTUY4c3hETzNJNDlhRGhKWlBsZzlIUUxxWmk3ZDQvRnMxRWdndXEvKzRaUS9qYWJNVmtUVDZkbVgxSGJrZWhKbG01RlNRbmZiS3l4bW9KaVdkMU50UE9ZQkY3VzhJNDl5aG0rQ1plU2RlaDN6TTlLc2xTaU5nUnR4dGFReHhaWk9WL1BHVXRzU08raVdEdjBGSFR6MFgxTWg1WmlxY3JhVlh5am9KUmtKaUxDekF6bzMrVHRwT293RUsxV3dRWUdkaThFMzRGV2NaaHVJdjVzQ2FHQUh4d0s2TjV3ZWgyTjV1Ujl3dHZ1UkdYVEl4dTF1eWtTWC9obDVPMmlTZTRmbmtRNGxXdmJmT1VVYWwzTzAwdm8vWUgxek9lMlpoZUUzUjd2MnJML3lXSVZBbnF3WWdNbVlQZ3RtUDVxc1VDOEIycmZRVFdLRWYzNUZtUXFYblNzR09qbXpXaUgvYjdkNGEzcnljU2wxODQ2Um5ydkFpa2FmeUF5ZEZQYkhBQ0YzZHJITG5KRnZ5Wi96WU9ldithNkpua0ZocVpXSDZzVXJpaUI4THFwbTR6cVRNNGZHM1pVZy9DMll2dnZCTFdTTXZYRHdySGU2L2JIYStvTWNhVVVybVdNd21meCt4akZLbjFoMTNTZEdBdUlNUHNSRUlOYTR0bG9aWGhTRlR1YXNTQ2FLZ3JNWlVUQStjL2UvWGUwd1hkVk9kRmNrTWtXcjRTaVROdDZQSHd2cTNzRkFkTXR2Yk91UUVMdHRUODZHQjd6RWo2UkFvT0FwbitzNzdZSVp6dlpRRWttQXh1Y2JabEh1TEllbnRsUmpRd1BSTk8xYkZtRStaK0U2dXdqK2QrQ21LSEpHN1FjbnpIQ0tnUFBoU0RoNzkrcW5CaGZNTUF2THpwbmd1T1QwR3dBSkg0RnVRUUtUTDNKNVAza1gxRHQxWi9uT094Z1NOVEk3eklUSkl0MkE5eUQvZ2pqZWpmUVViUmw2bmRQMG5jbkxKOVBrOE5hRTNOSlBHTlVkcWI0eFZRVXpkU1BEanZnWEtvQTJNVHl2dmFGTmMra28wMlhQSElKZFN2ZnpYWWp4NXBDRk5NbFRDV25VRzAyZEZFZElhT1hxcmlMRkZpWk0vdnpOY01aQk9wQ3IzUTVYZlRweHE0UUVGWXNGd25MU0R5NUxiNFJsamFleG4rcnBmRUlUcExUVzFiR3FESExFVkJxTGhxUUl6ZHNTa3VwZVlzaWM3YXN1QmRMNldzV3ZNRG9WdkxmYUNzS0orWVFlTk9TVnAzdXd2K3RaeVlYOXBHZkwwZEtESE1NVWcwUmY2dThoWHZQSGxMYjhLQlpOWnJnd240a1NneDh1d0ptY2VDMjVIQ1FNeGJxZ0R5bnRnTS9sZFBwZVpSV3YwaGFrZjFjZVMxTTAvbjlMQTVlVTBPOW15U2hwQW9TM01leFcrbEJzZGhRSTB5UXQyLzdjcEN5R3c0QkFBcHhla0lOT2NmQWE2ZGx4ZG9SazlkWWd1S1lGQ1A3US91ZGZVa1NUQWFXTHBSREgvR3RKdFdDOHJEZ3Q0Q2p5VEtDNlBTUFFiSGh1a1NtSUZVVXhzeUZmQ3VnSlN5dGdMYmowWWY3R0RHUVFJZUsrektpanE3QU1NdE5DbVJYUGpiWHN4aTBKelZLaDFqTmdibUlXOXF2NCs0Z2hFQ0s4WURMd3hHd0k2SUpYTEV0SWxiNVVNdjE5cjlDVEpEVzhKc3kzSGRaN1U1cDVCeEN0c0VtTWJoRnNQclRQQ1V4VlhieEI1NFJHWXdKVEZRbUZPTS9ZejVQNyswNXlVSHk2bWdKbS8yTzc3UnFPS2U3YXc1OFkzNmtrZ1laNzJHTUptUXZ2dlNnc292RFlrUTlWQTB0bHQvaVBQdlpLS1hoM3ZvL1RzbzZTV2V0ZTRxaUxVaFZIMHJmeHd3d3o0N1hFd3pUQzI3RFJMR1lIWDZXby9QdVRFYkNZajY4U2xIdTFwRDJGVituMmFRZW9tSlFKSW8rdm9KT2VyOWozblZKd2tjdENqK2JCWWd4bTU1SmFqMERBMjhQd09oaGpzNFZiV3BiYUQrUTdjYVN6RmJHZ0N5cm1RSEVQWVkyRU1jOG13STFhVDlkclhvb21OckZiWG1EQ2Zoc09UcFZmeGFaYVlXSlIxdFc1YWE0S3pWYmxadyttN0RtVE12YWFZS1lSY3JCWjZFVEY1d1gyeGd6d3ZNL044bmxKVG4wSE1DNk02dzk5WERtWkY2cmpUYlhvY0EzRDVMdjZ2VHdDT3RGekhCa1BEbUV2ZUs0L09NcFJlRmFOSDgwQ0dXUERDZ0FVUU42RUl6RGlnY21RcUdIVVE2QXJnMktZV0J3Z0h1MUJqb3RnTGFYc28vb1dsOHFzZUhvQUNkcUNNN0t2MzRUbDg3cFlLYjQyaGJVTEFudkZYaEZlV1M5Y25qenFYMENFOWpZN0p1MDAyY1E0OE5ra2Y2c2NocjIwUGMvL0RYc3FmaUMvN2F5d3VvNkw3TG9hQmdjQm1OV2kvUjFXVEt3NGhvQnNPTFNlS09Jend5TDRSbVZ2NkpZOFZOSTVCb1FpOHVvTXhTbmY1OTVnSFhsN2VYSnhHTmhScDJtb3RnbmNOUDNJSmxkR0ZJZkh5TGtHTE1ic1h0RlF6bUcvNmJyZFFyNFlsRVhzaGhsR0NwbjgyaVVnS3dHNVF3OUx6UUtKcXZwdUlDV0RaRWRXYWgvUUlGeXQ4VnpWNm9uTWN6NnNjQzZQYWI2VTY0QnNaT2hmckprNzNvYk5iMnRvanJmUUhzajEza3dzNHhKT2hyT1ptU2g5aEsrUXBYdzFlZ0lPMW9aWnIyb01JUFFFUmZTVnpPeTNzZlk4cEtMcGdxdW9yVFFaUzJsR2tGMzNXQWF3WVFXMXF6S1BPandpeHZ4cExsUHVNTXorQjFMV2luVDZiY2t3bXYrdzhpbEFxTit6ZmtqMVNrNTJnTS9EcE5ZcXFvY29RVXhxNUdyNXJTZDhaM1pFM043RVluU0grM3N0U0V6TUJlZ2VnZ1dVQ0ZhZGRoNFprNGhQbTExa0NkM0Z3dUd1Mzk0YzBHN092NHhVQWo0djhYRm9EWFJmN3g0RUN6dkUzWHhIclA4QmVXZWNjdnYyZFRsRjA0U2dPRkNJVXFZaDFrZXdVMy9MYVcvQThDQk5PYjU1dS9R"
    if use_hotmailbox == True:
        email, email_password = purchase_email()
    else:
        pass

    if if_ip_auth == False:
        conn = proxy.get_connection("discord.com")
        print("|>" + Fore.LIGHTWHITE_EX +" Attempting to create account...")
        headers = {
            "origin": "https://discord.com",
            "referer": "https://discord.com/register",
            "user-agent": user_agent,
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-fingerprint": fingerprint,
            "x-super-properties": x_super_prop
        }
        if join_server == True:
            if invite_link != "None":
                payload = {
                    "captcha_key": Captcha,
                    "consent": "true",
                    "date_of_birth": birthday,
                    "email": email,
                    "fingerprint": fingerprint,
                    "gift_code_sku_id": "null",
                    "invite": invite_link,
                    "password": password,
                    "username": username
                }
            else:
                print("|>" + Fore.RED +"You have Join Server Enabled but there so invite link for the server to join please add it to the config.json file to fix this error!")
                return
        else:
            payload = {
                "captcha_key": Captcha,
                "consent": "true",
                "date_of_birth": birthday,
                "email": email,
                "fingerprint": fingerprint,
                "gift_code_sku_id": "null",
                "invite": "null",
                "password": password,
                "username": username
            }
        payload = json.dumps(payload)
        conn.request("POST", "/api/v9/auth/register", payload, headers)
        response = conn.getresponse()
        data = response.read().decode()
        if "token" not in str(data):
            print("|>" + Fore.LIGHTMAGENTA_EX +" Looks like the Captcha Solver returned an invalid response or maybe a ratelimit!")
            return
        else:
            data = data.replace('{"token": "', '')
            data = data.replace('"}', '')
            token = data
            print("|>" + Fore.LIGHTGREEN_EX + f" Created Account {token}")
            file = open("data/tokens.txt", "a+")
            file.write(f"{email}:{password}:{token}\n")
            file.close()
            if use_hotmailbox == True:
                print("|>" + Fore.CYAN + f" Attemping To Email Verify {token}")
                verify_mail = verify_email(token, email, email_password, proxy, fingerprint, dcfduid, sdcfduid)
            if use_5sim == True:
                print("|>" + Fore.CYAN + f" Attempting to Phone Verify {token}")
                res = verify_phone(proxy, token, password, dcfduid, sdcfduid)
            else:
                return
            return
    else:
        proxy_details = {
            "url" : ip_ip, 
            "port" : ip_port, 
            "username" : ip_username, 
            "password" : ip_password 
        }
        
        payload = {
            "captcha_key": Captcha,
            "consent": "true",
            "date_of_birth": birthday,
            "email": email,
            "fingerprint": fingerprint,
            "gift_code_sku_id": "null",
            "invite": "null",
            "password": password,
            "username": username
        }
        headers = {
            
            "cookies": f"__dcfduid={dcfduid}; __sdcfduid={sdcfduid}",
            "origin": "https://discord.com",
            "referer": "https://discord.com/register",
            "user-agent": user_agent,
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-fingerprint": fingerprint,
            "x-super-properties": x_super_prop
        }
        payload = json.dumps(payload)
        try:
            conn = auth_proxy_request(proxy_details['url'], proxy_details['port'], proxy_details['username'], proxy_details['password'], "POST", "/api/v9/auth/register", payload, headers)
            response = conn.getresponse()
        except Exception:
            print("Proxy Remote end closed connection without response!")
            return
        data = response.read().decode()
        if "token" not in str(data):
            print("|>" + Fore.LIGHTMAGENTA_EX +" Looks like the Captcha Solver returned an invalid response or maybe a ratelimit!")
            return
        else:
            data = data.replace('{"token": "', '')
            data = data.replace('"}', '')
            token = data
            print("|>" + Fore.LIGHTGREEN_EX + f" Created Account {token}")
            file = open("data/tokens.txt", "a+")
            file.write(f"{email}:{password}:{token}\n")
            file.close()
            if use_hotmailbox == True:
                print("|>" + Fore.CYAN + f" Attemping To Email Verify {token}")
                verify_mail = verify_email(token, email, email_password, fingerprint, dcfduid, sdcfduid)
            if use_5sim == True:
                print("|>" + Fore.CYAN + f" Attempting to Phone Verify {token}")
                res = verify_phone(proxy, token, password, dcfduid, sdcfduid)
            else:
                return
            return

# Every Single Thread runs through this 
class Thread(threading.Thread):
    def run(self):
        global index_pos
        global proxy_recycle_message_sent
        while True:
            if if_ip_auth == False:
                try:
                    with next(proxies) as proxy:
                        proxy = proxy
                        if proxy in blacklisted_IPS:
                            print("Skipping proxy cuz previous connection issues!")
                        if use_custom_usernames == True:
                            data = []
                            try:
                                with open(f"data/{custom_username_file}", "r+") as f:
                                    dataa = f.readlines()
                            except FileNotFoundError:
                                print(f"File {custom_username_file} not found!")
                                time.sleep(15)
                                exit(0)
                            for line in dataa:
                                line = line.replace("\n", "")
                                data.append(line)
                            username = random.choice(data)
                            generate_account = create_account(proxy, username)
                        else:
                            generate_account = create_account(proxy)
                        return self.run()
                except Exception as err:
                    if show_proxy_errors == True:
                        print("|>"+ Fore.RED + f" Proxy Error: {err}")
                    else:
                        print("|>" + Fore.RED + " Proxy Error")
                    blacklisted_IPS.append(proxy)
            else:
                if index_pos == total_auth_proxies:
                    if proxy_recycle_message_sent == False:
                        print("Went through all proxies, please wait around 5 minutes before using them again!!!")
                    proxy_recycle_message_sent = True
                    time.sleep(8)
                    index_pos = 0
                    return self.run()

                try:
                    proxy = auth_proxies[index_pos]
                except IndexError:
                    if proxy_recycle_message_sent == False:
                        print("Went through all proxies, please wait around 5 minutes before using them again!!!")
                    proxy_recycle_message_sent = True
                    time.sleep(8)
                    index_pos = 0
                    return self.run()

                index_pos += 1
                if use_custom_usernames == True:
                    data = []
                    try:
                        with open(f"data/{custom_username_file}", "r+") as f:
                            dataa = f.readlines()
                    except FileNotFoundError:
                        print(f"File {custom_username_file} not found!")
                        time.sleep(15)
                        exit(0)
                    for line in dataa:
                        line = line.replace("\n", "")
                        data.append(line)
                    username = random.choice(data)
                    generate_account = create_account(proxy, username)
                else:
                    generate_account = create_account(proxy)
                return self.run()

# Function Initiates Threads to start running
def main():
    print(Fore.GREEN + "Started Generator!")
    threads = [Thread() for _ in range(threadss)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

# ASCII menu for choices and stuff
def menu():
    clear_screen()
    print("")
    print(Fore.RED + "                      /$$$$$$    /$$      /$$$$$$                   /$$$$$$                     ")
    print(Fore.LIGHTMAGENTA_EX + "                     /$$$_  $$  | $$     /$$$_  $$                 /$$__  $$                    ")
    print(Fore.LIGHTGREEN_EX + "  /$$$$$$   /$$$$$$ | $$$$\ $$ /$$$$$$  | $$$$\ $$ /$$$$$$$       | $$  \__/  /$$$$$$  /$$$$$$$ ")
    print(Fore.GREEN + " /$$__  $$ /$$__  $$| $$ $$ $$|_  $$_/  | $$ $$ $$| $$__  $$      | $$ /$$$$ /$$__  $$| $$__  $$")
    print(Fore.BLUE + "| $$  \ $$| $$  \__/| $$\ $$$$  | $$    | $$\ $$$$| $$  \ $$      | $$|_  $$| $$$$$$$$| $$  \ $$")
    print(Fore.LIGHTCYAN_EX + "| $$  | $$| $$      | $$ \ $$$  | $$ /$$| $$ \ $$$| $$  | $$      | $$  \ $$| $$_____/| $$  | $$")
    print(Fore.LIGHTRED_EX + "| $$$$$$$/| $$      |  $$$$$$/  |  $$$$/|  $$$$$$/| $$  | $$      |  $$$$$$/|  $$$$$$$| $$  | $$")
    print(Fore.LIGHTMAGENTA_EX + "| $$____/ |__/       \______/    \___/   \______/ |__/  |__/       \______/  \_______/|__/  |__/")
    print(Fore.YELLOW + "| $$                                                                                            ")
    print(Fore.LIGHTGREEN_EX + "| $$                                                                                            ")
    print(Fore.LIGHTBLUE_EX + "|__/                                                                                            \n")
    print(f"Version: {Version}")
    check_up_to_date()
    print("1) Start")
    print("2) Check Config")
    print("3) Links")
    print("4) Credits")
    print("5) Check tokens (token)")
    print("6) Convert from email:password:token to Token")
    print("7) Exit\n")
    choice = input("Choice: ")
    choice = int(choice)
    clear_screen()
    if choice == 1:
        return main()
    elif choice == 2:
        print("config.json Configurations\n")
        print(f"Threads Running: {threadss}")
        print(f"2Captcha API key: {twocaptcha_API}")
        print(f"AntiCaptcha API key: {anticaptcha_API}")
        print(f"CapMonster API key: {capmonster_API}")
        print(f"InvisiFox API key: {InvisiFox_api_key}")
        print(f"Use Capmonster API: {use_capmonster}")
        print(f"Use 2captcha API: {use_2captcha}")
        print(f"Use InvisiFox API: {use_InvisiFox}")
        print(f"Use Username:Pass@IP:PORT proxy format: {if_ip_auth}")
        print(f"Password for accounts: {password}")
        print(f"Hotmailbox API key: {hotmailbox_API_key}")
        print(f"Use Hotmailbox API: {use_hotmailbox}")
        print(f"Generate random passwords: {gen_passwords}")
        print(f"Date of Birth for accounts: {birthday}")
        print(f"Display Proxy Errors: {show_proxy_errors}")
        print(f"Join Server on token Creation: {join_server}")
        print(f"Invite Link to join on token creation: {invite_link}")
        print(f"Use proxies for capmonster: {use_proxies_for_capmonster}")
        print(f"5sim API key: {fivesim_API}")
        print(f"Use 5sim: {use_5sim}")
        print(f"5sim OPERATOR: {operator}")
        print(f"5sim COUNTRY: {country}")
        print(f"Generating {token_type}\n\n")
        input("Click Enter to return to menu")
        return menu()
    elif choice == 3:
        print("Github Link: https://github.com/Pr0t0ns/Discord-Token-Generator\n")
        print("Telegram Link: https://t.me/+Tvbz-xGh_5pjYzVh")
        print("Discord Server Link: https://discord.gg/FSqsR2HEJR")
        print("Discord Username: JTW#1427")
        print("Telegram Name: @FounderMainMarket")
        input("Click Enter to return to menu")
        return menu()
    elif choice == 4:
        print("Lead Developer: Pr0t0n (JTW, FounderMainMarket)\nContributors: LocalMOD (FWAuto), surreal, manu\nTo become a contributor all you have to do is make a good suggestion or report a real program issue!")
        input("Click Enter to return to menu")
        return menu()
    elif choice == 5:
        locked = 0
        unlocked = 0
        locked_tokens = []
        file = input("Enter the file where your tokens are located: ")
        output = input("Enter the output for the valid tokens: ")
        if ".txt" not in file:
            file += '.txt'
        try:
            with open(f"data/{file}", 'r+') as f:
                data = f.readlines()
                f.close()
        except FileNotFoundError:
            print(f"File data/{file} not found!")
            time.sleep(15)
            exit(0)
        if ".txt" not in output:
            output += ".txt"
        try:
            with open(f"data/{output}", 'a+') as f1:
                pass
        except FileNotFoundError:
            print(f"File data/{file} not found!")
            time.sleep(15)
            exit(0)
        f1 = open(f"data/{output}", "a+")
        f1.truncate(0)
        for token in data:
            data = TokenUtils.check_token(token)
            if data == False:
                print("|> " + Fore.LIGHTGREEN_EX + f"Token Unlocked {token}")
                f1.write(f"{token}\n")
                unlocked += 1
            else:
                print("|> " + Fore.LIGHTRED_EX + f"Token Locked {token}")
                locked_tokens.append(token)
                locked += 1
        f1.close()
        print(f"checked all tokens\nResults\nLocked: {locked}\nUnlocked: {unlocked}\nAll valid tokens are in the {output} file\n\n")
        input("Click enter to return to the main menu!")
        return menu()
    elif choice == 6:
        tokens = []
        tokens_parsed = 0
        file = input("Enter the file where your tokens are located: ")
        if ".txt" not in file:
            file += '.txt'
        try:
            with open(f"data/{file}", 'r+') as f:
                data = f.readlines()
                f.close()
        except FileNotFoundError:
            print(f"File data/{file} not found!")
            time.sleep(15)
            exit(0)
        
        for token in data:
            token = TokenUtils.parse_email_password_token(token)
            tokens.append(token)
        try:
            file = open("data/tokens.txt", "a+")
            file.truncate(0)
            file.close()
        except FileNotFoundError:
            print("tokens.txt file not found please create one and rerun this command!")
            time.sleep(15)
            exit(0)
        file = open("data/tokens.txt", "a+")
        for token in tokens:
            file.write(f"{token}\n")
            tokens_parsed += 1
        file.close()
        print(f"Parsed {tokens_parsed} Tokens")
        input("Click enter to return to main menu")
        return menu()
    elif choice == 7:
        exit(0)
    else:
        print("Option Not found")
        time.sleep(3)
        return menu()

#Calling menu function
menu()
