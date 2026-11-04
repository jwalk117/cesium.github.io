import time
import os
import sys
import random

# --- MEMORY & STORAGE ---
class MemoryManager:
    def __init__(self, size=1024):
        self.memory = ['' for _ in range(size)]
        self.files = {}

    def write_file(self, filename, content):
        self.files[filename] = content

    def read_file(self, filename):
        return self.files.get(filename, "Error: File not found.")

    def format(self):
        self.files = {}
        self.memory = ['' for _ in range(1024)]
        print("[KERNEL] File system formatted.")

# --- KERNEL ---
class Kernel:
    def __init__(self):
        self.memory = MemoryManager()
        self.running = True
        self.user = "root"
        self.cwd = "/"

    def boot(self):
        print("\033[92m" + "="*40 + "\033[0m")
        print("   SlitherOS V. 1.0")
        print("="*40)
        print("Loading Kernel... OK")
        print("Initializing Memory... 1024 Bytes OK")
        print("Mounting Virtual FS... OK")
        print("\033[93m" + "Welcome to SlitherOS. Type 'help' for commands." + "\033[0m\n")
        
        # Pre-load the game file
        self.memory.write_file("snake.py", self.get_game_code())

    def run(self):
        while self.running:
            try:
                user_input = input(f"{self.user}@slos:{self.cwd}$ ").strip()
            except EOFError:
                break
            
            if not user_input:
                continue

            self.execute_command(user_input)

    def execute_command(self, cmd):
        parts = cmd.split()
        command = parts[0].lower()

        if command == "help":
            print("\033[96mAvailable Commands:\033[0m")
            print("  help       - Show this menu")
            print("  clear      - Clear the screen")
            print("  echo [msg] - Print a message")
            print("  ls         - List files")
            print("  cat [file] - Read a file")
            print("  run [file] - Execute a script")
            print("  format     - Wipe the file system")
            print("  exit       - Shut down")
            print("  game       - Play Snake (Simplified)")

        elif command == "clear":
            os.system('clear || cls')

        elif command == "echo":
            print(" ".join(parts[1:]))

        elif command == "ls":
            if self.memory.files:
                for f in self.memory.files:
                    print(f"  📄 {f}")
            else:
                print("  (empty directory)")

        elif command == "cat":
            if len(parts) < 2:
                print("Usage: cat <filename>")
            else:
                print(self.memory.read_file(parts[1]))

        elif command == "run":
            if len(parts) < 2:
                print("Usage: run <filename>")
            else:
                filename = parts[1]
                if filename in self.memory.files:
                    print(f"\033[94m[PROCESS] Running {filename}...\033[0m")
                    self.run_script(self.memory.read_file(filename))
                else:
                    print("Error: File not found.")

        elif command == "game":
            self.run_game()

        elif command == "format":
            confirm = input("U sure? (y/n): ")
            if confirm.lower() == 'y':
                self.memory.format()

        elif command == "exit":
            self.running = False
            print("\033[91mSystem halted. Goodbye.\033[0m")

        else:
            print(f"Command not found: {command}")

    def run_script(self, code):
        # Simple "script" execution: just print the code
        print("\033[90m" + code.replace('\n', '\n  ') + "\033[0m\n")
        print("[PROCESS] Script executed.")

    def get_game_code(self):
        return '''
# Snake Game (Terminal)
import time
import random

board = [[' ' for _ in range(10)] for _ in range(10)]
snake = [(5, 5)]
food = (2, 2)
direction = 'RIGHT'

def print_board():
    os.system('clear || cls')
    for row in board:
        print(' '.join(row))
    print(f"Score: {len(snake)}")


print("Snake Game Loaded. Use WASD to move.")
time.sleep(1)
'''

    def run_game(self):
        print("\033[95m" + "="*30 + "\033[0m")
        print("   SNAKE (Simplified Text Mode)")
        print("="*30)
        print("Controls: W (Up), S (Down), A (Left), D (Right)")
        print("Press 'Q' to Quit")
        print("\033[0m")

        board = [['.' for _ in range(10)] for _ in range(10)]
        snake = [(5, 5)]
        food = (2, 2)
        direction = 'RIGHT'
        score = 0
        running = True

        # Initial draw
        board[food[0]][food[1]] = 'F'
        for r, c in snake:
            board[r][c] = 'S'
        self.print_board_simplified(board)

        while running:
            try:
                move = input("Move (W/A/S/D/Q): ").upper()
            except EOFError:
                break

            if move == 'Q':
                running = False
                break

            if move in ['W', 'A', 'S', 'D']:
                direction = move

            # Calc new head
            r, c = snake[0]
            if direction == 'W': r -= 1
            elif direction == 'S': r += 1
            elif direction == 'A': c -= 1
            elif direction == 'D': c += 1

            # Collision
            if r < 0 or r >= 10 or c < 0 or c >= 10:
                print("\033[91mGame Over! Hit wall.\033[0m")
                running = False
                break
            
            if (r, c) in snake:
                print("\033[91mGame Over! Hit self.\033[0m")
                running = False
                break

            # Move snake
            snake.insert(0, (r, c))
            
            # Check food
            if (r, c) == food:
                score += 1
                food = (random.randint(0, 9), random.randint(0, 9))
                # Make sure food doesn't spawn on snake
                while food in snake:
                    food = (random.randint(0, 9), random.randint(0, 9))
            else:
                snake.pop()

            # Update board
            board = [['.' for _ in range(10)] for _ in range(10)]
            board[food[0]][food[1]] = 'F'
            for r, c in snake:
                board[r][c] = 'S'
            
            self.print_board_simplified(board)
            time.sleep(0.3) # Slow down the game

        print(f"\033[93mFinal Score: {score}\033[0m")

    def print_board_simplified(self, board):
        os.system('clear || cls')
        for row in board:
            print(' '.join(row))
        print(f"Score: {len([p for p in sum(board, []) if p == 'S'])}")

# --- MAIN EXE ---
if __name__ == "__main__":
    os = Kernel()
    os.boot()
    os.run()