def second_index(text, some_str):
    number = text.find(some_str)
    number = text.find(some_str, number + 1)
    if number != -1:
        return number
    else:
        None
text = str(input('Type anything:'))
some_str = str(input('Type letters to find:'))
second_index(text, some_str)

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')