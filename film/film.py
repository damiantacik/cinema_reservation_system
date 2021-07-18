class Film:
    def __init__(self, film_name, cinema):
        self.cinema = cinema
        self.film_name = film_name

        rows, letters = self.cinema.get_seating_plan()
        self.seats = [None] + [{letters: None for letters in letters} for _ in rows]

    # def get_airlines(self):
    #     return self.flight_number[:2]
    #
    # def get_number(self):
    #     return self.flight_number[2:]

    def get_cinema_model(self):
        return self.cinema.get_audience()

    def _parse_seat(self, seat):
        rows, letters = self.cinema.get_seating_plan()

        letter = seat[-1]

        if letter not in letters:
            raise ValueError(f"Invalid seat letter: {letter}")

        row_text = seat[:-1]

        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid row number: {row_text} ")

        if row not in rows:
            raise ValueError(f"Row number is out of seating range: {row} ")

        return row, letter

    def allocate_spectators(self, seat, spectators):
        row, letter = self._parse_seat(seat)
        if self.seats[row][letter] is not None:
            raise ValueError(f"Seat {seat} is already taken")

        self.seats[row][letter] = spectators

    def relocate_spectators(self, seat_from, seat_to):
        row_from, letter_from = self._parse_seat(seat_from)

        if self.seats[row_from][letter_from] is None:
            raise ValueError(f"No spectator assigned to place {seat_from}")

        row_to, letter_to = self._parse_seat(seat_to)

        if self.seats[row_to][letter_to] is not None:
            raise ValueError(f"Seat {seat_to} is already taken")

        self.seats[row_to][letter_to] = self.seats[row_from][letter_from]
        self.seats[row_from][letter_from] = None

    def get_num_empty_seats(self):
        return sum(sum(1 for seat in row.values() if seat is None)
                   for row in self.seats if row is not None)

    def print_ticket(self, printer):
        for spectator, seat in self.get_spectators():
            printer(spectator, seat, self.film_name, self.get_cinema_model())

    def get_spectators(self):
        for idx, row in enumerate(self.seats):
            if row is not None:
                for letter, spectator in row.items():
                    if spectator is not None:
                        yield spectator, f"{idx}{letter}"
