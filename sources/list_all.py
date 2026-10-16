from pathlib import Path

def local_music_loc():
    p = Path(input("Input your path: "))
    music_list = []
    for x in p.iterdir():
        music_list.append(x.resolve())
    return music_list

def get_music(source):
    if source == 'local':
        return local_music_loc()


