# Leetcode 1169

def invalidTransactions(self, transactions: List[str]) -> List[str]:
    self.transactions_map = defaultdict(dict)
    results = []

    # storing all the transactions in a dictionary, wrt time, name and then city

    for vals in transactions:
        name, time, amount, city = vals.split(',')
        time = int(time)

        if name not in self.transactions_map[time]:
            self.transactions_map[time][name] = {city}

        else:
            self.transactions_map[time][name].add(city)

    # going through all the transactions to check for invalid ones
    for vals in transactions:
        name, time, amount, city = vals.split(',')
        time = int(time)

        if int(amount) > 1000:
            results.append(vals)
            continue

        for t in range(time - 60, time + 61):
            if name in self.transactions_map[t]:
                if city not in self.transactions_map[t][name] or len(self.transactions_map[t][name]) > 1:
                    results.append(vals)
                    break
    return results
