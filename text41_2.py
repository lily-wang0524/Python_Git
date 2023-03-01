from urllib.request import urlopen  
import sys

WORD_URL = "http://learncodethehardway.org/words.txt" #内容所在的url网站
WORDS =[] #创建空列表

#urlopen打开网址URL, 返回值始终为一个对象,并按行读取
for word in urlopen(WORD_URL).readlines():
    #删除word字符串开头或结尾的空格，并转化字符串格式，添加值WORDS列表
    WORDS.append(str(word.strip(), encoding = "utf-8"))

print(WORDS)