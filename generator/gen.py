
# MADE BY PR0T0N!!! I am working on adding Email Verification and Phone Verification!
import colorama
from colorama import init, Fore
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
from capmonster_python import HCaptchaTask
from anticaptchaofficial.hcaptchaproxyless import *
blacklisted_IPS = []
IPS_in_use = []
auth_proxies = []
total_auth_proxies = 0
index_pos = 0
Version = "V1.4"

init(convert=True)
colorama.init(autoreset=True)
site_key = "4c672d35-0701-42b2-88c3-78380b0db560"
with open("config.json") as config:
    config = json.load(config)
    anticaptcha_API = config["anticaptcha_api_key"]
    capmonster_API = config["capmonster_api_key"]
    use_capmonster = config["use_capmonster"]
    threadss = config['threads']
    password = config['password']
    birthday = config['Date_of_birth']
    show_proxy_errors = config['Display_proxy_errors']
    join_server = config['Join_Server_On_Creation']
    invite_link = config['Server_Invite']
    if_ip_auth = config['user:pass@ip:port format']
    del config
try:
	ctypes.windll.kernel32.SetConsoleTitleW(f"[FREE] Pr0t0n Generator | {Version} | Threads: {threadss}")
except:
	pass
with open("proxies.txt") as proxy:
    if if_ip_auth == False:
        proxies = ProxyPool(proxy.read().splitlines())
    else:
        proxies = proxy.read().splitlines()
        for proxy in proxies:
            auth_proxies.append(proxy)
            total_auth_proxies += 1
def solve_captcha():
    if capmonster_API != "" and use_capmonster == True:
        print("|>" + Fore.YELLOW + " Solving Captcha")
        capmonster = HCaptchaTask(capmonster_API)
        task_id = capmonster.create_task("https://discord.com", site_key)
        result = capmonster.join_task_result(task_id)
        g_response = result.get("gRecaptchaResponse")
        return g_response
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
        return fingerprint
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

        return fingerprint
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

def create_account(proxy):
    if proxy in IPS_in_use:
        return
    IPS_in_use.append(proxy)
    if if_ip_auth == True:
        ip_username, ip_password, ip_ip, ip_port = parse_auth_proxy(proxy)
    fingerprint = get_fingerprint(proxy)
    username = generate_username(random.randint(8, 12))
    email = generate_email(random.randint(9, 13))
    Captcha = solve_captcha()
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
            return
def clear_screen():
    os.system("clear")
    os.system("cls")
    return
class Thread(threading.Thread):
    def run(self):
        global index_pos
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
                    print("Went through all proxies, please wait around 5 minutes before using them again!!!")
                    time.sleep(8)
                    exit(0)
                try:
                    proxy = auth_proxies[index_pos]
                except IndexError:
                    print("Went through all proxies, please wait around 5 minutes before using them again!!!")
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
        print(f"Invite Link to join on token creation: {invite_link}\n")
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
