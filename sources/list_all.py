from pathlib import Path

suffixes = {".3gp", ".ac3", ".act", ".aif", ".aifc", ".aiff", ".alac", ".amr", ".ape", ".au", ".avr", ".awb", ".caf", ".ds2", ".dsf", ".dff", ".dss", ".dts", ".dtshd", ".dvf", ".eac3", ".flac", ".gsm", ".htk", ".iff", ".it", ".kar", ".m4a", ".m4b", ".m4p", ".m4r", ".mid", ".midi", ".mlp", ".mod", ".mp1", ".mp2", ".mp3", ".mpc", ".msv", ".oga", ".ogg", ".opus", ".pcm", ".ra", ".raw", ".rm", ".rmi", ".s3m", ".sd2", ".sf2", ".shn", ".sln", ".snd", ".spc", ".svx", ".tta", ".voc", ".vox", ".vqf", ".wav", ".wma", ".wv", ".xm"}
def local_music_loc(p: Path):
    music_list = []
    for x in p.iterdir():
        if x.suffix in suffixes:
            music_list.append(x.resolve())
    if music_list != []:
        return music_list
    else:
        print("No music found...")
        return []


def get_music(p: str):
    path = Path(p)
    if path.is_dir():
        return local_music_loc(path)
    else:
        print("Path doesnt exist...n/")
        return []