def tsp(graph):
    N = len(graph)
    dp = [[None]*(1<<N) for _ in range(N)]
    VISITED_ALL = (1<<N) - 1
    INF = int(1e9)

    def find_path(last, visited):
        if visited == VISITED_ALL:
            return graph[last][0] or INF

        if dp[last][visited]:
            return dp[last][visited]
        
        tmp = INF
        for n_city in range(N):
            if visited & (1<<n_city) == 0 and graph[last][n_city] != 0:
                tmp = min(tmp, find_path(n_city, visited | (1<<n_city))+graph[last][n_city])
        dp[last][visited] = tmp
        return tmp
    return find_path(0, 1<<0)