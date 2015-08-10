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
        },
        {
            "input": {'tin-copper': [6, 7], 'iron-copper': [3, 7], 'copper-gold': [3, 8]},
            "answer": [5, 112],
            "explanation": {'iron': [11, 112], 'tin': [59, 112], 'copper': [37, 112], 'gold': [5, 112]}
        },
        {
            "input": {'iron-tin': [6, 17], 'copper-iron': [5, 8], 'tin-copper': [3, 4]},
            "answer": [37, 272],
            "explanation": {'iron': [31, 272], 'copper': [139, 272], 'tin': [65, 272], 'gold': [37, 272]}
        },
        {"input": {'iron-copper': [1, 1000], 'iron-tin': [1, 1000], 'iron-gold': [999, 1000]},
         "answer": [1997, 2000],
         "explanation": {'copper': [1, 2000], 'gold': [1997, 2000], 'tin': [1, 2000], 'iron': [1, 2000]}},
        {"input": {'gold-copper': [2, 3], 'gold-iron': [1, 3], 'gold-tin': [1, 3]},
         "answer": [1, 6],
         "explanation": {'tin': [1, 6], 'iron': [1, 6], 'copper': [1, 2], 'gold': [1, 6]}}
    ]
}
