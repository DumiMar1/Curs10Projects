def area(a, b):
    return a * b

print(area(5, 10))

def mean(*args):
    return sum(args) / len(args)

print(mean(1,2,3,4))


def return_string(*args):
    list = []
    for arg in args:
        list.append(arg.upper())

    return sorted(list)

print(return_string("snow", "glacier", "iceberg"))

#File Processing
