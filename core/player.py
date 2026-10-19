import miniaudio

def play_music(path: str):
    p = miniaudio.stream_file(path)

    with miniaudio.PlaybackDevice() as device:
        device.start(p)
