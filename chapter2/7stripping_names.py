# Laura Turner 6/30/2022
# Different variations on stripping extra spaces.

what_name = "     Mike Tyson     "
message = f"\n\tThe best boxer in the world is:\n {what_name}"
print(message)

what_name = "     Mike Tyson     "
message = f"\n\tThe best boxer in the world is:\n {what_name.lstrip()}"
print(message)

what_name = "     Mike Tyson     "
message = f"\n\tThe best boxer in the world is:\n {what_name.rstrip()}"
print(message)

what_name = "     Mike Tyson     "
message = f"\n\tThe best boxer in the world is:\n {what_name.strip()}"
print(message)
