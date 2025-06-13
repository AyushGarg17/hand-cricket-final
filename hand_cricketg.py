import random
import time

def display_hand(number):
    """Display hand emoji based on number"""
    hand_emojis = {
        0: "✊",  # Fist (0)
        1: "👆",  # Index finger (1)
        2: "✌️",   # Peace sign (2)
        3: "🤟",  # Three fingers
        4: "🖖",  # Four fingers
        5: "🖐️",   # Open hand (5)
        6: "👋"   # Six fingers representation
    }
    return hand_emojis.get(number, "❓")

def print_separator():
    print("=" * 60)

def print_match_header():
    print_separator()
    print("🏏" * 10 + " HAND CRICKET CHAMPIONSHIP " + "🏏" * 10)
    print_separator()
    print("Rules:")
    print("• Choose numbers 0-6")
    print("• Same number = WICKET!")
    print("• Different numbers = Sum becomes runs")
    print("• Sum = 6 → NO BALL (extra ball)")
    print("• Match: 3 overs per innings (18 balls each)")
    print_separator()

def display_scoreboard(innings, score, balls_faced, total_balls, wickets, current_over, balls_in_over):
    print(f"\n📊 {innings} SCOREBOARD:")
    print(f"Score: {score}/{wickets} | Balls: {balls_faced}/{total_balls} | Over: {current_over}.{balls_in_over}")
    if balls_faced > 0:
        run_rate = (score * 6) / balls_faced
        print(f"Run Rate: {run_rate:.2f}")
    print("-" * 40)

def play_batting_innings(player_name, target=None):
    print(f"\n🏏 {player_name.upper()} BATTING INNINGS")
    if target:
        print(f"🎯 Target to chase: {target} runs")
    print("-" * 40)
    
    # Game settings
    total_overs = 3
    balls_per_over = 6
    total_balls = total_overs * balls_per_over
    
    # Player stats
    score = 0
    balls_faced = 0
    current_over = 1
    balls_in_over = 0
    wickets = 0
    max_wickets = 1  # Single wicket = innings over
    
    while balls_faced < total_balls and wickets < max_wickets:
        # Check if target achieved
        if target and score >= target:
            print(f"\n🎉 TARGET ACHIEVED! {player_name} wins by {max_wickets - wickets} wickets!")
            break
            
        # Display current status
        display_scoreboard(player_name.upper(), score, balls_faced, total_balls, wickets, current_over, balls_in_over)
        
        if target:
            needed = target - score
            balls_left = total_balls - balls_faced
            if balls_left > 0:
                req_rate = needed / balls_left * 6
                print(f"Need {needed} runs from {balls_left} balls (Required Rate: {req_rate:.2f})")
        
        # Get player input
        print(f"\nOver {current_over}.{balls_in_over + 1}")
        while True:
            try:
                player_choice = int(input(f"🎯 {player_name}, enter your number (0-6): "))
                if 0 <= player_choice <= 6:
                    break
                else:
                    print("❌ Please enter a number between 0-6!")
            except ValueError:
                print("❌ Please enter a valid number!")
        
        # Computer's choice (bowler)
        computer_choice = random.randint(0, 6)
        
        # Display hands
        print(f"\n🏏 {player_name}: {display_hand(player_choice)} ({player_choice})")
        time.sleep(0.5)
        print(f"🤖 Computer: {display_hand(computer_choice)} ({computer_choice})")
        time.sleep(0.5)
        
        # Check result
        if player_choice == computer_choice:
            print(f"\n💀 WICKET! Both showed {player_choice}")
            print(f"🏏 {player_name} is OUT!")
            wickets += 1
            balls_faced += 1
            balls_in_over += 1
            
            if wickets >= max_wickets:
                print(f"\n📉 {player_name} ALL OUT!")
                break
        else:
            # Calculate runs
            runs = player_choice + computer_choice
            score += runs
            
            # Check for no ball
            if runs == 6:
                print(f"\n🚫 NO BALL! {runs} runs scored!")
                print("🎁 Extra ball awarded!")
                time.sleep(1)
            else:
                balls_faced += 1
                balls_in_over += 1
                
                if runs == 0:
                    print(f"\n😴 DOT BALL! No runs scored")
                elif runs >= 4:
                    print(f"\n🎉 BOUNDARY! {runs} runs! What a shot!")
                else:
                    print(f"\n✅ {runs} runs scored!")
                
                time.sleep(1)
                
                # Check if over complete
                if balls_in_over == balls_per_over:
                    if current_over < total_overs:
                        print(f"\n🏏 End of Over {current_over}")
                        current_over += 1
                        balls_in_over = 0
                        time.sleep(1)
    
    # Final scoreboard
    print(f"\n🏁 END OF {player_name.upper()} INNINGS")
    display_scoreboard(player_name.upper(), score, balls_faced, total_balls, wickets, current_over, balls_in_over)
    
    return score, balls_faced, wickets

