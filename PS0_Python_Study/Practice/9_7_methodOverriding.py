# 메소드 오버라이딩 : 부모 클래스에서 정의한 메소드 말고, 자식 클래스에서 정의한 메소드를 쓰고 싶을 떄,
# 메소드를 새롭게 정의해서 사용 가능

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

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음. 
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("9시")

# 지상 유닛은 move, 공중 유닛은 fly를 사용해야 함. 매번 확인하기 힘듦 -> 메소드 오버라이딩 사용
# 공중 유닛의 경우 move() 함수를 재정의 함