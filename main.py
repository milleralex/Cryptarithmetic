# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import copy


def replace_with_num(term, swaps):
    for letter, number in swaps.items():
        term = term.replace(letter, str(number))
    return term

def get_min(dictionary):
    min_val = 1000
    min_key = ""
    for key, value in dictionary.items():
        if min_val > value:
            min_val = value
            min_key = key
    return min_key

def find_answers(equation, swaps):
    ans = replace_with_num(equation, swaps)
    print(ans)
    try:
        if exec(ans):
            print(swaps)
            return swaps
    except SyntaxError:
        pass
    new_swaps = copy.deepcopy(swaps)
    next = get_min(new_swaps)
    if new_swaps[next] < 9:
        new_swaps[next] = new_swaps[next] + 1
        find_answers(equation, new_swaps)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    equation = "TWO + TWO == FOUR"
    variables = {x: 0 for x in equation if x.isalpha()}
    print(find_answers(equation, variables))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
