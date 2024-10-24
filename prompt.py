def report_count(token):
    from .helperFunctions import tokenCount
g    count = 0
    with open('dummy/corpus.txt', 'r') as file:
        paragraph = file.read()
        count = tokenCount(token, paragraph)
    print(f"The term '{token}' shows up in the corpus {count} times.")