def play_bowling_innings(player_name, target):
    print(f"\n🥎 {player_name.upper()} BOWLING INNINGS")
    print(f"🎯 Computer needs {target} runs to win")
    print("-" * 40)
    
    # Game settings
    total_overs = 3
    balls_per_over = 6
    total_balls = total_overs * balls_per_over
    
    # Computer batting stats
    score = 0
    balls_faced = 0
    current_over = 1
    balls_in_over = 0
    wickets = 0
    max_wickets = 1
    
    while balls_faced < total_balls and wickets < max_wickets:
        # Check if target achieved
        if score >= target:
            print(f"\n💔 COMPUTER WINS! Target achieved with {balls_faced} balls to spare!")
            return False  # Player loses
            
        # Display current status
        display_scoreboard("COMPUTER", score, balls_faced, total_balls, wickets, current_over, balls_in_over)
        
        needed = target - score
        balls_left = total_balls - balls_faced
        if balls_left > 0:
            req_rate = needed / balls_left * 6
            print(f"Computer needs {needed} runs from {balls_left} balls (Required Rate: {req_rate:.2f})")
        
        # Get player bowling input
        print(f"\nOver {current_over}.{balls_in_over + 1}")
        while True:
            try:
                player_choice = int(input(f"🥎 {player_name}, bowl your number (0-6): "))
                if 0 <= player_choice <= 6:
                    break
                else:
                    print("❌ Please enter a number between 0-6!")
            except ValueError:
                print("❌ Please enter a valid number!")
        
        # Computer's batting choice
        computer_choice = random.randint(0, 6)
        
        # Display hands
        print(f"\n🥎 {player_name} (Bowler): {display_hand(player_choice)} ({player_choice})")
        time.sleep(0.5)
        print(f"🏏 Computer (Batsman): {display_hand(computer_choice)} ({computer_choice})")
        time.sleep(0.5)
        
        # Check result
        if player_choice == computer_choice:
            print(f"\n🎉 WICKET! Both showed {player_choice}")
            print(f"💀 Computer is OUT!")
            wickets += 1
            balls_faced += 1
            balls_in_over += 1
            
            if wickets >= max_wickets:
                print(f"\n🎊 COMPUTER ALL OUT!")
                break
        else:
            # Calculate runs
            runs = player_choice + computer_choice
            score += runs
            
            # Check for no ball
            if runs == 6:
                print(f"\n🚫 NO BALL! Computer scores {runs} runs!")
                print("💔 Extra ball given!")
                time.sleep(1)
            else:
                balls_faced += 1
                balls_in_over += 1
                
                if runs == 0:
                    print(f"\n🛡️ DOT BALL! Great bowling!")
                elif runs >= 4:
                    print(f"\n💔 BOUNDARY! Computer scores {runs} runs!")
                else:
                    print(f"\n📈 Computer scores {runs} runs")
                
                time.sleep(1)
                
                # Check if over complete
                if balls_in_over == balls_per_over:
                    if current_over < total_overs:
                        print(f"\n🥎 End of Over {current_over}")
                        current_over += 1
                        balls_in_over = 0
                        time.sleep(1)
    
    # Final scoreboard
    print(f"\n🏁 END OF COMPUTER INNINGS")
    display_scoreboard("COMPUTER", score, balls_faced, total_balls, wickets, current_over, balls_in_over)
    
    # Determine result
    if score < target:
        print(f"\n🎊 {player_name.upper()} WINS!")
        print(f"🏆 Computer fell short by {target - score} runs!")
        return True  # Player wins
    else:
        print(f"\n💔 COMPUTER WINS!")
        print(f"🎯 Target achieved!")
        return False  # Player loses

