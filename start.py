import random, yaml, time, sys, requests
class Discord:

    def __init__(self, t):
        self.base = "https://discord.com/api/v10"
        self.auth = { 'authorization': t }
        
    def getMe(self):
        m = requests.get(self.base + "/users/@me", headers=self.auth).json()
        return m
        
    def getMessage(self, cid, l):
        m = requests.get(self.base + "/channels/" + str(cid) + "/messages?limit=" + str(l), headers=self.auth).json()
        return m
        
    def sendMessage(self, cid, txt):    
        m = requests.post(self.base + "/channels/" + str(cid) + "/messages", headers=self.auth, json={ 'content': txt }).json()
        return m

    def deleteMessage(self, cid, mid):
        m = requests.delete(self.base + "/channels/" + str(cid) + "/messages/" + str(mid), headers=self.auth)
        return m
with open("pesan.txt", "r") as f:
    words = f.readlines()
def main():
    with open('settings.yaml') as cfg:
        conf = yaml.load(cfg, Loader=yaml.FullLoader)

    if not conf['TOKEN']:
        print("Periksa Token anda di settings.yaml")
        sys.exit()

    if not conf['CHANNEL_ID']:
        print("masukkan Channel ID di settings.yaml")
        sys.exit()

    mode = conf['MODE']
    delay = conf['DELAY']
    del_msg = conf['DELETE_MSG']
    
    if not mode: 
        mode = "teks"

    while True:
        for token in conf['TOKEN']:
            try:

                for chan in conf['CHANNEL_ID']:

                    Bot = Discord(token)
                    me = Bot.getMe()['username'] + "#" + Bot.getMe()['discriminator']
                    
                    if mode == "teks":
                        te = random.choice(words).strip()
                        send = Bot.sendMessage(chan, te)
                        print("[{}][{}] {}".format(me, chan, te))                
                        if del_msg:
                            Bot.deleteMessage(chan, send['id'])
                            print("[{}][DELETE] {}".format(me, send['id']))

                    elif mode == "copas":
                        res = Bot.getMessage(chan, 70)
                        getlast = list(reversed(res))[0]                    
                        send = Bot.sendMessage(chan, getlast['content'])
                        print("[{}][{}] {}".format(me, chan, getlast['content']))
                        if del_msg:
                            Bot.deleteMessage(chan, send['id'])
                            print("[{}][DELETE] {}".format(me, send['id']))
                        
            except:
                print(f"[Error] {token} : TOKEN INVALID ATAU USER DI BAN DARI SERVER, CEK COBA")
        
        print("delay {} detik".format(delay))
        time.sleep(delay)

if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print(f"{type(err).__name__} : {err}")
