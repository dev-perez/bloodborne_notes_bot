import csv
import os.path


FILE_PATH = "./bloodborne_notes.csv"

if not os.path.exists(FILE_PATH):
    raise FileNotFoundError(
        f"The CSV file was not found at the specified path: {FILE_PATH}"
    )


def generate_note(number_note: int, file_path: str):
    """
    Reads a CSV file containing game notes and prints
    the result according to the chosen number.

     Parameters:
     number_note(int): An integer from 1 to 20.

     Return: A list containing the note number and its content."
    """
    with open(file_path, "r") as file:
        csv_notes = csv.reader(file, delimiter=",")
        for line in csv_notes:
            if line and line[0].isdigit():
                order_note = int(line[0])
                if order_note == number_note:
                    return line


try:
    number_note = int(input("choose a note [1 a 20]: "))
    if number_note < 1 or number_note > 20:
        raise ValueError
except ValueError:
    print("Please enter a valid number between 1 and 20.")


bb_note = generate_note(number_note, FILE_PATH)
print(bb_note)
