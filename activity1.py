#create a tuple with different data types
tuplex = ("tuple", False, 2.3, 1)
print(tuplex)

#create a tuple
tuplex = (4, 6, 3, 2, 5, 1)
print(tuplex)

#tuples are immutable, so u can not add new elements
#useing merge of tuples with the + operator you can add an element and it will create a new tuple

tuplex = tuplex + (9,)
print(tuplex)

#counts the number of frequency of item 50 from a tuple
tuple1= (50, 10, 60, 70, 50)
print(tuple1.count(50))

#create a tuple
tuplex = (2, 4, 3, 5, 6, 7, 8, 4, 6, 1)
#used tuple[start: stop] the start index is inclusive and the stop index

_slice = tuplex[3:5]
#is exclusive
print(_slice)

#if the start index isnt defined, is taken from the beginning of the tuple
_slice = tuplex[:6]
print(_slice)