class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    # Base case: check if the user is directly in the group
    if user in group.get_users():
        return True

    # Recursive case: check if the user is in any subgroups
    for sub_group in group.get_groups():
        if is_user_in_group(user, sub_group):
            return True

    # If the user is not found in the group or any subgroups, return False
    return False

## include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

# Normal case where the user is in a nested group
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

parent.add_group(child)
child.add_group(sub_child)

sub_child.add_user("user1")

print(is_user_in_group("user1", parent))  # Expected output: True

# Edge case where the group is empty
empty_group = Group("empty")

print(is_user_in_group("user1", empty_group))  # Expected output: False

# Edge case where the user is not in any group
parent = Group("parent")
child = Group("child")

parent.add_group(child)

print(is_user_in_group("user1", parent))  # Expected output: False

# Edge case with deeply nested groups
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_sub_child = Group("subsubchild")

parent.add_group(child)
child.add_group(sub_child)
sub_child.add_group(sub_sub_child)

sub_sub_child.add_user("user1")

print(is_user_in_group("user1", parent))  # Expected output: True

# Edge case where the input is null
print(is_user_in_group(None, None))  # Expected output: False or an appropriate error message