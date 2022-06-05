
# MADE BY PR0T0N!!! I am working on adding Email Verification and Phone Verification!
from ast import AnnAssign
import email
from http import cookies
import colorama
from colorama import init, Fore
from numpy import char, result_type
from structures import ProxyPool, Proxy
import threading
import json
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
blacklisted_IPS = []
IPS_in_use = []
auth_proxies = []
total_auth_proxies = 0
index_pos = 0
Version = "V1.5"
proxy_recycle_message_sent = False
init(convert=True)
colorama.init(autoreset=True)
site_key = "4c672d35-0701-42b2-88c3-78380b0db560"
with open("config.json") as config:
    config = json.load(config)
    anticaptcha_API = config["anticaptcha_api_key"]
    capmonster_API = config["capmonster_api_key"]
    twocaptcha_API = config['2captcha_API_key']
    use_2captcha = config['use_2captcha']
    use_capmonster = config["use_capmonster"]
    if use_2captcha == True and use_capmonster == True:
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
    
    del config
try:
	ctypes.windll.kernel32.SetConsoleTitleW(f"[FREE] Pr0t0n Generator | {Version} | Threads: {threadss}")
except:
	pass
def purchase_email():
    url = f"https://api.hotmailbox.me/mail/buy?apikey={hotmailbox_API_key}&mailcode=HOTMAIL&quantity=1"
    r = requests.get(url)
    data = r.json()
    email = data['Data']['Emails'][0]['Email']
    email_password = data['Data']['Emails'][0]['Password']
    return email, email_password

def parse_ip_port_proxy(proxy):
    IP = ""
    PORT = ""
    colons = False
    for character in proxy:
        if character == ":":
            colons = True
        else:
            if colons == False:
                IP += character
            else:
                PORT += character
    return IP, PORT
with open("proxies.txt") as proxy:
    if if_ip_auth == False:
        proxies = ProxyPool(proxy.read().splitlines())
    else:
        proxies = proxy.read().splitlines()
        for proxy in proxies:
            auth_proxies.append(proxy)
            total_auth_proxies += 1
def solve_email_captcha(proxy=None):
    site_key = "f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"
    if capmonster_API != "" and use_capmonster == True:
        if use_proxies_for_capmonster == True and proxy != None:
            if if_ip_auth == False:
                ip, port = parse_ip_port_proxy(proxy)
                print("|>" + Fore.YELLOW + " Solving Email Captcha")
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
            else:
                ip_username, ip_password, ip_ip, ip_port = parse_auth_proxy(proxy)
                print("|>" + Fore.YELLOW + " Solving Email Captcha")
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
        else:
            print("|>" + Fore.YELLOW + " Solving Email Captcha")
            capmonster = HCaptchaTask(capmonster_API)
            task_id = capmonster.create_task("https://discord.com", site_key)
            result = capmonster.join_task_result(task_id)
            g_response = result.get("gRecaptchaResponse")
            return g_response
    elif use_2captcha == True:
        print("|>" + Fore.YELLOW + " Solving Email Captcha")
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
            return result
    else:
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
def solve_captcha(proxy=None):
    if capmonster_API != "" and use_capmonster == True:
        if use_proxies_for_capmonster == True and proxy != None:
            if if_ip_auth == False:
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
            else:
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
        else:
            print("|>" + Fore.YELLOW + " Solving Captcha")
            capmonster = HCaptchaTask(capmonster_API)
            task_id = capmonster.create_task("https://discord.com", site_key)
            result = capmonster.join_task_result(task_id)
            g_response = result.get("gRecaptchaResponse")
            return g_response
    elif use_2captcha == True:
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
        
    else:
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
def generate_username(length):
    username = ""
    for i in range(int(length)):
        letter = random.choice(string.ascii_lowercase)
        username += letter
    return username

def generate_email(length):
    domains = ["@gmail.com", "@yahoo.com", "@outlook.com", "@hotmail.com", "@protonmail.com"]
    domain = random.choice(domains)
    email = ""
    for i in range(int(length)):
        letter = random.choice(string.ascii_lowercase)
        email += letter
    email += domain
    return email
