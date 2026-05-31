import multiprocessing

# 1. The 'Program' to be sent to the data
def mapper_function(data_slice):
    """Simple task: Find the max price in this slice"""
    return max(data_slice)

if __name__ == "__main__":
    # 2. The 'Data' sliced into pieces
    big_data = [1900, 2050, 2100, 1950, 2200, 2010, 2300, 1980]
    slices = [big_data[0:4], big_data[4:8]] 

    # 3. Sending the program to the slices (Parallel Processing)
    with multiprocessing.Pool(processes=2) as pool:
        map_results = pool.map(mapper_function, slices)

    # 4. The 'Reduce' process: Combining the results
    final_max = max(map_results)
    print(f"Global Max Price: {final_max}") # Output: 2300