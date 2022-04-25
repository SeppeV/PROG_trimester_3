from iniconfig import SectionWrapper


class Family:
    def __init__(self, sex, hair, relation, age, name):
        self.race = "human"
        self.sex = sex
        self.hair = hair
        self.relation = relation
        self.age = age
        self.name = name

    def Is_age(self):
        return self.age
    
    def Is_sex(self):
        return self.sex

    def birthday(self):
        self.age += 1
        return f"Happy birthday {self.name} is {self.age}"

    def related(self):
        return self.relation
    
    def paint_hair(self, color):
        self.hair = color
    
seppe = Family("Man", "buin", "ikzelf", 18, "Seppe")
seppe.birthday()
print(seppe.Is_age())

herman = Family("Man", "bruin", "papa", 49, "Herman")
herman.paint_hair("blauw")
print(herman.hair)

heidi = Family("Woman", "blond", "mama", 45, "Heidi")
print(heidi.Is_sex())
