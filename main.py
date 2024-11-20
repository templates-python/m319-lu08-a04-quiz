def main():
    total_points = 0

    # Input values need to be converted to integers
    correct_answers = int(input('Wie viele richtige Antworten? '))
    incorrect_answers = int(input('Wie viele falsche Antworten? '))

    # Correct logic for total points calculation
    total_points = correct_answers * 10 - incorrect_answers * 5

    # Syntax error fixed: Missing colon after `if` statement
    if total_points > 100:
        total_points = 100
    # Syntax error fixed: Correct elif structure
    elif total_points < 0:
        total_points = 0

    # Fixed concatenation by using f-strings
    print(f'Endpunktzahl: {total_points}')


# Syntax error fixed: `=` replaced with `==`
if __name__ == '__main__':
    main()
