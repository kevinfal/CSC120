#! /usr/bin/env python3


"""generate_puzzle.py

   Author: Russ Lewis

   Auto-generates solutions to the jigsaw puzzle problem.  Auto-selects a
   puzzle size from 2-10 (inclusive) in each dimension; the two sizes are
   independent, so puzzles are typically not square.
"""


import random


wid = random.randint(2,10)
hei = random.randint(2,10)


# -------------------- ALGORITHM OVERVIEW --------------------
# The purpose of this program is to generate a random puzzle, and to print out
# a file, which will be in the correct format as input for the 'jigsaw'
# program.  We want the puzzle to be completely unambiguous, so the pieces must
# have no duplicate sides.
#
# A solved jigsaw puzzle (for example, 3x3) has this general form:
#      --- --- ---
#     |   x   x   |
#     |   x   x   |
#     |   x   x   |
#      xxx xxx xxx
#     |   x   x   |
#     |   x   x   |
#     |   x   x   |
#      xxx xxx xxx
#     |   x   x   |
#     |   x   x   |
#     |   x   x   |
#      --- --- ---
#
# We will need to generate random strings to fill in all of the xxx's in the
# puzzle.  We will go through the following steps:
#
#    1) Generate the correct *number* of strings (making sure to not allow
#       duplicates, nor "mirrored" strings), completely ignoring the location
#
#    2) Lay the generated strings out in a random arrangement, by filling in
#       "columns" and rows.  In the example above, there are two columns, each
#       with 3 elements in them.  (Or, if you include the edges, you might say
#       that the puzzle has 4 columns.)
#
#    3) Generate the list of puzzle pieces by iterating through the grid, and
#       reading the proper strings from the columns and rows that we've
#       generated.
#
#    4) Shuffle the set of pieces that we've generated, and print it out.
#
# ------------------------------------------------------------



# the total number of sides required is:
#    4 * total number of pieces
#    minus 2*(wid+hei) because of the edges
#    divided by 2 because each side is on two pieces
total_reqd = (4*wid*hei - 2*(wid+hei)) // 2


sides = set()
while len(sides) < total_reqd:

    # three character lowercase string
    #
    # META-COMMENT: I thought about making this a function.  But the function
    #               would only have one line - or else, would have a for() loop
    #               with only one line in the body.  I judged, in this case,
    #               that three nearly-identical lines, right next to each
    #               other, would be clear enough - more clear than creating a
    #               new function calls.  Such things are often difficult
    #               judgement calls!

    s  = chr(ord('a') + random.randint(0,25))
    s += chr(ord('a') + random.randint(0,25))
    s += chr(ord('a') + random.randint(0,25))

    # account for mirror words
    rev = s[::-1]
    if rev < s:
        s = rev

    # don't allow dups
    if s in sides:
        continue

    sides.add(s)


# sets were useful for O(1) detecting duplicates.  Now that we have completed
# that phase, a list is more handy.  But we want to randomly shuffle the values
# before we use them.  So we'll add random prefixes to each, sort (the random
# prefix is the primary key of the search), and then strip the prefixes
#
# META-COMMENT: Confused by the [] syntax I'm using?  It's one of the coolest
#               features of Python, called a "list comprehension."  We'll
#               discuss this later in the semester.  But if you want a quick
#               introduction, Google for the info, or follow this link:
#
#               https://www.pythonforbeginners.com/basics/list-comprehensions-in-python

sides = sorted([(random.randint(0,1000), side) for side in sides])
sides = [side for (rand,side) in sides]


# the columns of the puzzle.  We need wid-1 columns (fencepost problem), but
# each column needs exactly hei elements.  Then just the opposite for the rows.
# But, to make the code easier to write later on, we'll actually *include* the
# edges in these lists.

cols = []
cols.append(["|||"]*hei)
for i in range(wid-1):

    # slicing into a list like this isn't wonderful for performance - it is
    # O(n^2), of course.  So if we thought we'd have large puzzles, I'd use a
    # more efficient design, such as pop()-ing off the end of the list.  But
    # since we know we are limiting ourselves to 10x10 lists, we can live with
    # this less-than-ideal loop.  The code is *so* nice, I'm loathe to give it
    # up.  (Insert RickRoll joke here.)

    assert len(sides) >= hei
    cols.append(sides[:hei])
    sides = sides[hei:]
cols.append(cols[0])

rows = []
rows.append(["---"]*wid)
for i in range(hei-1):
    assert len(sides) >= wid
    rows.append(sides[:wid])
    sides = sides[wid:]
rows.append(rows[0])

assert len(sides) == 0


# build the pieces in a predictable order (2D iteration).  But since we want to
# mix up the pieces, put them into a data structure that has the same
# random-prefix trick as above.  When we're done, we'll sort, and then print
# out the pieces ignoring the prefix.

pieces = []
for x in range(wid):
    for y in range(hei):
        # remember: with 'rows', the first index is the row number (y), and the
        # second is the position in the row (x).  For cols, it's reversed.

        top = rows[y+1][x]
        rgh = cols[x+1][y]
        bot = rows[y  ][x] [::-1]
        lft = cols[x  ][y] [::-1]

        rand = random.randint(0,1000)

        pieces.append((rand, top,rgh,bot,lft))

pieces.sort()


# ready to print out the puzzle!
print("%d %d" % (wid,hei))

for p in pieces:
    print("  %s %s %s %s" % (p[1],p[2],p[3],p[4]))


