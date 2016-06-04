import collections

from kivy.app import App
from kivy import properties
from kivy import graphics
from kivy.uix import label
from kivy.uix.floatlayout import FloatLayout
import math

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
            self.main_map.add_widget(self.pick_hex_cell(row=row, col=col))


    def pick_hex_cell(self, row, col):
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
        self.region_in_map = MapCoords(row, col)
        super(HexMapCell, self).__init__(**kwargs)

class BU(HexMapCell):
    pass
class TD(HexMapCell):
    pass
class L(HexMapCell):
    pass
class R(HexMapCell):
    pass


class StrategyGameApp(App):
    def build(self):
        return StrategyGame()

if __name__ == '__main__':
    StrategyGameApp().run()
