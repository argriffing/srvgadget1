import argparse
import cherrypy


class MyForm:

    @cherrypy.expose
    def reverse_complement(self, dna=None):
        d = {'a':'t', 't':'a', 'c':'g', 'g':'c'}
        arr = [d.get(c, c) for c in reversed(dna.lower())]
        return ''.join(arr)

    @cherrypy.expose
    def index(self):
        arr = [
                '<html><body>',
                '<form action="reverse_complement" method="post">',
                '<label for="dna">DNA</label>',
                '<input type="text" id="dna" name="dna" />',
                '</form>'
                '</body></html>']
        return '\n'.join(arr)


def main(args):
    cherrypy.config.update({
        'server.socket_host': args.host,
        'server.socket_port': args.port})
    cherrypy.quickstart(MyForm())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default='127.0.0.1')
    parser.add_argument('--port', type=int, default=8080)
    main(parser.parse_args())
