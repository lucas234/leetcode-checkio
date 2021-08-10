# coding=utf-8
# auther：Liul5
# date：2019/5/5 13:09
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/voice-tv-control/


class VoiceCommand(object):
    def __init__(self, channels):
        self.channels = channels
        self.current_index = 1
        self.length = len(self.channels)

    def first_channel(self):
        return self.channels[0]

    def last_channel(self):
        last_index = self.channels.index(self.channels[-1]) + 1
        self.current_index = last_index
        return self.channels[last_index - 1]

    def turn_channel(self, index):
        self.current_index = index
        return self.channels[index - 1]

    def next_channel(self):
        next_index = self.current_index + 1
        if next_index > self.length:
            next_index = 1
        self.current_index = next_index
        return self.channels[next_index - 1]

    def previous_channel(self):
        previous_index = self.current_index - 1
        if previous_index <= 0:
            previous_index = self.channels.index(self.channels[-1]) + 1
        self.current_index = previous_index
        return self.channels[previous_index - 1]

    def current_channel(self):
        return self.channels[self.current_index - 1]

    def is_exist(self, channel):
        if isinstance(channel, str):
            return "Yes" if channel in self.channels else "No"
        else:
            return "Yes" if channel <= self.length else "No"


CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = VoiceCommand(CHANNELS)

# print controller.turn_channel(3)
# print controller.next_channel()
# print controller.current_channel()
#
#
# print controller.turn_channel(1)
# print controller.previous_channel()
# print controller.current_channel()


print controller.last_channel()
print controller.previous_channel()
print controller.current_channel()

# print controller.first_channel() #== "BBC"
# print controller.last_channel() #== "TV1000"
# print controller.turn_channel(1) #== "BBC"
# print controller.next_channel() #== "Discovery"
# print controller.previous_channel() #== "BBC"
# print controller.current_channel() #== "BBC"
# print controller.is_exist(4) #== "No"
# print controller.is_exist("BBC") #== "Yes"
