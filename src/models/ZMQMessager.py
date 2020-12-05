import zmq
import base64
import os


class ZMQMessager:
    __instance = None
    connected = False

    def __init__(self):
        if ZMQMessager.__instance is not None:
            raise Exception("Error")
        else:
            ZMQMessager.__instance = self
            self.stream_port = "5555"
            self.sound_port = "5556"
            self.context = zmq.Context()
            self.stream_socket = self.context.socket(zmq.REQ)
            self.stream_socket.connect("tcp://ip:" + self.stream_port)
            self.sound_socket = self.context.socket(zmq.REQ)
            self.sound_socket.connect("tcp://ip:" + self.sound_port)
            self.connected = True
            self.frame = 0

    def sendAudio(self, name):
        print("sending file...")
        url = "../res/sounds/" + name + "_mod.wav"
        if os.path.isfile(url):
            f = open(url, "rb")
        else:
            url = "../res/sounds/" + name + ".wav"
            f = open(url, "rb")
        wave = f.read()
        f.close()
        file = base64.b64encode(wave)
        self.sound_socket.send(file)
        message = self.sound_socket.recv_string()
        print(message)

    def getStream(self):
        self.stream_socket.send_string("requesting stream....")
        frame = self.stream_socket.recv()
        self.frame = base64.b64decode(frame)

    @staticmethod
    def getInstance():
        if ZMQMessager.__instance is None:
            ZMQMessager()
        return ZMQMessager.__instance
