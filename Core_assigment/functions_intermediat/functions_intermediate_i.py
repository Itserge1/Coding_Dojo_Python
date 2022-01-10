x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# 1

# a
x[1][0] = 15
print(x)
# b
students[0]['last_name'] = 'Bryant'
# c
sports_directory["soccer"][0] = "Andres"
# d
z[0]['y'] = 30

# 2
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(some_list):
    for i in range (len(some_list)):
        print(some_list[i])

iterateDictionary(students)

# 3
# def iterateDictionary2(key_name, some_list):
#     for i in range( len(some_list)):
#         if key_name == "first_name":
#             print(some_list[i]["first_name"])
#         elif key_name == "last_name":
#             print(some_list[i]["last_name"])

# iterateDictionary2("first_name", students)
# iterateDictionary2("last_name", students)

def iterateDictionary2(key_name, some_list):
    for i in range( len(some_list)):
        print(some_list[i][key_name])
iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)

# 4

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for i in range (len(some_dict)):
        if (i % 2 == 0):
            num = len(some_dict[some_dict.keys()[i + 1]])
            nums = str(num)
            print(nums +" "+ some_dict.keys()[i + 1].upper())
            for j in range(len(some_dict[some_dict.keys()[0 +1]])):
                print ( some_dict[some_dict.keys()[i +1]][j])
        elif (i % 2 != 0):
            num = len(some_dict[some_dict.keys()[i - 1]])
            nums = str(num)
            print(nums +" "+ some_dict.keys()[i - 1].upper())
            for y in range (len(some_dict[some_dict.keys()[1 - 1]])):
                print (some_dict[some_dict.keys()[i - 1]][y])

printInfo(dojo)