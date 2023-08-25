from pweb import PWebEngine

pweb_engine = PWebEngine.bstart("PWebEngine", __file__)
pweb_engine.version = "1.0.0"


if __name__ == '__main__':
    pweb_engine.run()

