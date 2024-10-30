immutable_va = (1, 5, True, 'srtring')
print(immutable_va)

# immutable_va [0] = 100
# кортеж не поддерживает обращение по элементам,
# Кортежи часто используются в качестве хранилищ данных, особенно когда необходимо сохранить список в неизменном виде

mutable_list = ([1,2,3],0)
print(mutable_list)
mutable_list[0][1] = 3
print(mutable_list)