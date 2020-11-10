"""
Return the length of the longest substring with no repeating characters

"""


def solution(s):
    # Type your solution here

    string_length = float('-inf')
    character_map = {}
    left = 0

    for i, c in enumerate(s):
        if c in character_map:
            left = max(left, character_map[c] + 1)

        character_map[c] = i
        string_length = max(string_length, i - left + 1)

    return string_length if string_length != float('-inf') else len(s)


    return string_length if string_length != float('-inf') else len(s)

s = "nndNfdfdf"
solution(s)

