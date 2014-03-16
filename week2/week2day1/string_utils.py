def lines(text):
    lines = text.split("\n")
    return lines


def unlines(elements):
    text = ""
    for i in range(len(elements) - 1):
        text += elements[i] + "\n"
    text += elements[len(elements) - 1]
    return text


def words(text):
    text1 = text.replace("\n", " ")
    words = text1.split(" ")
    i = 0
    n = len(words)
    while i < n:
        if words[i] == "":
            words.pop(i)
            n = len(words)
        i += 1

    return words


def unwords(elements):
    text = ""
    for i in range(len(elements) - 1):
        text += elements[i] + " "
    text += elements[len(elements) - 1]
    return text


def tabs_to_spaces(str, one_tab_n_spaces):
    repl = " "* int(one_tab_n_spaces)
    new_str = str.replace("\t", repl)
    return new_str