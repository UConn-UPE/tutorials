#lists

workers = ["Micheal", "Jim", "Pam", "Creed"]

print(workers)

#-------------------------------------------------------------------------
workers = ["Micheal", "Jim", "Pam", "Creed"]

print(len(workers))

#-------------------------------------------------------------------------
workers = ["Micheal", "Jim", "Pam", "Creed"]

print(workers[0])

#-------------------------------------------------------------------------
workers = ["Micheal", "Jim", "Pam", "Creed"]

print(workers[3])

#-------------------------------------------------------------------------
workers = ["Micheal", "Jim", "Pam", "Creed"]

print(workers[-1])

#-------------------------------------------------------------------------
workers = ["Micheal", "Jim", "Pam", "Creed"]

print(workers[0:2])

#-------------------------------------------------------------------------
workers = ["Micheal", "Jim", "Pam", "Creed"]

print(workers[:2])

#-------------------------------------------------------------------------
workers = ["Micheal", "Jim", "Pam", "Creed"]

print(workers[2:])

#-------------------------------------------------------------------------
workers = ["Micheal", "Jim", "Pam", "Creed"]

workers.append("Kevin")

print(workers)

#-------------------------------------------------------------------------
workers = ["Micheal", "Jim", "Pam", "Creed"]

workers.insert(0, "Kevin")

print(workers)

# add kevin spilling chili
#-------------------------------------------------------------------------
workers = ["Micheal", "Jim", "Pam", "Creed"]
workers_2 = ["Angela", "Oscar"]

workers.insert(0, workers_2)

print(workers)
print(workers[0])

#-------------------------------------------------------------------------
workers = ["Micheal", "Jim", "Pam", "Creed"]

workers[1] = "Oscar"

print(workers)

#-------------------------------------------------------------------------
workers = ["Micheal", "Jim", "Pam", "Creed"]
workers_2 = ["Angela", "Oscar"]

workers.extend(0, workers_2)

print(workers)

#-------------------------------------------------------------------------
workers = ["Micheal", "Jim", "Pam", "Creed"]

workers.remove("Creed")

print(workers)

#-------------------------------------------------------------------------
workers = ["Micheal", "Jim", "Pam", "Creed"]

workers.reverse()

print(workers)

#-------------------------------------------------------------------------
workers = ["Micheal", "Jim", "Pam", "Creed"]

nums = [2,3,5,1,4]

workers.sort()
nums.sort()

print(workers)
print(nums)

#-------------------------------------------------------------------------
workers = ["Micheal", "Jim", "Pam", "Creed"]
nums = [2,3,5,1,4]

sorted_workers = sorted(workers)

print(workers)
print(sorted_workers)

#-------------------------------------------------------------------------
workers = ["Micheal", "Jim", "Pam", "Creed"]
nums = [2,3,5,1,4]

print(min(nums))
print(max(nums))

#-------------------------------------------------------------------------
workers = ["Micheal", "Jim", "Pam", "Creed"]

print(workers.index("Pam"))

#-------------------------------------------------------------------------
workers = ["Micheal", "Jim", "Pam", "Creed"]

print("Pam" in workers)
print("Kevin" in workers)

#-------------------------------------------------------------------------
workers = ["Micheal", "Jim", "Pam", "Creed"]

for worker in workers:
    print(worker)

#-------------------------------------------------------------------------
workers = ["Micheal", "Jim", "Pam", "Creed"]

worker_str = ", ".join(workers)

print(worker_str)

new_list = worker_str.split(", ")

print(new_list)

#-------------------------------------------------------------------------
# tuples, use for values that you know won't

workers_tup = ("Micheal", "Jim", "Pam", "Creed")

print(workers_tup)
print(workers_tup[1])

#-------------------------------------------------------------------------
workers_tup = ("Micheal", "Jim", "Pam", "Creed")

workers_tup[1] = "Oscar"

#-------------------------------------------------------------------------
# sets, for values that are unordered and no duplicates

workers_set = {"Micheal", "Jim", "Pam", "Creed"}

print(workers_set)

print(workers_set)

#-------------------------------------------------------------------------
workers_set = {"Micheal", "Jim", "Pam", "Creed"}

print("Jim" in workers_set)

#-------------------------------------------------------------------------
workers_set = {"Micheal", "Jim", "Pam", "Creed"}
workers_2_set = {"Micheal", "Jim", "Pam", "Oscar", "Angela", "Creed"}

print(workers_set.difference(workers_2_set))
print(workers_set.union(workers_2_set))

#-------------------------------------------------------------------------
# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()