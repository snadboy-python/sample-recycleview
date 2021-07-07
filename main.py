from kivy.lang import Builder
from kivy.app import App
from kivy.properties import ListProperty, NumericProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout

class TestApp(App):
    # A list of the data items
    data = ListProperty()

    def build(self):
        # Initialize the data items
        self.data = [
            dict(
                text=f'Key: {i}',
                rv_key=i,
                is_active=i % 3 == 0,
            )
            for i in range(250)
        ]

        return 

if __name__ == '__main__':
    TestApp().run()