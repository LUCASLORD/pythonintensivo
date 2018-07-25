alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_0['speed'] = 'medium'

print("Posição X Original: {}".format(alien_0['x_position']))

if alien_0['speed'] == 'slow' : x_increment = 1
elif alien_0['speed'] == 'mediun' : x_increment = 2
else:
    # Este deve ser um alienígena rápido
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("Nova Posição X: {}".format(alien_0['x_position']))

print(alien_0)
del alien_0['points']
print(alien_0)
