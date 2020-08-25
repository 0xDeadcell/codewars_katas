def find_short(s):
    ''' the sorted key arguments lets us find the shortest word using lambda '''
    shortest_words = sorted(s.split(), key=lambda x: len(x))
    return len(shortest_words[0])

