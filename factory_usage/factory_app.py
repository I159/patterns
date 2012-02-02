import factory

class RatBug(factory.Donor):
    def get_model(self):
        return "VW Cafer'65"

    def get_style(self):
        return 'Rat Look'


class RestoWagenWorkShop(factory.WorkShop):
    objects = {'Bug': RatBug,}


WorkShop = RestoWagenWorkShop()
Bug = WorkShop.build_it('Bug')

print Bug
