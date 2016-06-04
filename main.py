import collections

from kivy.app import App
from kivy import properties
from kivy import graphics
from kivy.uix import label
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
            self.main_map.add_widget(HexMapCell(row=row, col=col))


class HexMapCell(label.Label):
    def __init__(self, row=0, col=0, **kwargs):
        self.region_in_map = MapCoords(row, col)
        super(HexMapCell, self).__init__(**kwargs)
        self.draw_hex_edge()

    def draw_hex_edge(self):
        edge = ''
        if self.region_in_map.col % 2 == 0:
            row_mod = self.region_in_map.row % 6
            if row_mod == 0:
                edge = 'BU'
                with self.canvas:
                    graphics.Color(1, 1, 1, 1)
                    graphics.Line(points=[self.x, self.y, self.width + self.x, self.height + self.y])
            elif row_mod in (1, 2):
                edge = 'L '
            elif row_mod == 3:
                edge = 'TD'
            elif row_mod in (4, 5):
                edge = ' R'
        else:
            row_mod = self.region_in_map.row % 6
            if row_mod == 0:
                edge = 'TD'
            elif row_mod in (1, 2):
                edge = ' R'
            elif row_mod == 3:
                edge = 'BU'
            elif row_mod in (4, 5):
                edge = 'L '

        self.text = edge

class StrategyGameApp(App):
    def build(self):
        return StrategyGame()

if __name__ == '__main__':
    StrategyGameApp().run()
