from pathlib import Path

def local_music_loc(p: Path):
    music_list = []
    for x in p.iterdir():
        music_list.append(x.resolve())
    return music_list

def get_music(p: str):
    path = Path(p)
    print(path.is_dir())
    if path.exists():
        return local_music_loc(path)
    else:
        return []


