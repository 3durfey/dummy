def report_count(token):
    count = 0
    with open(file_path, 'r') as file:
        paragraph = file.read()
        count = tokenCount(token, paragraph)
    print(f"The term '{token}' shows up in the corpus {count} times.")