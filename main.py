from core.player import play_music
from sources.list_all import get_music

def main():
    start = True
    while start:
        p = input("Input your path: ")
        songs = get_music(p)
        while songs == []:
            p = input("Input your path: ")
            songs = get_music(p)
        for x, song in enumerate(songs, start=1):
                print(f'{x}: {song.name}')
        i = input("Select a song number: ")
        while not i.isdigit() or not (1 <= int(i) <= len(songs)):
            print("Make sure to input an Integer that matches the given ones.")
            i = input("Select a song number: ")
        index = int(i) - 1
        play_music(str(songs[index]))
        if input("C for close ").upper() == "C": start = False





if __name__ == '__main__':
    main()