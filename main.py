def main():
    total_points = 0
    correct_answers = input('Wie viele richtige Antworten? ')
    incorrect_answers = input('Wie viele falsche Antworten? ')

    total_points = correct_answers * 10 - incorrect_answers - 5

    if total_points > 100
        total_points = 100
    elif total_points < 0:
        total_points = 0

    print('Endpunktzahl: ' + total_points)


if __name__ = '__main__':
    main()