def showRange(min, max = None):
    if max is None:
        rangeStr = f'(at least {str(min)})'
    else:
        rangeStr = f'({str(min)} - {str(max)})'
    return rangeStr

def make_selection(prompt, options):
    msg = (f"Please select {prompt}\n")
    for i, name in enumerate(options, start=1):
        msg += (f"{i} {name}\n")
    msg += (f"{showRange(1,i)} or 0 to quit: ")
    return msg

