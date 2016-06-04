from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class StrategyGame(FloatLayout):
    pass


class StrategyGameApp(App):
    def build(self):
        return StrategyGame()

if __name__ == '__main__':
    StrategyGameApp().run()
