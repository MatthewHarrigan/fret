from fretboard.fretboard import get_index


def first_fret_position(open_string_indices, str_num):
    return open_string_indices[str_num - 1] + 1


def twelfth_fret_position(open_string_indices, str_num):
    return open_string_indices[str_num - 1] + 13


def display_fretboard(curr_string, curr_note):
    open_strings = ['e', 'b', 'g', 'd', 'a', 'e']
    open_string_positions = [24, 19, 15, 10, 5, 0]

    output = '0 1 2 3 4 5 6 7 8 9 10 11 12 \n';

    str_i = 1
    for open_string in open_strings:
        output += open_string + ' '
        is_curr_note_open = False

        for note_index in range(
                first_fret_position(open_string_positions, str_i),
                twelfth_fret_position(open_string_positions, str_i)):

            if get_index(curr_string, curr_note) == open_string_positions[str_i - 1]:
                is_curr_note_open = True

            if str_i == curr_string and is_curr_note_open and note_index == open_string_positions[str_i - 1] + 12:
                output += curr_note + ' '
                is_curr_note_open = False
            elif str_i == curr_string and get_index(curr_string, curr_note) == note_index :
                output += curr_note + ' '
            else:
                output += '| '
        output += '\n'
        str_i += 1

    return output