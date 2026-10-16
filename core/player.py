import miniaudio

def play_music(path):
    p = miniaudio.stream_file(path)

    with miniaudio.PlaybackDevice() as device:
        device.start(p)
        input("Playing... press Enter to stop")