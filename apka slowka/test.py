words = [
'a',
'b',
'""',
]
dous = (''""'')

for i in list(words):
    if i in dous:
        words.remove(i)

print(words)