from pytube import YouTube

link = input('enter the link: ')
yt = YouTube(link)
yt.streams.filter(progressive=True,file_extension="mp4")
yt.streams.get_highest_resolution().download()
