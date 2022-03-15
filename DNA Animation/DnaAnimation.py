import random
import time


class DnaAnimation:
    PAUSE = 0.15  # (!) Try changing this to 0.5 or 0.0.
    ROWS = [
        # 123456789 <- Use this to measure the number of spaces:
        '         ##',  # Index 0 has no {}.
        '        #{}-{}#',
        '       #{}---{}#',
        '      #{}-----{}#',
        '     #{}------{}#',
        '    #{}------{}#',
        '    #{}-----{}#',
        '     #{}---{}#',
        '     #{}-{}#',
        '      ##',  # Index 9 has no {}.
        '     #{}-{}#',
        '     #{}---{}#',
        '    #{}-----{}#',
        '    #{}------{}#',
        '     #{}------{}#',
        '      #{}-----{}#',
        '       #{}---{}#',
        '        #{}-{}#'
    ]

    def animate(self):
        row_index = 0
        while True:  # Main program loop.
            # Increment row_index to draw next row:
            row_index += 1
            if row_index == len(self.ROWS):
                row_index = 0

            # Row indexes 0 and 9 don't have nucleotides:
            if row_index == 0 or row_index == 9:
                print(self.ROWS[row_index])
                continue

            # Select random nucleotide pairs, guanine-cytosine and
            # adenine-thymine:
            match random.randint(1, 4):
                case 1:
                    leftNucleotide, rightNucleotide = 'A', 'T'
                case 2:
                    leftNucleotide, rightNucleotide = 'T', 'A'
                case 3:
                    leftNucleotide, rightNucleotide = 'C', 'G'
                case 4:
                    leftNucleotide, rightNucleotide = 'G', 'C'

            # Print the row.
            print(self.ROWS[row_index].format(leftNucleotide, rightNucleotide))
            time.sleep(self.PAUSE)  # Add a slight pause.


if __name__ == "__main__":
    dna = DnaAnimation()

    print('DNA Animation')
    print('Press Ctrl-C to quit...')

    try:
        dna.animate()
    except KeyboardInterrupt:
        quit()
