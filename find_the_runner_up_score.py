if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # TODO: Fix the following

    winner = -102
    runner_up = -103

    for score in arr:
        if score >= winner:
            winner, runner_up = score, winner
        elif score >= runner_up:
            runner_up = score
    
    print(runner_up)