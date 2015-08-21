def get_index(string, note):
    notes = ['E','F','F#/Gb','G','G#/Ab','A','A#/Bb', 'B', 'C', 'C#/Db', 'D',  'D#/Eb']
    note_i = notes.index(note)

    if string == 5:
        open_string = 5
        if note_i < open_string:
            return note_i + 12

    # Return 12 fret for open E
    if string == 6 and note_i == 0:
        return 12
    elif string == 5 and note_i == 5:
        return 17
    elif string == 4 and note_i == 10:
        return 22 

    return notes.index(note)

