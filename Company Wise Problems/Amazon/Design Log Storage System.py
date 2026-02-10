'''
Problem Summary
You need to design a system that:
Stores logs with id and timestamp
Retrieves log IDs within a time range, based on a granularity
exapmle: Year    → 4
Month   → 7
Day     → 10
Hour    → 13
Minute  → 16
Second  → 19

2017:01:01:23:59:59
'''
class LogSystem:

    def __init__(self):
        self.logs = []
        self.g = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19
        }

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str):
        idx = self.g[granularity]
        start = start[:idx]
        end = end[:idx]
        res = []

        for id, time in self.logs:
            t = time[:idx]
            if start <= t <= end:
                res.append(id)

        return res
