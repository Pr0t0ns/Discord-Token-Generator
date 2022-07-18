# Made a new file so gen.py doesn't get to messy also made it so you can add to your own project and check tokens and parse tokens simply and swiftly
import requests
import json

class TokenUtils:

    def check_token(token):
        url = "https://discord.com/api/v9/users/@me/billing/payment-sources"
        token = token.replace("\n", "")
        headers = {
            "authorization": token,
            "cookie": "__dcfduid=29fe1a9006a611edbb902108d1ecd517; __sdcfduid=29fe1a9106a611edbb902108d1ecd517768118c357086cde2d237c2268657ae53c501bc01849155283d04de596e059b7; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Mon+Jul+18+2022+10%3A31%3A22+GMT-0400+(Eastern+Daylight+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F%40me&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __cf_bm=inThuqheyf4Z1ix.wHqpcgZqvTjTpXzu8cd8EyCwcnE-1658154683-0-AY4x/D+8+CjIa5PYJmA95kN+sZxYgXlxCijunlpIujVgx0wZ5jJ5AOXNgw28Pl08MMJaZWQAFbdfzu+YOECiEWnaMWzVzPj2NvxM7c9ezwR9A2QsISyYXI4RudjpV6isIw==",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAzLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjEzNzA5NSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0"
        }   
    
        result = requests.get(url, headers=headers)
        if "Unauthorized" in result.text:
            return True
        else:
            return False 
        

    def parse_email_password_token(token):
        token = token.replace("\n", "")
        token = token[-70:]
        return token





