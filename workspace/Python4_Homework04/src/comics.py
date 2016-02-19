"""
pubandsub.py
"""

class Publisher:
    
    def __init__(self):
        self.subscribers = []
        
    def subscribe(self, subscriber):
        if subscriber in self.subscribers:
            raise ValueError("Multiple subscriptions are not allowed")
        self.subscribers.append(subscriber)
        
    def unsubscribe(self, subscriber):
        if subscriber not in self.subscribers:
            raise ValueError("Can only unsubcribe existing subscribers")
        self.subscribers.remove(subscriber)
        
    def publish(self, s):
        print(s)
        altList = list(self.subscribers)
        for subscriber in self.subscribers:
            subscriber(s)
            
if __name__ == '__main__':
    
    class Subscriber:
        def __init__(self, name, publisher):
            self.name = name
            self.proc_calls = 0
            self.publisher = publisher
            publisher.subscribe(self.process)
        def process(self, s):
            self.proc_calls += 1
            print(self.name, "is going around %s time" % self.proc_calls)
            if self.proc_calls == 3:
                self.publisher.unsubscribe(self.process)
                print(self.name, "is getting off thanks.")
        def __repr__(self):
            return self.name
    
    tourists = []
    publisher = Publisher()
    for i in range(10):
        if i < 4:
            rider = Subscriber(name = input("Name: "), publisher = publisher)
            tourists.append(rider)
        line = "=== Rotation: %s" % i
        publisher.publish(line)
        
    for t in tourists:
        print(t.name, "went around", t.proc_calls, "times")
