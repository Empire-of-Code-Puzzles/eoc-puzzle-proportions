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
                'gold-tin': (1, 2),
                'gold-iron': (1, 3),
                'gold-copper': (1, 4),
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
            "explanation": "5+7=?"
        }
    ],
    "Extra": [
    ]
}
