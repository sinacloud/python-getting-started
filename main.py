import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado import gen
from tornado.httpclient import AsyncHTTPClient

class MainHandler(tornado.web.RequestHandler):

    @gen.coroutine
    def get(self):
        http_client = AsyncHTTPClient()
        response = yield http_client.fetch("http://www.sinacloud.com")
        self.set_header('content-type', 'text/plain')
        self.write('Hello, World! ' + response.body[:100])

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(5050 or os.environ['PORT'])
    tornado.ioloop.IOLoop.current().start()
