class Prisoner:
    def __init__(self, name, id_number, also_known_as, age, birthdate,
                 home_state, charge, background):
        """ (str, str, str, str) -> Nonetype """
        self.name = name
        self.id_number = id_number
        self.also_known_as = also_known_as
        self.age = age
        self.birthdate = birthdate
        self.home_state = home_state
        self.charge = charge
        self.background = background

    def __str__(self):
        return 'Name: {0} | ID number: {1} | A.K.A: {2} | Age: {3} | Birthdate: {4} | Home State: {5} | Charge: {6}'.format(
            self.name, self.id_number, self.also_known_as, self.age,
            self.birthdate, self.home_state, self.charge)


class Prison:
    def __init__(self, prisoners):
        self.prisoners = prisoners

    def find_by_id(self, id_number):
        for p in self.prisoners:
            if p.id_number == id_number:
                return p

    def background_info(self, background):
        for b in self.prisoners:
            if b.background == background:
                return 'Psychiatrist Diagnosis: {0}'.format(b.background)