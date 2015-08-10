TESTS = {
    "Rank_01": [
        {
            "input": "Ad+Fe=0.33,Ad+Cu=0.25,Ad+Ti=0.5",
            "answer": 0.04,
            "explanation": {'Fe': [7, 24], 'Ti': [11, 24], 'Ad': [1, 24], 'Cu': [5, 24]}},
        {
            "input": "Ti+Fe=0.5,Fe+Cu=0.5,Cu+Ti=0.5",
            "answer": 0.25,
            "explanation": {'Fe': [1, 4], 'Ti': [1, 4], 'Ad': [1, 4], 'Cu': [1, 4]}},
        {
            "input": "Fe+Ad=0.5,Fe+Ti=0.67,Fe+Cu=0.25",
            "answer": 0.29,
            "explanation": {'Fe': [5, 24], 'Ti': [11, 24], 'Ad': [7, 24], 'Cu': [1, 24]}},
        {
            "input": "Ad+Cu=0.29,Ti+Ad=0.5,Cu+Ti=0.56",
            "answer": 0.115,
            "explanation": {'Fe': [83, 252], 'Ti': [97, 252], 'Ad': [29, 252], 'Cu': [43, 252]}},
        {
            "input": "Fe+Ti=0.29,Ti+Cu=0.59,Ad+Ti=0.32",
            "answer": 0.22,
            "explanation": {'Fe': [1847, 9842], 'Ti': [965, 9842], 'Ad': [2143, 9842],
                            'Cu': [4887, 9842]}},
        {
            "input": "Cu+Ad=0.38,Fe+Cu=0.43,Ti+Cu=0.86",
            "answer": 0.045,
            "explanation": {'Fe': [11, 112], 'Ti': [59, 112], 'Ad': [5, 112], 'Cu': [37, 112]}},
        {
            "input": "Cu+Fe=0.62,Fe+Ti=0.35,Ti+Cu=0.75",
            "answer": 0.14,
            "explanation": {'Fe': [31, 272], 'Ti': [65, 272], 'Ad': [37, 272], 'Cu': [139, 272]}},
        {
            "input": "Fe+Ad=1.0,Fe+Ti=0.0,Fe+Cu=0.0",
            "answer": 1.0,
            "explanation": {'Fe': [1, 2000], 'Ti': [1, 2000], 'Ad': [1997, 2000],
                            'Cu': [1, 2000]}},
        {
            "input": "Ad+Fe=0.33,Ad+Cu=0.67,Ad+Ti=0.33",
            "answer": 0.165,
            "explanation": {'Fe': [1, 6], 'Ti': [1, 6], 'Ad': [1, 6], 'Cu': [1, 2]}},
    ]
}
