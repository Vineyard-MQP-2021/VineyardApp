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
            self.connection_status_port = "5557"
            self.client_ip = "ip"
            self.context = zmq.Context()
            self.stream_socket = self.context.socket(zmq.REQ)
            self.stream_socket.connect("tcp://%s:%s" % (self.client_ip, self.stream_port))
            self.sound_socket = self.context.socket(zmq.REQ)
            self.sound_socket.connect("tcp://%s:%s" % (self.client_ip, self.sound_port))
            self.connection_socket = self.context.socket(zmq.SUB)
            self.connection_socket.setsockopt_string(zmq.SUBSCRIBE, "")
            self.connection_socket.setsockopt(zmq.CONFLATE, 1)
            self.connection_socket.connect("tcp://%s:%s" % (self.client_ip, self.connection_status_port))
            self.status = True
            self.frame = 0
            self.sentWithoutReply = False

    def sendAudio(self, name):
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
        self.sound_socket.recv_string()

    def getStream(self):
        self.stream_socket.send_string("requesting stream....")
        frame = self.stream_socket.recv()
        self.frame = base64.b64decode(frame)

    def getConnection(self):
        try:
            s = self.connection_socket.recv_string(zmq.NOBLOCK)
            return s
        except:
            return "n"

    @staticmethod
    def getInstance():
        if ZMQMessager.__instance is None:
            ZMQMessager()
        return ZMQMessager.__instance
