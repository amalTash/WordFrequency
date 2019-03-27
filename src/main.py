from word import *
def main():
    while True:
        try:
            print("***Find song from lyrics.wikia.com***")
            userArtist=input("Enter name of artist: ")
            userSong=input("Enter song name: ")
            obj = WordFreq(userArtist,userSong)
            lyricData=obj.cleanData()
            obj.pushToDict(lyricData)
            obj.writeToFile()
            obj.appearMost()
            print("***Frequency generated, check freqword.json***")
            toQuit=input("Do you want to quit? (y/n): ")
            if(toQuit.lower()=='y'):
                break
            else:
                continue
        except ValueError:
            print("Try again, artist or song does not exist")

if __name__=='__main__':
    main()
