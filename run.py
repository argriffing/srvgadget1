"""
"""

import argparse
import cherrypy

class HelloWorld:
    def index(self):
        return 'ohai'
    index.exposed = True

def main(args):
    cherrypy.config.update({
        'server.socket_host': args.host,
        'server.socket_port': args.port})
    cherrypy.quickstart(HelloWorld())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default='localhost')
    parser.add_argument('--port', type=int, default=8080)
    main(parser.parse_args())
