from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView


class ToDoListApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tasks = []
    
    def build(self):
        layout = BoxLayout(orientation='vertical')
        scroll_view = ScrollView()
        task_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        scroll_view.add_widget(task_layout)
        
        for task in self.tasks:
            task_widget = BoxLayout(orientation='horizontal', spacing=10)
            checkbox = CheckBox()
            task_label = Label(text=task)
            task_widget.add_widget(checkbox)
            task_widget.add_widget(task_label)
            task_layout.add_widget(task_widget)
        
        add_button = Button(text='Add Task', size_hint=(1, 0.1))
        add_button.bind(on_press=self.add_task)
        layout.add_widget(scroll_view)
        layout.add_widget(add_button)
        
        return layout
    
    def add_task(self, instance):
        self.tasks.append('New Task')
        self.root.clear_widgets()
        self.build()


if __name__ == '__main__':
    ToDoListApp().run()
