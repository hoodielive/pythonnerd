from collections import deque 

self._chanages = deque(maxlen=2)

def _caculate(self, change):
    if change not in self._changes:
        self._changes.append(change)
    compute = {'rate', 'time', 'distance'} - set(self._changes)
