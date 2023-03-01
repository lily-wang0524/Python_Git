from sys import exit  #退出程序。退出python程序首选方法
from random import randint #随机数取整
from textwrap import dedent #删除字符串中的前导空格

#创建第一个父类，具有所有场景的公共属性
#场景-类，enter-函数
class Scene(object):
    
    def enter(self):
        print("This scene is not yet configured.") #这个场景还没有被设置
        print("Subclass it and implemet enter().") #设置其子类并且执行enter()函数
        exit(1) #出现程序异常退出程序

#引擎-类，play-函数
class Engine(object):
    def __init__(self, scene_map): #scene_map是Map类的对象
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene() #目前所在场景，通过Map对象调用Map类中的函数opening_scene
        last_scene = self.scene_map.next_scene('finished') #最后一个场景,同上，通过Map对象调用Map类中函数next_scene

        while current_scene != last_scene: #while循环，当前场景不是最后一个场景的情况下
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #be sure to print out the last scene
        current_scene.enter()

        
#Scene的子类
class Death(Scene):
    
    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ] #字符串列表，各种不同情况

    def enter(self):
        print(Death.quips[randint(0,len(self.quips)-1)]) #打印，quips列表中的值，该索引为0到列表长度-1中的随机数值。
        exit(1)#程序异常退出

#中央走廊场景
class CentralCorridor(Scene):
    
    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and
            destroyed your entire crew. You are the last surviving
            member and your last mission is to get the neutron destruct
            bomb from the Weapons Armory, put it in the bridge,and
            blow the ship up after getting into an escape pod.
            
            You're running down the central corridor to the Weapons
            Armory when a Gothon jumps out, red scaly skin, drak grimy
            teeth, and evil clown costume flowing around his hate
            filled body, He's blocking the door to the Armory and 
            about to pull a weapon to blast you.
            """)) #进入游戏的前景介绍
        
        action = input("> ") #输入行为

        if action == "shoot!": #如果行动是shoot
            print(dedent("""
                Quick on the draw you yank out your blaster and fire
                it at the Gothon. His clown costume is flowing and
                moving around his body, which throws off your aim.
                Your laser hits his costume but misses him entirely.
                This completely ruins his brand new costume his mother
                bought him, which makes him fly into an insane rage
                and blast you repeatedly in the face until you are 
                dead. Then he eats you.
                """))
            return 'death' #返回值

        elif action == "dodge!": #行动是dodge时
            print(dedent("""
            Like a world class boxer you dodge, weave,slip and 
            slide right as the Gothon's blaster cranks a laser
            past your head. In the middle of your artful dodge
            your foot slips and you bang your head on the metal
            wall and pass out. You wake up shortly after only to
            die as the Gothon stomps on your head and eats you. 
            """)) 
            return 'death' #返回值
        
        elif action == "tell a joke": #如果行动是tell a joke
            print(dedent("""
            Lucky for you they made you learn Gothon insults in
            the academy. You tell the one Gothon joke you know:
            Lbhe Zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
            fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
            not to laugh, then busts out laughing and can't move.
            While he's laughing you run up and shoot him square in
            Weapon Armory door.
            """))
            return 'laser_weapon_armory' #返回值
        
        else:
            print("DOES NOT COMPUTE")
            return 'central_corridor' #返回值

#激光武器库场景
class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
        You do a dive roll into the Weapon Armory, crouch and scan
        the room for more Gothons that might be hidding. It's dead
        quiet, too quiet. You stand up and run to the far side of
        the room and find the neutron bomb in its container.
        There's a keypad lock on the box and you need the code to 
        get the bomb out. If you get the wrong 10 times then 
        the lock closes forever and you can't get the bomb. The
        code is 3 digits.
        """))  #场景提示
    
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}" #变量字符串格式化，密码为三个1-9之间的随机整数，包括1和9
        guess = input("[keypad]> ") #猜测密码
        # guesses = 0 #猜测次数初始值
        guesses = 1 #修改初始值

        while guess != code and guesses < 10: #while循环，无法确定循环次数时使用while而不是for循环。猜想密码与密码不一致且猜测次数小于10.
            print("BZZZZEDDDD!")
            guesses += 1 #猜测次数不断累加
            guess = input("[keypad]> ") #重新猜测密码

        if guess == code: #如果密码正确
            print(dedent("""
            The container clicks open and the seal breaks, letting
            gas out. You grab the neutron bomb and run as fast as
            you can to the bridge where you must place it in the 
            right spot.
            """)) #打印结果
            return 'the_bridge' #返回值
        else:
            print(dedent("""
            The lock buzzes one last time and then you hear a 
            sickening melting sound as the mechanism is fused
            together. You decide to sit there, and finally the 
            Gothons blow up the ship from their ship and you die.
            """)) 
            return 'death'
    
