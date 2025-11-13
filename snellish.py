#imports
import argparse

#per word translator
def snellify(word):
    vowels = "aeiouAEIOU"
    if word[0] in vowels:
        return "sn" + word
    else:
        current_index = 0
        if word[0] == "s":
            if word[1] == "n":
                return "sn" + word
            else:
                pass
        else:
            pass
        for i in word:
            if current_index > 0 and i.lower() == "y":
                break
            if i not in vowels:
                current_index += 1
            else:
                break
        return "sn" + word[current_index:]

def snellify_d(word):
    print(f"translating {word}...")
    vowels = "aeiouAEIOU"
    if word[0] in vowels:
        print(f"{word} begins with vowel")
        return "sn" + word
    else:
        current_index = 0
        if word[0] == "s":
            if word[1] == "n":
                print(f"{word} begins with 'sn'")
                return "sn" + word
            else:
                pass
        else:
            pass
        for i in word:
            if current_index > 0 and i.lower() == "y":
                print(f"{word} has a vowel-sounding 'y'")
                break
            if i not in vowels:
                current_index += 1
            else:
                break
        print(f"translated {word} into: sn" + word[current_index:])
        return "sn" + word[current_index:]

#info arg -i
def info():
    print("---------------------------")
    print("--SNELLISH TRANSLATOR 1.0--")
    print("---------------------------")
    print(
    '''
--GENERAL INFO--
ENG: The snellish language is the official language of the snails. It is an alteration of the english language, to accomodate 'sn' as
the most important and key sound in the language. Because of this, context and tone become very important when speaking snellish. Due
to the fact that some english words can be spelt the same way as each other in snellish, it is important to observe the context and tone
of the convsersation to avoid misunderstandings.

SNL: Sne snsnellish snanguage snis sne snofficial snanguage snof sne snsnails. snIt snis snan snalteration snof sne snenglish snanguage, sno snaccomodate 'sn' snas
sne snost simportant snand sney snound snin sne snanguage. snecause snof snis, snontext snand sone snecome snery snimportant snen sneaking snsnellish. snue
sno sne snact snat snome snenglish sords snan sne snelt sne sname snay snas sneach snother snin snsnellish, snit snis snimportant sno snobserve sne snontext snand snone
snof sne snonversation sno snavoid snisunderstandings.

--GRAMMATICAL RULES--
1. Snellish follows the same grammatical rules as english, apart from the below alterations
1. All words begin with 'sn-'
2. To add 'sn-' to the start of a word you must first remove all consanants until you reach a vowel. e.g: plays = snays
3. If there are no consonants before the first vowel, simply add 'sn-' straight onto the beginning of the word. e.g: apple = snapple
4. 'y' is included as a vowel in the above conditions when it is at a position that is not first. e.g: symphony = snymphony
5. If a word already begins with 'sn', then simply add another 'sn-' to the beginning. e.g: snail = snsnail

--TRANSLATOR GUIDANCE--
1. The translator does not handle special characters, don't use them
2. For correct numerical pronunciation outputs, enter numbers in their full word form
3. The translator cannot capitalise correctly, you will have to munually edit for proper grammar

--TERMINAL ARGUMENTS--
-i : display this informational screen
-l : display the translation line-by-line, as the translator does it's work
    ''')

#main
def main():
    print("---------------------------")
    print("--SNELLISH TRANSLATOR 1.0--")
    print("---------------------------")
    print("Run 'snellish -i' for more info")
    print("---------------------------")
    phrase = input("Enter string to translate: ")
    split_phrase = phrase.split(" ")
    translated_phrase = ""
    for i in split_phrase:
        word = snellify(i)
        translated_phrase = translated_phrase + word + " "

    print("translation (snellish): " + translated_phrase)

def main_d():
    print("---------------------------")
    print("--SNELLISH TRANSLATOR 1.0--")
    print("---------------------------")
    print("running in debug mode")
    print("---------------------------")
    phrase = input("Enter string to translate: ")
    split_phrase = phrase.split(" ")
    translated_phrase = ""
    for i in split_phrase:
        word = snellify_d(i)
        translated_phrase = translated_phrase + word + " "

    print("translation (snellish): " + translated_phrase)


#run
if __name__ == '__main__':
    #setup argument parser
    parser = argparse.ArgumentParser(description="snellish translator 1.0 - terminal argument parser")
    parser.add_argument("-i", action="store_true", help="get info on snellish translator 1.0")
    parser.add_argument("-d", action="store_true", help="run the translator in debug mode")
    args = parser.parse_args()

    #get info
    if args.i:
        info()
    elif args.d:
        main_d()
    else:
        main()
