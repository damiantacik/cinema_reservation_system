from cinema import Cinema


class Audience2(Cinema):
    @staticmethod
    def get_audience():
        return "Audience 2"

    @staticmethod
    def get_seating_plan():
        return range(1, 21), "ABCDEFGHIJKLMNO"