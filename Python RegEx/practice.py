from pprint import pprint
import csv
import re

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    ns_dict = {}
    new_contacts_list = []

    for contact_list in contacts_list:
        edit_num = r"+7(\2)\3-\4-\5 \6"
        contact_list[5] = re.sub(
            r'(\+*?[78])[ ]*?\(?(\d\d\d)\)*?[\s-]*?(\d\d\d)-*?(\d\d)-*?(\d\d)[\s\(]*(доб. \d\d\d\d)*[\)]?',
            edit_num,
            contact_list[5])
        fio = ' '.join(contact_list[:3]).split()
        contact_list[:len(fio)] = fio
        name_surname = ' '.join(contact_list[:2])

        if ns_dict.get(name_surname):  # 1.проверка на наличие ключа в словаре
            ns_dict[name_surname] = [
                ns_dict[name_surname][i] if ns_dict[name_surname][i]
                else contact_list[i] for i in range(7)
            ]
            # 2.прибавление значения дополнительного к значению ключа

        else:
            ns_dict[name_surname] = contact_list  # 3. добавление в словарь ключ-значение

    new_contacts_list = [values for key, values in ns_dict.items()]
    pprint(new_contacts_list)

# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_contacts_list)
