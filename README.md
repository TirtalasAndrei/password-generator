# Password Generator (Simple version)
This is a Python project that generates a random password based on the user input.

## How it works!
``import random`` first we import the random module to allow the computer to make a random choice for our lists.

1. We define three list ``list_letters`` - Contains a-z and A-Z, ``list_numbers`` - Contains 0-9, ``list_symbols`` - Contains special Characters (! $ &).

By implementing an InputFunction in our program, it will be more interactive, allowing the user to generate the password with as many letters, numbers, or symbols as they want.

2. Generating logic

We start with an empty string ``password``, here will be adding the letters, numbers and symbols and will print the entire password.
For that will using the ``for`` loop so we can iterate in lists and take some random characters from there and adding in our empty string.
After we iterate for each list and add characters in our string the code is finish.

### Remark!!!
This code is not very effective, because our password even though our user will choose his password to have a lot of characters it will still be a easy password to break through. Because we ask first for the letters and adding them in our string, after that we are asking for the numbers and same on, our password has an easy pattern (first will be the letters, then will be the numbers and after that will be symbols) so for this reason is easy to break through. We need to shuffle with the characters in our password to be stronger!


# Password Generator (More Complex)
First we change the empty string into a list because we know that in a list has a colection of sets that are mutable, that means that we can shuffle our characters in it.
So for this we need a vid list ``password_list = []``

## Logical Part
We change the structure of the ``for`` loop now we need to use the ``.append()`` attribute so that we can add characters in our list. After we repeat the same thing for the last two loops we are gooing to use the ``random.shuffle()`` method so our password is not having the same pattern. 

Now if we ``print(password_list)`` we are going to see that our password is in a list with random set of characters in it. It's good that our shaffle method work, but now we need to convert the list into a string.

For that we are going to crate again the same empty string ``password = ""`` and make a ``for`` loop where our characters can be added from list in a string.