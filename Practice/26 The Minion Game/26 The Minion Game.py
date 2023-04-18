def minion_game(string):
    vowels = 'aeiou'
    length = len(string)
    stuart, kevin = [0]*2
    for i, letter in enumerate(string.lower()):
        if (letter in vowels):
            kevin += length - i
        else:
            stuart += length - i
    
    print(f'Stuart {stuart}' if(stuart > kevin) else f'Kevin {kevin}' if (kevin > stuart) else 'Draw') 

if __name__ == '__main__':
    s = input()
    minion_game(s)