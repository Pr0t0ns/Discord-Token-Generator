# MADE BY PR0T0N!!! Working on adding AI Solver 
# Telegram link: https://t.me/+Tvbz-xGh_5pjYzVh
# New Discord Server: https://discord.gg/FSqsR2HEJR
from utils import TokenUtils
import colorama
from colorama import init, Fore
from structures import ProxyPool, Proxy
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
check_users = "https://WeeReflectingWaterfall.crypticsserver.repl.co/users"
response2 = requests.get(check_users)
data2 = response2.text
data2 = "{:,}".format(int(data2))
host_details = {
    "url" : "discord.com",
    "port" : 443 
}
blacklisted_IPS = []
IPS_in_use = []
auth_proxies = []
char_symbols = ["!", "@", "#", "$", "5"]
total_auth_proxies = 0
index_pos = 0
Version = "V1.7"
bot = InvisiFox()
proxy_recycle_message_sent = False
init(convert=True)
colorama.init(autoreset=True)
product = 'discord'
site_key = "4c672d35-0701-42b2-88c3-78380b0db560"
email_site_key = "f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"
with open("config.json") as config:
    config = json.load(config)
    anticaptcha_API = config["anticaptcha_api_key"]
    capmonster_API = config["capmonster_api_key"]
    twocaptcha_API = config['2captcha_API_key']
    InvisiFox_api_key = config['invisiFox_API_key']
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
    del config
bot.apiKey = InvisiFox_api_key
token_type = ""
_5s_token = fivesim_API

if use_5sim == True and use_hotmailbox == True:
    token_type = "Email & Phone Verified Tokens"
elif use_5sim == True and use_hotmailbox == False:
    token_type = "Phone Verified Tokens"
elif use_5sim == False and use_hotmailbox == True:
    token_type = "Email Verified Tokens"
else:
    token_type = "Unverified Tokens"


try:
	ctypes.windll.kernel32.SetConsoleTitleW(f"[FREE] Pr0t0n Generator | {Version} | Threads: {threadss} | Token Type: {token_type}")
except:
	pass


def purchase_email():
    url = f"https://api.hotmailbox.me/mail/buy?apikey={hotmailbox_API_key}&mailcode=HOTMAIL&quantity=1"
    r = requests.get(url)
    data = r.json()
    email = data['Data']['Emails'][0]['Email']
    email_password = data['Data']['Emails'][0]['Password']
    return email, email_password

def auth_proxy_request(url, port, username, password, method, route, payload, headers):
    conn = http.client.HTTPSConnection(url, port)
    auth = '%s:%s' % (username, password)
    headers['Proxy-Authorization'] = 'Basic ' + str(base64.b64encode(auth.encode())).replace("b'", "").replace("'", "")
    conn.set_tunnel(host_details['url'], host_details['port'], headers)
    conn.request(method, route, payload, headers)
    return conn

def parse_ip_port_proxy(proxy):
    IP = proxy.split(":")[0].replace('\n', '')
    PORT = proxy.split(":")[1].replace('\n', '')
    return IP, PORT


with open("proxies.txt") as proxy:
    if if_ip_auth == False:
        proxies = ProxyPool(proxy.read().splitlines())
    else:
        proxies = proxy.read().splitlines()
        for proxy in proxies:
            auth_proxies.append(proxy)
            total_auth_proxies += 1



def solve_captcha(site_key, proxy=None):
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
    elif use_InvisiFox == True and proxy == None:
        print("To use InvisiFox as your Captcha provider you are required to pass in a proxy!")
        return "Error"
    elif use_InvisiFox == True and proxy != None:
        print("|>" + Fore.YELLOW + " Solving Captcha")
        if if_ip_auth == True:
            try:
                solution = bot.solveHCaptcha(site_key, 'https://discord.com', f'http://{proxy}')
            except Exception as error:
                print("There was an error trying to solve captcha using InvisiFox!")
                time.sleep(0.1)
                return "error"
            print("|>" + Fore.GREEN + " Solved Captcha")
            return solution
        else:
            try:
                solution = bot.solveHCaptcha(site_key, 'https://discord.com', proxy)
            except Exception as error:
                print(f"There was an error trying to solve captcha using InvisiFox! {error}")
                time.sleep(0.1)
                return "error"
            print("|>" + Fore.GREEN + " Solved Captcha")
            return solution
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
        headers = {}
        payload = {}
        try:
            conn = auth_proxy_request(proxy_details['url'], proxy_details['port'], proxy_details['username'], proxy_details['password'], "GET", "/api/v9/experiments", payload, headers)
        except http.client.RemoteDisconnected:
            print("Auth Proxy Error")
            return None, None, None
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