def get_fingerprint(proxy):
    if if_ip_auth == False:
        conn = proxy.get_connection("discord.com")
        conn.putrequest("GET", "/api/v9/experiments")
        conn.endheaders()
        response = conn.getresponse()
        response = response.read()
        fingerprint = json.loads(response)
        fingerprint = fingerprint['fingerprint']
        session = requests.Session()
        cookiess = session.get("https://discord.com")
        cookiess = session.cookies.get_dict()
        dcfduid = cookiess.get("__dcfduid")
        sdcfduid = cookiess.get("__sdcfduid")
        return fingerprint, dcfduid, sdcfduid
    else:
        ip_username, ip_password, ip_ip, ip_port = parse_auth_proxy(proxy)
        proxy_details = {
            "url" : ip_ip, 
            "port" : ip_port, 
            "username" : ip_username, 
            "password" : ip_password 
        }
        host_details = {
            "url" : "discord.com",
            "port" : 443 
        }
        headers = {}
        payload = {}
        conn = http.client.HTTPSConnection(proxy_details['url'], proxy_details['port'])
        auth = '%s:%s' % (proxy_details['username'], proxy_details['password'])
        headers['Proxy-Authorization'] = 'Basic ' + str(base64.b64encode(auth.encode())).replace("b'", "").replace("'", "")
        conn.set_tunnel(host_details['url'], host_details['port'], headers)
        conn.request("GET", "/api/v9/experiments", payload, headers)
        response = conn.getresponse()
        response = response.read()
        fingerprint = json.loads(response)
        fingerprint = fingerprint['fingerprint']
        session = requests.Session()
        cookiess = session.get("https://discord.com")
        cookiess = session.cookies.get_dict()
        dcfduid = cookiess.get("__dcfduid")
        sdcfduid = cookiess.get("__sdcfduid")
        return fingerprint, dcfduid, sdcfduid
def parse_auth_proxy(proxy):
    proxy = proxy.replace("@", ":")
    colons_hit = 0
    ip_username = ""
    ip_password = ""
    ip_ip = ""
    ip_port = ""
    for character in proxy:
        if character == ":":
            colons_hit = colons_hit + 1
        else:
            if colons_hit == 0:
                ip_username += character
            elif colons_hit == 1:
                ip_password += character
            elif colons_hit == 2:
                ip_ip += character
            elif colons_hit == 3:
                ip_port += character
    return ip_username, ip_password, ip_ip, ip_port
def verify_email(token, username, password, proxy):
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
        conn.request("GET", Verfication_Link, payload, headers)
        response = conn.getresponse()
        headers = response.getheaders()
        ans = [val for key, val in headers if key == 'Location'][0]
        str_ans = str(ans)
        url_token = str_ans.replace("https://discord.com/verify#token=", "")
        ans = ans[19:]
        captcha_key = solve_email_captcha(proxy)
        fingerprint, dcfduid, sdcfduid = get_fingerprint(proxy)
        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "cookie": f"__dcfduid={dcfduid}; __sdcfduid={sdcfduid}; locale=en-US",
            "origin": "https://discord.com",
            "referer": "https://discord.com/verify",
            "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.33 Safari/537.36",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-fingerprint": fingerprint,
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjUwNjAuMzMgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMy4wLjUwNjAuMzMiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwODMyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
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
        host_details = {
            "url" : "click.discord.com",
            "port" : 443 
        }
        headers = {}
        payload = {}
        conn = http.client.HTTPSConnection(proxy_details['url'], proxy_details['port'])
        auth = '%s:%s' % (proxy_details['username'], proxy_details['password'])
        headers['Proxy-Authorization'] = 'Basic ' + str(base64.b64encode(auth.encode())).replace("b'", "").replace("'", "")
        conn.set_tunnel(host_details['url'], host_details['port'], headers)
        Verfication_Link = Verfication_Link.replace("\r\n\r\n", "")
        conn.request("GET", Verfication_Link, payload, headers)
        response = conn.getresponse()
        response = response.getheaders()
        ans = [val for key, val in response if key == 'Location'][0]
        str_ans = str(ans)
        url_token = str_ans.replace("https://discord.com/verify#token=", "")
        ans = ans[19:]
        captcha_key = solve_email_captcha(proxy)
        fingerprint, dcfduid, sdcfduid = get_fingerprint(proxy)
        host_details = {
            "url" : "discord.com",
            "port" : 443 
        }
        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "cookie": f"__dcfduid={dcfduid}; __sdcfduid={sdcfduid}; locale=en-US",
            "origin": "https://discord.com",
            "referer": "https://discord.com/verify",
            "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.33 Safari/537.36",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-fingerprint": fingerprint,
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjUwNjAuMzMgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMy4wLjUwNjAuMzMiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwODMyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
        }
        payload = {
            "captcha_key": captcha_key,
            "token": url_token
        }
        payload = json.dumps(payload)
        conn = http.client.HTTPSConnection(proxy_details['url'], proxy_details['port'])
        auth = '%s:%s' % (proxy_details['username'], proxy_details['password'])
        headers['Proxy-Authorization'] = 'Basic ' + str(base64.b64encode(auth.encode())).replace("b'", "").replace("'", "")
        conn.set_tunnel(host_details['url'], host_details['port'], headers)
        conn.request("POST", "/api/v9/auth/verify", payload, headers)
        r1 = conn.getresponse()
        if int(r1.status) == 200:
            print("|>" + Fore.LIGHTGREEN_EX + f" Email Verified {token}")
            return
        else:
            print("|>" + Fore.RED + " Issue Verifying Email!")
            return
        
