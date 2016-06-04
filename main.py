from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class HelloWorld(FloatLayout):
    pass

class HelloWorldApp(App):
    def build(self):
        return HelloWorld()

if __name__ == '__main__':
    HelloWorldApp().run()
