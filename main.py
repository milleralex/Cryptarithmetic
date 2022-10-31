from itertools import permutations
import sys

# Replaces the letter in the equation with numbers
def replace_with_num(term, swaps):
    for letter, number in swaps.items():
        term = term.replace(letter, str(number))
    return term



#  Tests each equation with the given variables.
def find_answers(equation, swaps):
    ans = replace_with_num(equation, swaps)
    try:
        if eval(ans):
            print(swaps)
            print(ans)
            # Exit When we Find a valid answer
            sys.exit()
    except SyntaxError:  # Leading Zeros Cause a Syntax Error, so we ignore them.
        pass


# Brute Force Solution to Cryptarthimatic Problem
if __name__ == '__main__':
    answer = "No Valid Answer Found"
    equation = "TWO + TWO == FOUR"
    variables = [x for x in equation if x.isalpha()]
    # Generates all the possible variable permutations. (Contains Duplicates)
    perms = list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], len(variables)))
    count = 0
    for perm in perms:
        count += 1
        swaps = {x:y for x, y in zip(variables, perm)}
        find_answers(equation, swaps)
        # Keeps track of progress
        if count % 1000 == 0:
            print(f"{count / len(perms):.2%}, {count} / {len(perms)}")
