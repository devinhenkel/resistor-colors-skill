from mycroft import MycroftSkill, intent_file_handler


class ResistorColors(MycroftSkill):
    def __init__(self):
        self.register_entity_file('colorone')
        self.register_entity_file('colortwo')
        self.register_entity_file('colorthree')
        MycroftSkill.__init__(self)

    @intent_file_handler('colors.resistor.intent')
    def handle_colors_resistor(self, message):
        colorone = message.data.get('colorone')
        colortwo = message.data.get('colortwo')
        colorthree = message.data.get('colorthree')

        self.log.info([colorone, colortwo, colorthree])

        self.speak_dialog('colors.resistor', data={
            'colorone': colorone,
            'colortwo': colortwo,
            'colorthree': colorthree
        })


def create_skill():
    return ResistorColors()
