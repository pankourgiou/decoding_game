import time
import os
import random

# Alien characters for display effects
ALIEN_CHARS = '▓▒░█▀■@#$%&/\\[]{}=*+-?><~;:△▲◭◮'

# Riddles database
RIDDLES = [
    {
        "alien_text": "▓▒░█▀■@#$%&/\\[]{}",
        "question": "I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?",
        "answer": "fire"
    },
    {
        "alien_text": "@#$%&/\\[]{}=*+-?><",
        "question": "The more you take, the more you leave behind. What am I?",
        "answer": "footsteps"
    },
    {
        "alien_text": "█▀■@#$%&/\\△▲◭◮",
        "question": "What has keys, but no locks; space, but no room; you can enter, but not go in?",
        "answer": "keyboard"
    },
    {
        "alien_text": "▒░█▀■@#$%&△▲◭◮",
        "question": "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. I have roads, but no cars. What am I?",
        "answer": "map"
    },
    {
        "alien_text": "░█▀■@#$%&/\\[]{}",
        "question": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
        "answer": "echo"
    }
]

class RiddleGame:
    def __init__(self):
        self.current_riddle = 0
        self.score = 0
        self.total_riddles = len(RIDDLES)
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def display_alien_text(self, text):
        """Display alien text with animation effect"""
        for _ in range(3):  # Show 3 rows of random alien characters
            alien_line = ''.join(random.choice(ALIEN_CHARS) for _ in range(len(text) * 2))
            print(alien_line)
            time.sleep(0.3)
        print("\n" + "="*50 + "\n")
        
    def display_header(self):
        print("\n" + "="*50)
        print(f"ALIEN TRANSMISSION #{self.current_riddle + 1}/{self.total_riddles}")
        print("="*50 + "\n")
        
    def play_game(self):
        while self.current_riddle < self.total_riddles:
            self.clear_screen()
            self.display_header()
            
            # Display alien text effect
            current_riddle = RIDDLES[self.current_riddle]
            print("Incoming alien transmission...")
            self.display_alien_text(current_riddle["alien_text"])
            
            # Display riddle
            print(f"DECODED MESSAGE: {current_riddle['question']}\n")
            
            # Get user answer
            user_answer = input("Enter your answer to decode: ").lower().strip()
            
            # Check answer
            if user_answer == current_riddle["answer"]:
                self.score += 1
                print("\n🟢 Correct! Decoding next transmission...")
                self.current_riddle += 1
            else:
                print("\n🔴 Incorrect! Try again...")
                
            time.sleep(2)
            
        # Game complete
        self.display_game_over()
            
    def display_game_over(self):
        self.clear_screen()
        print("\n" + "="*50)
        print("GAME OVER - ALL TRANSMISSIONS DECODED")
        print("="*50)
        print(f"\nFinal Score: {self.score}/{self.total_riddles}")
        
        # Calculate percentage
        percentage = (self.score / self.total_riddles) * 100
        print(f"Decoding Accuracy: {percentage:.1f}%")
        
        if percentage == 100:
            print("\n🏆 Perfect score! You are a master decoder!")
        elif percentage >= 70:
            print("\n🌟 Great job! You have strong decoding skills!")
        else:
            print("\n👽 Keep practicing your alien decoding skills!")

def main():
    # Display welcome message
    print("\n" + "="*50)
    print("WELCOME TO ALIEN RIDDLE DECODER")
    print("="*50)
    print("\nPrepare to decode alien transmissions...")
    time.sleep(2)
    
    # Start game
    game = RiddleGame()
    game.play_game()
    
    # Ask to play again
    while input("\nWould you like to play again? (y/n): ").lower().strip() == 'y':
        game = RiddleGame()
        game.play_game()
    
    print("\nThank you for playing Alien Riddle Decoder!\n")

if __name__ == "__main__":
    main()
