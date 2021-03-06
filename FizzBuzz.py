def fizzbuzz(divisors, words, length):
    """
    :param divisors: List of Int variables to check against.
    :param words: List of String variables to modify output, must be the same length as <divisors>
    :param length: Int to determine the size of the output.
    :return: None
    """
    if len(divisors) != len(words):
        raise IndexError("The number of divisors and words do not match.")
    if length < 1:
        raise ValueError("Length must be an integer above 1")
    for i in range(1, length+1):
        output = ""
        iterator = 0
        for j in divisors:
            if i % j == 0:
                output += words[iterator]
                iterator += 1
            else:
                iterator += 1
        if output == "":
            output = i
        print(output)
#Add a relevant output later.
