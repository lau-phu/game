/* OOP demonstration using C++
this is a simple rock, paper, scissor game where player and computer each have 3 lives
the loser lose 1 life and when your life reachs 0, you lose the game.

the OOP concepts were demonstrated as follows

Inheritance: The HumanPlayer and ComputerPlayer classes are derived from the base Player class, inheriting its properties and methods.

Encapsulation: The member variables in the Player class (name and health) are encapsulated and accessed through getter and setter methods to control their visibility and provide data abstraction.

Polymorphism: The attack method in the base Player class is declared as a pure virtual function, making it an abstract method. The derived classes (HumanPlayer and ComputerPlayer) override this method, providing their own implementation of the attack behavior.

Abstraction: The Player class serves as an abstraction for the common properties and behaviors of players. It provides a common interface (attack method) that can be used to interact with players without knowing their specific types.
*/

#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

using namespace std;

// Base class representing a player
class Player {
protected:
    string name;
    int health;

public:
    Player(const string& playerName) : name(playerName), health(3) {}

    string getName() const {
        return name;
    }

    int getHealth() const {
        return health;
    }

    void setHealth(int newHealth) {
        health = newHealth;
    }

    virtual void attack(Player& other) = 0;
};

// Derived class representing a human player
class HumanPlayer : public Player {
public:
    HumanPlayer(const string& playerName) : Player(playerName) {}

    void attack(Player& other) override {
        cout << name << ", choose your move (1 = Rock, 2 = Paper, 3 = Scissors): ";
        int choice;
        cin >> choice;

        int computerChoice = rand() % 3 + 1;

        cout << name << " chose ";
        switch (choice) {
            case 1:
                cout << "Rock";
                break;
            case 2:
                cout << "Paper";
                break;
            case 3:
                cout << "Scissors";
                break;
            default:
                cout << "Invalid choice";
                return;
        }
        cout << ". " << other.getName() << " chose ";
        switch (computerChoice) {
            case 1:
                cout << "Rock";
                break;
            case 2:
                cout << "Paper";
                break;
            case 3:
                cout << "Scissors";
                break;
        }

        cout << endl;

        if (choice == computerChoice) {
            cout << "It's a tie!\n";
        } else if ((choice == 1 && computerChoice == 3) ||
                   (choice == 2 && computerChoice == 1) ||
                   (choice == 3 && computerChoice == 2)) {
            cout << name << " wins!\n";
        } else {
            cout << other.getName() << " wins!\n";
            other.setHealth(other.getHealth() - 1);
        }
    }
};

// Derived class representing a computer player
class ComputerPlayer : public Player {
public:
    ComputerPlayer(const string& playerName) : Player(playerName) {}

    void attack(Player& other) override {
        int choice = rand() % 3 + 1;

        cout << name << " chose ";
        switch (choice) {
            case 1:
                cout << "Rock";
                break;
            case 2:
                cout << "Paper";
                break;
            case 3:
                cout << "Scissors";
                break;
        }
        cout << ". ";

        int humanChoice;
        cout << other.getName() << ", choose your move (1 = Rock, 2 = Paper, 3 = Scissors): ";
        cin >> humanChoice;

        cout << other.getName() << " chose ";
        switch (humanChoice) {
            case 1:
                cout << "Rock";
                break;
            case 2:
                cout << "Paper";
                break;
            case 3:
                cout << "Scissors";
                break;
            default:
                cout << "Invalid choice";
                return;
        }

        cout << endl;

        if (choice == humanChoice) {
            cout << "It's a tie!\n";
        } else if ((choice == 1 && humanChoice == 3) ||
                   (choice == 2 && humanChoice == 1) ||
                   (choice == 3 && humanChoice == 2)) {
            cout << name << " wins!\n";
        } else {
            cout << other.getName() << " wins!\n";
            other.setHealth(other.getHealth() - 1);
        }
    }
};

// Game class
class Game {
    Player* player1;
    Player* player2;

public:
    Game(Player* p1, Player* p2) : player1(p1), player2(p2) {}

    void play() {
        while (player1->getHealth() > 0 && player2->getHealth() > 0) {
            player1->attack(*player2);
            player2->attack(*player1);

            cout << "Health: " << player1->getName() << ": " << player1->getHealth() << " "
                 << player2->getName() << ": " << player2->getHealth() << "\n";
        }

        cout << "Game Over!\n";
        if (player1->getHealth() > 0) {
            cout << player1->getName() << " wins!\n";
        } else if (player2->getHealth() > 0) {
            cout << player2->getName() << " wins!\n";
        } else {
            cout << "It's a tie!\n";
        }
    }
};

int main() {
    srand(time(0));

    string playerName;
    cout << "Enter your name: ";
    cin >> playerName;

    Player* humanPlayer = new HumanPlayer(playerName);
    Player* computerPlayer = new ComputerPlayer("Computer");

    Game game(humanPlayer, computerPlayer);
    game.play();

    delete humanPlayer;
    delete computerPlayer;

    return 0;
}