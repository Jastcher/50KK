


class Time:
    def __init__(self, h, m):
        self.epoch = self.ConvertHtoMillis(h)
        self.epoch += self.ConvertMtoMillis(m)

    def display(self):
        print(ConvertMillis(self.epoch))
    
    def AddTime(self, h, m):
        self.epoch += ConvertHtoMillis(h)
        self.epoch += ConvertMtoMillis(m)

    def ConvertMillis(millis):
        #seconds = int(millis / 1000) % 60

        minutes = int(millis / (1000 * 60)) % 60

        hours = int(millis / (1000 * 60 * 60))

        return (hours, minutes)

    def ConvertHtoMillis(h):
        return h * 3_600_000

    def ConvertMtoMillis(m):
        return m * 60_000 



time = Time(16, 0)
time.display()

time.AddTime(4, 80)
time.display()

