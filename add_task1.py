types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def remove_duplicates():
    duplicate_value = []
    for ticket in tickets:
        unique_value = []
        for value in tickets[ticket]:
            if value not in duplicate_value:
                duplicate_value.append(value)
                unique_value.append(value)
        tickets[ticket] = unique_value
    return tickets



def bind_dict():
    ticket = remove_duplicates()
    tickets_by_type = {}
    for t in types:
        if t in ticket:
            tickets_by_type[types[t]] = ticket[t]
    return tickets_by_type


print(bind_dict())