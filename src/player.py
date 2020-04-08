# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, location):
        self.location = location

    def move(self, direction):
        if direction == 'n':
            return self.location.n_to
        if direction == 's':
            return self.location.s_to
        if direction == 'e':
            return self.location.e_to
        if direction == 'w':
            return self.location.w_to

    def quit(self):
        """quit game in some way"""
