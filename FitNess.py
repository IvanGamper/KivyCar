from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.video import Video  # Video-Widget importieren

# Übungen (Daten direkt im Code gespeichert)
exercises = [
    {"id": 1, "name": "Push-ups", "description": "Push-ups to work on chest and arms.", "video": "pushups.jpg"},
    {"id": 2, "name": "Squats", "description": "Squats to strengthen your legs.", "video": "squats.jpg"},
    {"id": 3, "name": "Plank", "description": "Plank for core strength.", "video": "plank.mp4"},
    {"id": 4, "name": "Jumping Jacks", "description": "Full-body cardio exercise.", "video": "jumping_jacks.jpg"},
    {"id": 5, "name": "Lunges", "description": "Lunges for leg muscles.", "video": "lunges.jpg"},
    {"id": 6, "name": "Burpees", "description": "Burpees for full-body strength and cardio.", "video": "burpees.jpg"},
]

class FitnessApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Title
        self.layout.add_widget(Label(text="Fitness Workout App", font_size=30))

        # Scrollable Exercise List
        self.exercise_list = ScrollView(size_hint=(1, 2))
        self.exercise_list_container = GridLayout(cols=1, size_hint_y=None)
        self.exercise_list_container.bind(minimum_height=self.exercise_list_container.setter('height'))
        self.exercise_list.add_widget(self.exercise_list_container)
        self.layout.add_widget(self.exercise_list)

        # Input field for Exercise ID
        self.exercise_id_input = TextInput(hint_text="Enter Exercise ID", multiline=False)
        self.layout.add_widget(self.exercise_id_input)

        # Button to add exercise to workout
        self.add_button = Button(text="Add to Workout", on_press=self.add_exercise_to_workout)
        self.layout.add_widget(self.add_button)

        # Button to remove exercise from workout
        self.remove_button = Button(text="Remove from Workout", on_press=self.remove_exercise_from_workout)
        self.layout.add_widget(self.remove_button)

        # List of selected exercises (for workout)
        self.selected_exercise_list = GridLayout(cols=1, size_hint_y=None)
        self.selected_exercise_list.bind(minimum_height=self.selected_exercise_list.setter('height'))

        self.selected_scroll_view = ScrollView(size_hint=(1, 2))
        self.selected_scroll_view.add_widget(self.selected_exercise_list)
        self.layout.add_widget(Label(text="Your Workout:"))
        self.layout.add_widget(self.selected_scroll_view)

        # Workout-Liste, um die hinzugefügten Übungen zu speichern
        self.selected_exercises = []

        # Video-Widget (wird dynamisch mit dem richtigen Video aktualisiert)
        self.video_player = Video(source="", state='pause', options={'allow_stretch': True}, size_hint=(1, 2))
        self.layout.add_widget(self.video_player)

        # Load exercises initially
        self.load_exercises()

        return self.layout

    def load_exercises(self):
        """Lädt die Übungsliste und zeigt sie an."""
        self.exercise_list_container.clear_widgets()  # Clear old list

        for exercise in exercises:
            exercise_text = f"{exercise['id']} - {exercise['name']}: {exercise['description']}"
            self.exercise_list_container.add_widget(Label(text=exercise_text, size_hint_y=None, height=30))

    def add_exercise_to_workout(self, instance):
        """Fügt die ausgewählte Übung der Workout-Liste hinzu."""
        exercise_id = self.exercise_id_input.text
        if exercise_id.isdigit():
            exercise_id = int(exercise_id)
            for exercise in exercises:
                if exercise["id"] == exercise_id:
                    if exercise_id not in [ex["id"] for ex in self.selected_exercises]:
                        self.selected_exercises.append(exercise)
                        self.update_workout_list()
                        self.update_video(exercise["video"])  # Video abspielen
                    else:
                        self.show_alert("Exercise already in your workout!")
                    return
            self.show_alert("Exercise not found!")
        else:
            self.show_alert("Please enter a valid Exercise ID.")

    def remove_exercise_from_workout(self, instance):
        """Entfernt die ausgewählte Übung von der Workout-Liste."""
        exercise_id = self.exercise_id_input.text
        if exercise_id.isdigit():
            exercise_id = int(exercise_id)
            for exercise in self.selected_exercises:
                if exercise["id"] == exercise_id:
                    self.selected_exercises.remove(exercise)
                    self.update_workout_list()
                    return
            self.show_alert("Exercise not found in your workout!")
        else:
            self.show_alert("Please enter a valid Exercise ID.")

    def update_workout_list(self):
        """Aktualisiert die Workout-Liste in der Benutzeroberfläche."""
        self.selected_exercise_list.clear_widgets()  # Clear old list
        for exercise in self.selected_exercises:
            exercise_text = f"{exercise['name']} - {exercise['description']}"
            self.selected_exercise_list.add_widget(Label(text=exercise_text, size_hint_y=None, height=30))

    def update_video(self, video_source):
        """Aktualisiert das Video-Widget mit dem neuen Video."""
        self.video_player.source = video_source
        self.video_player.state = 'play'

    def show_alert(self, message):
        """Zeigt eine Warnmeldung an."""
        alert_label = Label(text=message, font_size=15)
        self.layout.add_widget(alert_label)

        # Entfernt die Nachricht nach 2 Sekunden
        from kivy.clock import Clock
        Clock.schedule_once(lambda dt: self.layout.remove_widget(alert_label), 2)

if __name__ == '__main__':
    FitnessApp().run()
