import itertools

def combine_letters(D):
    letter_lists = list(D.values())

    combinations = itertools.product(*letter_lists)

    for combination in combinations:
        print(''.join(combination))

data = {'1': ['a', 'b'], '2': ['c', 'd']}

combine_letters(data)