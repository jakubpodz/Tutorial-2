# Assign a variable: my_string = 'Today we are learning about variables and data-types'. 
# Extract  (using slicing syntax) the following strings from 'my_string': 
#	'Today'
#	'data-types'
#	'learning about variables'
#	'sepyt-atad dna selbairav tuoba gninrael era ew yadoT' (backwards!)
#	'yadoT'
#	 'Tdyw r erigaotvralsaddt-ye' (?!?)

# Enter your code below here:
my_string = 'Today we are learning about variables and data-types'
print(my_string[0:5]) # 'Today'
print(my_string[42:51]) # 'data-types'
print(my_string[13:38]) # 'learning about variables'
print(my_string[::-1]) # 'sep yt-adat dna selbairav tuoba gn
print(my_string[5::-1]) # 'yadoT'
print(my_string[::2]) # 'Tdyw r erigaotvralsaddt-ye' 
