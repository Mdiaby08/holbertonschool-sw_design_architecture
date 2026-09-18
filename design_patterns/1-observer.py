#!/usr/bin/env python3

class NewsSubject:
    def __init__(self):
        self._observers = {}

    def subscribe(self, observer, topics=None):
        if topics is None:
            topics = {"*"}
        for topic in topics:
            self._observers.setdefault(topic, set()).add(observer)

    def unsubscribe(self, observer):
        for topic in list(self._observers.keys()):
            if observer in self._observers[topic]:
                self._observers[topic].remove(observer)

    def notify(self, topic, data):
        observers = set()
        if topic in self._observers:
            observers |= self._observers[topic]
        if "*" in self._observers:
            observers |= self._observers["*"]

        for obs in list(observers):
            obs.update(topic, data)


class LogObserver:
    def update(self, topic, data):
        print(f"log:{topic}={data}")


class EmailObserver:
    def update(self, topic, data):
        print(f"email:{topic}={data}")


class SmsObserver:
    def update(self, topic, data):
        print(f"sms:{topic}={data}")


def main():
        subject = NewsSubject()

        log = LogObserver()
        email = EmailObserver()

        subject.subscribe(log, {"sports", "breaking"})
        subject.subscribe(email)

        sms = SmsObserver()
        subject.subscribe(sms, {"breaking"})

        subject.notify("weather", "rain")
        subject.notify("sports", "goal")
        subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
