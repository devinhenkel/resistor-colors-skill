from mycroft import MycroftSkill, intent_file_handler


class ResistorColors(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('colors.resistor.intent')
    def handle_colors_resistor(self, message):
        self.speak_dialog('colors.resistor')


def create_skill():
    return ResistorColors()

