# -*- coding=UTF-8 -*-

class Talk:
    """class represent a talk
    properties:
        words: list of talk name's word
        duration: number of minutes talk last
        name: talk's name
    """

    def __init__(self, line):
        """line: each line from input.txt that marked talk's name and duration
        """
        self.words = line.split(' ')
        duration = self.words[len(self.words) - 1].strip()
        # calculate the duration of this talk(unit of duration is minute)
        if duration == "lightning":
            self.duration = 5
        else:
            self.duration = int(duration[:-3])

        self.name = ' '.join(self.words)
