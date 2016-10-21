import sublime, sublime_plugin

class HtmlUiCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        css = sublime.load_resource("Packages/sandbox/html/ui.css")
        html = sublime.load_resource("Packages/sandbox/html/ui.html").format(css=css)
        self.view.show_popup(html, 0, -1, 480, 700, self.on_navigate, self.on_hide)

    def on_navigate(self, href):
        print(href)

    def on_hide(self):
        print("closed popup")


class MyPhantomCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # html = sublime.load_resource("Packages/sandbox/html/phantom.html")
        css = sublime.load_resource("Packages/sandbox/html/ui.css")
        html = sublime.load_resource("Packages/sandbox/html/ui.html").format(css=css)
        v = self.view.window().new_file()
        v.settings().set('gutter', False)
        v.settings().set('margin', 0)
        v.set_read_only(True)
        v.set_scratch(True)
        sel = v.sel()
        sel.clear()
        # LAYOUT_INLINE
        # LAYOUT_BELOW
        # LAYOUT_BLOCK
        v.add_phantom("test", self.view.sel()[0], html, sublime.LAYOUT_INLINE)
    # view.erase_phantoms("test")
