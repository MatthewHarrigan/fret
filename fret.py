from fretboard.fretboard import get_index
from strings.strings import invert_string_number
from list_sound_files.list_sound_files import list_files
from display_fretboard.display_fretboard import display_fretboard
from subprocess import call
import argparse
import random
import sys
import time
import curses
from curses import wrapper
import re

from list_sound_files.list_sound_files import list_files
from fretboard.fretboard import get_index

from config import config


class Fret:
    current_note = 0
    current_string = 0
    inclusive = False
    notes = ['E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B', 'C',
             'C#/Db', 'D', 'D#/Eb']
    string_indices = [6, 5, 4, 3, 2, 1]
    string = ['6th', '5th', '4th', '3rd', '2nd', '1st']
    strings = [0, 1, 2, 3, 4, 5]
    string_names = ['Low E', '\'A\'', 'D', 'G', 'B', 'High E']
    order = config['order']
    files = []
    sequential_random_index = 0
    index_for_first_six = 0

    to_string = 1
    from_string = 6

    def zero_based_string_to_string_number(self, current_string):
        return self.string_indices[current_string]

    def get_file(self, current_string, note):
        return self.files[get_index(
            self.zero_based_string_to_string_number(current_string), note)]

    def get_note_and_file(self, current_string, day, notes):
        if self.inclusive:
            rand_n = random.randint(0, day - 1)
            note = notes[self.order[rand_n]]
            file = self.get_file(current_string, note)
        else:
            note = notes[self.order[day - 1]]
            file = self.get_file(current_string, note)

        return file, note

    def notes_by_day(self, day):
        p = ''
        arrows = ''
        #for s in range(1, 12):
            #p += str(s) + '\t'
        #p += '\n'
        for s in self.order:
            p += self.notes[s] + '\t'
        p += '\n'
        i = 0
        for s in self.order:
            if i < day:
                p += '^\t'
            i += 1
        return "%s" % p

    def play_back_options(self, args):
        rate = '200'
        if args.level == 'beginner' or args.level == 'Lil_Wayne':
            playback = '1'
            rand_from = 2
            rand_to = 4
        elif args.level == 'easy' or args.level == 'Noel_Gallagher':
            playback = '1'
            rand_from = 1
            rand_to = 3
        elif args.level == 'medium' or args.level == 'Jimmy_Page':
            playback = '0.5'
            rand_from = 0
            rand_to = 0
        elif args.level == 'hard' or args.level == 'Hendrix':
            playback = '0.1'
            rand_from = 0
            rand_to = 0
            rate = '350'
        elif args.level == 'impossible' or args.level == 'Chuck_Norris':
            playback = '0.01'
            rand_from = 0
            rand_to = 0
            rate = '450'
        return playback, rand_from, rand_to, rate

    def play_sound(self, file, playback):
        call(["afplay", config['sounds_folder'] + file, "-t", playback])

    def display_string_and_note(self, current_string, note):
        out = '%s string %s\r' % (current_string, note)
        return out

    def say_string_and_note(self, out, rate):
        out = out.replace('b', ' flat')
        call(["say", out])
        #call(["say", out, '--rate', rate])

    def sleep(self, rand_from, rand_to):
        time.sleep(random.uniform(rand_from, rand_to))

    # Choose a non-repeating string
    # Reset when all the strings have been selected
    def random_string(self):
        if self.to_string == self.from_string:
            return self.to_string-1

        reset = self.from_string - self.to_string
        # reset run-through strings
        if self.sequential_random_index > reset:
            self.sequential_random_index = 0
            # make a copy of the original string list 
            self.strings_tmp = list(self.strings)
        current_string = random.choice(self.strings_tmp[self.to_string-1 : self.from_string-1])
        self.strings_tmp.remove(current_string)
        self.sequential_random_index += 1
        return current_string

    def get_current_string(self):
        if self.index_for_first_six > 5 or self.inclusive:
            current_string = self.random_string()
        else:
            current_string = self.index_for_first_six
            self.index_for_first_six += 1
        return current_string

    def fretboard(self, string, note):
        out = display_fretboard(string, note)
        out = re.sub(r'\s', '\t', out)
        return out

    def draw_fretboard_dots(self, stdscr):
        stdscr.addstr(9, 20, 'o')
        stdscr.addstr(9, 36, 'o')
        stdscr.addstr(9, 52, 'o')
        stdscr.addstr(9, 68, 'o')
        stdscr.addstr(8, 92, 'o')
        stdscr.addstr(10, 92, 'o')

    def __init__(self):
        self.strings_tmp = list(self.strings)

        self.files = list_files(config['sounds_folder'], config['low_e_file'])

        inclusive = False

        parser = argparse.ArgumentParser()
        parser.add_argument('-d', '--day', default=0,
                            help='the day of your 12 day challenge')
        parser.add_argument('-l', '--level', default='easy',
                            help='beginner|easy|medium|hard|impossible')
        parser.add_argument('-i', '--inclusive',
                            help="Whether the session includes previous days' notes",
                            action="store_true")
        parser.add_argument('-ns', '--no-sound', help="Don't play note samples",
                            action="store_true")
        parser.add_argument('-fb', '--fretboard', help="Show fretboard. Experimental",
                            action="store_true")
        parser.add_argument('-f', '--from-str', default=1, help="from (from) string")
        parser.add_argument('-t', '--to-str', default=6, help="to (to) string")
        parser.add_argument('-n', '--name', help="Say string name rather than string number", action="store_true")

        args = parser.parse_args()

        day = int(args.day)

        self.to_string = invert_string_number(int(args.to_str))
        self.from_string = invert_string_number(int(args.from_str))

        if args.inclusive:
            self.inclusive = True
        else:
            self.inclusive = False

        if args.no_sound:
            sound = False
        else:
            sound = True

        if args.fretboard:
            show_fretboard = True
        else:
            show_fretboard = False

        if args.name:
            say_name = True
        else:
            say_name = False

        playback, sleep_from, sleep_to, rate = self.play_back_options(args)

        def string_name(current_string, say_name):
            if say_name:
                string = self.string_names[current_string]
            else:
                string = self.string[current_string]
            return string

        def main(stdscr):

            curses.curs_set(0)
            # Clear screen
            stdscr.clear()

            stdscr.addstr(0, 0, "Day %s of 12. Today is a %s day\n" % (
            day, self.notes[self.order[day - 1]]))
            stdscr.addstr(2, 0, self.notes_by_day(day) + '\n')
            stdscr.refresh()

            time.sleep(1)

            try:
                while True:

                    stdscr.clear()

                    current_string = self.get_current_string()

                    file, note = self.get_note_and_file(current_string, day,
                                                        self.notes)

                    name = string_name(current_string, say_name)
                    
                    out = self.display_string_and_note(name, note)

                    stdscr.addstr(0, 0, "Day %s of 12. Today is a %s day\n" % (
                    day, self.notes[self.order[day - 1]]))
                    stdscr.addstr(2, 0, self.notes_by_day(day) + '\n')
                    stdscr.addstr(4, 0, out, curses.A_BOLD)
                    if show_fretboard:
                        stdscr.addstr(6, 0, self.fretboard(0, 0))
                        self.draw_fretboard_dots(stdscr)
                    stdscr.refresh()

                    self.say_string_and_note(out, rate)

                    self.sleep(sleep_from, sleep_to)

                    if show_fretboard:
                       stdscr.addstr(6, 0, self.fretboard(self.string_indices[current_string], note))
                       self.draw_fretboard_dots(stdscr)

                    stdscr.refresh()

                    if sound:
                        self.play_sound(file, playback)

            except KeyboardInterrupt:
                sys.exit(0)

        wrapper(main)

if __name__ == '__main__':
    fret = Fret()
