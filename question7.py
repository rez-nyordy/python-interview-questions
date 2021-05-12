# Question #8
# If this code were run, what would the outcome be?

cats = list(({
                 "breed": "Tortoise Shell",
                 "weight_kg": 4.22,
                 "name": "Oscar"
             },
             {
                 "breed": "Persian",
                 "weight_kg": 3.78,
                 "name": "Felix"
             }))

cats.append({
    "Sparky",
    "British Shorthair",
    6.33
})

copy_cats = cats

cats.pop()

assert len(copy_cats) == len(cats), "Should match"
