from collections import deque

def monkey_banana_solver(start_state):
    goal_state = ('under_bananas', 'under_bananas', True)
    queue = deque([(start_state, [])])
    visited = {start_state}

    while queue:
        current_state, path = queue.popleft()
        m_pos, b_pos, m_on_b = current_state
        
        # Check if we have reached the goal state
        if m_on_b and m_pos == 'under_bananas':
            return path + ["GRASP Bananas"]

        successors = []
        
        # If the monkey is not on the box
        if not m_on_b:
            # If the monkey and box are at different positions, it can move the box
            if m_pos != b_pos:
                successors.append((
                    (b_pos, b_pos, False), f"MOVE: {m_pos} -> {b_pos}"
                ))

            # If the monkey is at the box and the box is not under bananas, it can push it
            if m_pos == b_pos and m_pos != 'under_bananas':
                successors.append((
                    ('under_bananas', 'under_bananas', False), f"PUSH Box: {b_pos} -> under_bananas"
                ))

            # If the monkey is at the box, it can climb it
            if m_pos == b_pos:
                successors.append((
                    (m_pos, b_pos, True), "CLIMB Box"
                ))

        # Explore all possible valid successors
        for next_state, action in successors:
            if next_state not in visited:
                visited.add(next_state)
                new_path = path + [action]
                queue.append((next_state, new_path))

    return None

if __name__ == "__main__":
    START_STATE = ('at_floor', 'at_window', False)
    print("--- Monkey Banana Problem Solver ---")
    print(f"Initial State: {START_STATE}")
    
    solution_path = monkey_banana_solver(START_STATE)
    
    if solution_path:
        print("\nSolution Path (Sequence of Actions):")
        for i, action in enumerate(solution_path):
            print(f"{i+1}. {action}")
        print("Goal Achieved!")
    else:
        print("\nCould not find a solution.")
