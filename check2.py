# import random
# from urllib.request import urlopen
# import sys
#
# print("WORD_URL")
# WORD_URL = "http://learncodethehardway.org/words.txt"
#
#
# WORDS = []
#
# PHRASES = {"class%%%(%%%):":"Make a class named %%% that is-a %%%.",
#             "class%%%(object):\n\tdef__init__(self,***):":"class %%% has-a __init__ that takes self and *** params",
#             "class %%%(object)\n\tdef***(self,@@@):":"class %%% has-a function *** that takes self and @@@ params",
#             "*** = %%%()":"set *** to an instance of class %%%.",
#             "***.***(@@@)":"from *** get the *** function, call it with params self, @@@",
#             "***.***='***'":"from *** get the *** attribute and set it to '***'."}
#
# if len(sys.argv) == 2 and sys.argv[1] == "english":
#     PHRASE_FIRST = True
# else:
#     PHRASE_FIRST = False
#
# print("lin16.22")
# x=urlopen(WORD_URL).readlines()
#
# print(x)
# print("lin17.26")
# # # print(WORDS.append(str(x.strip(),encoding="utf-8")))
# # for word in urlopen(WORD_URL).readlines():
# #     print(WORDS.append(str(word.strip(),encoding="utf-8")))
#
# # WORD_URL=["cam","tank","sit","but","apple"]
# #
# # for word in WORD_URL:
# #     print(WORDS.append(str(word.strip(),encoding="utf-8")))
# # if len(sys.argv) == 2 and sys.argv[1] == "english":
# #     PHRASE_FIRST = True
# # else:
# #     PHRASE_FIRST = False
#
# #load up the words from the website
# for word in urlopen(WORD_URL).readlines():
#     WORDS.append(str(word.strip(),encoding="utf-8"))
# print("lin43")
# print(WORDS[0:2])
# print("lin45")
# print(len(WORDS))
# print("lin47")
# print(type(WORDS))
# print("lin50")
# print(WORDS)
# print("lint51")
# # def pip(snippet,phrase):
# #     pip2=[w.capitalize() for w in
# #                         random.sample(WORDS,snippet.count("%%%"))]
# #     print(pip2)
# # print(pip(snippet,phrase))
# banana="class%%%"
# print("lin58")
# print(banana.count("%%%"))
# print("lin60")
#
# print('This is sample to count i'.count('i',0,7))
# print("lin63")
# print('This is sample to count i'.count('i'))
# print("lin65")
# print("class%%%".count("%%%"))
# print("lin67")
# print(random.randint(1,3))
# print("lin69")
# print(random.randint(1,2))
# print("lin71")
# for i in range(0,6):
#     print (i,end="; ")
# print("lin74")
# for i in range(0,1):
#     print (i,end="; \n")
# print("lin77")
# for i in range(0,0):
#     p_count=random.randint(1,3)
#     print(p_count)
# snippets = list(PHRASES.keys())
# for snippet in snippets:
#     phrase=PHRASES[snippet]
# print("lin83")
# for sentence in snippet,phrase:
#     result=sentence[:]
#     print(result)
#     # type(result)
#     # len(result)
#     print(result[2])
# print("lin91")
# print(type(result))
# print(result)
# # apple=["on","two","thr","four","fiv","six"]
# # banana=["class%%%(%%%)",
# #             "class%%%(object):\n\tdef__init__(self,***)",
# #             "class %%%(object)\n\tdef***(self,@@@)",
# #             "*** = %%%()",
# #             "***.***(@@@)"]
# # print("apple")
# # print(random.sample(apple,banana.count("%%%"))
#
# def convert(snippet,phrase):
#     class_names=[w.capitalize() for w in random.sample(WORDS,snippet.count("%%%"))]
#     print("line40.105********************************************class name")
#     print(class_names)
#     other_names=random.sample(WORDS,snippet.count("***"))
#     print("lin92.108******************************************other name")
#     print(other_names)
#     print("lin94.110")
#     results=[]
#     param_names=[]
#     for i in range(0,snippet.count("@@@")):
#         param_count=random.randint(1,3)
#         print(param_count)
#         print("lin100.116****************************************params name")
#         param_names.append(', '.join(random.sample(WORDS,param_count)))
#         print(param_names)
#         print("lin103.119")
#     for sentence in snippet,phrase:
#         result=sentence[:]
#         print("lin123.123")
#         print(result)
#         print("lin107.123")
#         #fake class name
#         for word in class_names:
#             result.replace("%%%",word,1)
#             print("lin129")
#             print(result.replace("%%%",word,1))
#             if len(result.replace("%%%",word,1))!=0 and len(other_names)!=0:
#                 x=result.replace("%%%",word,1)
#                 print("lin131")
#                 for word in other_names:
#                     x=x.replace("***",word,1)
#                     print("lin132")
#                     print(x)
#                     if len(x)!=0:
#                         for word in param_names:
#                             x=x.replace("@@@",word,1)
#                             print("lin139")
#                             print(x)
#                             print("lin141")
#                             results.append(x)
#                             print(results.append(x))
#             else:
#                     # for word in other_names:
#                     #     result.replace("***",word,1)
#                     #     if len(result.replace("***",word,1))!=0:
#                     #         x=result.replace("%%%",word,1)
#                     #         print("lin149")
#                     #         print(x)
#                     if len(x)!=0:
#                         for word in param_names:
#                             x=x.replace("@@@",word,1)
#                             print("154")
#                             print(x)
#                             print("lin141")
#                             results.append(x)
#                             print(results.append(x))
#                         else:
#                             for word in param_names:
#                                 result.replace("@@@",word,1)
#                                 print("lin162")
#                                 print(replace("@@@",word,1))
#                                 results.append(result)
#                                 print("lin165.165")
#                                 print(results.append(result))
#
#
# #keep going untill they hit CTRL-D
# try:
#     while True:
#         snippets = list(PHRASES.keys())
#         print("lint135.146")
#         print(snippets)
#         random.shuffle(snippets)
#         for snippet in snippets:
#             phrase=PHRASES[snippet]
#             print("lin140.151")
#             print(phrase)
#             question,answer=convert(snippet,phrase)
#             if PHRASE_FIRST:
#                 question,answer=answer,question
#
#             print(question)
#
#             input("< ")
#             print(f"ANSWER: {answer}\n\n")
# except EOFError:
#     print("\nBye")


