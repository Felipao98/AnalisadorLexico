from collections import defaultdict

grammar = {
    "E": [["T", "E'"]],
    "E'": [["+", "T", "E'"], ["ε"]],
    "T": [["F", "T'"]],
    "T'": [["*", "F", "T'"], ["ε"]],
    "F": [["(", "E", ")"], ["id"]]
}

terminals = set()
non_terminals = set(grammar.keys())
first = defaultdict(set)
follow = defaultdict(set)

# terminais
for productions in grammar.values():
    for prod in productions:
        for symbol in prod:
            if symbol not in grammar and symbol != "ε":
                terminals.add(symbol)

def compute_first(symbol):
    if symbol in terminals or symbol == "ε":
        return {symbol}
    if symbol in first and first[symbol]:
        return first[symbol]

    for production in grammar[symbol]:
        for sym in production:
            sym_first = compute_first(sym)
            first[symbol].update(sym_first - {"ε"})
            if "ε" not in sym_first:
                break
        else:
            first[symbol].add("ε")
    return first[symbol]

def compute_follow():
    follow["E"].add("$") 
    updated = True
    while updated:
        updated = False
        for lhs, productions in grammar.items():
            for prod in productions:
                trailer = follow[lhs].copy()
                for symbol in reversed(prod):
                    if symbol in non_terminals:
                        before = follow[symbol].copy()
                        follow[symbol].update(trailer)
                        if "ε" in first[symbol]:
                            trailer.update(first[symbol] - {"ε"})
                        else:
                            trailer = first[symbol]
                        updated |= follow[symbol] != before
                    else:
                        trailer = compute_first(symbol)

for nonterm in grammar:
    compute_first(nonterm)

deferred = compute_follow()

table = defaultdict(dict)
for A in grammar:
    for prod in grammar[A]:
        first_set = set()
        for symbol in prod:
            symbol_first = compute_first(symbol)
            first_set.update(symbol_first - {"ε"})
            if "ε" not in symbol_first:
                break
        else:
            first_set.add("ε")

        for terminal in first_set:
            if terminal != "ε":
                table[A][terminal] = prod
        if "ε" in first_set:
            for terminal in follow[A]:
                table[A][terminal] = prod

print("\nFIRST:")
for k, v in first.items():
    print(f"FIRST({k}) = {v}")

print("\nFOLLOW:")
for k, v in follow.items():
    print(f"FOLLOW({k}) = {v}")

print("\nTabela M:")
for nt in table:
    for t in table[nt]:
        print(f"M[{nt}, {t}] = {table[nt][t]}")
