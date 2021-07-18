class Cinema:

    def get_num_seats(self):
        row, letters = self.get_seating_plan()
        return len(row) * len(letters)