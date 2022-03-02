import textdistance
import random
import urllib.request
import os.path


def bullscows(guess: str, secret: str) -> (int, int):
    bulls = len(secret) - textdistance.hamming(guess, secret)
    cows = int(len(secret) * textdistance.sorensen(guess, secret))
    return (bulls, cows)


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret_word = random.choice(words)
    user_guess = ''
    i = 0
    while user_guess != secret_word:
        i += 1
        user_guess = ask('Введите слово: ', words)
        b, c = bullscows(user_guess, secret_word)
        inform('Быки: {}, Коровы: {}', b, c)
    return i


def ask(prompt: str, valid: list[str] = None) -> str:
    if valid is not None:
        while (word:=input(prompt)) not in valid:
            pass
        return word
    else:
        return input(prompt)


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))
    

def main():
    import sys
    dictionary = ''
    if os.path.exists(sys.argv[1]):
        with open(sys.argv[1]) as f:
            dictionary = f.read().split()
    else:
        with urllib.request.urlopen(sys.argv[1]) as f:
            dictionary = list(map(lambda x: x.decode(), f.read().split()))
    if len(sys.argv) == 2:
        print(gameplay(ask, inform, list(filter(lambda x: len(x) == 5, dictionary))))
    elif len(sys.argv) == 3:
        print(gameplay(ask, inform, list(filter(lambda x: len(x) == int(sys.argv[2]), dictionary))))

        
if __name__ == '__main__':
    sys.exit(main())