#桥场景
class TheBridge(Scene):
    def enter(self):
        print(dedent("""
        You burst onto the Bridge with the netron destruct bomb
        under your arm and surprise 5 Gothons who are trying to
        take control of the ship. Each of them has an even uglier
        clown costume than the last. They haven't pulled their
        weapons out yet, as they see the active bomb under your
        arm and don't want to set it off.
        """)) #进入时场景

        action = input("> ") #输入行动

        if action == "throw the bomb": #如果行动是throw the bomb时
            print(dedent("""
            In a panic you throw the bomb at the group of Gothons
            and make a leap for the door. Right as you drop it a 
            Gothons shoots you right in the back killing you. As
            you die you see another Gothon frantically try to
            disarm the bomb. You die knowing they will probably
            blow up when it goes off.
            """))
            return 'death' #返回值

        elif action == "slowly place the bomb": #如果行动为slowly place the bomb时
            print(dedent("""
            You point your blaster at the bomb under your arm and
            the Gothons put their hands up and start to sweat.
            You inch backward to the door, open it, and then
            carefully place the bomb on the floor, pointing your
            blaster at it. You then jump back through the door,
            punch the close button and blast the lock so the
            Gothons can't get out. Now that the bomb is placed 
            you run to the escape pod to get off this tin can.
            """)) #发生的事情
            return 'escape_pod' #返回值
        
        else:
            print("DOES NOT COMPUTE!")
            return 'the_bridge' #返回值

#逃生舱场景
class EscapePod(Scene):
    def enter(self):
        print(dedent("""
        You rush through the ship desperately trying to make it
        the escape pod before the whole ship explodes. It seems
        like hardly any Gothons are on the ship, so your run is
        clear of interference. You get to the chamber with the
        escape pods, and now need to pick one to take. Some of
        them could be damaged but you don't have time to look.
        There's 5 pods, which one do you take?
        """)) #进入场景
        
        good_pod = randint(1,5) #1-5之间的随机整数
        guess = input("[pod]> ") #输入猜想

        if int(guess) != good_pod: #猜想与好用的逃生舱不一致时
            print(dedent(f"""
            You jump into pod {guess} and hit the eject button.
            The pod escapes out into the void of space, then
            implodes as the hull ruptures, crushing your body into
            jam jelly.
            """))  #字符串格式化guess变量
            return 'death' #返回值
        else:
            print(dedent(f"""
            You jump into pod {guess} and hit the eject button.
            The pod easily slides out into space heading to the
            planet below. As it flies to the planet, you look
            back and see your ship implode then explode like a 
            bright star, taking out the Gothon ship at the same
            time. You won!
            """)) #字符串格式化guess变量

            return 'finished' #返回值

#结束场景
class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished' #返回值



# 地图-类。next_scene-函数，opening_scene-函数
class Map(object):

    scenes = {
        'central_corridor':CentralCorridor(),
        'laser_weapon_armory':LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod':EscapePod(),
        'death':Death(),
        'finished':Finished()
    } #字典，字符串键对应-子类值
    #初始化函数
    def __init__(self, start_scene):
        self.start_scene =start_scene #定义start_scene

    def next_scene(self, scene_name): #定义next_scene函数，作用：通过获取的场景字符串,得到对应的的字典的值，即子类场景
        val = Map.scenes.get(scene_name) #get()获取字典的值，若值不存在不报错
        return val #返回值

    def opening_scene(self): #定义函数 调用了next_scene()函数
        return self.next_scene(self.start_scene) #返回值，返回next_scene函数，参数scene_name = start_scene.

a_map = Map('central_corridor') #地图初始场景
a_game = Engine(a_map) #游戏引擎
a_game.play() #游戏启动