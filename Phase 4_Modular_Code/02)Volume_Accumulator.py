hourly_volumes = [1.2, 0.5, 2.8, 1.1]
total_volume = 0.0

for volume in hourly_volumes:
    total_volume += volume


print("The total Volume is: ", round(total_volume, 2))

