class StudentQueue:
    def __init__(self):
        self.queue = []

    # Joining the queue
    def enqueue(self, student):
        self.queue.append(student)

    # Dequeue students being served
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty."

    # Checking if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

   # Determining the current size of the queue
    def queue_size(self):
        return len(self.queue)


# Example 
student_queue = StudentQueue()

student_queue.enqueue("Alvin")
student_queue.enqueue("Peter")
student_queue.enqueue("Arijole")

print(student_queue.queue)  # The Output is: ['Alvin', 'Peter', 'Arijole']

served_student = student_queue.dequeue()
print("Served Student:", served_student)  # The Output is: Served Student: Alvin

print("Is the queue empty?", student_queue.is_empty())  # The Output is: Is the queue empty? False

print("Current queue size:", student_queue.queue_size())  # The Output is: Current queue size: 2




