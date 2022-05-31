# MADE BY PR0T0N!!! I am working on adding Email Verification and Phone Verification!
from ast import For
import colorama
from colorama import init, Fore
from structures import ProxyPool, Proxy
import threading
import json
import time
import random
import string
from anticaptchaofficial.hcaptchaproxyless import *
blacklisted_IPS = []
IPS_in_use = []
init(convert=True)
colorama.init(autoreset=True)
site_key = "4c672d35-0701-42b2-88c3-78380b0db560"
with open("config.json") as config:
    config = json.load(config)
    anticaptcha_API = config["anticaptcha_api_key"]
    threadss = config['threads']
    password = config['password']
    birthday = config['Date_of_birth']
    show_proxy_errors = config['Display_proxy_errors']
    join_server = config['Join_Server_On_Creation']
    invite_link = config['Server_Invite']
    del config

with open("proxies.txt") as proxy:
    proxies = ProxyPool(proxy.read().splitlines())
def solve_captcha():
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
def get_fingerprint(proxy: Proxy):
    conn = proxy.get_connection("discord.com")
    conn.putrequest("GET", "/api/v9/experiments")
    conn.endheaders()
    response = conn.getresponse()
    response = response.read()
    fingerprint = json.loads(response)
    fingerprint = fingerprint['fingerprint']
    return fingerprint

def create_account(proxy: Proxy):
    if proxy in IPS_in_use:
        return
    IPS_in_use.append(proxy)
    fingerprint = get_fingerprint(proxy)
    username = generate_username(random.randint(8, 12))
    email = generate_email(random.randint(9, 13))
    Captcha = solve_captcha()
    conn = proxy.get_connection("discord.com")
    print("|>" + Fore.LIGHTWHITE_EX +" Established Connection to discord using Proxy")
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
class Thread(threading.Thread):
    def run(self):
        while True:
            try:
                with next(proxies) as proxy:
                    proxy = proxy
                    if proxy in blacklisted_IPS:
                        print("Skipping proxy cuz pervious connection issues!")
                    generate_account = create_account(proxy)
                    return self.run()
            except Exception as err:
                if show_proxy_errors == True:
                    print("|>"+ Fore.RED + f" Proxy Error: {err}")
                else:
                    print("|>" + Fore.RED + " Proxy Error")
                blacklisted_IPS.append(proxy)
def main():
    threads = [Thread() for _ in range(threadss)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

main()
