# Music Player

A music player I'm building from scratch in Python, with a one-of-a-kind look and a proper "new releases" feed.

> **Work in progress.** Right now it's a command-line prototype. The real interface comes later.

## Why

Most music players look the same and miss the basics. I want one that is fast, looks different, works without any paid account, and actually shows me new releases from the artists I listen to.

## What works right now

- Enter a folder with music files
- See a numbered list of the files in it
- Pick a number to play that song

## Planned

- Real gapless playback, with visible shuffle and repeat
- A fast library with cover art and tags
- Browse by artist, then album, then song
- A "new releases" screen for the artists in my library
- A custom interface with a music visualizer
- More sources later (internet radio and free music catalogs)

## Requirements

- [uv](https://docs.astral.sh/uv/) (it installs the right Python version and the libraries for you)
- The libraries are listed in `pyproject.toml`

## Getting started

```bash
git clone https://github.com/Quix-ux681/QMusic.git
cd QMusic
uv sync
uv run python main.py
```

When asked, enter the path to a folder that contains your music, then type the number of the song you want to play. Press Enter to stop playback.

## Project structure

```
core/      playback code (no interface code in here)
sources/   where music comes from (local files for now)
main.py    command-line prototype
```

## Notes

- Music files are never included in this repo.
- The goal is that nobody needs a paid account to use it.

## License

Not chosen yet.
