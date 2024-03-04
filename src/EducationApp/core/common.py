from django.db.models import QuerySet
from EducationApp.utils import query_debugger


@query_debugger
def distribute_pupiles_in_groups(groups: QuerySet, users: QuerySet) -> None:
    '''Dictribute pupiles, who has access to the particular product, into groups of a product.'''

    groups_number = groups.count()
    users_number = users.count()
    min_amount_per_group = users_number // groups_number
    r = min_amount_per_group * groups_number

    users = list(users)
    groups_of_users = [users[i:i+min_amount_per_group] for i in range(0, r, min_amount_per_group)]
    print(groups_of_users)


    for i in range(groups_number):
        groups[i].members.set(groups_of_users[i])

    remainder = users_number - min_amount_per_group * groups_number
    added_users = []
    [added_users.extend(user) for user in groups_of_users]

    remainder_users = [user for user in users if user not in added_users]
    if remainder_users:
        for i in range(remainder):
            groups[i].members.add(remainder_users[i])
