TESTS = {
    "Rank_01": [
        {
            'input': 'Ad+Fe=0.33,Ad+Cu=0.25,Ad+Ti=0.5',
            'explanation': {'Ad': [1, 24], 'Ti': [11, 24], 'Cu': [5, 24], 'Fe': [7, 24]},
            'answer': [1, 24],
        },
        {
            'input': 'Ti+Fe=0.5,Fe+Cu=0.5,Cu+Ti=0.5',
            'explanation': {'Ad': [1, 4], 'Ti': [1, 4], 'Cu': [1, 4], 'Fe': [1, 4]},
            'answer': [1, 4], },
        {
            'input': 'Fe+Ad=0.5,Fe+Ti=0.67,Fe+Cu=0.25',
            'explanation': {'Ad': [7, 24], 'Ti': [11, 24], 'Cu': [1, 24], 'Fe': [5, 24]},
            'answer': [7, 24], },
        {
            'input': 'Ad+Cu=0.29,Ti+Ad=0.5,Cu+Ti=0.56',
            'explanation': {'Ad': [29, 252], 'Ti': [97, 252], 'Cu': [43, 252], 'Fe': [83, 252]},
            'answer': [29, 252], },
        {
            'input': 'Fe+Ti=0.29,Ti+Cu=0.59,Ad+Ti=0.32',
            'explanation': {'Ad': [2143, 9842], 'Ti': [965, 9842], 'Cu': [4887, 9842],
                            'Fe': [1847, 9842]}, 'answer': [2143, 9842],
        },
        {
            'input': 'Cu+Ad=0.38,Fe+Cu=0.43,Ti+Cu=0.86',
            'explanation': {'Ad': [5, 112], 'Ti': [59, 112], 'Cu': [37, 112], 'Fe': [11, 112]},
            'answer': [5, 112], },
        {
            'input': 'Cu+Fe=0.62,Fe+Ti=0.35,Ti+Cu=0.75',
            'explanation': {'Ad': [37, 272], 'Ti': [65, 272], 'Cu': [139, 272], 'Fe': [31, 272]},
            'answer': [37, 272], },
        {
            'input': 'Fe+Ad=1.0,Fe+Ti=0.0,Fe+Cu=0.0',
            'explanation': {'Ad': [1997, 2000], 'Ti': [1, 2000], 'Cu': [1, 2000], 'Fe': [1, 2000]},
            'answer': [1997, 2000], },
        {

            'input': 'Ad+Fe=0.33,Ad+Cu=0.67,Ad+Ti=0.33',
            'explanation': {'Ad': [1, 6], 'Ti': [1, 6], 'Cu': [1, 2], 'Fe': [1, 6]},
            'answer': [1, 6], }
    ]
}


def rework(test):
    data = test["input"]
    test["input"] = ",".join(["{}={}".format(k, round(v[0] / v[1], 2)) for k, v in data.items()]),
    return test


# for t in TESTS["Rank_01"]:
# print(rework(t))

from fractions import Fraction

METALS = ('Cu', 'Fe', 'Ti', 'Ad')
N = 4
D = 8


def solve(log):
    matrix = [[1 for _ in range(5)]]
    for entry in log.split(","):
        alloy, prop = entry.split("=")
        new_row = [0, 0, 0, 0, float(prop)]
        metals = alloy.split("+")
        for m in metals:
            new_row[METALS.index(m)] = Fraction(1, 1)
        matrix.append(new_row)
    matrix.sort(reverse=True, key=lambda x: [1 if z else 0 for z in x])
    for i in range(N - 1):
        if matrix[i][i]:
            matrix[i] = [round(el / matrix[i][i], D) for el in matrix[i]]
        for j in range(i + 1, len(matrix)):
            if not matrix[i][i]:
                continue
            koof = matrix[j][i] / matrix[i][i]
            matrix[j] = [round(matrix[j][k] - matrix[i][k] * koof, D) for k in range(5)]
        matrix.sort(reverse=True, key=lambda x: [1 if z else 0 for z in x])
    matrix[3] = [round(el / matrix[3][3], D) for el in matrix[3]]
    return matrix[3][-1] / matrix[3][-2]

for t in TESTS["Rank_01"]:
    ans = solve(t["input"])
    print("""{{
    "input": "{}",
    "answer": {},
    "explanation": {}}},""".format(t["input"], ans, t["explanation"]))