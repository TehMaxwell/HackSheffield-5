# HackSheffield5
A repository for the code our team wrote at Hack Sheffield 5.

## Sheffield Blackjack Rules
- Each player is dealt 2 cards **face-down**.
- A player's turn consists of either sticking or twisting:
	- Stick = the player is dealt no more cards, and their current total is now considered their final total. The player who has stuck closest to 21 wins.
	- Twist = the player is dealt as many **face-up** cards as they desire.
- If, at any point, a player exceeds 21, they are **bust** and are automatically out of contention for a win.
- There is a win counter per player, but this bears no statistical weight.
- When all players have either stuck or become bust, a showdown occurs at the end where all face-down cards are revealed:
	- **The player closest to 21 wins.**
	- In the event of a tie, the player who has been dealt the most amount of cards wins. If this is the same for 2 players, a draw is declared.
