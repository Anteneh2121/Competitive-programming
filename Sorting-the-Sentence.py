class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        dic = {}
        for i in words:
            dic[i[-1]] = i[:-1]
        return ' '.join([dic[j] for j in sorted(dic)])
