from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

class Example(MDApp):
    def build(self):

        self.data_tables = MDDataTable(
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            size_hint = (0.6, 0.6),
            sort = True,
            use_pagination = True,
            rows_num = 10,
            column_data = [
                ("No.", dp(30)),
                ("Column 1", dp(30)),
                ("Column 2", dp(30)),
                ("Column 3", dp(30)),
                ("Column 4", dp(30)),
                ("Column 5", dp(30)),
            ],
            row_data = [
                (f"{i + 1}", "1", "2", "3", "4", "5") for i in range(50)
            ],
        )

    def on_start(self):
        self.data_tables.open()

Example().run()