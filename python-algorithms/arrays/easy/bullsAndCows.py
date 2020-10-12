class Solution:
    def getHint(self, secret, guess):
        nBulls = 0
        secretMap = {}
        guessMap = {}
        for secretDigit, guessDigit in zip(secret, guess):
            print((secretDigit, guessDigit))
            if secretDigit == guessDigit:
                nBulls += 1
            secretMap[secretDigit] = secretMap.get(secretDigit, 0) + 1
            guessMap[guessDigit] = guessMap.get(guessDigit, 0) + 1
        nCows = 0
        for key in guessMap:
            if key not in secretMap:
                continue
            guessVal = guessMap[key]
            secretVal = secretMap[key]
            nCows += (secretVal if guessVal >= secretVal else min(guessVal, secretVal))
        print(nCows)
        print(nBulls)
        return "{}A{}B".format(nBulls, nCows-nBulls)

i = 2

from collections import Counter


secret = "1123"
guess = "0111"

secretCounter = Counter(secret)
guessCounter = Counter(guess)

solution = Solution()
solution.getHint(secret, guess)
