"""Calendar Maker
Create monthly calendars, saved to a text file and fit for printing.
"""

import datetime


class CalendarMaker:
    # Set up the constants:
    DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday')
    MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December')

    VERTICAL_LINE = '|'
    EOL = '\n'
    SPACE = ' '

    WEEK_DAYS = '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..' + EOL

    # The horizontal line string that separate weeks:
    WEEK_SEPARATOR = ('+----------' * 7) + '+' + EOL

    # The blank rows have ten spaces in between the | day separators:
    BLANK_ROW = (f'{VERTICAL_LINE}{SPACE * 10}' * 7) + VERTICAL_LINE + EOL

    @property
    def year(self):
        while True:  # Loop to get a year from the user.
            print('Enter the year for the calendar:')
            response = input('> ')

            if response.isdecimal() and int(response) > 0:
                return int(response)

            print('Please enter a numeric year, like 2023.')

    @property
    def month(self):
        while True:  # Loop to get a month from the user.
            print('Enter the month for the calendar, 1-12:')
            response = input('> ')

            if not response.isdecimal():
                print('Please enter a numeric month, like 3 for March.')
                continue

            month = int(response)
            if 1 <= month <= 12:
                return month

    def make(self, year, month):
        cal_text = ''  # calText will contain the string of our calendar.

        # Put the month and year at the top of the calendar:
        cal_text += (self.SPACE * 34) + \
            self.MONTHS[month - 1] + self.SPACE + str(year) + self.EOL

        # Add the days of the week labels to the calendar:
        # (!) Try changing this to abbreviations: SUN, MON, TUE, etc.
        cal_text += self.WEEK_DAYS

        # Get the first date in the month. (The datetime module handles all
        # the complicated calendar stuff for us here.)
        currentDate = datetime.date(year, month, 1)

        # Roll back currentDate until it is Sunday. (weekday() returns 6
        # for Sunday, not 0.)
        while currentDate.weekday() != 6:
            currentDate -= datetime.timedelta(days=1)

        while True:  # Loop over each week in the month.
            cal_text += self.WEEK_SEPARATOR

            # dayNumberRow is the row with the day number labels:
            day_number_row = ''
            for _ in range(7):
                day_number_row += self.VERTICAL_LINE + \
                    str(currentDate.day).rjust(2) + (self.SPACE * 8)
                currentDate += datetime.timedelta(days=1)  # Go to next day.
            # Add the vertical line after Saturday.
            day_number_row += self.VERTICAL_LINE + self.EOL

            # Add the day number row and 3 blank rows to the calendar text.
            cal_text += day_number_row
            for _ in range(3):  # (!) Try changing the 4 to a 5 or 10.
                cal_text += self.BLANK_ROW

            # Check if we're done with the month:
            if currentDate.month != month:
                break

        # Add the horizontal line at the very bottom of the calendar.
        cal_text += self.WEEK_SEPARATOR
        return cal_text


if __name__ == "__main__":

    print('Calendar Maker')
    cal_maker = CalendarMaker()
    year = cal_maker.year
    month = cal_maker.month

    cal_text = cal_maker.make(year, month)
    print(cal_text)  # Display the calendar.

    # Save the calendar to a text file:
    file_name = 'calendar_{}_{}.txt'.format(year, month)
    with open(file_name, 'w') as fileObj:
        fileObj.write(cal_text)

    print('Saved to ' + file_name)
