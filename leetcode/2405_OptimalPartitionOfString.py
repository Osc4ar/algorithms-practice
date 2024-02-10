class Solution:
    def partition string(self, s: str) -> int:
        current_partition = set()
        partitions = 1

        for c in s:
            if c in current_partition:
                current_partition.clear()
                partitions += 1
            current_partitions.add(c)

        return partitions
