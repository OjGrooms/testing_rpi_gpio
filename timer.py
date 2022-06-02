from threading import Timer

class ButtonTimeout():
  def __init__(self, time, callbackFunction):
    print('timer init')
    self.time = time
    self.callbackFunction = callbackFunction
    self.thread = Timer(self.time, self.handle_function)

  def handle_function(self):
    print('handling callback')
    self.callbackFunction()

  def start(self):
    print('timer started')
    self.thread = Timer(self.time, self.handle_function)
    self.thread.start()

  def cancel(self):
    print('timer cancelled')
    self.thread.cancel()
