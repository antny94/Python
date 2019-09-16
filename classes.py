# practice with classes in Python


class Anime:

    def __init__(self, name="", genre=""):
        self.name = name
        self.genre = genre

    def message(self):
        print("Your anime is trash.")


MyAnime = Anime("Bleach", "Shonen")

print(MyAnime.name)
print(MyAnime.genre)
