from pweb import PWebEngine

pweb_engine = PWebEngine.bstart("PWebExample", __file__)
pweb_engine.version = "1.0.0"

cli = pweb_engine.cli
wsgi = pweb_engine.get_app()


if __name__ == '__main__':
    pweb_engine.run()

