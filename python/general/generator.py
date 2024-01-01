#!/usr/bin/python3
import queue

def task(name, queue):
    while not queue.empty():
        count = queue.get()
        total = 0
        print(f"Task {name} running")
        for x in range(count):
            total += 1
            print(f'before yield {total=} and {x=}')
            yield print(f'this is yield line for {name}')
            print('after yield x is:', x)
            print()
        print(f"Task {name} total: {total}")

def main():
    """
    This is the main entry point for the program
    """
    # Create the queue of work
    work_queue = queue.Queue()

    # Put some work in the queue
    for work in [10, 7, 5, 2]:
        work_queue.put(work)

    # Create some tasks
    tasks = [task("One", work_queue), task("Two", work_queue)]

    # Run the tasks
    done = False
    while not done:
        for t in tasks:
            try:
                if t == tasks[0]:
                    print('Task 11111 is running')
                else:
                    print('Task 222222 is running')
                next(t)
            except StopIteration:
                tasks.remove(t)
            print('length of tasks inside while is: ', len(tasks))
            if len(tasks) == 0:
                done = True

if __name__ == "__main__":
    main()
