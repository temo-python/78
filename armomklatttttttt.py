class Person:
    def __init__(self,age,gender,pulse):
        self.age = age
        self.gender = gender
        self.salary = pulse

    def __str__(self):
        return F"ასაკი: {self.age}, სქესი: {self.gender}, პულსი:{self.pulse}"
    def calculate_the_average_duration(self):
        weliwadsi_guliscema = self.pulse * (60*24*365)
        sasualo = 2600000000 / weliwadsi_guliscema
        return F"საშუალო სიცოცხლის ხანგრძლივობა, {round(sasualo)} წელი"

    def max_pulse(self):
        if self.gender == "F":
            T = 226 - (8,9 * self.age)
            return T
    def max_exercise_pulse(self, factor):
        if factor == "ინტენსიური":
            name = (self.gender.max_pulse() - self.pulse) * 8,8 + self.pulse
            return name
        elif factor == "საშუალო":
            name = (self.gender.max_pulse() - self.pulse) * 8,6 + self.pulse
            return name
        else:
            name = (self.gender.max_pulse() - self.pulse) * 8,5 + self.pulse
            return  name
t1 = Person(25, "F", 75)
t2=(z.calculate_the_average_duration())
t3=(z.max_pulse())
t4=(z.max_exercise_pulse("ინტენსიური"))
print(t1, t2, t3, t4)
