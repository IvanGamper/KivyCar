from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock

# Car data stored directly in the Kivy app
cars = [
    {"id": 1, "brand": "Tesla", "model": "Model3", "available": True},
    {"id": 2, "brand": "BMW", "model": "M5", "available": True},
    {"id": 3, "brand": "BMW", "model": "X6", "available": True},
    {"id": 4, "brand": "BMW", "model": "M3", "available": True},
    {"id": 5, "brand": "Mercedes-Benz", "model": "S-Klasse", "available": True},
    {"id": 6, "brand": "Audi", "model": "A3", "available": True},
]

class CarRentalApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Title
        self.layout.add_widget(Label(text="Car Sharing App", font_size=30))

        # Scrollable Car List
        self.car_list = ScrollView(size_hint=(1, 2))
        self.car_list_container = GridLayout(cols=1, size_hint_y=None)
        self.car_list_container.bind(minimum_height=self.car_list_container.setter('height'))
        self.car_list.add_widget(self.car_list_container)  # ✅ Add container to scroll view
        self.layout.add_widget(self.car_list)

        # Input field for Car ID
        self.car_id_input = TextInput(hint_text="Enter Car ID", multiline=False)
        self.layout.add_widget(self.car_id_input)

        # Buttons
        self.rent_button = Button(text="Rent Car", on_press=self.rent_car)
        self.layout.add_widget(self.rent_button)

        self.return_button = Button(text="Return Car", on_press=self.return_car)
        self.layout.add_widget(self.return_button)

        # Load Cars initially
        self.load_cars()

        return self.layout

    def load_cars(self):
        """Updates the car list dynamically."""
        self.car_list_container.clear_widgets()  # ✅ Clear old list

        for car in cars:
            car_text = f"{car['id']} - {car['brand']} {car['model']} - Available: {'Yes' if car['available'] else 'No'}"
            self.car_list_container.add_widget(Label(text=car_text, size_hint_y=None, height=30))

    def rent_car(self, instance):
        car_id = self.car_id_input.text
        if car_id.isdigit():
            car_id = int(car_id)
            for car in cars:
                if car["id"] == car_id:
                    if car["available"]:
                        car["available"] = False
                        self.load_cars()  # ✅ Refresh UI
                        self.show_alert("Car rented successfully!")
                        return
                    else:
                        self.show_alert("Car is already rented!")
                        return
            self.show_alert("Car not found!")
        else:
            self.show_alert("Please enter a valid Car ID.")

    def return_car(self, instance):
        car_id = self.car_id_input.text
        if car_id.isdigit():
            car_id = int(car_id)
            for car in cars:
                if car["id"] == car_id:
                    if not car["available"]:
                        car["available"] = True
                        self.load_cars()  # ✅ Refresh UI
                        self.show_alert("Car returned successfully!")
                        return
                    else:
                        self.show_alert("Car is not rented!")
                        return
            self.show_alert("Car not found!")
        else:
            self.show_alert("Please enter a valid Car ID.")

    def show_alert(self, message):
        """Show a temporary alert message"""
        alert_label = Label(text=message, font_size=15)
        self.layout.add_widget(alert_label)

        # Remove message after 2 seconds
        Clock.schedule_once(lambda dt: self.layout.remove_widget(alert_label), 2)

if __name__ == '__main__':
    CarRentalApp().run()
