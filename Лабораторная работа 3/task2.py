# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой


def find_common_participants(str1, str2, delimiter=','):
    participants_set1 = set(str1.split(delimiter))
    participants_set2 = set(str2.split(delimiter))
    common_participants = participants_set1.intersection(participants_set2)
    common_list = sorted(participant.strip() for participant in common_participants)
    return common_list

common_participants = find_common_participants(participants_first_group, participants_second_group, delimiter='|')

print(common_participants)