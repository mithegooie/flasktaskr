from fabric.api import local


def test():
    local("nosetests -v")

def commit():
    message = raw_input("Enter a git commit message: ")
    local("cd .. && git add . && git commit -am '{}'".format(message))

def push():
    local("git push -u origin master")

def prepare():
    test()
    commit()
    push()