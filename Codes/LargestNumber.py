numberOne, numberTwo, numberThree = 4533, 434, 453
if numberOne > numberTwo and numberOne > numberThree:
    print("{0} is greater than {1} and {2}".format(numberOne, numberTwo, numberThree))
elif numberTwo > numberOne and numberTwo > numberThree:
    print("{0} is greater than {1} and {2}".format(numberTwo, numberOne, numberThree))
else:
    print("{0} is greater than {1} and {2}".format(numberThree, numberOne, numberTwo))