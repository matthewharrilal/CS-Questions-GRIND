class Solution(object):
    # DFS code for traversing accounts.
    def dfs(self,current_account, unique_emails, visited_accounts, accounts, emails_accounts_map):
        if visited_accounts[current_account]:
            return
        
        visited_accounts[current_account] = True  # Mark the
        for j in range(1, len(accounts[current_account])):
            email = accounts[current_account][j] 
            unique_emails.add(email)  # Email wont get added if it is not unique
            
            for neighbor in emails_accounts_map[email]: # For each account position that contains the email that we are on
                
                # How is this recursive call working ? Visit the next account subarray if it hasn't been visited 
                self.dfs(neighbor, unique_emails, visited_accounts, accounts, emails_accounts_map)
                
    def accountsMerge(self, accounts):
        from collections import defaultdict
        visited_accounts = [False] * len(accounts)
        emails_accounts_map = defaultdict(list)
        res = []
        
        # Build up the graph. ADJACENCY LIST OF EMAILS
        for i, account in enumerate(accounts): # Each account in the list of accounts
            for j in range(1, len(account)):
                email = account[j] # For each email in the account
                emails_accounts_map[email].append(i)
                
       
        # Perform DFS for accounts and add to results.  HAVE TO UNDERSTAND THIS FIRST 
        for current_account, account in enumerate(accounts):
            if visited_accounts[i]: # If the account has already been marked as visited we don't need to visit it again
                continue
                
            name, unique_emails = account[0], set() # Create a set of unique emails
            self.dfs(current_account, unique_emails, visited_accounts, accounts, emails_accounts_map)
            res.append([name] + sorted(emails))
        return res