# main.py
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder 

Builder.load_file("app.kv")

# ---Screen Classes---
class HomeScreen(Screen):
    pass

class ShopScreen(Screen):
    pass

class CartScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class RiderScreen(Screen):
    pass

class ShopNearScreenManager(Screen):
    pass

class ShopNearApp(App):
    def build(self):
        return ShopNearScreenManager()
    
if __name__ == "__main__":
    ShopNearApp().run()