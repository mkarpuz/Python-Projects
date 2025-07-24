{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9fd996a2-f019-4e2b-9336-3ca5a0ca6b02",
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"We are going to create a GPA converter tool to convert different grading systems to the German\n",
    "Grading System of using Baviaran model\"\"\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8b12dff6-77b8-4b44-86b7-5dca0aecc07d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Minimum passing grade in your grading system:  2\n"
     ]
    }
   ],
   "source": [
    "\"\"\"Defining Variables\n",
    "\n",
    "1: Min = represents Minimum the passing grade in the targetting grading system.\n",
    "2:  Y  = represents the overall grade of the user in the gargeting grading system.\n",
    "3: Max = represents maximum passing grade in the targeting grading system. \n",
    "\n",
    "\n",
    "Formular1 = represents the first body of the formula \n",
    "Formular2 = represents the second body of the formula\n",
    "Formular3 = represents the third body of the formula\n",
    "Formular4= represents the forth body of the formula.\n",
    "\n",
    "\"\"\"\n",
    "\n",
    "Min = int(input(\"Minimum passing grade in your grading system: \"))\n",
    "\n",
    "Y = float(input(\"Overall grade: \"))\n",
    "\n",
    "Max = int(input(\"Maximum passing grade in your grading system: \"))\n",
    "\n",
    "\n",
    "\"\"\"Formula =  ----((\"(Max - Y) / \"(Max - Min) * 3) - 1)\n",
    "\"\"\"\n",
    "\n",
    "Formula1 = (Max - Y)\n",
    "\n",
    "Formula2 = (Max - Min)\n",
    "\n",
    "Formula3 = (Formula1/Formula2) \n",
    "\n",
    "Formula4 = (Formula3*3)\n",
    "\n",
    "x = str(Formula4 + 1)\n",
    "\n",
    "\"\"\"Grade\"\"\"\n",
    "\n",
    "\n",
    "print(\"German Grade: \" + x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a8de5d0d-629e-4350-af43-3c55d5d9648d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "288c66d7-17a2-4a73-a187-8abe6c953971",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
