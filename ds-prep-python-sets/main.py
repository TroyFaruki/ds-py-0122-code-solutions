trailmix = {"m&ms", "peanuts", "raisins"}
print(trailmix)
print("cashews" in trailmix)
print("peanuts" in trailmix)
trailmix.add("pretzels")
trailmix.update(["peanuts", "banana chips", "bits of jerky"])
print(trailmix)
trailmix.remove("m&ms")
trailmix.discard("raisins")
trailmix.discard("rat poisin")
print(trailmix)

nuts = {"peanuts", "cashews", "almonds", "walnuts", "pecans"}

nuts_in_both = nuts.intersection(trailmix)
print("nuts_in_both: ", nuts_in_both)

nuts_in_trailmix = nuts.union(trailmix)
print("nuts_in_trailmix: ", nuts_in_trailmix)

trailmix_not_in_nuts = trailmix.difference(nuts)
print("trailmix_not_in_nuts: ", trailmix_not_in_nuts)

nuts_not_in_trailmix = nuts.difference(trailmix)
print("Nuts Not in trailmix: ", nuts_not_in_trailmix)
