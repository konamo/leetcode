import collections

class UF:
    def __init__(self, N):
        self.parents = list(range(N))
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]


class Solution:
    # union-find
    def accountsMerge2(self, accounts: list[list[str]]) -> list[list[str]]:
        ans = [None] * len(accounts)
        merge = {}
        self.u = [ii for ii in range(len(accounts))]

        for ii in range(len(accounts)):
            for jj in range(1, len(accounts[ii])):
                if accounts[ii][jj] in merge:
                    self.union(merge[accounts[ii][jj]], ii)
                else:
                    merge[accounts[ii][jj]] = ii

        for ii in range(len(accounts)):
            root = self.find(ii)
            if ans[root]:
                ans[root] += accounts[ii][1:]
            else:
                ans[root] = accounts[ii]

        ret = []
        for ii in range(len(ans)):
            if ans[ii]:
                ret.append([ans[ii][0]] + sorted(set(ans[ii][1:])))
        return ret

    def union(self, a, b):
        self.u[self.find(b)] = self.find(a)

    def find(self, a):
        while self.u[a] != a:
            a = self.u[a]
        return a


    # connect account number and dfs
    def accountsMerge3(self, accounts: list[list[str]]) -> list[list[str]]:
        graph = {}
        for ii in range(len(accounts)):
            for jj in range(1, len(accounts[ii])):
                graph[accounts[ii][jj]] = graph.get(accounts[ii][jj], []) + [ii]

        def dfs(node, emails):
            if visited[node]:
                return

            visited[node] = True

            for email in accounts[node][1:]:
                emails.add(email)
                for next in graph[email]:
                    dfs(next, emails)
            return

        visited = [False] * len(accounts)
        res = []
        for ii in range(len(accounts)):
            if not visited[ii]:
                emails = set()
                dfs(ii, emails)
                res.append([accounts[ii][0]] + sorted(emails))

        return res
    
    # connect emails and dfs
    def accountsMerge4(self, accounts: list[list[str]]) -> list[list[str]]:
        G, seen, ans = defaultdict(list), set(), []

        for acc in accounts:
            for i in range(2,len(acc)):
                G[acc[i]].append(acc[i-1])
                G[acc[i-1]].append(acc[i])

        def dfs(email):
            seen.add(email)
            emailList = [email]
            for E in G[email]:
                if E not in seen:
                    emailList += dfs(E)
            return emailList

        for acc in accounts:
            if acc[1] not in seen:
                ans.append([acc[0]] + sorted(dfs(acc[1])))
        return ans 

    # union-find
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        uf = UF(len(accounts))
        
        # Creat unions between indexes
        ownership = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i, ownership[email])
                else:
                    ownership[email] = i
        
        # Append emails to correct index
        ans = collections.defaultdict(list)
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]



def main():
    s = Solution()
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    print(s.accountsMerge(accounts))

    accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
    print(s.accountsMerge(accounts))

    accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
    print(s.accountsMerge(accounts))

    accounts = [["David","David0@m.co","David4@m.co","David3@m.co"],["David","David5@m.co","David5@m.co","David0@m.co"],["David","David1@m.co","David4@m.co","David0@m.co"],["David","David0@m.co","David1@m.co","David3@m.co"],["David","David4@m.co","David1@m.co","David3@m.co"]]
    print(s.accountsMerge(accounts))


    return



if __name__ == '__main__':
    main()
