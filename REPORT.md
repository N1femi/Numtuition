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

This project matters because it hints towards the real application of the programming logic I've been building throughout CMPSC 131 & 132. 

To be more technical, how this program works is pretty straightforward. The program starts by asking the user to guess the number. After the user successfully geusses the program prompts the user to play again, it accepts a variety of words synonymously used as yes to play the game again. This is done with a `while True:` loop.

Then when invalid inputs are given 3 times the program restarts with a new number to guess.

One of the main challenges was figuring out how to loop the cycle of:

1. Recieving Input
2. Validating it
3. Outputting Response

At first I thought I may have had to use a toggle variable that kept everything in check. But after brainstorming longer, I found that I could take a more embedded approach and incorporate it into a loop.

For future work, I will definitely keep in mind to brainstorm and scaffold ideas before finally implementing them.