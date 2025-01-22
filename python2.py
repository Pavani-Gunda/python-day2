#slicing(+)
text="If you can't find a way, create one!"
print(text)
print(len(text))
print(text[2: 6])
print(text[5])
print(text[ :12])
print(text[26: ])
print(text[1:1])
print(text[26: 2: -1])#-1 indicates reverse direction
print(text[-1:-36]) #empty string
print(text[-5: -15 : -2])
print(text[-34 : -32 : ])
print(text[ : : -3])
print("index 16 value is", text[16])
#text[16] = 'l'
#print(text[16]) #immutability but when reassign it will change
print(id(text))#to know the address value.
text1="If you can't find a way, create one!"
text2="If you can't find a way, create one!"
print(id(text2))
print(id(text1))
print(type(2))#int
print(type(10.63514))#float
print(type(5+8j))#complex
