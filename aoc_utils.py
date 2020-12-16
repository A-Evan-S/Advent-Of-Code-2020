import time

def timed(f, x):
    start_time = time.time_ns()
    answer = f(x)
    end_time = time.time_ns()
    runtime = convert_time_units(end_time-start_time)
    return f"{answer:<15} ({runtime})"

def convert_time_units(runtime):
    if runtime == 0:
        return 'Less than measurable'
    units = 'ns'
    if runtime > 10 ** 9:
        runtime /= 10 ** 9
        units = 's'
    elif runtime > 10 ** 6:
        runtime /= 10 ** 6
        units = '\u03BCs'
    elif runtime > 10 ** 3:
        runtime /= 10 ** 3
        units = 'ms'
    return str(runtime) + ' ' + units