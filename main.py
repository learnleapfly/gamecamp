import collections
import random

from kivy import app, properties
from kivy.uix import button, label
from kivy.uix.floatlayout import FloatLayout

MapCoords = collections.namedtuple('MapCoords', ['row', 'col'])


class StrategyGame(FloatLayout):
    main_map = properties.ObjectProperty(None)
    map_rows = properties.NumericProperty(0)
    map_cols = properties.NumericProperty(0)

    def __init__(self, **kwargs):
        super(StrategyGame, self).__init__(**kwargs)

        number_of_regions = self.map_rows * self.map_cols
        for region in xrange(0, number_of_regions):
            row = region / self.map_cols
            col = region % self.map_cols

            # Add hex cells to make up the map.
            hex_cell = self.pick_hex_cell(row=row, col=col)
            self.main_map.add_widget(hex_cell)

            # Add overlay conditionally.
            if (row % 6 == 2 and col % 2 == 0) or (row % 6 == 5 and col % 2 == 1):
                print('({}, {})'.format(row, col))
                self.add_widget(HexMapControlCell(hex_bind=hex_cell))

    @staticmethod
    def pick_hex_cell(row, col):
        row_mod = row % 6
        if col % 2 == 0:
            if row_mod == 0:
                return BU()
            elif row_mod in (1, 2):
                return L()
            elif row_mod == 3:
                return TD()
            elif row_mod in (4, 5):
                return R()
        else:
            if row_mod == 0:
                return TD()
            elif row_mod in (1, 2):
                return R()
            elif row_mod == 3:
                return BU()
            elif row_mod in (4, 5):
                return L()


class HexMapCell(label.Label):
    def __init__(self, row=0, col=0, **kwargs):
        super(HexMapCell, self).__init__(**kwargs)
        self.coords = MapCoords(row, col)


class BU(HexMapCell):
    pass


class TD(HexMapCell):
    pass


class L(HexMapCell):
    pass


class R(HexMapCell):
    pass


class HexMapControlCell(button.Button):
    def __init__(self, hex_bind=None, **kwargs):
        super(HexMapControlCell, self).__init__(**kwargs)
        self.hex_bind = hex_bind
        self.background_color = random.random(), random.random(), random.random(), 1
        self.bind(pos=self.reposition_control_cell, size=self.resize_control_cell)
        self.text = '({}, {})'.format(self.hex_bind.coords.row, self.hex_bind.coords.col)

    def reposition_control_cell(self, obj, value):
        self.pos = self.hex_bind.pos

    def resize_control_cell(self, obj, value):
        self.height = self.hex_bind.height * 2
        self.width = self.hex_bind.width * 2


class StrategyGameApp(app.App):
    def build(self):
        return StrategyGame()

if __name__ == '__main__':
    StrategyGameApp().run()
