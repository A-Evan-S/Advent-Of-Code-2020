import json
import datetime

def main():
    with open('leaderboard.json') as f:
        leaderboard_data = json.load(f)
    print('Average Part 1 Times:')
    part1_times = find_average_part1_times(leaderboard_data)
    for user in part1_times:
        print(f'\t{user} : {part1_times[user]}')
    print('Average Part 2 Times:')
    part2_times = find_average_part2_times(leaderboard_data)
    for user in part2_times:
        print(f'\t{user} : {part2_times[user]}')
    print('Average Time Deltas:')
    delta_times = find_average_delta_times(leaderboard_data)
    for user in delta_times:
        print(f'\t{user} : {delta_times[user]}')

def find_average_delta_times(leaderboard_data):
    avg_delta_times = {}
    for member in leaderboard_data['members']:
        name = leaderboard_data['members'][member]['name']
        avg_delta_times[name] = get_average_delta_time(leaderboard_data['members'][member])
    return avg_delta_times

def get_average_delta_time(member_data):
    member_data = member_data['completion_day_level']
    total_time = 0
    num_completed = 0
    for day in member_data:
        if '2' in member_data[day]:
            start_time = int(member_data[day]['1']['get_star_ts'])
            end_time = int(member_data[day]['2']['get_star_ts'])
            total_time += end_time - start_time
            num_completed += 1
    return convert_from_seconds(int(total_time / num_completed))

def find_average_part2_times(leaderboard_data):
    avg_part2_times = {}
    for member in leaderboard_data['members']:
        name = leaderboard_data['members'][member]['name']
        avg_part2_times[name] = get_average_part2_time(leaderboard_data['members'][member])
    return avg_part2_times

def find_average_part1_times(leaderboard_data):
    avg_part1_times = {}
    for member in leaderboard_data['members']:
        name = leaderboard_data['members'][member]['name']
        avg_part1_times[name] = get_average_part1_time(leaderboard_data['members'][member])
    return avg_part1_times

def get_average_part1_time(member_data):
    member_data = member_data['completion_day_level']
    total_time = 0
    num_completed = 0
    for day in member_data:
        start_time = int((datetime.datetime(2020,12,int(day),21) - datetime.timedelta(days=1)).timestamp())
        end_time = int(member_data[day]['1']['get_star_ts'])
        total_time += end_time - start_time
        num_completed += 1
    return convert_from_seconds(int(total_time/num_completed))

def get_average_part2_time(member_data):
    member_data = member_data['completion_day_level']
    total_time = 0
    num_completed = 0
    for day in member_data:
        if '2' in member_data[day]:
            start_time = int((datetime.datetime(2020,12,int(day),21) - datetime.timedelta(days=1)).timestamp())
            end_time = int(member_data[day]['2']['get_star_ts'])
            total_time += end_time - start_time
            num_completed += 1
    return convert_from_seconds(int(total_time/num_completed))

def convert_from_seconds(seconds):
    hours = seconds // 3600
    minutes = seconds // 60 % 60
    seconds = seconds % 60
    return f'{hours:02}:{minutes:02}:{seconds:02}'

if __name__ == '__main__':
    main()