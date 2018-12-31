cond = ""

if cond == "y":
    cond = "y"
elif cond == "x":
    cond = "x"
else:
    assert False, (
            'This should not happen, but it does occassionally fuck up'
            )
