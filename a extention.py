import random
import sqlite3
npcs = []
npchp = []
npcwealth = []


class NPC:
    stats = { 'str' : 0, 'int' : 0, 'pie' : 0, 'agi' : 0, 'stm' : 0, 'cha' : 0 }
    level = 0
    hp = 0
    gold = 0
    silver = 0
    copper = 0
    wealth = 0
    randlist = [1,1,1,1,2,2,2,3,3,4]

    def __init__(self):
        self.create()
        for i in range(100):
            self.insert()
            self.printall()

    def randItem(self,options):
        x = list(options.keys())
        itemName = random.choice(x)
        number = options[itemName]

        return {itemName:number}
    
    def insert(self):
        connection = sqlite3.connect('dbase.db')
        cursor = connection.cursor()

        for i in self.stats:
            rand1 = random.randint(1,6)
            rand2= random.randint(1,6)
            rand3 = random.randint(1,6)
            self.stats[i] = rand1+rand2+rand3

        self.level = self.randlist[random.randint(0,9)]

        self.hp = (random.randint(1,10)*self.level)
        
        if random.randint(1,100) < 30:
            self.gold = random.randint(0,6)

        if random.randint(1,100) < 50:
            self.silver = random.randint(3,12)

        if self.gold == 0:
            if random.randint(1,100) < 75:
                self.copper = random.randint(4,20)

        self.wealth = ( (self.gold*100)+(self.silver*10)+self.copper)

        self.headwear = {"leather cap":1,"iron cap":2,"helmet":3}
        self.armor = {"studded leather":9,"chainmail":21,"scalemail":15,"platemail":29}
        self.shield = {"buckler":1,"embossed leather shield":2,"kite shield":4}

        self.equipment = {}
        self.equipment[0] = self.randItem(self.headwear)
        self.equipment[1] = self.randItem(self.armor)
        self.equipment[2] = self.randItem(self.shield)

        query = f"insert into npcs (hp,level,gold,silver,copper,wealth,armor,headware,chestplate,shield) values ('{self.hp}','{self.level}','{self.gold}','{self.silver}','{self.copper}','{self.wealth}','{(list(self.equipment[0].values()))[0]+(list(self.equipment[1].values()))[0]+(list(self.equipment[2].values()))[0]}','{(list(self.equipment[0].keys()))[0]}','{(list(self.equipment[1].keys()))[0]}','{(list(self.equipment[2].keys()))[0]}');"
        cursor.execute(query)
        connection.commit()

    def create(self):
        connection = sqlite3.connect('dbase.db')
        cursor = connection.cursor()
        cursor.execute('drop table npcs')
        
        query = """
        create table if not exists npcs (
            id integer primary key autoincrement,
            hp smallint,
            level smallint,
            gold smallint,
            silver smallint,
            copper smallint,
            wealth smallint,
            armor tinytext,
            headware tinytext,
            chestplate tinytext,
            shield tinytext);
        """
        cursor.execute(query)
        cursor.execute('PRAGMA table_info(npcs);')

    def printall(self):
        connection = sqlite3.connect('dbase.db')
        cursor = connection.cursor()
        query = "select * from npcs"
        cursor.execute(query)
        result = cursor.fetchall()
            
        for i in result:
            print(i)
NPC()