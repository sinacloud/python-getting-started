import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, world!")

def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(5050 or os.environ['PORT'])
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
