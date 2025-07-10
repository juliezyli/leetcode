def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse=True)
        rank = {sorted_scores[i]: str(i + 1) for i in range(len(score))}
        rank[sorted_scores[0]] = "Gold Medal"
        if len(score) > 1: 
            rank[sorted_scores[1]] = "Silver Medal"
        if len(score) > 2:
            rank[sorted_scores[2]] = "Bronze Medal"
        return [rank[s] for s in score]