#场景-类，enter-函数
class Scene(object):
    def enter(self):
        pass

#引擎-类，play-函数
class Engine(object):
    def __init__(self, scene_map):
        pass
    def play(self):
        pass

#Scene的子类
class Death(Scene):
    def enter(self):
        pass

class CentralCorridor(Scene):
    def enter(self):
        pass

class LaserWeaponArmory(Scene):
    def enter(self):
        pass

class TheBridge(Scene):
    def enter(self):
        pass

class EscapePod(Scene):
    def enter(self):
        pass

# 地图-类。next_scene-函数，opening_scene-函数
class Map(object):
    def __init__(self, start_scene):
        pass
    def next_scene(self, Scene_name):
        pass
    def opening_scene(self):
        pass

a_map = Map('central_corridor') #地图初始场景
a_game = Engine(a_map) #游戏引擎
a_game.play() #游戏启动