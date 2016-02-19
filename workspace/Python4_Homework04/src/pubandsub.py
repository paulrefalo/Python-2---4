'''
Created on Nov 10, 2015

@author: prefalo
'''

class Publisher:
    def __init__(self):
        self.subscribers = []
    def subscribe(self, subscriber):
        if subscriber in self.subscribers:
            raise ValueError("Multiple subscriptions are not allowed")
        self.subscribers.append(subscriber)
    def unsubscribe(self, subscriber):
        if subscriber not in self.subscribers:
            raise ValueError("Can only unsubscribe subscribers")
        self.subscribers.remove(subscriber)
    def publish(self, s):
        altList = list(self.subscribers)
        for subscriber in altList:
            #print(s, subscriber.__name__)
            subscriber(s)

if __name__ == '__main__':
    def multiplier(s):
        print(2*s)
        
    class SimpleSubscriber:
        def __init__(self, name, publisher):
            self.name = name
            self.count = 0
            self.tally = 0
            self.publisher = publisher
            publisher.subscribe(self.process)
        def process(self, s):
            self.count += 1
            if self.tally > 1:
                self.count += self.tally
            #print("The count is:", self.count)
            print(self.name, ":", s.upper())
            if self.count > 3:
                publisher.unsubscribe(publisher.subscribers[0])
                self.tally = 0
            self.tally = self.count
            #print("Tally is:", self.tally)
            """
            The count of the subscribers list is off.  Making a copy of the
            subscribers list fixed this count.
            """

        def __repr__(self):
            return self.name
            
    publisher = Publisher()
    publisher.subscribe(multiplier)
    for i in range(6):
        newsub = SimpleSubscriber("Sub" + str(i), publisher)
        line = input("Input {}: ".format(i))
        #print("Line is:", line)
        publisher.publish(line)
