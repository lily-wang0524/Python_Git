class Song(object): #定义类Song

    def __init__(self, lyrics): #初始化，定义类的属性lyrics（抒情诗）
        self.lyrics = lyrics #实例的属性

    def sing_me_a_song(self): # 定义函数
        for line in self.lyrics:
            print(line)

#实例化对象happy_bday
happy_bday = Song(["Happy birthday to you",
                "I don't want to get sued",
                "So I'll stop right there"])

#实例化对象bulls_on_parade 
bulls_on_parade = Song(["They rally around the family",
                    "With pockets full of shells"])

happy_bday.sing_me_a_song() #调用类里面的函数sing_me_a_song()

bulls_on_parade.sing_me_a_song()#调用类里面的函数sing_me_a_song()

#附加练习1，实例化对象happy
happy = Song(["When we are children",
        "The God told us",
        "when you feel happy",
        "Although you have nothing",
        "You also feel the world is very huge"])
    
#调用类的函数sing_me_a_song
happy.sing_me_a_song()

#附加练习2，将歌词放入变量中。

#创建变量Sing_1为列表
Sing_1 = ["Happy birthday to you",
                "I don't want to get sued",
                "So I'll stop right there"]

#创建变量Sing_2为列表
Sing_2 = ["When we are children",
        "The God told us",
        "when you feel happy",
        "Although you have nothing",
        "You also feel the world is very huge"]

#创建对象F_Song,S_Song
F_Song = Song(Sing_1)
S_Song = Song(Sing_2)

#调用类中的函数
F_Song.sing_me_a_song()
S_Song.sing_me_a_song()


