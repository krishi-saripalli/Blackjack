# Blackjack
Simple CLI version of Blackjack
## Instructions
To run the program, make sure you are in the "Blackjack" directory. You don't need any dependencies other than ```random``` which should come with python3.
Simply run the command ```python3 blackjack.py ```
## Assumptions
Some base assumptions I made about the game were that the time complexity of operations was not the main priorirty when querying for information like the output of a player's hand, which is why I simply loop through the hand each time instead of storing that information each time I query.

Other assumptions included the inability to look at your own hand via a command, or reverse previous moves.

## Design Choices
I chose to implement an object-oriented style game as the different aspects of Blackjack (the cards, players and deck) are somewhat insular. That is, their basic functionalities can be modelled independently of each other and instead, encapsulated within individual classes!

As such, I have a ```Card```,```Deck```, and ```Player``` class to represent these aspects of the game. Probably most challenging was dealing with ace calculations, which I did by treating the aces as an 11 and subtracting a 10 from the player's sum while they were at risk of busting.

## Tradeoffs
As a result of writing the main logic in the ```blackjack.py``` script, **unit testing** was much harder than I anticipated, as I was not able to call methods on my objects, since most of the methods that orchestrated the game were found in the script. I also had to focus on correct implementation in the alloted time, which coupled with the preivous challenged, left little room for testing.

The subtracting algorithim for aces is also pretty inefficient, since we have to do multiple operations everytime we encounter a potential bust (score> 21)

## Manual Testing
Manual testing ranged from checking that busts were in fact recorded and a result, the game was exited, to making sure that card draws were indeed random. Other manual testing included making sure that the only accepted inputs from the user were either (H) or (S) and that any other input required a retry.

## Unit Tests
My one unit test is in the ```test.py``` file, which you can run using ```python3 test.py ```
