###exercise lpthw 41 modified****


print("********************************************************")


import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"

WORDS = []
# print("load dict of phrases")
PHRASES = {"class%%%(%%%):":"Make a class named %%% that is-a %%%.",
            "class%%%(object):\n\tdef__init__(self,***):":"class %%% has-a __init__ that takes self and *** params",
            "class %%%(object)\n\tdef***(self,@@@):":"class %%% has-a function *** that takes self and @@@ params",
            "*** = %%%()":"set *** to an instance of class %%%.",
            "***.***(@@@)":"from *** get the *** function, call it with params self, @@@",
            "***.***='***'":"from *** get the *** attribute and set it to '***'."}

#do they want to drill phrases first
# print("do they want to drill phrases first")
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
    # print("""Executed PHRASE_FIRST=True""")
else:
    PHRASE_FIRST = False
    # print("""Executed PHRASE_FIRST=False""")

#load up the words from the website
# print("load up the words from the website")
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(),encoding="utf-8"))
# print(WORDS)

# print("fn convert")
def convert(snippet,phrase):
    # print("calling function convert")
    class_names=[w.capitalize() for w in random.sample(WORDS,snippet.count("%%%"))]
    class_names="Sara"
    # print(f"class_names:{class_names}")
    other_names=random.sample(WORDS,snippet.count("***"))
    other_names="Bow"
    # print(f"other_names:{other_names}")
    results=[]
    # print(f"line236:results:{results}")
    param_names=[]
    # print(f"line238:param_names:{param_names}")
    param_names="Puhal"
    for i in range(0,snippet.count("@@@")):
        # print("calling 'for' param_names")
        param_count=random.randint(1,3)
        # print(f"param_count:{param_count}")
        # param_names.append(', '.join(random.sample(WORDS,param_count)))
        param_names="Puhal"
        # print(f"param_names:{param_names}")
    for sentence in snippet,phrase:
        # print("calling 'for' sentence in (snippet,phrase)")
        result=sentence[:]
        # print(f"line248.result for snippet/phrase:\n\t{result}")
        #fake class name
        class replace_word():
            # print("to replace names")

            def __init__(self, class_names,other_names,param_names):
                self.class_names = result.replace("%%%",class_names,1)
                # print("self.class_names")
                self.other_names = self.class_names.replace("***",other_names,1)
                # print("self.other_names")
                self.param_names = self.other_names.replace("@@@",param_names,1)
                # print("self.param_names")

        # print("replace_word2 is an instance of class replace_word")
        replace_word2=replace_word(class_names,other_names,param_names)
        # print("call dot class_names")
        result=replace_word2.class_names
        # print(f"rclass_names:{result}")
        # print("call dot other_names")
        result=replace_word2.other_names
        # print(f"rother_names:{result}")
        # print("call dot param_names")
        result=replace_word2.param_names

        # print(f"rparam_names:{result}")
        # print("replace_word2")
        # print(results.append(result))
        results.append(result)
        # print(f"results: {results}")
    return results

#keep going untill they hit CTRL-C
try:
    # print("Start-while_loop")
    while True:
        # print("while_loop-when True")
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)
        # print(f"QUESTION: snippets:{snippets}")
        # print(random.shuffle(snippets))
        # print("calling 'for' # QUESTION: answer")
        for snippet in snippets:
            # print("calling 'for' # QUESTION: answer")
            phrase=PHRASES[snippet]
            # print(f"ANSWER: phrase:{phrase}")
            question,answer=convert(snippet,phrase)
            # print("calling convert function lin284")
            # print("end convert function lin286")
            # print("if phrase first")
            if PHRASE_FIRST:
                question,answer=answer,question
            # print("QUESTION: ")
            print(question)

            input("< ")
            # print("ANSWER:***************************************************** ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("EOFError lin297")
    print("\nBye")
