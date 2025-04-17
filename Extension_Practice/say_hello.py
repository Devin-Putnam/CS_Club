import sublime
import sublime_plugin

class SayHelloCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "Hello from your Sublime plugin!\n")
