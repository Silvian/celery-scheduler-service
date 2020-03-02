from app import app
from flask_script import Manager, Server


manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=8889))


@manager.command
def hello_world():
    from app.tasks.hello import print_hello_world_task

    print_hello_world_task()


if __name__ == '__main__':
    manager.run()
