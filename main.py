from detentiondata import DetentionForm
from person_data_creator import PersonDataCreator


class AWP:

    def __init__(self):
        self.person_data = PersonDataCreator().person_data

    # fill detention_form with person_data
        self.detention_form = DetentionForm(self.person_data[0], self.person_data[1], self.person_data[2],
                                            self.person_data[3], self.person_data[4], self.person_data[5],
                                            self.person_data[6], self.person_data[7])

        something = self.detention_form.collect_detention_data()
        print(something)


awp = AWP()