def create_account(proxy):
    if proxy in IPS_in_use:
        return
    IPS_in_use.append(proxy)
    if if_ip_auth == True:
        ip_username, ip_password, ip_ip, ip_port = parse_auth_proxy(proxy)
    fingerprint, dcfduid, sdcfduid = get_fingerprint(proxy)
    username = generate_username(random.randint(8, 12))
    email = generate_email(random.randint(9, 13))
    Captcha = solve_captcha(proxy)
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
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-fingerprint": fingerprint,
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjEgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjEiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwMTUzLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
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
            file = open("tokens.txt", "a+")
            file.write(f"{email}:{password}:{token}\n")
            file.close()
            if use_hotmailbox == True:
                print("|>" + Fore.CYAN + f" Attemping To Email Verify {token}")
                verify_mail = verify_email(token, email, email_password, proxy)
                return
            else:
                return
    else:
        proxy_details = {
            "url" : ip_ip, 
            "port" : ip_port, 
            "username" : ip_username, 
            "password" : ip_password 
        }
        host_details = {
            "url" : "discord.com",
            "port" : 443 
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
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-fingerprint": fingerprint,
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjEgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjEiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwMTUzLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
        }
        payload = json.dumps(payload)
        conn = http.client.HTTPSConnection(proxy_details['url'], proxy_details['port'])
        auth = '%s:%s' % (proxy_details['username'], proxy_details['password'])
        headers['Proxy-Authorization'] = 'Basic ' + str(base64.b64encode(auth.encode())).replace("b'", "").replace("'", "")
        conn.set_tunnel(host_details['url'], host_details['port'], headers)
        try:
            conn.request("POST", "/api/v9/auth/register", payload, headers)
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
            file = open("tokens.txt", "a+")
            file.write(f"{email}:{password}:{token}\n")
            file.close()
            if use_hotmailbox == True:
                print("|>" + Fore.CYAN + f" Attemping To Email Verify {token}")
                verify_mail = verify_email(token, email, email_password, proxy)
            else:
                return
            return
def clear_screen():
    os.system("clear")
    os.system("cls")
    return
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
                    exit(0)
                try:
                    proxy = auth_proxies[index_pos]
                except IndexError:
                    if proxy_recycle_message_sent == False:
                        print("Went through all proxies, please wait around 5 minutes before using them again!!!")
                    proxy_recycle_message_sent = True
                    time.sleep(8)
                    exit(0)
                index_pos += 1
                generate_account = create_account(proxy)
                time.sleep(2)
                return self.run()
def main():
    print(Fore.GREEN + "Started Generator!")
    threads = [Thread() for _ in range(threadss)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
def check_up_to_date():
    url = "https://checkuptodate.crypticsserver.repl.co"
    response = requests.get(url)
    data = response.text
    if Version in data:
        print(Fore.LIGHTGREEN_EX + "Generator Up to Date!")
    else:
        print(Fore.RED + "Generator Out of date please update for new features!\nLink: https://github.com/Pr0t0ns/Discord-Token-Generator/releases")
    return
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
    print("3) Github Link")
    print("4) Credits")
    print("5) Exit\n")
    choice = input("Choice: ")
    choice = int(choice)
    clear_screen()
    if choice == 1:
        return main()
    elif choice == 2:
        print("config.json Configurations\n")
        print(f"Threads Running: {threadss}")
        print(f"AntiCaptcha API key: {anticaptcha_API}")
        print(f"CapMonster API KEY: {capmonster_API}")
        print(f"Use Capmonster API: {use_capmonster}")
        print(f"Use Username:Pass@IP:PORT proxy format: {if_ip_auth}")
        print(f"Password for accounts: {password}")
        print(f"Date of Birth for accounts: {birthday}")
        print(f"Display Proxy Errors: {show_proxy_errors}")
        print(f"Join Server on token Creation: {join_server}")
        print(f"Invite Link to join on token creation: {invite_link}")
        print(f"Use proxies for capmonster: {use_proxies_for_capmonster}\n")
        input("Click Enter to return to menu")
        return menu()
    elif choice == 3:
        print("Github Link: https://github.com/Pr0t0ns/Discord-Token-Generator\n")
        input("Click Enter to return to menu")
        return menu()
    elif choice == 4:
        print("Token Generator made completley by Pr0t0n mainly using http.client library\n")
        input("Click Enter to return to menu")
        return menu()
    elif choice == 5:
        exit(0)
    else:
        print("Option Not found")
        time.sleep(3)
        return menu()
menu()
