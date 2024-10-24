"""

def report_count(token):
    count = 0
    with open('/content/corpus.txt', 'r') as file:
        paragraph = file.read()
        count = tokenCount(token, paragraph)
    print(f"The term '{token}' shows up in the corpus {count} times.")
"""
def report_count(token):
    count = 0
    with open('dummy/corpus.txt', 'r') as file:
        paragraph = file.read()

        inputArray = paragraph.split()
        count = 0
        for i in inputArray:
          if i == token:
            count += 1
    print(f"The term '{token}' shows up in the corpus {count} times.")

