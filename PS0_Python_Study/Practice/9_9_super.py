# 일반 유닛 # 부모 클래스
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
              .format(self.name, location, self.speed))

# 공격 유닛 # 자식 클래스
class AttackUnit(Unit):  # Unit class 를 상속받아서 AttackUnit 를 만든다면, name과 hp 상속 가능
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)    
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
              .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다. ".format(self.name))

# 날 수 있는 기능을 가진 클라스
class Flyable: 
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
              .format(name, location, self.flying_speed))
        
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0 
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, speed)
        super().__init__(name, hp, 0) # 슈퍼를 통해 초기화 할 때는 'self' 없이 써야 한다
        self.location = location

# class Unit:
#     def __init__(self):
#         print("Unit 생성자")

# class Flyable:
#     def __inti__(self):
#         print("Flyable 생성자")

# class FlyableUnit(Flyable, Unit):
#     def __init__(self):
#         # super().__init__()
#         Unit.__init__(self)
#         Flyable.__init__(self)

# # 드랍쉽
# drpoship = FlyableUnit()

# # 두 개 이상의 부모에게서 상속을 받을 때, super를 사용하면,
# # 맨 처음에 상속받는 클래스에 대해서만 __init__ 함수가 호출이 된다.
# # 다중 상속의 경우 2번 상속 받는게 좋음