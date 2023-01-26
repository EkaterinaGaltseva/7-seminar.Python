def add_surname(d):

    with open ('telefon_book.bd', 'a') as file:
        file.write('Фамилия: {}\n'
        
    .format (d))

def add_name(d):

    with open ('telefon_book.bd', 'a') as file:
        file.write('Имя: {}\n'
 .format (d))

def add_number(d): 
    from tabulate import tabulate
    tabl = ["Фамилия", "Имя", "Номер телефона", "Описание"]
    print(tabulate(tabl))
    return d

def add_data(d):
    with open ('telefon_book.bd', 'a') as file:
        file.write('phone_number: {}\n'
 .format (d))
def add_description(d):
    from tabulate import tabulate
    file.write(tabulate(d, headers ='head', tablefmt="grid")) 
    with open ('telefon_book.bd', 'a') as file:
        file.write('discripion: {}\n'.format (d))