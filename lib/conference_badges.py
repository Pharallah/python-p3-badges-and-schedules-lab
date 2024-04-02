def badge_maker(name):
    badge = f"Hello, my name is {name}."
    return badge

# FOR LOOP batch_badge_creator
# def batch_badge_creator(names):
#     badge = []
#     for name in names:
#         badge.append(f"Hello, my name is {name}.")
#     return badge

# LIST COMPREHENSION
def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

# FOR LOOP
# def assign_rooms(names):
#     assigned_rooms = []
#     for index, name in enumerate(names, start= 1):
#         assigned_rooms.append(f"Hello, {name}! You'll be assigned to room {index}!")
#     return assigned_rooms

# LIST COMPREHENSION assign_rooms
def assign_rooms(names):
    return [f"Hello, {name}! You'll be assigned to room {index}!" for index, name in enumerate(names, start= 1)]

# FOR LOOP
# def printer(names):
#     badges = batch_badge_creator(names)
#     for badge in badges:
#         print(badge)
#     rooms = assign_rooms(names)
#     for room in rooms:
#         print(room)

# LIST COMPREHENSION assign_rooms
def printer(names):
    badges = batch_badge_creator(names)
    badge_printer = [print(badge) for badge in badges]
    rooms = assign_rooms(names)
    room_printer = [print(room) for room in rooms]