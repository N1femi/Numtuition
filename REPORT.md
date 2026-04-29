# Project Report

My selected project was a number guesser where the user has unlimited attempts to guess the number.

Their only hints are implied by the program's reponses when the user inputs a number, either "Too High" or "Too Low".

To make sure input is valid, I have a check implemented in the program like so:

```python
if nerves_left <= 0:
            print("\n All I require are numbers, NUMBERS!! IS THAT TOO MUCH TO ASK? \n")
            break
```

I also made sure to make my variables semantic so if it was worked on by others, they would have some reasonable level of intuition when interacting with the code.

Finally, I made sure to use proper conventions that are in practice with many people. This way it reduces the amount of confusion if new persons were to be involved with this project.