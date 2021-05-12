# Question #5
# If this code were run, what would the output to the console?

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

copy_cats = cats.copy()

cats.pop()

assert len(copy_cats) == len(cats), "Should match"
