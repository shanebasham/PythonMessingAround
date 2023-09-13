
def main():
    # Read provinces.txt into a list named provinces_list.
    provinces_list = read_list("provinces.txt")
    # Print list.
    print(provinces_list)
    # Remove the first element from the list.
    provinces_list.pop(0)
    # Remove the last element from the list.
    provinces_list.pop()
    # Replace "AB" with "Alberta".
    for i in range(len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"
    count = provinces_list.count("Alberta")
    print(f"Alberta occurs {count} times in the modified list.")


def read_list(filename):
    text_list = []
    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)
        return text_list

main()