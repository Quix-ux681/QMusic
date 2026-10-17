from core.player import play_music
from sources.list_all import get_music

def main():
    p = input("Input your path: ")
    songs = get_music(p)
    for x, song in enumerate(songs):
            print(f'{x}: {song.name}')
    i = input("Select a song number: ")
    while not i.isdigit() or not (1 <= int(i) <= len(songs) - 1):
        print("Make sure to input an Integer that matches the given ones.")
        i = input("Select a song number: ")
    index = int(i)

    play_music(str(songs[index]))

if __name__ == '__main__':
    main()