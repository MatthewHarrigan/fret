Memorise the guitar fretboard in 12 days
========================================

You will learn 36 pitches i.e. 3 octaves over 72 positions over 12 days.
Each day you will learn a new note and get to practise all the other notes from
the previous days (excluding the first day).

How it works:
* The computer says the name of the note for you play i.e. "5th string E"
* You play the note
* The correct note at the correct pitch is played back for reference

At the start of your session run:

    python3 fret.py --day 1 --level beginner

This will play only the new note, first in order from the 6th string down and
then by random string

Once you are comfortable with the note and its positions you can run the command
with the '--inclusive' flag which play all the other note from the previous days
(not including the first day)

    python3 fret.py --day 12 --level beginner --inclusive

If it's getting too easy you can change to level easy, hard or impossible.

Inspired by Guitarist / Teacher Mike Walker (http://www.mike-walker.co.uk/)

The default order is open strings first then the other notes. In Mike Walker's
terms, planetary and orbital notes. The idea is that each planetary note is next
 to and orbital note. You can change the order in the config. If you slide up to
 note, you don't know it yet.

Also note that you never play an open string; play the note at the 12 fret instead.

Installation
------------

Requires
* OS X only
* python 3 (though it seems to work with python 2.x)
* 36 sound files in /sounds or similar location. Specify the location in the config. I've been using the sounds from http://www.reactor-site.com/samples/reactor_strat.zip specifically those from the Reactor Strat/Reactor Strat Samples/p folder. A word of warning when downloading a library of samples, a few I tried where missing notes including those from other folders mentioned previously. Also they're a bit out of tune. Beware! I've included the sounds but in no way claim any copywrite.
* Run the commands above

Configuration
------------------
Look at confi.py for config details


Run the unit tests
-----------------------
python3 -m unittest discover
