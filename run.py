import webbrowser
import uvicorn

from multiprocessing import Process

def run_localhost():
    uvicorn.run('main:app')


if __name__ == '__main__':
    run_localhost_proc = Process(target=run_localhost)

    run_localhost_proc.start()