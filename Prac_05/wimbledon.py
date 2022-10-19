def main():
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        """set list and split by line"""
        text = {}
        text = in_file.read().split("\n")
        del text[0]

        name_reader(text)

        country_printer(text)


def name_reader(text):
    print("Wimbledon Champions:")
    win_dictionary = {}
    for line in text:
        split_lines = line.split("\t")
        name = split_lines[2]
        if name not in win_dictionary:
            win_dictionary[name] = 0
        win_dictionary[name] += 1
    for pair in win_dictionary:
        print(f"{pair:17} - {win_dictionary[pair]}")


def country_printer(text):
    print("These 12 countries have been in Wimbledon:")
    countries_list = []
    for line in text:
        split_lines = line.split("\t")
        country = split_lines[1]
        if country not in countries_list:
            countries_list.append(country)
    countries_list.sort()
    sep = ", "
    print(sep.join(countries_list))


main()

