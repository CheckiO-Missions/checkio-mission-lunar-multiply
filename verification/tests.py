"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [2, 3],
            "answer": 2,
        },
        {
            "input": [8, 9],
            "answer": 8,
        },
        {
            "input": [10, 10],
            "answer": 100,
        },
        {
            "input": [11, 11],
            "answer": 111,
        },
        {
            "input": [17, 24],
            "answer": 124,
        },
        {
            "input": [357, 64],
            "answer": 3564,
        },
    ],
    "Extra": [
        {
            "input": [123, 321],
            "answer": 12321,
        },
        {
            "input": [123456789, 987654321],
            "answer": 12345678987654321,
        },
    ]
}
