def minCosts(self, cost: List[int]) -> List[int]:
        answer = []
        for i in range(len(cost)):
            swap_cost = min(cost[:i + 1])
            indiv_cost = cost[i]
            answer.append(min(indiv_cost, swap_cost))
        return answer