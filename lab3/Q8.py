import random

def generate_random_sequence(length):
    sequence = [random.randint(1, 100) for _ in range(length)]
    sequence.sort()
    return sequence

num_sequences = 5
max_length = 10  # 数列最大长度

sequences = []
for _ in range(num_sequences):
    length = random.randint(1, max_length)
    sequence = generate_random_sequence(length)
    sequences.append(sequence)