"""Model for aircraft flights"""


class Flight:

    def __init__(self, number, aircraft):
        """A flight with a particular passenger aircraft aircraft."""
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{0}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code in '{0}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number in '{0}'".format(number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        # The initial [None] uses the 0 index first entry so we don't have to offset later
        # We concat with a list of the seats using a list comprehension to
        # iterate through the rows, but the row number will always match the index number so
        # we discard that using the dummy _ marker. This list will hold dictionaries, not rownums.
        # The item in the list comprehension is a dictionary comprehension
        # This iterates through the letters and maps None to each one for an empty seat
        # A list comprehension is used instead of using a multiplication operator
        # because we need a distinct dictionary to be created for each row (not a shallow copy)
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def _parse_seat(self, seat):
        """
        Parse a seat designator into a valid row and letter.

        Args:
            seat: A seat designator such as '12C'.

        Returns:
            A tuple consisting of an integer for the row and a string for the seat.
        """
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))

        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))

        return row, letter

    def allocate_seat(self, seat, passenger):
        """Allocates a seat to a passenger.

        Args:
            seat: A seat desigantor such as '12C' or '21F'.
            passenger: The passenger name.

        Raises:
            ValueError: If the seat is unavailable.
        """

        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} is already occupied".format(seat))

        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        """Relocates a passenger to a different seat.

        Args:
            from_seat: The existing seat designation for the passenger to be moved.

            to_seat: The new seat designator.
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to relocate from seat{}".format(from_seat))

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} is already occupied".format(to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        """An iterable series of passenger seating allocations."""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row, letter))


class Aircraft:

    def __init__(self, registration):
        self._registration = registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)

    def registration(self):
        return self._registration


class AirbusA319(Aircraft):

    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1,23), "ABCDEF"

class Boeing777(Aircraft):

    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        return range(1, 56), "ABCKDEFGHJK"



def make_flights():
    """This function is just for development purposes, so we don't have to keep
    rerunning the code in the REPL"""
    f = Flight("BA758", AirbusA319("G-EUPT"))
    f.allocate_seat('12A', 'Guido von Rossum')
    f.allocate_seat('15F', 'Bjarne Riis')
    f.allocate_seat('15E', 'George Harrison')
    f.allocate_seat('1D', 'Ringo Starr')
    f.allocate_seat('1E', 'Ken Bruce')

    g = Flight("AF72", Boeing777("F-GSPS"))
    g.allocate_seat('55K', 'Paul McCartney')
    g.allocate_seat('55J', 'John Lennon')
    g.allocate_seat('33J', 'Steve Rogers')
    g.allocate_seat('1A', 'Natasha Romanov')
    g.allocate_seat('32J', 'Tony Stark')

    return f, g


def console_card_printer(passenger, seat, flight_number, aircraft):
    """Prints a boarding card"""
    output = "| Name: {0}"      \
            " Flight: {1}"      \
            " Seat: {2}"         \
            " Aircraft: {3}"     \
            " |".format(passenger, flight_number, seat, aircraft)
    banner = '+' + '-' * (len(output)-2) + '+'
    border = '|' + ' ' * (len(output)-2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()
