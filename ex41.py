#random模块提供生成伪随机数的函数
import random
#urlib.request模块打开和浏览URL，其中urlopen()函数，打开url网站
from urllib.request import urlopen  
import sys

WORD_URL = "http://learncodethehardway.org/words.txt" #内容所在的url网站
WORDS =[] #创建空列表，存储URL中读取的单词

PHRASES = {
    "class %%%(%%%):":
    "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self,***)":
    "class %%% has-a __init__ that takes self and ***params.",
    "class %%%(object):\n\tdef ***(self,@@@)":
    "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
    "Set *** to a instance of class %%%.",
    "***.***(@@@)":
    "From *** get the *** function, call it with params self @@@.",
   " ***.*** = '***'":
   "From *** get the *** attribute and set it to '***'."
   } #创建字典，键为面向对象术语，值为对应的自然语言描述

#do they want to drill phrases first
#(他们想要首先训练短语吗)
if len(sys.argv) == 2 and sys.argv[1] == "english": 
#sys.argv的参数列表数量为2 且 参数列表的第二个参数为'english'时
#此脚本未定义argv列表的数量，所以数量可以外部随意输入
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
#(从网站加载单词)
#urlopen打开网址URL, 返回值始终为一个对象,并按行读取
for word in urlopen(WORD_URL).readlines():
    #删除word字符串开头或结尾的空格，并转化字符串格式，添加值WORDS列表
    WORDS.append(str(word.strip(), encoding = "utf-8"))

#定义函数convert（转换），参数为snippet（一条）：字符串，phrase（词汇）：字符串。
def convert(snippet, phrase):
    #定义列表变量class_names（类名），根据count()函数计算'%%%'数量，并以此为依据随机截取WORDS列表。
    #w.capitalize(),将字符串的开头小写字母更改为大写字母
    class_names = [w.capitalize() for w
    in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS,snippet.count("***")) #截取WORDS列表的随机数列表，数目为'***'的数量。
    param_names = [] #空列表，用于存储类中函数的参数名
    results = [] #空列表，用于存储替换字符串后，面向对象术语的解

    #for循环，循环次数为"@@@"的数量
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3) #1到3之间的整数，包括1和3。
        #根据param_count的数目截取WORDS的随机数列表，并转化为字符串用"，"连接,并添加到列表。
        param_names.append(", ".join(random.sample(WORDS, param_count))) 
    
    #for循环，变量sentence，序列snippet，phrase两个字符串，遍历的方式就是将两个字符串转化到变量中，得到一个字符串列表。
    for sentence in snippet, phrase:  
        result = sentence[:] #复制列表
        # print(result)#调试加的
        
        #fake class names(伪装类名)
        for word in class_names:  #for循环，遍历class_names的列表
            result = result.replace("%%%", word, 1)#替换字符串，旧字符"%%%",新字符=word变量的值，替换一个字符

        #fake other names(伪装其他名称)
        for word in other_names:
            result = result.replace("***", word, 1) #同上，只是新字符为other_names中的词
        
        #fake parameter lists(伪装参数列表)
        for word in param_names:
            result = result.replace("@@@", word, 1) #同上，新字符为param_names中的词
        
        results.append(result) #添加至results列表
   # print(results)
    return results #函数convert()返回值为results

# keep going until they hit CTRL-D 继续运行直到点击CTRL-D
#try....except: 用来检测 try 语句块中的错误，从而让 except 语句捕获异常信息并处理
try:
    while True:
        snippets = list(PHRASES.keys()) #定义变量snippets为列表，且内容为字典PHRASE的键。
        random.shuffle(snippets) #打乱snippets列表元素顺序

        for snippet in snippets:  #for循环，以PHRASE字典键的数量和内容循环
            phrase = PHRASES[snippet] #变量为PHRASES字典对应键的值
            question, answer = convert(snippet, phrase) #定义变量，对应值为convert()函数返回值results列表中的元素。
            if PHRASE_FIRST: #判断PHRASE_FIRST的值，若为True则进行，否则跳过
                question, answer = answer, question  #对调question和answer的值

            print(question) #打印question

            input("> ") #输入question对应的结果
            print(f"ANSWER: {answer}\n\n") #打印结果，并换两行运行，课余自己输入的结果做对比。
except EOFError:
    print("\nBye")