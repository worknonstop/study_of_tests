from capitalize import capitalize

if capitalize("hello") != "Hello":
    raise Exception("The function doesn't work properly")


if capitalize("") != "":
    raise Exception("The function doesn't work properly")


print("All tests passed")
