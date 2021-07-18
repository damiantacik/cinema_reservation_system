from pprint import pprint

from film import Film
from audience import *
from helpers import card_printer


def create_film():
    hall_1 = Audience1()
    hall_2 = Audience2()

    f = Film("Titanic", hall_2)

    f.allocate_spectators("10C", "Damian")
    f.allocate_spectators("1F", "Jan")

    f.relocate_spectators("10C", "5C")
    f.allocate_spectators("5A", "Jan")

    f.print_ticket(card_printer)
    f.get_num_empty_seats()

    pprint(f.get_num_empty_seats())
    pprint(f.seats)
    print(f.film_name)
    print(f.get_cinema_model())
    print(hall_1.get_seating_plan())
    print(hall_2.get_seating_plan())
    print(hall_1.get_num_seats())
    print(hall_2.get_num_seats())

if __name__ == '__main__':
    create_film()
