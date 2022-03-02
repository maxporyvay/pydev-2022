import textdistance

def bullscows(guess: str, secret: str) -> (int, int):
    bulls = len(secret) - textdistance.hamming(guess, secret)
    cows = int(len(secret) * textdistance.sorensen(guess, secret))
    return (bulls, cows)
