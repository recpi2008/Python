import sys, time
# sys.executable

def teleprint(*args, delay=0.05, str_join=' '):
    text = str_join.join(str(x) for x in args)
    n = len(text)
    for i, char in enumerate(text, 1):
        if i == n:
            char = f'{char}\n'
        sys.stdout.write(char)
        time.sleep(delay)

teleprint('Печать с задержкой!', 10, 12.5, 'Super!!!', delay=0.07)

for line in sys.stdin:
    print(line.rstrip('\n')[::-1])
    sys.exit(0)

try:
    10/0
except ZeroDivisionError:
    sys.stderr.write("Exception occured!")