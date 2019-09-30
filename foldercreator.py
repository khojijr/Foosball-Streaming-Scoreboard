import os

class FolderCreator:
    def __init__(self):
        if not os.path.exists('Files'):
            os.mkdir('Files')

        f = open("Files\\round.txt", "w+")
        f.write("")
        f.close()

        f = open("Files\\game_number.txt", "w+")
        f.write("")
        f.close()

        f = open("Files\\misc1.txt", "w+")
        f.write("")
        f.close()

        f = open("Files\\misc2.txt", "w+")
        f.write("")
        f.close()

        f = open("Files\\misc3.txt", "w+")
        f.write("")
        f.close()

        f = open("Files\\t1games.txt", "w+")
        f.write("0")
        f.close()

        f = open("Files\\t1name.txt", "w+")
        f.write("")
        f.close()

        f = open("Files\\t1score.txt", "w+")
        f.write("0")
        f.close()

        f = open("Files\\t1TO.txt", "w+")
        f.write("2")
        f.close()

        f = open("Files\\t2games.txt", "w+")
        f.write("0")
        f.close()

        f = open("Files\\t2name.txt", "w+")
        f.write("")
        f.close()

        f = open("Files\\t2score.txt", "w+")
        f.write("0")
        f.close()

        f = open("Files\\t2TO.txt", "w+")
        f.write("2")
        f.close()



