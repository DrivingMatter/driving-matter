import websocket

class CameraOneReceiver(websocket.WebSocket):
    #def on_open(self):
    #    self.write('hello, world')

    def on_message(self, data):
        try:
            .write_message(base64.b64encode(sio.getvalue()))
        except tornado.websocket.WebSocketClosedError:
        print data

class ActionSensorReceiver(websocket.WebSocket):
    def on_message(self, data):
        print data

class CameraOneForwarder(tornado.websocket.WebSocketHandler):
    def on_message(self, data):
        print data

class ActionSensorForwarder(tornado.websocket.WebSocketHandler):
    def on_message(self, data):
        print data


cam1 = CameraOne('ws://192.168.0.110:8000/CameraOne')
sensor = SensorAction('ws://192.168.0.110:8000/ActionAndSensor')

cam1.connect()
sensor.connect()

handlers = [
            (r"/CameraOne", CameraOneReceiver),
            (r"/ActionAndSensor", ActionSensorReceiver),
          	(r'/static/(.*)', tornado.web.StaticFileHandler, {'path': ROOT}),    
        ];

application = tornado.web.Application(handlers)
application.listen(args.port)

webbrowser.open("http://localhost:7881/", new=2)

tornado.ioloop.IOLoop.instance().start()