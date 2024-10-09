#task1
# coords = [(10, 20), (40, 20), (10, 30), (40, 30)]
#
# def seach_square(coords):
#     new_array =  sorted(coords,key=lambda item:item[0])
#     first_side = abs(new_array[0][1]-new_array[1][1])
#     second_side = abs(new_array[1][0]-new_array[2][0])
#     square = first_side*second_side
#     return square
#
#
# print(seach_square(coords))
ticket_types = ('Ж', 'К', 'З')
user_tickets = ['З', 'К', 'Ж', 'З', 'З', 'З', 'Ж', 'К', 'К']

obj = {}

obj[ticket_types[0]] = user_tickets.count(ticket_types[0])
obj[ticket_types[1]] = user_tickets.count(ticket_types[1])
obj[ticket_types[2]] = user_tickets.count(ticket_types[2])

newArray = []
for j in range(0,len(ticket_types)):
    for i in range(0,user_tickets.count(ticket_types[j])):
        newArray.append(ticket_types[j])
print(newArray)


def sorted_ticket(ticket_types,user_tickets):
    newArray = []
    for i in ticket_types:
        for j in user_tickets:
            if i == j:
                newArray.append(j)
    return newArray


# print(sorted_ticket(ticket_types, user_tickets))
