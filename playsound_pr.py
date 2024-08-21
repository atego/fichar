from ffpyplayer.player import MediaPlayer
from time import sleep

player = MediaPlayer('https://atres-live.ondacero.es/live/ondacero/bitrate_1.m3u8')
while True:
    player.get_metadata()


