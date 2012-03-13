class FormControl(object):
    def __init__(self):
        self.form = None

    def construct_form(self):
        self.form.new_construction()
        self.form.get_tag()
        self.form.get_type()
        self.form.get_attrs()

    def get_construction(self):
        return self.form.construction


class TagBuilder(object):
    def __init__(self, tag):
        self.construction = None
        self.tag = TagBuilder

    def new_construction(self):
        self.construction = Representation()


class Representation(object):
    def __init__(self):
        self.tag = None
        self.tag_type = None
        self.attrs = None

    def __repr__(self):
        return '<%s %s %s>' % (self.tag, self.tag_type, ' '.self.attrs)


class BuildIt(object):
    def __init__(self, tag, form):
        self.controller = FormControl()
        self.tag = tag
        self.form = form
        self.construction = None

    def build(self):
        self.controller.form = self.form(tag=self.tag)
        self.controller.construct_form()
        self.constraction = self.controller.get_construction()
        return self.construction

    def __call__(self):
        return self.build()


class Form(Representation):
    def get_donor(self):
        self.constraction.tag = self.TagBuilder

    def get_types(self):
        self.constraction.tag_type = 'text'

    def get_attrs(self):
        self.constraction.attrs = 'class'


form = BuildIt(tag='input', form=Form)

print form()
