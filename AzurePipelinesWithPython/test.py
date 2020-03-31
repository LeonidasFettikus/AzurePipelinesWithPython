class Value:
    ButtonId: str
    ButtonPressCount: int

    def __init__(self, button_id, button_press_count):
        self.ButtonId = button_id
        self.ButtonPressCount = int(button_press_count)

    def to_dict(self):
        return {"ButtonId": self.ButtonId, "ButtonPressCount": self.ButtonPressCount}

class Test:
    values: list
    subscribers: set

    def __init__(self):
        self.values = list()  
        self.subscribers = set()

    def register(self, subscriber):
        self.subscribers.add(subscriber)

    def test(self, data):        
        objVal = Value(data.split(';')[0], data.split(';')[1])
        if(objVal.ButtonPressCount > 0 and 
        not any(v.ButtonId == objVal.ButtonId and v.ButtonPressCount == objVal.ButtonPressCount for v in self.values)):
            self.values.append(objVal)

    def send_values(self):
        for subscriber in self.subscribers:
            subscriber.receive_values(self.values)

class Receiver:
    values: list
    
    def __init__(self):
        self.values = list()

    def receive_values(self, values):
        self.values.extend(values)        

    def run(self):
        test = Test()
        test.register(self)
        test.test("002312312;23")
        test.test("002312312;23")
        test.test("002312312;23")
        test.send_values()

    def print_values(self):
        for value in self.values:
            print(value)

receiver = Receiver()
receiver.run()
receiver.print_values()