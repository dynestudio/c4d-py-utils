tags = '#cinema4d #c4d #maxon'

tags2 = tags.replace('#',',')

tags3 = tags2.replace(' ','')

tags4 = tags3.replace(',',', ')

tags5 = tags4[2:] + ','

print tags5
