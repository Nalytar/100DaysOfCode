def replace_placeholder_and_return_content(name):
    with open("./input/letter/starting_letter.txt", "rt") as letter:
        content = letter.read()
        return content.replace("[name]", name)


def write_letter(filename, content):
    with open(filename, "w") as letter:
        letter.write(content)


def create_letters():
    with open("./input/names/invited_names.txt", "rt") as names:
        for name in names.readlines():
            name = name.strip()

            filename = "./output/ReadyToSend/letter_for_" + name.lower() + ".txt"
            content = replace_placeholder_and_return_content(name)
            write_letter(filename, content)


create_letters()
