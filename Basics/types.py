def type_of(value):
    return(f"type of {value} is {value.__class__.__name__}.")

print(type_of('hello world'))
print(type_of(1))
print(type_of(1.0))
print(type_of(True))
print(type_of([]))
print(type_of({}))
print(type_of(()))

# print(type('hello world'))

# this is a bad exercise for a couple of reasons:
# Copy and pasting a function and play around is not a good exercise, especially when that function is beyond the comprehension of this point in the course. Dunder methods have not been explained.
# As shown above type() is itself already a function that does the same thing as your type_of() function.
# My recomendation is that in all exercises you make, you provide a goal to achieve. Ohterwise it doesn't really function properly as an exercise.
# Play around is something someone enthusiastic will do anyway but in providing exercises you're supposed to give a framework in which someone can see how what you've explained is useful.