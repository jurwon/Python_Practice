class Hangman():
  def __init__(self,word,remainingGuesses):
    self.word = word.toLowerCase().split('')
    self.remainingGuesses = remainingGuesses
    self.guessedLetters = ['abcde']
    self.status = 'playing' #시작 여부

  # def finished(self):
  #   self.word.

  # def calculateStatus(self):
  #   finished = self.word.every((letter) -> self.guessedLetters.includes(letter))

game1 = Hangman("b","do")
print(f"game1 : {game1}")
  