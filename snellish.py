### SNELLISH-TRANSLATOR 1.0
### Version: 1.0 (main branch)
### Original Creator: HyperGlowGames on Github


#imports
import argparse
import sys
import os

#modes detection variables
is_debug = False
is_info = False

#per word translator
def snellify(word):
    vowels = "aeiouAEIOU1234567890"
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

#per word translator (debug mode)
def snellify_d(word):
    print(f"-d: translating '{word}'...")
    vowels = "aeiouAEIOU"
    if word[0] in vowels:
        print(f"-d: '{word}' begins with vowel")
        return "sn" + word
    else:
        print(f"-d: '{word}' does not begin with a vowel")
        current_index = 0
        if word[0] == "s":
            if word[1] == "n":
                print(f"-d: '{word}' begins with 'sn'")
                return "sn" + word
            else:
                pass
        else:
            pass
        for i in word:
            if current_index > 0 and i.lower() == "y":
                print(f"-d: '{word}' contains a vowel-sounding 'y' at position {current_index}")
                break
            if i not in vowels:
                print(f"-d: '{word}' contains a consonant at position {current_index}")
                current_index += 1
            else:
                print(f"-d: '{word}' contains a vowel at position {current_index}")
                break
        print(f"-d: translated '{word}' into: sn" + word[current_index:])
        return "sn" + word[current_index:]

#info arg -i
def info():
    print("-------------------------------")
    print("----SNELLISH TRANSLATOR 1.0----")
    print("-------------------------------")
    print("     informational screen      ")
    print("-------------------------------")
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
1. The translator does not handle special characters at the beginning of a word
2. For correct numerical pronunciation outputs, enter numbers in their full word form
3. The translator cannot capitalise correctly, you will have to munually edit for proper grammar
4. The Translator cannot handle double spaces, this is a known error

--TERMINAL ARGUMENTS--
-i : display this informational screen
-d : run the translator in debug mode
    ''')

#main
def main():
    print("-------------------------------")
    print("----SNELLISH TRANSLATOR 1.0----")
    print("-------------------------------")
    print("run 'snellish -i' for more info")
    print("-------------------------------")
    phrase = input("Enter string to translate: ")
    split_phrase = phrase.split(" ")
    translated_phrase = ""
    for i in split_phrase:
        word = snellify(i)
        translated_phrase = translated_phrase + word + " "

    print("translation (snellish): " + translated_phrase)

#main (debug mode)
def main_d():
    print("-------------------------------")
    print("----SNELLISH TRANSLATOR 1.0----")
    print("-------------------------------")
    print("     running in debug mode     ")
    print("-------------------------------")
    phrase = input("Enter string to translate: ")
    split_phrase = phrase.split(" ")
    print(f"-d: split '{phrase}' into {split_phrase}")
    translated_phrase = ""
    for i in split_phrase:
        word = snellify_d(i)
        translated_phrase = translated_phrase + word + " "

    print("translation (snellish): " + translated_phrase)


#run
if __name__ == '__main__':
    try:
        #setup argument parser
        parser = argparse.ArgumentParser(description="snellish translator 1.0 - terminal argument parser")
        parser.add_argument("-i", action="store_true", help="get info on snellish translator 1.0")
        parser.add_argument("-d", action="store_true", help="run the translator in debug mode")
        args = parser.parse_args()

        #get info
        if args.i:
            is_info = True
            info()
        elif args.d:
            is_debug = True
            main_d()
        else:
            main()
    except Exception as error:
        e_type, e_obj, e_tb = sys.exc_info()
        file = os.path.split(e_tb.tb_frame.f_code.co_filename)[1]
        print("")
        print("-------------------------------")
        print("---------! E R R O R !---------")
        print("-------------------------------")
        print("The translator has encountered an error!")
        print("Please rpeort this issue at: https://github.com/HyperGlowGames/Snellish-translator/issues")
        print(f'''
--DETAILS--
Translator version: 1.0
File: {file}
Debug Mode: {is_debug}
Info Screen: {is_info}
Exception type: {e_type}
Error Message: {error}
Line: {e_tb.tb_lineno}
                ''')


