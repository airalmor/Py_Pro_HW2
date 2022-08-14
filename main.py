import csv
import re
from logger import logger

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def change_income_file(contacts_list):
    contacts_list[0][0], contacts_list[0][2] = contacts_list[0][2], contacts_list[0][0]
    find_phone_pattern = r"(\+7|8)\s?\(?(\d{3})\)?\s?\-?(\d{3})\-?(\d{2})\-?(\d{2})\s?\(?([доб. ]*)(\d*)\)?"
    change_phone_pattern = r'+7(\2)\3-\4-\5 \6\7'
    find_name_pattern = r'(\w+)\s(\w+)\s?(\w+)?'
    change_pattern_surname = r'\1'
    change_pattern_firstname = r'\2'
    change_pattern_lastname = r'\3'

    for i in contacts_list:
        result = re.sub(find_phone_pattern, change_phone_pattern, i[5])
        i[5] = result
        i[0] = i[0] + ' ' + i[1] + ' ' + i[2]
        i[2] = (re.sub(find_name_pattern, change_pattern_lastname, i[0]).strip())
        i[1] = (re.sub(find_name_pattern, change_pattern_firstname, i[0]).strip())
        i[0] = (re.sub(find_name_pattern, change_pattern_surname, i[0]).strip())
    return contacts_list


@logger
def delete_dupe(contacts_list):
    contacts_list.sort()
    new_contact_list = []
    check_name = ''
    for i, person in enumerate(contacts_list):

        if check_name != person[0] + person[1]:
            new_contact_list.append(person)
        else:

            if new_contact_list[-1][2] == '':
                new_contact_list[-1][2] = contacts_list[i][2]
            if new_contact_list[-1][3] == '':
                new_contact_list[-1][3] = contacts_list[i][3]
            if new_contact_list[-1][4] == '':
                new_contact_list[-1][4] = contacts_list[i][4]
            if new_contact_list[-1][5] == '':
                new_contact_list[-1][5] = contacts_list[i][5]
            if new_contact_list[-1][6] == '':
                new_contact_list[-1][6] = contacts_list[i][6]

        check_name = person[0] + person[1]
    return new_contact_list


if __name__ == '__main__':
    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    change_income_file(contacts_list)

    new_contact_list = delete_dupe(contacts_list)

    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_contact_list)
