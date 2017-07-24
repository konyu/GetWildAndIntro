import mplayer
import time

class Player:
    """A simple example class"""

    def __init__(self, dir_path):
        self.player = mplayer.Player()
        self.dir_path = dir_path

    def playWild(self, file_path, firs_get_wild_seek):
        self.player.loadfile(self.dir_path + "/" + file_path)
        # player.pause()
        self.player.time_pos = firs_get_wild_seek
        self.player.pause()
        # player.play()
        time.sleep(8)
        self.player.pause()