###Original code
print("********************************************************")


import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"

WORDS = []
print("load dict of phrases")
PHRASES = {"class%%%(%%%):":"Make a class named %%% that is-a %%%.",
            "class%%%(object):\n\tdef__init__(self,***):":"class %%% has-a __init__ that takes self and *** params",
            "class %%%(object)\n\tdef***(self,@@@):":"class %%% has-a function *** that takes self and @@@ params",
            "*** = %%%()":"set *** to an instance of class %%%.",
            "***.***(@@@)":"from *** get the *** function, call it with params self, @@@",
            "***.***='***'":"from *** get the *** attribute and set it to '***'."}

#do they want to drill phrases first
print("do they want to drill phrases first")
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
    print("""Executed PHRASE_FIRST=True""")
else:
    PHRASE_FIRST = False
    print("""Executed PHRASE_FIRST=False""")

#load up the words from the website
print("load up the words from the website")
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(),encoding="utf-8"))
print(WORDS)

print("fn convert")
def convert(snippet,phrase):
    print("calling function convert")
    class_names=[w.capitalize() for w in random.sample(WORDS,snippet.count("%%%"))]
    print(f"class_names:{class_names}")
    other_names=random.sample(WORDS,snippet.count("***"))
    print(f"other_names:{other_names}")
    results=[]
    print(f"line236:results:{results}")
    param_names=[]
    print(f"line238:param_names:{param_names}")
    for i in range(0,snippet.count("@@@")):
        print("calling 'for' param_names")
        param_count=random.randint(1,3)
        print(f"param_count:{param_count}")
        param_names.append(', '.join(random.sample(WORDS,param_count)))
        print(f"param_names:{param_names}")
    for sentence in snippet,phrase:
        print("calling 'for' sentence in (snippet,phrase)")
        result=sentence[:]
        print(f"line248.result for snippet/phrase:\n\t{result}")
        #fake class name
        for word in class_names:
            print("calling 'for' class_names replace")
            result.replace("%%%",word,1)
            print(f"""class_names replaced:\n\t{result.replace("%%%",word,1)}""")
        #fake other names
        for word in other_names:
            print("calling 'for' other_names replace")
            result.replace("***",word,1)
            print(f"""other_names replaced:\n\t{result.replace("***",word,1)}""")
        #fake params list
        for word in param_names:
            print("calling 'for' param_names replace")
            result.replace("@@@",word,1)
            print(f"""param_names replaced:\n\t{result.replace("@@@",word,1)}""")
        print("append result to results")
        results.append(result)
        # print(f"check if it returns none:{results.append(result)}")
        print(f"results.append(result):\n\t{results}")
    print("returning final results")
    return results
    print(f"printing final results:\n\t{results}")
#keep going untill they hit CTRL-D
try:
    print("Start-while_loop")
    while True:
        print("while_loop-when True")
        snippets = list(PHRASES.keys())
        print(f"QUESTION: snippets:{snippets}")
        random.shuffle(snippets)
        print(random.shuffle(snippets))
        print("calling 'for' # QUESTION: answer")
        for snippet in snippets:
            print("calling 'for' # QUESTION: answer")
            phrase=PHRASES[snippet]
            print(f"ANSWER: phrase:{phrase}")
            print("calling convert function lin284")
            question,answer=convert(snippet,phrase)
            print("end convert function lin286")
            print("if phrase first")
            if PHRASE_FIRST:
                question,answer=answer,question
            print("QUESTION: ")
            print(question)

            input("< ")
            print("ANSWER:***************************************************** ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("EOFError lin297")
    print("\nBye")
