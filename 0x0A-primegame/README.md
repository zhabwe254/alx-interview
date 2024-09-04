0x0A-primegame
Prime Game
This project implements a solution to the Prime Game task, where two players, Maria and Ben, take turns choosing prime numbers from a set of consecutive integers. The player who cannot make a move loses the game.

Files
0-prime_game.py: the main Python script that implements the solution.
main_0.py: a test script that demonstrates how to use the isWinner function.
Usage
To use the solution, simply run the main_0.py script:

bash

Verify

Open In Editor
Edit
Copy code
./main_0.py
This will output the winner of the game for the given input.

Functions
The solution defines four functions:

is_prime(n): checks if a number n is prime.
remove_multiples(n, nums): removes multiples of n from the list of numbers nums.
play_round(n): plays a round of the game for a given n.
isWinner(x, nums): determines the winner of the game by playing multiple rounds.
Example
To test the solution, you can use the following example:

python

Verify

Open In Editor
Edit
Copy code
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
This should output Winner: Ben.

Author
GIDEON HABWE
