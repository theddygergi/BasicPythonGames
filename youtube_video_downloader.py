from pytube import YouTube

def download_video(url):
    try:
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download()
        
        print('Video downloaded successfully')
    except Exception as e:
        print("An error occured while downloading:",str(e))


vid_url = input("Enter the url: ")
download_video(vid_url)