def play_complete_match():
    print_match_header()
    
    player_name = input("👤 Enter your name: ").strip()
    if not player_name:
        player_name = "Player"
    
    print(f"\n🎮 Welcome {player_name}! Let's play a complete match!")
    
    # Toss
    print(f"\n🪙 TOSS TIME!")
    toss_choice = input("Choose (H)eads or (T)ails: ").upper().strip()
    toss_result = random.choice(['H', 'T'])
    
    print(f"🪙 Toss Result: {'Heads' if toss_result == 'H' else 'Tails'}")
    
    if (toss_choice == 'H' and toss_result == 'H') or (toss_choice == 'T' and toss_result == 'T'):
        print(f"🎉 {player_name} wins the toss!")
        choice = input("Choose to (B)at first or Bowl first? ").upper().strip()
        bat_first = choice == 'B'
    else:
        print("💔 Computer wins the toss!")
        bat_first = random.choice([True, False])
        print(f"🤖 Computer chooses to {'bat' if bat_first else 'bowl'} first!")
    
    time.sleep(2)
    
    if bat_first:
        # Player bats first
        print(f"\n🏏 {player_name.upper()} BATTING FIRST")
        player_score, _, _ = play_batting_innings(player_name)
        
        if player_score == 0:
            print(f"\n💀 {player_name} DUCK! Computer wins without batting!")
            return
        
        target = player_score + 1
        print(f"\n🎯 COMPUTER NEEDS {target} RUNS TO WIN")
        time.sleep(2)
        
        # Computer bats second (Player bowls)
        player_wins = play_bowling_innings(player_name, target)
        
    else:
        # Computer bats first (Player bowls)
        print(f"\n🤖 COMPUTER BATTING FIRST")
        print("🥎 You are bowling first!")
        
        # Simulate computer batting (player bowling)
        computer_score = 0
        balls_faced = 0
        total_balls = 18
        current_over = 1
        balls_in_over = 0
        wickets = 0
        
        while balls_faced < total_balls and wickets < 1:
            display_scoreboard("COMPUTER", computer_score, balls_faced, total_balls, wickets, current_over, balls_in_over)
            
            print(f"\nOver {current_over}.{balls_in_over + 1}")
            while True:
                try:
                    player_choice = int(input(f"🥎 {player_name}, bowl your number (0-6): "))
                    if 0 <= player_choice <= 6:
                        break
                    else:
                        print("❌ Please enter a number between 0-6!")
                except ValueError:
                    print("❌ Please enter a valid number!")
            
            computer_choice = random.randint(0, 6)
            
            print(f"\n🥎 {player_name} (Bowler): {display_hand(player_choice)} ({player_choice})")
            time.sleep(0.5)
            print(f"🏏 Computer (Batsman): {display_hand(computer_choice)} ({computer_choice})")
            time.sleep(0.5)
            
            if player_choice == computer_choice:
                print(f"\n🎉 WICKET! Computer is OUT!")
                wickets = 1
                balls_faced += 1
                break
            else:
                runs = player_choice + computer_choice
                computer_score += runs
                
                if runs == 6:
                    print(f"\n🚫 NO BALL! Computer scores {runs}!")
                else:
                    balls_faced += 1
                    balls_in_over += 1
                    
                    if runs == 0:
                        print(f"\n🛡️ DOT BALL! Great bowling!")
                    elif runs >= 4:
                        print(f"\n💔 BOUNDARY! Computer scores {runs}!")
                    else:
                        print(f"\n📈 Computer scores {runs} runs")
                    
                    if balls_in_over == 6:
                        if current_over < 3:
                            print(f"\n🥎 End of Over {current_over}")
                            current_over += 1
                            balls_in_over = 0
                
                time.sleep(1)
        
        print(f"\n🏁 END OF COMPUTER INNINGS")
        display_scoreboard("COMPUTER", computer_score, balls_faced, total_balls, wickets, current_over, balls_in_over)
        
        if computer_score == 0:
            print(f"\n🎊 COMPUTER DUCK! {player_name.upper()} WINS WITHOUT BATTING!")
            return
        
        target = computer_score + 1
        print(f"\n🎯 {player_name.upper()} NEEDS {target} RUNS TO WIN")
        time.sleep(2)
        
        # Player bats second
        player_score, _, _ = play_batting_innings(player_name, target)
        
        # Determine winner
        if player_score >= target:
            print(f"\n🏆 {player_name.upper()} WINS!")
            print(f"🎉 Target chased successfully!")
        else:
            print(f"\n💔 COMPUTER WINS!")
            print(f"🎯 {player_name} fell short by {target - player_score} runs!")
    
    # Match summary
    print_separator()
    print("🏏" * 15 + " MATCH COMPLETE " + "🏏" * 15)
    print_separator()
    
    # Ask for another match
    play_again = input("\n🎮 Play another match? (y/n): ").lower().strip()
    if play_again == 'y':
        print("\n" * 3)
        play_complete_match()
    else:
        print(f"\n👋 Thanks for playing, {player_name}!")
        print("🏏 Come back anytime for more cricket action!")

# Start the complete match
if __name__ == "__main__":
    play_complete_match()
