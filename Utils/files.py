import csv

EXAMPLE_TRAIN = 'CBF_TRAIN.csv'
EXAMPLE_TEST = 'CBF_TEST.csv'

# appenda cada linha ao elemento[i] do array
def read_file(path):
    f = open(path, 'r', encoding='utf-8')
    rdr = csv.reader(f)
    page = []
    for line in rdr:
        page.append(line)
    f.close()

    return page


# retorna dados para o treinamento do modelo
def get_data(name):
    x_trains = []
    y_trains = []
    x_tests = []
    y_tests = []
    trains = read_file(name+'_TRAIN.csv')
    for line in trains:
        x_trains.append(list(map(float, line[1:])))
        y_trains.append(int(line[0]))
 	
    tests = read_file(name+'_TEST.csv')
    for line in tests:
        x_tests.append(list(map(float, line[1:])))
        y_tests.append(int(line[0]))

    return x_trains, y_trains, x_tests, y_tests


# retorna dados para caso examplo
def get_data_example(name):
    x_trains = []
    y_trains = []
    x_tests = []
    y_tests = []
    trains = read_file(EXAMPLE_TRAIN)
    for line in trains:
        x_trains.append(list(map(float, line[1:])))
        y_trains.append(int(line[0]))

    tests = read_file(EXAMPLE_TEST)
    for line in tests:
        x_tests.append(list(map(float, line[1:])))
        y_tests.append(int(line[0]))

    return x_trains, y_trains, x_tests, y_tests


if __name__ == '__main__':
    x_trains, y_trains, x_tests, y_tests = get_example_train_test_datasets()
