import collections

from kivy.app import App
from kivy import properties
from kivy.uix import button
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
            self.main_map.add_widget(MapRegion(row=row, col=col))


class MapRegion(button.Button):
    def __init__(self, row=0, col=0, **kwargs):
        self.region_in_map = MapCoords(row, col)
        super(MapRegion, self).__init__(**kwargs)
        self.text = '({}, {})'.format(self.region_in_map.row, self.region_in_map.col)


class StrategyGameApp(App):
    def build(self):
        return StrategyGame()

if __name__ == '__main__':
    StrategyGameApp().run()
