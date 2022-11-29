import requests, urllib.request, sys, os, time, ssl

try:
    if sys.platform.startswith('linux'):
        os.system("clear")
    elif sys.platform.startswith('win32'):
        os.system("cls")
except:
    pass
    
print("░█▀▀░█▄█░█▀▀░█▀▄░█▀▀░█▀▀░█▀█░█▀▀░█░█░░░░░█▀▄░█▀▀░█▀█░▀█▀".center(50))
print("░█▀▀░█░█░█▀▀░█▀▄░█░█░█▀▀░█░█░█░░░░█░░░░░░█▀▄░█▀▀░█▀█░░█░".center(50))
print("░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░░▀░░▀▀▀░▀▀░░▀▀▀░▀░▀░░▀░".center(50))
print("beatstars downloader by lovegap \n".center(50))
song_id = input("id: ")
name = input("name(optional): ")

ssl._create_default_https_context = ssl._create_unverified_context
if len(name) <= 0:
    name = "beat.mp3"
else:
    name = f"{name}.mp3"

song_url = f"https://main.v2.beatstars.com/stream?id={song_id}&return=audio"
def resolve(url):
    return urllib.request.urlopen(url).geturl()

r = requests.get(resolve(song_url))

with open(f"{name}", 'wb') as f:
    f.write(r.content)
    print(f"tu beat se ha descargado en {os.getcwd()}\\{name}")
    exit()
