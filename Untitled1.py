"""Defining Variables

1: Min = represents Minimum the passing grade in the targetting grading system.
2:  Y  = represents the overall grade of the user in the gargeting grading system.
3: Max = represents maximum passing grade in the targeting grading system. 


Formular1 = represents the first body of the formula 
Formular2 = represents the second body of the formula
Formular3 = represents the third body of the formula
Formular4= represents the forth body of the formula.

"""

Min = int(input("Minimum passing grade in your grading system: "))

Y = float(input("Overall grade:"))

Max = int(input("Maximum passing grade in your grading system: "))


"""Formula =  ----(("(Max - Y) / "(Max - Min) * 3) - 1)
"""

Formula1 = (Max - Y)

Formula2 = (Max - Min)

Formula3 = (Formula1/Formula2) 

Formula4 = (Formula3*3)

x = str(Formula4 + 1)

"""Grade"""


print("German Grade: " + x)
