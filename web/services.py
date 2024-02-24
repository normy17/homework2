def three_numbers(numbers):
    if 'choice' in numbers:
        if numbers['choice'] == 'max':
            return max(int(numbers['number1']), int(numbers['number2']), int(numbers['number3']))
        if numbers['choice'] == 'min':
            return min(int(numbers['number1']), int(numbers['number2']), int(numbers['number3']))
        if numbers['choice'] == 'avg':
            return (int(numbers['number1']) + int(numbers['number2']) + int(numbers['number3'])) / 3


def prog_day(year):
    if 'year' in year:
        if int(year['year']) % 4 == 0:
            return '12'
        else:
            return '13'