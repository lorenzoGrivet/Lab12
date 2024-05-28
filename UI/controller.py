import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        # anni= map(lambda x: ft.dropdown.Option(x),self._model.anni)
        # self._view.ddyear.options= anni
        # self._view.update_page()
        #
        # nazioni= map(lambda x: ft.dropdown.Option(x),self._model.nazioni)
        # self._view.ddcountry.options=nazioni

        for a in self._model.anni:
            self._view.ddyear.options.append(ft.dropdown.Option(a))
        for a in self._model.nazioni:
            self._view.ddcountry.options.append(ft.dropdown.Option(a))

        self._view.update_page()
        pass


    def handle_graph(self, e):
        self._model.creaGrafo(self._view.ddyear.value,self._view.ddcountry.value)

        pass



    def handle_volume(self, e):
        pass


    def handle_path(self, e):
        pass
