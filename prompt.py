def report_count(token):
    #from .helperFunctions import tokenCount
    import dummy
    count = 0
    with open(dummy.path, 'r') as file:
        paragraph = file.read()
        count = dummy.tokenCount(token, paragraph)
    print(f"The term '{token}' shows up in the corpus {count} times.")
