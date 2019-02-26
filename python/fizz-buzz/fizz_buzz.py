import sys

class fizzBuzz:
  def __init__(self, inputData):
    inputData = inputData.split(':');
    self.number = int(inputData[0])
    self.word = inputData[1]

def getFizzBuzzResult(fizzBuzzs, targetNumber):
  joinedWord = ""
  for fb in fizzBuzzs:
    if targetNumber % fb.number == 0:
      joinedWord += fb.word

  if len(joinedWord) == 0:
    return targetNumber
  else:
    return joinedWord

def main(argv):

  fizzBuzzs = [fizzBuzz(argv[i]) for i in range(len(argv) - 1)]
  sorted(fizzBuzzs, key=lambda x: x.number)
  print(getFizzBuzzResult(fizzBuzzs, int(argv[-1])))



if __name__ == '__main__':
    main(sys.argv[1:])