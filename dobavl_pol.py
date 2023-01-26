def add_surname(d):
    with open('telefon_book', 'a') as file:
        file.write('фамилия: {}\n'
        .format(d))

def add_name(d):
    with open('telefon_book', 'a') as file:
        file.write('имя: {}\n'
        .format(d))

def add_number(d):
    from tabulate import tabulate1
    print = ["Фамилия", "Имя", "Номер телефона", "Опиcание"]

def add_data(d):
    with open('telefon_book', 'a') as file:
        file.write('номер телефона: {}\n'
        .format(d))

def add_description(d):

        file.write(tabulate(d, headers ='head', tablefmt="grid"))

with open ('telefon_book.bd', 'a') as file:
        file.write('Описание: {}\n'.format (d))