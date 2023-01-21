# Heynotbot 
artinya apa bang messi?


kamu adalah pencari OG paling hebat sedunia

# Disclaimer :
menggunakan script ini berarti setuju dg segala resiko yg di akibatkan
saya tidak bertanggung jawab apabila akun discordmu ke ban, harga btc turun , puan jadi presiden, dll. setelah menggunakan =script ini

script ini hasil edit dari beberapa sumber


# Fitur dan lain lain
1. multi account
2. multi channel
3. send messages yg sudah diatur sendiri di pesan.txt
   - minus : karna menggunakan random order kalo kata didalam pesan.txt sedikit maka bakalan banyak pengulangan 
   - solusi : perbanyak pembendaharaan kata di pesan.txt atau gunakan saja untuk channel khusus spam
4. copas messages atau repost messages yg sebelumnya sudah dikirim orang lain di channel tujuan
   - minus : kalau server sepi maka akan terjadi pengulangan karna pesan yg di copas max 70 pesan sebelumnya
             jadi kalau hanya ada 50 pesan di channel tsb maka script akan mengirim 20 pesan yg sama baru pesan ke 21 beda
   - solusi : gunakan pada channel yg rame 
5. delete message (otomatis menghapus pesan yg dikirim oleh script sebelumnya)
   - minus : rada aneh juga kalo level bnyak tp history chat ga ada

# How to install in linux or VPS:

```
apt-get update
```
```
apt-get install git
```
```
git clone https://github.com/umyams/heynotbot
```
```
apt install python
```
```
apt install python3
```
```
cd heynotbot
pip install -r requirements.txt
```

# Konfigurasi
sebelum menjalankan script kita setting dulu file settings.yaml
bisa menggunakan command 
```
nano settings.yaml
```
dan pesan.txt
```
nano pesan.txt
```
untuk save CTRL+X > Y > ENTER

bisa juga pake cara lain ===>>> cek tutor di dc

settings.yaml
```
TOKEN: 
  - ODAtsgu7c4hMxxxxxxxxxxxxxxxxxxxx   # Token akun discordmu, untuk multi akun bisa ditambahi sepuasnya
  - Mzuan73gdi3xxxxxxxxxxxxxxxxxxxxx   # tergantung spek vps mu, 
CHANNEL_ID: 
  - 12345xxxxxxxxxxxxxx                # channel ID server tujuan, untuk multi channel bisa ditambahi sepuasnya
  - 67890xxxxxxxxxxxxxx                # tergantung spek vps mu,
MODE:                                  # mode (teks,copas) untuk mode teks bisa dikosongi atau di tulis "teks"
                                       # untuk mode copas tinggal di isi "copas" 
                                       
DELAY: 10                              # delay dalam detik(second)

DELETE_MSG:                            # fitur untuk delete pesan (kosongi untuk menonaktifkan, isi dg "Y" untuk mengaktifkan)
```

pesan.txt
tinggal diedit sesuka hati pisahkan tiap kata dg enter

untuk tutor mendapatkan token discord dan channel id check dc

# Start Script
pastikan sudah berada di folder heynotbot jika belum gunakan command
```
cd heynotbot
```
lalu untuk menjalankan script
```
python3 start.py
```

untuk menghentikan script menggunkan CTRL+C

agar script bisa tetap berjalan ketika tidak terhubung dg vps gunakan command "screen"
untuk tuto screen check DC
