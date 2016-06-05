import collections
import random
import math
from kivy import app, properties
from kivy.uix import button, label
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Ellipse, Line
from kivy.logger import Logger

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
            if (row % 6 == 1 and col % 2 == 1) or (row % 6 == 4 and col % 2 == 0):
                print('({}, {})'.format(row, col))
                #radius = math.sqrt(hex_cell.width**2 + hex_cell.height**2)
                radius = 2*hex_cell.height
                with hex_cell.canvas.after:
                    Color(1,0,1,1)
                    hex_cell.ell = Line(circle=(hex_cell.x, hex_cell.y,radius, 0, 360, 6), width=2)
                hex_cell.bind(pos=hex_cell.update_pos, size=hex_cell.update_pos)


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

    def update_pos(self, instance, value):
        Logger.info("StratGame: {}".format(instance))
        #radius = math.sqrt(self.width**2 + self.height**2)
        radius = 2*self.height
        self.ell.circle = (self.x, self.y, radius, 0, 360, 6)



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
