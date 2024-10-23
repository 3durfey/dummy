def report_count(token):
    count = 0
    with open(file_path, 'r') as file:
        paragraph = file.read()
        count = helperFunctions.tokenCount(token, paragraph)
    print(count)