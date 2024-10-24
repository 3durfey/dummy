def report_count(token):
    from .helperFunctions import tokenCount
    import dummy
    count = 0
    with open(dummy.p, 'r') as file:
        paragraph = file.read()
        count = tokenCount(token, paragraph)
    print(f"The term '{token}' shows up in the corpus {count} times.")
