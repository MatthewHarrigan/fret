def display_fretboard(string, note):

    open_strings = ['e', 'b', 'g', 'd', 'a', 'e']

    fret_numbers = '0 1 2 3 4 5 6 7 8 9 10 11 \n';

    if (string == 1 and note == 'E'):
        str = ('0 1 2 3 4 5 6 7 8 9 10 11 \n'
               'e | | | | | | | | | | E \n'
               'b | | | | | | | | | | | \n'
               'g | | | | | | | | | | | \n'
               'd | | | | | | | | | | | \n'
               'a | | | | | | | | | | | \n'
               'e | | | | | | | | | | | \n')
    elif (string == 1 and note == 'F'):
        str = ('0 1 2 3 4 5 6 7 8 9 10 11 \n'
               'e F | | | | | | | | | | \n'
               'b | | | | | | | | | | | \n'
               'g | | | | | | | | | | | \n'
               'd | | | | | | | | | | | \n'
               'a | | | | | | | | | | | \n'
               'e | | | | | | | | | | | \n')
    else:
        str = fret_numbers;
        for open_string in open_strings:
            str += open_string + ' '
            for fret in range(0, 11):
                str += '| '
            str += '\n'

    return str