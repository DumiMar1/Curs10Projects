def area(a, b):
    return a * b

print(area(5, 10))

def mean(*args):
    return sum(args) / len(args)

print(mean(1,2,3,4))


def return_string(*args):
    empty_list = []
    for arg in args:
        if type(arg) == str:

            empty_list.append(arg.upper())

    return sorted(empty_list)


print(return_string("snow", "glacier", "iceberg"))
print(return_string(True, None, False, 12, 3+5j, 'aaa', [1, 2, 3], (1, 2, 3), {1, 2, 3}, {'a': 1, 'b': 2}))

#File Processing


with open("vegetables.txt", "w+") as myfile:

    myfile.write("tomatoes\ncucumbers\nonions\n")
    myfile.write("beans")

with open("vegetables.txt", "a+") as myfile:

    myfile.write("tomatoes\ncucumbers\nonions\n")
    myfile.write("beans")


