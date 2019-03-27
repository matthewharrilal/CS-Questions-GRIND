class Solution(object):
    # DFS code for traversing accounts.
    def dfs(self,current_account, unique_emails, visited_accounts, accounts, emails_accounts_map):
        if visited_accounts[current_account]: # If our neighbor has already been visited Neighbor/Current Account is the index
            return  # Meaning that another account already contains this email
        
        visited_accounts[current_account] = True  # Mark the current account we are on as true
        for j in range(1, len(accounts[current_account])):  # Given the neighbor then we go to that index in the accounts matrix if the account hasn't already been visited
            
            email = accounts[current_account][j] 
            unique_emails.add(email)  # Email wont get added if it is not unique. Why do we need to keep track of this Used for the output when printing all the emails belonging to a single account
            
            
            # So we are using the neighbor index in the adjacency list to be able to subscript the specific account in the accounts subarrary
            for neighbor in emails_accounts_map[email]: # For each account position that contains the email that we are on
                # How is this recursive call working ? Visit the next account subarray if it hasn't been visited 
                self.dfs(neighbor, unique_emails, visited_accounts, accounts, emails_accounts_map)
                
    def accountsMerge(self, accounts):
        from collections import defaultdict
        visited_accounts = [False] * len(accounts)  # Not using vertex nodes therefore keeping track of visited status using external array
        emails_accounts_map = defaultdict(list)  # Purpose is used to create the adjacency list
        res = []
        
        # Build up the graph. ADJACENCY LIST OF EMAILS
        for i, account in enumerate(accounts): # Each account in the list of accounts
            
            for j in range(1, len(account)):  # Every element after the name inside the account
                email = account[j] # For each email in the account
                emails_accounts_map[email].append(i)
                
        print(emails_accounts_map)
        # Perform DFS for accounts and add to results.  HAVE TO UNDERSTAND THIS FIRST 
        for current_account, account in enumerate(accounts):
            if visited_accounts[i]: # If the account has already been marked as visited we don't need to visit it again
                continue
                
            name, unique_emails = account[0], set() # Create a set of unique emails
            self.dfs(current_account, unique_emails, visited_accounts, accounts, emails_accounts_map)
            res.append([name] + sorted(unique_emails))
        return res