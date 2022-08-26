# 1) Set the users variable to be an empty list
users = []

assert users == [], f"Expected 'users' to be [] but got: {repr(users)}"

# 2) Add 'kevin', 'bob', and 'alice' to the users list in that order without reassigning the variable.
users.append('kevin')
users.append('bob')
users.append('alice')

assert users == ['kevin', 'bob', 'alice'], f"Expected 'users' to be ['kevin', 'bob', 'alice'] but got: {repr(users)}"

# 3) Remove 'bob' from the users list without reassigning  the variable.

assert users == ['kevin', 'alice'], f"Expected 'users' to be ['kevin', 'alice'] but got: {repr(users)}"

# 4) Reverse the users list and assign the result to the 'rev_users'

assert rev_users == ['alice', 'kevin'], f"Expected 'rev_users' to be ['alice', 'kevin'] but got: {repr(rev_users)}"

# 5) Add user 'melody' to users where 'bob' used to be.