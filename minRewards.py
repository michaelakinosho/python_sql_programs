# Credit: source of solution is AlgoExpert provided solution
def minRewards(scores):
    rewards = [1 for _ in scores]
    # print(f"printing rewards list {rewards}")
    # Moving from left to right in array
    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i - 1] + 1

    # Moving from right to left in array
    for i in reversed(range(len(scores) - 1)):
        #print(f"Position of index from right to left {i}")
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)
    return sum(rewards)

minRewards([1,2,3,4])