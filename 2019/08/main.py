# Image is 25x6
# Each layer is 150 digits
with open('input.txt') as f:
    layers = f.read().strip()
    layers = [layers[i:i+150] for i in range(0, len(layers), 150)]

l = min(layers, key=lambda x: x.count('0'))
print(l)
print(l.count('1') * l.count('2'))

final_image = ''
for i in range(len(l)):
    for layer in layers:
        if layer[i] != '2':
            final_image += layer[i]
            break

final_image = [final_image[i:i+25] for i in range(0, 150, 25)]

for row in final_image:
    print(row.replace('0', u"\u25A0").replace('1', u"\u25A1"))
