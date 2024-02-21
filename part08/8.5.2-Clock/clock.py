import time
class Clock:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.day = 0
    
    
    def tick(self):
        self.seconds +=1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
                if self.hours == 24:
                    self.hours = 0
                    self.day +=1

    def __str__(self):
        return f"Time {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d} Day: {self.day}"
    

watch = Clock()

for i in range(36000):
    time.sleep(0.4)
    print(watch)
    watch.tick()
                    
        