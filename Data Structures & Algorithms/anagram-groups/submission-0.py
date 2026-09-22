class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for words in strs:
            counts = [0] * 26

            for s in words:
                counts[ord(s) - ord("a")] += 1

            groups[tuple(counts)].append(words)

        return list(groups.values())


