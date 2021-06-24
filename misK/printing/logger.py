import traceback
from datetime import datetime

FILE = None
FUNC = None
MOTHER_FUNCTION = None
FUNCTION_CHANGE = False


def _get_head(depth=1):
    global FUNC
    stack = traceback.format_stack()
    file, line, FUNC = stack[-2 - depth].split('\n')[0].split(", ")
    file = file.split('"')[1]
    line = line.split(' ')[1]
    FUNC = FUNC.split(' ')[1]
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S,%f")

    return f"[{now}][{file}][{FUNC}][{line}][LOG] "


def open_logger(filename, mode='a'):
    global FILE
    FILE = open(filename, mode=mode)
    FILE.write(_get_head() + "logger opened." + '\n')


def log(*args, **kwargs):
    global FUNCTION_CHANGE, MOTHER_FUNCTION, FILE, FUNC

    head = _get_head()

    FUNCTION_CHANGE = FUNC != MOTHER_FUNCTION
    MOTHER_FUNCTION = FUNC

    if FUNCTION_CHANGE:
        print()
        FILE.write('\n')

    print(head, *args, **kwargs)
    FILE.write(head + ' '.join(map(str, args)) + '\n')


def close_logger():
    global FUNCTION_CHANGE, MOTHER_FUNCTION, FILE, FUNC

    head = _get_head()

    FUNCTION_CHANGE = FUNC != MOTHER_FUNCTION
    MOTHER_FUNCTION = FUNC

    if FUNCTION_CHANGE:
        print()
        FILE.write('\n')
    FILE.write(head + "logger closed." + "\n\n")
    if FILE is not None:
        FILE.close()


def sub_main(log=print):
    log("sub_main 1")
    log("sub_main 2")
    log("sub_main 3")
    dico = dict([(chr(97+i), sum([10**j for j in range(i)])) for i in range(20)])
    log("dictionary example:", dico)
    log("sub_main end")


def main(log=print):
    log("first line")
    for line in range(10, 20, 3):
        log(f"line n° {line}")
    sub_main(log=log)
    log("end")


if __name__ == "__main__":
    open_logger("log/log.log")
    main(log=log)
    close_logger()
