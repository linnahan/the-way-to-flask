# encoding: utf-8

from application import create_app


if __name__ == "__main__":
    app = create_app('devenlopment')
    app.run()