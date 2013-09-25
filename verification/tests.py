"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": {'gold-iron': [1, 3], 'gold-tin': [1, 2], 'gold-copper': [1, 4]},
            "answer": [1, 24],
            "explanation": {'iron': [7, 24], 'tin': [11, 24], 'copper': [5, 24], 'gold': [1, 24]}
        },
        {
            "input": {'iron-copper': [1, 2], 'tin-iron': [1, 2], 'copper-tin': [1, 2]},
            "answer": [1, 4],
            "explanation": {'iron': [1, 4], 'tin': [1, 4], 'copper': [1, 4], 'gold': [1, 4]}
        },
        {
            "input": {'iron-tin': [2, 3], 'iron-gold': [1, 2], 'iron-copper': [1, 4]},
            "answer": [7, 24],
            "explanation": {'iron': [5, 24], 'tin': [11, 24], 'copper': [1, 24], 'gold': [7, 24]}
        },
        {
            "input": {'copper-tin': [5, 9], 'gold-copper': [2, 7], 'tin-gold': [1, 2]},
            "answer": [29, 252],
            "explanation": {'iron': [83, 252], 'tin': [97, 252], 'copper': [43, 252], 'gold': [29, 252]}
        }
    ],
    "Extra": [
        {
            "input": {'tin-copper': [22, 37], 'iron-tin': [2, 7], 'gold-tin': [6, 19]},
            "answer": [2143, 9842],
            "explanation": {'iron': [1847, 9842], 'tin': [965, 9842], 'copper': [4887, 9842], 'gold': [2143, 9842]}
        }
    ]
}
