from cinema import Cinema


class Audience1(Cinema):
    @staticmethod
    def get_audience():
        return "Audience 1"

    @staticmethod
    def get_seating_plan():
        return range(1, 15), "ABCDEFGHIJ"
