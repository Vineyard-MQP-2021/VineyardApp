import zmq
import base64
import os


class ZMQMessager:
    __instance = None

    def __init__(self):
        if ZMQMessager.__instance is not None:
            raise Exception("Error")
        else:
            ZMQMessager.__instance = self
            self.port = "5555"
            self.context = zmq.Context()
            self.socket = self.context.socket(zmq.REQ)
            self.socket.connect("tcp://ip_address:" + self.port)
            # message = self.socket.recv()
            # print(message)

    def sendAudio(self, name):
        print("sending request...")
        url = "../res/sounds/" + name + "_mod.wav"
        if os.path.isfile(url):
            f = open(url, "rb")
        else:
            url = "../res/sounds/" + name + ".wav"
            f = open(url, "rb")
        wave = f.read()
        f.close()
        file = base64.b64encode(wave)
        self.socket.send(file)

    @staticmethod
    def getInstance():
        if ZMQMessager.__instance is None:
            ZMQMessager()
        return ZMQMessager.__instance
