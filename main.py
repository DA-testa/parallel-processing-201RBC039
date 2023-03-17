# python3

def parallel_processing(n, m, data):
    output = []
    threads = [(i,0)for i in range(n)]
    for i in range(m):
        t = data[i]
        thread_in = min(range(n), key=lambda i: threads[i][1])
        start_time = threads[thread_in][1]
        output.append((thread_in, start_time))
        threads[thread_in] = (thread_in, start_time + t)
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for thread_in, start_time in result:
        print(thread_in, start_time)

if __name__ == "__main__":
    main()
