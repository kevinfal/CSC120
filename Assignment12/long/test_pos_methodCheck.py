"""No descrption given.  What do *you* think this does?"""



from battleship import Pos



print("******** BEGINNING TESTCASE ********")

x = Pos(1,2)
y = Pos(3,4)

z = x.rotate(0)
a = y.rotate(1)
b = x.rotate(2)
c = y.rotate(3)


# confirm that the student asserts as required.

try:
    x.rotate(-1)
    print("ERROR: Your Pos.rotate() method does not assert on invalid inputs")
except AssertionError:
    print("step 1 of this testcase passed.")

try:
    x.rotate(4)
    print("ERROR: Your Pos.rotate() method does not assert on invalid inputs")
except AssertionError:
    print("step 2 of this testcase passed.")
try:
    x.rotate(100)
    print("ERROR: Your Pos.rotate() method does not assert on invalid inputs")
except AssertionError:
    print("step 3 of this testcase passed.")



print("Testcase completed successfully.")
    

