
# Tic Tac Toe Design

This document details the low-level design (LLD) for a **Tic Tac Toe** system that supports multiplayer instances running in parallel using **modern C++**.

---

## **Low-Level Design**

### **Classes**

1. **Player**
   - Represents a player in the game.
2. **GameBoard**
   - Manages the Tic Tac Toe board and game state.
3. **TicTacToeGame**
   - Handles game logic and interactions between players and the game board.
4. **GameManager**
   - Manages multiple game instances and allows them to run in parallel.

---

## **Class Definitions**

### **Player**
Represents a player in the game.

```cpp
#ifndef PLAYER_H
#define PLAYER_H

#include <string>

class Player 
{
private:
    std::string name;
    char symbol; // 'X' or 'O'

public:
    Player(const std::string& playerName, char playerSymbol);

    std::string getName() const;
    char getSymbol() const;
};

#endif // PLAYER_H
```

---

### **GameBoard**
Manages the game board and checks for game status.

```cpp
#ifndef GAMEBOARD_H
#define GAMEBOARD_H

#include <vector>
#include <string>

class GameBoard 
{
private:
    std::vector<std::vector<char>> board;
    int size;

public:
    GameBoard(int boardSize = 3);
    void displayBoard() const;
    bool makeMove(int row, int col, char symbol);
    bool isFull() const;
    char checkWinner() const;
};

#endif // GAMEBOARD_H
```

---

### **TicTacToeGame**
Handles the game logic and interaction between players.

```cpp
#ifndef TICTACTOEGAME_H
#define TICTACTOEGAME_H

#include "Player.h"
#include "GameBoard.h"
#include <mutex>

class TicTacToeGame 
{
private:
    GameBoard gameBoard;
    Player player1;
    Player player2;
    Player* currentPlayer;
    std::mutex gameMutex;

public:
    TicTacToeGame(const Player& p1, const Player& p2);
    void playGame();
    bool handleTurn();
};

#endif // TICTACTOEGAME_H
```

---

### **GameManager**
Manages multiple game instances and allows them to run in parallel.

```cpp
#ifndef GAMEMANAGER_H
#define GAMEMANAGER_H

#include "TicTacToeGame.h"
#include <vector>
#include <thread>

class GameManager 
{
private:
    std::vector<std::thread> gameThreads;

public:
    void startGame(const Player& p1, const Player& p2);
    void waitForGamesToFinish();
};

#endif // GAMEMANAGER_H
```

---

## **Class Implementation**

### **Player Implementation**
```cpp
#include "Player.h"

Player::Player(const std::string& playerName, char playerSymbol) 
    : name(playerName), symbol(playerSymbol) {}

std::string Player::getName() const 
{
    return name;
}

char Player::getSymbol() const 
{
    return symbol;
}
```

---

### **GameBoard Implementation**
```cpp
#include "GameBoard.h"
#include <iostream>

GameBoard::GameBoard(int boardSize) : size(boardSize), board(boardSize, std::vector<char>(boardSize, ' ')) {}

void GameBoard::displayBoard() const 
{
    for (const auto& row : board) 
	{
        for (char cell : row) 
		{
            std::cout << (cell == ' ' ? '.' : cell) << " ";
        }
        std::cout << std::endl;
    }
}

bool GameBoard::makeMove(int row, int col, char symbol) 
{
    if (row < 0 || col < 0 || row >= size || col >= size || board[row][col] != ' ') 
	{
        return false;
    }
    board[row][col] = symbol;
    return true;
}

bool GameBoard::isFull() const 
{
    for (const auto& row : board) 
	{
        for (char cell : row) 
		{
            if (cell == ' ') return false;
        }
    }
    return true;
}

char GameBoard::checkWinner() const 
{
    // Check rows and columns
    for (int i = 0; i < size; ++i) 
	{
        if (board[i][0] != ' ' && std::all_of(board[i].begin(), board[i].end(), [this, i](char c) { return c == board[i][0]; }))
            return board[i][0];

        if (board[0][i] != ' ' && std::all_of(board.begin(), board.end(), [this, i](const std::vector<char>& row) { return row[i] == board[0][i]; }))
            return board[0][i];
    }

    // Check diagonals
    if (board[0][0] != ' ' && std::all_of(board.begin(), board.end(), [this](const std::vector<char>& row) 
	{
        static int diagIndex = 0; return row[diagIndex++] == board[0][0];
    })) return board[0][0];

    if (board[0][size - 1] != ' ' && std::all_of(board.begin(), board.end(), [this](const std::vector<char>& row) 
	{
        static int diagIndex = size - 1; return row[diagIndex--] == board[0][size - 1];
    })) return board[0][size - 1];

    return ' '; // No winner
}
```

---

### **TicTacToeGame Implementation**
```cpp
#include "TicTacToeGame.h"
#include <iostream>

TicTacToeGame::TicTacToeGame(const Player& p1, const Player& p2)
    : player1(p1), player2(p2), currentPlayer(&player1) {}

void TicTacToeGame::playGame() 
{
    while (true) 
	{
        std::lock_guard<std::mutex> lock(gameMutex);

        gameBoard.displayBoard();
        if (!handleTurn()) continue;

        char winner = gameBoard.checkWinner();
        if (winner != ' ') {
            std::cout << currentPlayer->getName() << " wins!";
            break;
        }

        if (gameBoard.isFull()) 
		{
            std::cout << "It's a draw!";
            break;
        }

        currentPlayer = (currentPlayer == &player1) ? &player2 : &player1;
    }
}
bool TicTacToeGame::handleTurn() 
{
    int row, col;
    std::cout << currentPlayer->getName() << " (" << currentPlayer->getSymbol() << ") - Enter row and column: ";
    std::cin >> row >> col;

    if (!gameBoard.makeMove(row, col, currentPlayer->getSymbol())) 
	{
        std::cout << "Invalid move, try again!";
        return false;
    }
    return true;
}
```

---

### **GameManager Implementation**
```cpp
#include "GameManager.h"

void GameManager::startGame(const Player& p1, const Player& p2) 
{
    gameThreads.emplace_back([p1, p2]() 
	{
        TicTacToeGame game(p1, p2);
        game.playGame();
    });
}

void GameManager::waitForGamesToFinish() 
{
    for (auto& thread : gameThreads) 
	{
        if (thread.joinable()) 
		{
            thread.join();
        }
    }
}
```

---

## **Main Program**
```cpp
#include "GameManager.h"

int main() 
{
    GameManager manager;

    Player player1("Alice", 'X');
    Player player2("Bob", 'O');

    manager.startGame(player1, player2); // Start Game 1

    Player player3("Charlie", 'X');
    Player player4("Dave", 'O');

    manager.startGame(player3, player4); // Start Game 2

    manager.waitForGamesToFinish(); // Wait for all games to finish

    return 0;
}
```

---

## **Features**
1. **Multiplayer Support**: Each game instance runs in its own thread.
2. **Thread-Safe Operations**: Mutex ensures game logic is synchronized.
3. **Modern C++ Concepts**: Uses STL, multithreading, and RAII principles.
4. **Expandable**: Easy to add new features like online play or AI opponents.
