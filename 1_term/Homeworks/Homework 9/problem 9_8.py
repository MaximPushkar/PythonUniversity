def language_lexical_order(n):
    if n == 1:
        return ["a"]
    elif n == 2:
        return [["a", "b"], ["b", "a"]]
    else:
        t = language_lexical_order(n-1)
        ans = []
        for i in range(0, n):
            adding = chr(ord("a")+n-1)
            for q in t:
                w = q[::]
                w[i: i] += [adding]
                ans.append(w)
        return ans[::-1]


print(language_lexical_order(3))