def verify_phone(proxy, discord_token, discord_password):
    if use_5sim == True:
        
        headers = {
            'Authorization': 'Bearer ' + _5s_token,
            'Accept': 'application/json',
        }
        response = requests.get('https://5sim.net/v1/user/buy/activation/' + country + '/' + operator + '/' + product, headers=headers)
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
                "cookie": "__dcfduid=156676b0e52511ecab049748e388ba01; __sdcfduid=156676b1e52511ecab049748e388ba016c54df50488a2d1e13423eba666addd5a3d24e93d46dddf02e471fa26e7d7b7a",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.33 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-US",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjUwNjAuMzMgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMy4wLjUwNjAuMzMiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwODMyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
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
                'Authorization': 'Bearer ' + _5s_token,
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
                "cookie": "__dcfduid=156676b0e52511ecab049748e388ba01; __sdcfduid=156676b1e52511ecab049748e388ba016c54df50488a2d1e13423eba666addd5a3d24e93d46dddf02e471fa26e7d7b7a",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.33 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-US",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjUwNjAuMzMgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMy4wLjUwNjAuMzMiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwODMyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
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
                "cookie": "__dcfduid=156676b0e52511ecab049748e388ba01; __sdcfduid=156676b1e52511ecab049748e388ba016c54df50488a2d1e13423eba666addd5a3d24e93d46dddf02e471fa26e7d7b7a",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.33 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-US",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjUwNjAuMzMgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMy4wLjUwNjAuMzMiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwODMyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
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
                'Authorization': 'Bearer ' + _5s_token,
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
                "cookie": "__dcfduid=156676b0e52511ecab049748e388ba01; __sdcfduid=156676b1e52511ecab049748e388ba016c54df50488a2d1e13423eba666addd5a3d24e93d46dddf02e471fa26e7d7b7a",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.33 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-US",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjUwNjAuMzMgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMy4wLjUwNjAuMzMiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwODMyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
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
                "cookie": "__dcfduid=156676b0e52511ecab049748e388ba01; __sdcfduid=156676b1e52511ecab049748e388ba016c54df50488a2d1e13423eba666addd5a3d24e93d46dddf02e471fa26e7d7b7a",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.33 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-US",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjUwNjAuMzMgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMy4wLjUwNjAuMzMiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwODMyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
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
        Verfication_Link = Verfication_Link.replace("\r", "")
        conn.request("GET", Verfication_Link, payload, headers)
        response = conn.getresponse()
        headers = response.getheaders()
        ans = [val for key, val in headers if key == 'Location'][0]
        str_ans = str(ans)
        url_token = str_ans.replace("https://discord.com/verify#token=", "")
        ans = ans[19:]
        captcha_key = solve_captcha(email_site_key, proxy)
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
        conn = auth_proxy_request(proxy_details['url'], proxy_details['port'], proxy_details['username'], proxy_details['password'], "POST", "/api/v9/auth/verify", payload, headers)
        r1 = conn.getresponse()
        if int(r1.status) == 200:
            print("|>" + Fore.LIGHTGREEN_EX + f" Email Verified {token}")
            return
        else:
            print("|>" + Fore.RED + " Issue Verifying Email!")
            return


def generate_passwords(length):
    length -= 2
    password = ""
    for i in range(length):
        letter = random.choice(string.ascii_lowercase)
        password += letter
    symbol1 = random.choice(char_symbols)
    symbol2 = random.choice(char_symbols)
    password += symbol1
    password += symbol2
    return password

def create_account(proxy):
    if proxy in IPS_in_use:
        return
    IPS_in_use.append(proxy)
    if if_ip_auth == True:
        ip_username, ip_password, ip_ip, ip_port = parse_auth_proxy(proxy)
    if gen_passwords == True:
        password = generate_passwords(random.randint(15, 19))
    fingerprint, dcfduid, sdcfduid = get_fingerprint(proxy)
    username = generate_username(random.randint(8, 12))
    email = generate_email(random.randint(9, 13))
    Captcha = solve_captcha(site_key, proxy)
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
            if use_5sim == True:
                print("|>" + Fore.CYAN + f" Attempting to Phone Verify {token}")
                res = verify_phone(proxy, token, password)
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
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-fingerprint": fingerprint,
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjEgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjEiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwMTUzLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
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
            file = open("tokens.txt", "a+")
            file.write(f"{email}:{password}:{token}\n")
            file.close()
            if use_hotmailbox == True:
                print("|>" + Fore.CYAN + f" Attemping To Email Verify {token}")
                verify_mail = verify_email(token, email, email_password, proxy)
            if use_5sim == True:
                print("|>" + Fore.CYAN + f" Attempting to Phone Verify {token}")
                res = verify_phone(proxy, token, password)
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
                generate_account = create_account(proxy)
                time.sleep(0.5)
                return self.run()

                
def main():
    print(Fore.GREEN + "Started Generator!")
    threads = [Thread() for _ in range(threadss)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def check_up_to_date():
    url = "https://WeeReflectingWaterfall.crypticsserver.repl.co"
    response = requests.get(url)
    data = response.text
    print(Fore.WHITE + f"Total Users: {data2}")
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
        print(f"Generating {token_type}\n")
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
        file = input("Enter the file where your tokens are located: ")
        if ".txt" not in file:
            file += '.txt'
        try:
            with open(file, 'r+') as f:
                data = f.readlines()
                f.close()
        except FileNotFoundError:
            print(f"File {file} not found!")
            time.sleep(15)
            exit(0)
        
        for token in data:
            data = TokenUtils.check_token(token)
            if data == False:
                print("|> " + Fore.LIGHTGREEN_EX + f"Token Unlocked {token}")
                unlocked += 1
            else:
                print("|> " + Fore.LIGHTRED_EX + f"Token Locked {token}")
                locked += 1
        print(f"checked all tokens\nResults\nLocked: {locked}\nUnlocked: {unlocked}")
        input("Click enter to return to the main menu!")
        return menu()
    elif choice == 6:
        tokens = []
        tokens_parsed = 0
        file = input("Enter the file where your tokens are located: ")
        if ".txt" not in file:
            file += '.txt'
        try:
            with open(file, 'r+') as f:
                data = f.readlines()
                f.close()
        except FileNotFoundError:
            print(f"File {file} not found!")
            time.sleep(15)
            exit(0)
        
        for token in data:
            token = TokenUtils.parse_email_password_token(token)
            tokens.append(token)
        try:
            file = open("tokens.txt", "a+")
            file.truncate(0)
            file.close()
        except FileNotFoundError:
            print("tokens.txt file not found please create one and rerun this command!")
            time.sleep(15)
            exit(0)
        file = open("tokens.txt", "a+")
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
menu()
