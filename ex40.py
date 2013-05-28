class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

lyric_lines = ["Happy birthday to u",
               "I don't want to get sued",
               "So I'll stop right there"]
happy_birthday = Song(lyric_lines)

bulls_on_parade = Song(["They rally around the family",
                         "With pockets full of shells"])

happy_birthday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()