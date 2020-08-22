with open('script.txt', 'r') as read_file:
    with open('script_copy.txt', 'w') as write_file:
        for line in read_file:
            write_file.write(line)

