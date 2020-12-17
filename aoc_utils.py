import time

def timed(f, x):
    answer, runtime = time_execution(f, x)
    return f"{answer:<15} ({runtime})"

def time_execution(f, x):
    start_time = time.time_ns()
    answer = f(x)
    end_time = time.time_ns()
    runtime = convert_time_units(end_time - start_time)
    return answer, runtime

def convert_time_units(runtime):
    if runtime > 10 ** 9:
        runtime /= 10 ** 9
        units = 's'
    elif runtime > 10 ** 6:
        runtime /= 10 ** 6
        units = 'ms'
    else:
        return '< 1 ms'
    return f'{runtime:.4} {units}'