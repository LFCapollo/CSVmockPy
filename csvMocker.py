from faker import Faker
import time
from faker.providers import internet
import csv
import mockConfig as conf

fake = Faker()
for i in range(conf.mocker['numFiles']):
    with open(conf.mocker['destination']+'\\'+conf.mocker['fileName'] +str(i) +'.csv', mode='w', newline='') as destination_file:
        employee_writer = csv.writer(destination_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for i in range(conf.mocker['numRows']):
            employee_writer.writerow(['test1', fake.pystr(min_chars=None, max_chars=conf.mocker['maxChar']), fake.pystr(min_chars=None, max_chars=conf.mocker['maxChar'])])

