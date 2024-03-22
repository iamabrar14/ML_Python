'''
List is like array of C++. Basically it stores homogenous datas together
'''

subjects=["C","C++","Java","Python","OS","Microprocessor"]
print(subjects)
print("Java" in subjects) #will return true, cause Java is in the list
print("Dart" not in subjects) #will also return true, cause Dart is not in the list

print(subjects + ["Swift",15]) ##adding some elements in this list

