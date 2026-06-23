# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] Describe the game's purpose.
A Streamlit-based numbers guessing game designed to challenge the player across different difficulty modes (Easy, Normal, Hard) with a dynamic scoring system.
- [X] Detail which bugs you found.
Discovered inverted higher/lower hints due to swapped conditional logic, an unstable secret number tracking because of weird type-casting rules on even attempts, an unfair scoring mechanic, and an application lock-up after winning or losing because the game status state failed to clear upon resetting.
- [X] Explain what fixes you applied.
Refactored all core operations into `logic_utils.py`, streamlined type consistency for accurate comparisons, flattened the score penalty so it is consistently transparent, fixed the "New Game" state reset parameters within `app.py`, and updated the automated unit tests to handle the new tuple response format.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. -- Select Difficulty -- Launch the application and pick a difficulty from the sidebar settings (e.g., Easy, Normal, or Hard) to establish your target number range and maximum allowable attempts.
2. -- Review Debug Info -- Open the optional "Developer Debug Info" expander drop-down to check the registered backend state values, including the current score tracking, total attempts made, and current secret integer.
3. -- Submit a Guess -- Input a number inside the specified bounds in the numeric input text field and click the "Submit Guess 🚀" button.
4. -- Read Accurate Feedback -- Review the warning message prompts; the application now correctly signals a "Go LOWER!" or "Go HIGHER!" hint depending on your inputs.
5. -- Start a New Game -- Click the "New Game 🔁" action button at any point (or after a win/loss validation block) to instantly clear previous match histories, roll a new secret index, and seamlessly reset you play status.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
=================================================================================== test session starts ====================================================================================
platform win32 -- Python 3.13.13, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\Amand\Desktop\uni\codepath\AI110\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 6 items                                                                                                                                                                           

tests\test_game_logic.py ......                                                                                                                                                       [100%]

==================================================================================== 6 passed in 0.06s =====================================================================================
```


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
