from fretboard.fretboard import get_index


def display_fretboard(string, note):
    open_strings = ['e', 'b', 'g', 'd', 'a', 'e']
    open_string_indices = [24, 19, 15, 10, 5, 0]

    fret_numbers = '0 1 2 3 4 5 6 7 8 9 10 11 12 \n';

    str = fret_numbers;
    str_num = 1
    for open_string in open_strings:
        str += open_string + ' '
        for note_index in range(open_string_indices[str_num - 1] + 1,
                          open_string_indices[str_num - 1] + 13):
            if str_num == string and get_index(string, note) == note_index:
                str += note + ' '
            else:
                str += '| '
        str += '\n'
        str_num += 1

    return str