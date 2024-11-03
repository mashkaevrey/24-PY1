def find_common_participants(participants_first_group, participants_second_group, s=','):
    set_p1 = participants_first_group.split(s)
    set_p2 = participants_second_group.split(s)
    common = list(set(set_p1).intersection(set(set_p2)))
    common.sort()
    return common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, s='|'))
