status = None
balance = 500.0
withdraw = 499.5

status = "Success" if balance >= withdraw  else "Fail"
print(f"{status}!")



status = None
balance = 500.0
withdraw = 600.0

status = "Success" if balance >= withdraw  else "Fail"
print(f"{status}!")