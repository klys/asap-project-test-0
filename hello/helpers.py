import random
# generate ID using 5 first letters of the last name plus first 2 letter of name plus dash and 7 random numbers
def generate_id(first_name, last_name):
    return last_name[:5].upper() + first_name[:2].upper() + '-' + str(random.randint(1, 10000000))

# check that ID is unique on postgres
def check_id(member_id):
    if Member.objects.filter(member_id=member_id).exists():
        return False
    else:
        return True