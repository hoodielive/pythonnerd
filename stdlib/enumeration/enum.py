import enum 

class BugStatus(enum.Enum):
    new = 7 
    incomplete = 6
    invalid = 5
    wont_fix = 4 
    in_progress = 3
    fix_committed = 2 
    fix_released = 1 

print('\n Member name: {}'.format(BugStatus.wont_fix.name))
print('\n Member name: {}'.format(BugStatus.wont_fix.value))
