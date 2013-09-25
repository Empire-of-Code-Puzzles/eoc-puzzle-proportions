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
            "input": {
                'gold-tin': [1, 2],
                'gold-iron': [1, 3],
                'gold-copper': [1, 4],
            },
            "answer": [1, 24]
        },
        {
            "input": {
                'tin-iron': (1, 2),
                'iron-copper': (1, 2),
                'copper-tin': (1, 2),
            },
            "answer": [1, 4],
        },
        {
            "input": {
                'iron-tin': (2, 3),
                'iron-copper': (1, 4),
                'iron-gold': (1, 2)
            },
            "answer": [7, 24]
        },
        {
            "input": {
                'gold-copper': (2, 7),
                'iron-gold': (1, 2),
                'tin-gold': (1, 2),
                'copper-tin': (5, 9)
            },
            "answer": [1, 7]}
    ],
    "Extra": [
        {
            "input": {
                'gold-tin': (1, 19),
                'tin-copper': (2, 37),
                'iron-tin': (5, 6)
            },
            "answer": [697, 8436]}
    ]
}
