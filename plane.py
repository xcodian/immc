from random import randint, shuffle

import statistics

import numpy as np
import matplotlib.pyplot as plt

PLANE_FULLNESS_PERCENT = 100
ROW_COUNT = 33
SEATS_PER_ROW = 3

passenger_count = int(ROW_COUNT * SEATS_PER_ROW * PLANE_FULLNESS_PERCENT * 0.01 * 2)

class Passenger:
    def __init__(self, target: list = None):
        self.target = target or [0, 0]
        self.is_bagging = False
        self.bagging_remaining = randint(5, 10)
        self.boarding_time = 0

    def __repr__(self) -> str:
        return f'passenger{self.target} {"bagging" if self.is_bagging else "moving"}'

targets_pool = []

# make random target pool
for r in range(ROW_COUNT):
    for s in range(SEATS_PER_ROW*2):
        targets_pool.append([r+passenger_count, s])

# targets_pool = list(reversed(targets_pool))

shuffle(targets_pool)

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

def is_everyone_in():
    for v in middle.values():
        if v:
            return False

    return True

while True:
    if is_everyone_in():
        break
    step()

print('--- plane overview ---')

for row_num, row in seats.items():
    print(' '.join([':)' if p else '--' for p in row.values()]))

all_passengers = []
for row in seats.values():
    row_filtered = [p for p in row.values() if p]
    for p in row_filtered:
        all_passengers.append(p)

# print(all_passengers)

boarding_times = np.array([p.boarding_time for p in all_passengers])

print('\n--- numbers ---')
print('boarding time mean:', statistics.mean(boarding_times))
print('boarding time median:', statistics.median(boarding_times))
print('boarding time mode:', statistics.mode(boarding_times))

print()

print('boarding time min:', min(boarding_times))
print('boarding time max:', max(boarding_times))
print('boarding time range:', max(boarding_times) - min(boarding_times))

print()

print('boarding time stdev:', statistics.stdev(boarding_times))
print('boarding time 5th percentile: ', np.percentile(boarding_times, 5))
print('boarding time 95th percentile: ', np.percentile(boarding_times, 95))

plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})

# Plot Histogram on x
plt.hist(boarding_times, bins=50)
plt.gca().set(title=f'Boarding Times of {passenger_count} passengers', ylabel='Frequency')
plt.xlabel('Boarding Time (s)')
plt.show()