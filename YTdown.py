#A Very - Very Simple Youtuube Video Downloader

import os,sys,time
from pytube import YouTube

os.system('clear')

print("\033[91m  __  __     ______   _____     ______     __     __     __   __")
print("\033[91m /\ \_\ \   /\__  _\ /\  __-.  /\  __ \   /\ \  _ \ \   /\ '-.\ \ ")
print("\033[91m \ \____ \  \/_/\ \/ \ \ \/\ \ \ \ \/\ \  \ \ \/ '.\ \  \ \ \-.  \ ")
print("\033[91m  \/\_____\    \ \_\  \ \____-  \ \_____\  \ \__/'.~\_\  \ \_\\'\_\ By")
print("\033[91m   \/_____/     \/_/   \/____/   \/_____/   \/_/   \/_/   \/_/ \/_/ Qxzzhouz")

video_link = input('\033[94m Insert Your Link Here : ')
print("[+] Downloading")
yt = YouTube(video_link)
videos = yt.streams.first()
videos.download('hasil')
print('[+] Download Succes files saved in $HOME/YTdown/hasil')
os.system("exit")
if KeyboardInterrupt :
	sys.exit("[!] Keluar..")
else :	
	print("[!] Salah babyk!")