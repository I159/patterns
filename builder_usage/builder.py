
#Director
class Engineer(object):
    """
    Abstract class 
    """
    def __init__(self):
        self.project = None

    def construct_car(self):
        self.project.new_building()
        self.project.get_donor()
        self.project.build_engene()
        self.project.put_wheels()

    def get_building(self):
        return self.project.building


#Abstract Builder
class StyleStandard(object):
    def __init__(self, donor):
        self.building = None
        self.donor = donor

    def new_building(self):
        self.building = Building()


#Product
class Building(object):
    def __init__(self):
        self.donor = None
        self.engene = None
        self.wheels = None

    def __repr__(self):
        return '%s %s on %s' % (self.engene, self.donor, self.wheels)


#Client
class BuildIt(object):
    """
    Required parameters are `donor` as string car name
    and `style` as StyleStandard exended class instance.
    """
    def __init__(self, donor, style):
        self.engeneer = Engineer()
        self.donor = donor
        self.style = style
        self.building = None

    def build(self):
        self.engeneer.project = self.style(donor=self.donor)
        self.engeneer.construct_car()
        self.building = self.engeneer.get_building()
        return self.building

    def __call__(self):
        return self.build()
