from datetime import date, timedelta
from random import randint


class BirthdayParadox:

    def __init__(self) -> None:
        self.MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

    def run_simulations(self, times: int, number_of_birthdays: int):
        match = 0  # How many simulations had matching birthdays in them.
        for i in range(times):
            # Report on the progress every 10,000 simulations:
            if i % 10000 == 0:
                print(i, 'simulations run...')
            birthdays = self.generate_birthdays(number_of_birthdays)
            if self.get_match(birthdays) is not None:
                match += 1
        print(f'{times} simulations run.')
        probability = self.get_probability(match, times)
        return match, probability

    def get_probability(self, favorable_outcome: int, sample_space: int):
        return round(favorable_outcome / sample_space * 100, 2)

    def display_birthdays(self, birthdays: list[date]):
        for i, birthday in enumerate(birthdays):
            if i != 0:
                # Display a comma for each birthday after the first birthday.
                print(', ', end='')

            month_name = self.MONTHS[birthday.month - 1]
            date_text = f'{month_name} {birthday.day}'
            print(date_text, end='')
        print()

    def display_results(self, match: date | None):
        print('In this simulation, ', end='')
        if match is not None:
            month_name = self.MONTHS[match.month - 1]
            date_text = f'{month_name} {match.day}'
            print('multiple people have a birthday on', date_text)
        else:
            print('there are no matching birthdays.')

    def get_number_of_birthdays(self):
        # Keep asking until the user enters a valid amount.
        while True:
            print('How many birthdays shall I generate? (Max 100)')
            response = input('> ')
            if response.isdecimal() and (0 < int(response) <= 100):
                return int(response)  # User has entered a valid amount.

    def generate_birthdays(self, number_of_birthdays: int):
        """Returns a list of number random date objects for birthdays."""
        birthdays = [date(1997, 1, 1) + timedelta(randint(1, 364))
                     for _ in range(number_of_birthdays)]
        return birthdays

    def get_match(self, birthdays: list[date]):
        """Returns the date object of a birthday that occurs more than once in the birthdays list."""
        if len(birthdays) == len(set(birthdays)):
            return  # All birthdays are unique, so return early.

        unique = set()
        for birthday in birthdays:
            if birthday in unique:
                return birthday
            unique.add(birthday)


if __name__ == "__main__":
    print('''Birthday Paradox

    The birthday paradox shows us that in a group of N people, the odds
    that two of them have matching birthdays is surprisingly large.
    This program does a Monte Carlo simulation (that is, repeated random
    simulations) to explore this concept.

    (It's not actually a paradox, it's just a surprising result.)''')
    bp = BirthdayParadox()
    number_of_birthdays = bp.get_number_of_birthdays()

    print('Here are', number_of_birthdays, 'birthdays:')

    birthdays = bp.generate_birthdays(number_of_birthdays)

    bp.display_birthdays(birthdays)
    match = bp.get_match(birthdays)
    print(match)
    bp.display_results(match)

    # Run through 100,000 simulations:
    times = 100_000
    print('Generating', number_of_birthdays,
          f'random birthdays {times} times...')

    input('Press Enter to begin...')

    sim_match, probability = bp.run_simulations(
        times=times, number_of_birthdays=number_of_birthdays)

    print(f'Out of {times} simulations of',
          number_of_birthdays, 'people, there was a')

    print('matching birthday in that group', sim_match, 'times. This means')

    print('that', number_of_birthdays,
          'people have a', probability, '% chance of')

    print('having a matching birthday in their group.')

    print('That\'s probably more than you would think!')
