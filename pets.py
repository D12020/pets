class Pet:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0
        self.is_alive = True

    def eat(self):
        if self.is_alive:
            print(self.name + " goes 'Nom Nom Nom...MMMMMMM'")
        else:
            print("He dead.")

    def sleep(self):
        print("zzzzzzzzzzzzzz...")

    def bite(self, other):
        print(self.name + " bit " + other.name + "!!")

    def poop(self):
        print("DOINK.")

    def play(self):
        print("Yip, Yip, YIPEE!!")

    def throw(self, other):
        print(self.name + " throws a ball to " + other.name + " and he caught it!!")
        

    def rotate_right(self):
        self.direction += 1

        if self.direction == 4:
            self.direction = 0

    def rotate_left(self):
        self.direction -= 1

        if self.direction == -1:
            self.direction = 3

    def move(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1

    def kill(self, other):
        print(self.name + " emilinates" + other.name + " with it's paw!")
        other.is_alive = False
  
    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + "]"
    
    
pet1 = Pet("Jersey")
pet2 = Pet("Captain")
pet3 = Pet("Bear")

