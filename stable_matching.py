def stableMatching(n, menPreferences, womenPreferences):
    unmarriedMen = [i for i in range(n)]
    manSpouse = [None for i in range(n)]
    womanSpouse = [None for i in range(n)]
    nextManChoice = [0 for i in range(n)]
    while unmarriedMen:
        man = unmarriedMen[0]
        his_preferences = menPreferences[man]
        woman = his_preferences[nextManChoice[man]]
        nextManChoice[man] += 1
        her_preferences = womenPreferences[woman]
        husb = womanSpouse[woman]
        if husb != None:
            if her_preferences.index(husb) > her_preferences.index(man):
                womanSpouse[woman], manSpouse[man] = man, woman
                unmarriedMen.append(husb)
                unmarriedMen.remove(man)
        else:
            womanSpouse[woman], manSpouse[man] = man, woman
            unmarriedMen.remove(man)
    return manSpouse


n = 4
menPreferences = [[0, 1, 3, 2], [0, 2, 3, 1], [1, 0, 2, 3], [0, 3, 1, 2]]
womenPreferences = [[3, 1, 2, 0], [3, 1, 0, 2], [0, 3, 1, 2], [1, 0, 3, 2]]

print(stableMatching(n, menPreferences, womenPreferences))
