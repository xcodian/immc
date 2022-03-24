from datetime import datetime
from random import randint, shuffle, randrange

import statistics

import numpy as np
import matplotlib.pyplot as plt

PLANE_FULLNESS_PERCENT = 100 # this is very interesting
ROW_COUNT = 33
SEATS_PER_ROW = 3
SIM_COUNT = 1000 # reruns the plane simulation n times

MIN_INDIVIDUAL_BAGGING_TIME = 5
MAX_INDIVIDUAL_BAGGING_TIME = 20

MIN_INDIVIDUAL_BAGS = 1
MAX_INDIVIDUAL_BAGS = 3

PERCENTAGE_OF_PASSENGERS_NOT_FOLLOWING_INSTRUCTIONS = 5

passenger_count = int(ROW_COUNT * SEATS_PER_ROW * PLANE_FULLNESS_PERCENT * 0.01 * 2)

class Passenger:
    def __init__(self, target: list = None):
        self.target = target or [0, 0]
        self.is_bagging = False
        self.bagging_remaining = randint(MIN_INDIVIDUAL_BAGGING_TIME, MAX_INDIVIDUAL_BAGGING_TIME) * randint(MIN_INDIVIDUAL_BAGS, MAX_INDIVIDUAL_BAGS)
        self.boarding_time = 0

        # further away means more 
        self.sitdown_time = 1 + self.target[1] % 3

        if self.target[1] < 3: # left side gaming
            self.sitdown_time = 4 - self.sitdown_time

    def __repr__(self) -> str:
        return f'passenger{self.target} {"bagging" if self.is_bagging else "moving"}'

targets_pool = []
middle = {}
seats = {}

def partial_shuffle(l, factor=5):
    n = len(l)
    for _ in range(factor):
        a, b = randrange(n), randrange(n)
        l[b], l[a] = l[a], l[b]

def prepare(): 
    global targets_pool, middle, seats

    targets_pool = []
    middle = {}
    seats = {}
    
    # make random target pool
    for r in range(ROW_COUNT):
        for s in range(SEATS_PER_ROW*2):
            targets_pool.append([r+passenger_count, s])

    # targets_pool = list(reversed(targets_pool))

    shuffle(targets_pool)

    # passengers not following instructions
    swaps = int(len(targets_pool) * (PERCENTAGE_OF_PASSENGERS_NOT_FOLLOWING_INSTRUCTIONS / 100))
    # print(f'swapping {swaps} positions due to {PERCENTAGE_OF_PASSENGERS_NOT_FOLLOWING_INSTRUCTIONS}% not following instructions')
    partial_shuffle(targets_pool, swaps)

    _outside = {
        i: Passenger(
            target=targets_pool[i]
        ) for i in range(passenger_count)
    }

    middle = _outside | {
        i+passenger_count: None for i in range(ROW_COUNT)
    }

    seats = {
        i+passenger_count: {
            j: None
            for j in range(SEATS_PER_ROW*2)
        } for i in range(ROW_COUNT)
    }

# print('\n'.join([str(p) for p in middle.values()]))

def step():
    # run simulation

    row_numbers = list(reversed(middle.keys()))

    for row_number in row_numbers:
        passenger_at_index = middle[row_number]
        
        if passenger_at_index is None:
            continue

        passenger_at_index.boarding_time += 1
        
        # check if guy has to bag here
        if passenger_at_index.target[0] == row_number:
            if not passenger_at_index.is_bagging:
                passenger_at_index.is_bagging = True
                # print(f'{passenger_at_index} has started bagging')
                continue
            
            passenger_at_index.bagging_remaining -= 1

            if passenger_at_index.bagging_remaining == 0:
                # put into seat
                # print(f'{passenger_at_index} has gotten into their seat in {passenger_at_index.time_taken} cycles')
                seats[passenger_at_index.target[0]][passenger_at_index.target[1]] = passenger_at_index
                middle[row_number] = None
                continue
            
            # print(f'passenger {row_number} will not move because they are bagging')
            continue

        # check if p can move forward
        if middle.get(row_number+1) or row_number+1 >= ROW_COUNT+passenger_count:
            # print(f'{row_number} (wants to get to {passenger_at_index.target[0]}) cannot move forward as someone is obstructing {row_number+1}')
            continue

        # print(f'{row_number} (wants to get to {passenger_at_index.target[0]}) can move forward to {row_number+1}')

        middle[row_number+1] = middle[row_number]
        middle[row_number] = None

    # sitty downy
    globally_subtract_times_of_seated_passengers()

def is_everyone_in():
    for v in middle.values():
        if v:
            return False

    # check if everyone in seats is sitting down
    for row in seats.values():
        for p in row.values():
            if p is None:
                continue
            if p.sitdown_time:
                return False
    
    return True

def globally_subtract_times_of_seated_passengers():
    for row in seats.values():
        for p in row.values():
            if p is None:
                continue

            if p.sitdown_time:
                p.sitdown_time -= 1

average_boarding_times = []

def run():
    prepare()

    # print(f'simulating {passenger_count} passengers in {ROW_COUNT} x {SEATS_PER_ROW}+{SEATS_PER_ROW} plane')

    cycle = 0
    while True:
        if is_everyone_in():
            break
        step()

    # for row_num, row in seats.items():
    #     print(' '.join([':)' if p else '--' for p in row.values()]))

    all_passengers = []
    for row in seats.values():
        row_filtered = [p for p in row.values() if p]
        for p in row_filtered:
            all_passengers.append(p)

    boarding_times = [p.boarding_time for p in all_passengers]
    average_boarding_time = statistics.mean(boarding_times)

    return average_boarding_time


total_sims = 0

for sim_id in range(SIM_COUNT):
    # print(f'simulation #{sim_id} commencing...')
    btime = run()
    average_boarding_times.append(btime)
    print(f'[{(sim_id+1)/SIM_COUNT*100:.2f}%] simulation {sim_id+1}/{SIM_COUNT} done - average boarding time: {btime}')

    total_sims += 1

# print(all_passengers)

print('\n--- numbers ---')

print()

log = 'boarding times mean:' + str(statistics.mean(average_boarding_times)) + '\nboarding times median:' + str(statistics.median(average_boarding_times)) + '\nboarding times mode:' + str(statistics.mode(average_boarding_times)) + '\n\nboarding times min:' + str(min(average_boarding_times)) + '\nboarding times max:' + str(max(average_boarding_times)) + '\nboarding times range:' + str(max(average_boarding_times) - min(average_boarding_times)) + '\n\nboarding times stdev:' + str(statistics.stdev(average_boarding_times)) + '\nboarding times 5th percentile: ' + str(np.percentile(average_boarding_times, 5)) + '\nboarding times 95th percentile: ' + str(np.percentile(average_boarding_times, 95))

plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})

# Plot Histogram on x
plt.hist(average_boarding_times, bins=50)
plt.gca().set(title=f'Average boarding time of {passenger_count} passengers (simulated {total_sims} times)', ylabel='Frequency')
plt.xlabel('Boarding Time (s)')


now = datetime.now()

print('writing data...')
with open(f'data_{SIM_COUNT}_{now}.csv', 'w+') as f:
    f.write('average_boarding_time\n')
    f.write('\n'.join(
        [str(t) for t in average_boarding_times]
    ))

print('writing histogram...')
plt.savefig(f'fig_{SIM_COUNT}_{now}.png')

print('writing log...')
with open(f'log_{SIM_COUNT}_{now}.log', 'w+') as f:
    f.write(log)

plt.show()
