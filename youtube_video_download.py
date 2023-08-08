from pytube import YouTube
link = "https://www.youtube.com/watch?v=aTz4C-9PrHY"
youtube_1 = YouTube(link)

print(youtube_1.title) #youtube video title

print(youtube_1.thumbnail_url)  #youtube video thumbnail
videos  = youtube_1.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)

strm = int(input("enter : "))
videos[strm].download()
print("Succesfully")
