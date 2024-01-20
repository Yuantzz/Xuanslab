from itertools import permutations

def is_valid(state):
    # 检查状态是否合法
    if state[1] and state[2] and state[1] != state[2]:
        return False
    if state[3] and state[4] and state[3] != state[4]:
        return False
    return True

def print_result(states):
    # 输出结果
    for i, state in enumerate(states):
        print(f"解法 {i+1}: {state}")

def river_crossing():
    # 人、羊、狼的初始状态
    initial_state = (0, 0, 0, 0, 0)
    # 所有可能的状态排列
    all_permutations = permutations([0, 0, 1, 1, 1])

    valid_states = []

    for perm in all_permutations:
        # 尝试每种可能的状态排列
        state = tuple(perm)
        if is_valid(state):
            valid_states.append(state)

    print_result(valid_states)

if __name__ == "__main__":
    river_crossing()
