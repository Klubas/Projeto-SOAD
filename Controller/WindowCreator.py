import threading


class WindowCreator ():

    def __init__(self, thread_ID, window_cls, parent_obj):
        threading.Thread.__init__(self)
        self.thread_ID = thread_ID
        self.window_cls = window_cls
        self.parent_obj = parent_obj
        self.returnCode = -1

    def create_new_window(self, modal=False):
        form = self.window_cls(self.parent_obj)
        if modal:
            form.exec()
        else:
            form.show()

    def run(self):
        self.create_new_window()
        return 0
