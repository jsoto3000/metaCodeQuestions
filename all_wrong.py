def getWrongAnswers(N, C):
    wrong_answers = []
    for answer in C:
        if answer == 'A':
            wrong_answers.append('B')
        else:
            wrong_answers.append('A')
    return ''.join(wrong_answers)

# Sample test cases
print(getWrongAnswers(3, 'ABA'))  # Expected output: BAB
print(getWrongAnswers(5, 'BBBBB'))  # Expected output: AAAAA