from nltk import tokenize
import re

# Returns list of sentences filtered by the word
def filter_by_word(text, word):
    res = []
    sentences = tokenize.sent_tokenize(text)
    for sentence in sentences:
        if re.search(word, sentence, re.IGNORECASE):
            res.append(sentence)
    return res

if __name__ == '__main__':
    text = "Just A Rather Very Intelligent System a.k.a JARVIS is created by Tony Stark natural-language and a sophisticated artificial intelligence user interface computer system, named after Edwin Jarvis, the butler who worked for Howard Stark. Though its primary duty is to automate Stark’s Malibu estate, the lifelike program fulfills many other needs for Stark, like being an information source for him, a diagnostic tool, a consultant and a voice of reason in Stark’s life. It was also responsible to provide security for Tony Stark's Mansion and Stark Tower. After creating the Mark II armor, Stark uploaded JARVIS into all of the Iron Man Armors, as well as allowing him to interact with the other Avengers, giving them valuable information during combat. JARVIS may be the one intellect Stark feels most comfortable opening up to. JARVIS can object to Stark’s commands if necessary. JARVIS speaks with a refined British accent, and is capable of back talk, sarcasm and condescension. During the Ultron Offensive, JARVIS was destroyed by Ultron, although his remaining programming codes unknowingly continued to thwart Ultron's plans of gaining access to nuclear missiles. His remains were found by Stark, who uploaded them into a synthetic body made of vibranium and, in conjunction with Ultron's personality and an Infinity Stone. JARVIS' duties were then taken over by FRIDAY."
    # word = "ultron offensive"
    word = input("Enter the string for the filter: ")
    res = filter_by_word(text, word)
    print(res)