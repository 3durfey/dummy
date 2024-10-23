def tokenCount(token, paragraph):
  inputArray = paragraph.split()
  count = 0
  for i in inputArray:
    if i == token:
      count += 1
  return count
