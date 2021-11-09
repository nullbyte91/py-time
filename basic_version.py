import time

def main():
    """Calculate time taken for 100000 loop"""
    start = time.perf_counter()
    for i in range(100000):
        pass
    end = time.perf_counter()
    
    print("Elapsed time:{0:.8f} seconds".format(end - start))

if __name__ == "__main__":
    main()
