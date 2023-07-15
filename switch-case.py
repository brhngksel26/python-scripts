select = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'divide': lambda x, y: x / y,
    'multiply': lambda x, y: x * y,
}

print(select['add'](15, 5))
print(select['subtract'](15, 5))
print(select['divide'](15, 5))
print(select['multiply'](15, 5))
