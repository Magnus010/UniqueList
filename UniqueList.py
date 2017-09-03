def list_append(filename):
    with open(filename) as f:
        for line in open(filename):
            if not unique_list.__contains__(line[:-1]):
                unique_list.append(line[:-1])
    return unique_list

if __name__ == "__main__":
    original_filename = "adlists.list"
    additional_file = "lists.txt"
    new_filename = "adlists.list.new"

    unique_list = []

    list_append(original_filename)
    list_append(additional_file)

    output_file = open(new_filename, 'w')

for item in unique_list:
  output_file.write("%s\n" % item)


