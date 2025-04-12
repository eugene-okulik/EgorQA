results = [
    "результат операции: 42",
    "результат операции: 514",
    "результат работы программы: 9"
]

for line in results:
    colon_index = line.index(':')
    number_str = line[colon_index + 2:]
    number = int(number_str)
    result = number + 10
    print(result)
    