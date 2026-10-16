from core.player import play_music
from sources.list_all import get_music

def main():
    source = "local"
    songs = get_music(source)
    for x, song in enumerate(songs):
        print(f'{x}: {song.name}')
    while not (i := input("Enter a song number: ")).isdigit(): print("Make sure to input an Integer")
    i = int(i)
    play_music(str(songs[i]))

if __name__ == '__main__':
    main() 