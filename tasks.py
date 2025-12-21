from invoke import task

@task
def kaynnista(instanssi):
    instanssi.run("python3 src/dpll.py")

@task
def testit(instanssi):
    instanssi.run("pytest src")

@task
def kattavuus(instanssi):
    instanssi.run("coverage run --branch -m pytest src")
    instanssi.run("coverage report -m")
    instanssi.run("coverage html")