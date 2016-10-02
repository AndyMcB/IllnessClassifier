from numpy import genfromtxt, transpose
import sklearn

print("[plasma_glucose, bp, test_result, skin_thickness, num_pregnancies, insulin, bmi, pedigree, age]")

illness_data = genfromtxt("illness.txt", delimiter=',', dtype=None)
print(illness_data)

print ("\n... transposing \n")
illness_data_t = transpose(illness_data) # t for transpose
print("\n\n")

for row in illness_data_t:
    print(row)