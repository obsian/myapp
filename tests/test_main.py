
from myapp.main import MyAppTest

def test_myapp(tmp):
    with MyAppTest() as app:
        res = app.run()
        print(res)
        raise Exception

def test_command1(tmp):
    argv = ['command1']
    with MyAppTest(argv=argv) as app:
        app.run()
