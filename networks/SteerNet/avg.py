import random

one = []
two = []
expected = []

for i in range(100):
    one.append(random.uniform(-1, 1))

for i in range(100):
    two.append(random.uniform(-1, 1))

for i in range(100):
    expected.append(0)

def get_weights(one, two):
    weightOne = 0.0
    weightTwo = 0.0

    for i in range(len(one)):

        if abs(expected[i] - one[i]) < abs(expected[i] - two[i]): # if one is closest
            weightOne += abs(expected[i] - one[i])
        elif abs(expected[i] - one[i]) > abs(expected[i] - two[i]):
            weightTwo += abs(expected[i] - two[i])
        else:
            print("#rip")

    w1 = weightOne / (weightOne+weightTwo)
    w2 = weightTwo / (weightOne+weightTwo)

    print("WeightOne: " + str(w1*100) + "%")
    print("WeightTwo: " + str(w2*100) + "%")

    return (w1, w2)

g, h = get_weights()
