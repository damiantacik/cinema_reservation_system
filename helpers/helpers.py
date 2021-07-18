def card_printer(spectator, seat, film_name, cinema_model):
    text = f"| Name: {spectator}, Seat: {seat}, Film: {film_name}, Room: {cinema_model} |"
    frame = f"+{'-' * (len(text) - 2)}+"
    frame_empty = f"|{' ' * (len(text) - 2)}|"

    banner = [frame, frame_empty, text, frame_empty, frame]
    banner_text = "\n".join(banner)

    print(banner_text)
