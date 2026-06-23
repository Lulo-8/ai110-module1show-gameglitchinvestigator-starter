# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The first time I ran the game, it looked like a standard Streamlit layout, but it was completely
unplayable due to severely broken logic. The hints were giving inverted directions, the game was impossible to reset after a game-over scenario, and the scoring system applied weird mathematical penalties even when guessing correctly on the first attempt.

Bug 1: The game told me to go "LOWER" when my guess was smaller than the secret number, and "HIGHER" when it was larger.
Bug 2: Clicking the "New Game" button fails to reset the application status after losing or winning. Even though the tab title  stil shows "Glitchy Guesser", the screen stays locked, showing the message "Game over. Start a new game to try again." and preventing any new inputs from working.
Bug 3: Entering numbers outside the valid range (like 101, 0, or negative numbers) causes the game to lose its mind. For example, entering '101' makes the hint alternate erratically between "Go HIGHER!" and "Go LOWER!" on successive attempts, and entering '0' or negative numbers flags them as "Too High" and says "Go LOWER!".

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess: '3' (Secret: '51', Attempt 1) | Should display "Go HIGHER" because 3 is less than 51. | Displayed Go LOWER!" | None |

| Guess: '80' (Secret: '42', Attempt 2) | Should display "Go LOWER" because 80 is greater than 42. | Displayed Go HIGHER!" | None |

| Guess: `101` (Submitted multiple times) | Should consistently say "Go LOWER" since it is above the maximum range. | The hints alternated erratically between "GO HIGHER" and "GO LOWER" on consecutive clicks. | None |

| Clicked "New Game" button after losing | The app should reset the attempts, pick a new number, and let me play again. | The screen stays locked with the message "Game over. Start a new game to try again." and does not start a new round. | None |

| Correct guess on Attempt 1 (Secret: '99') | Should award the maximum perfect score of 100 points. | Awarded an incomplete score (70-80 points) due to an unfair calculation formula. | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude as my main AI pairing assistant and code refactoring companion inside VS Code to isolate and fix the game's broken logic.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Claude suggested an excellent approach to decouple the game's core architecture by successfully moving the main math and helper functions into `logic_utils.py`. It correctly stripped away the broken comparison loops and inverted conditions that were making the game unplayable. I verified this by running `python -m streamlit run app.py` and playing the game twice to confirm the hints consistently pointed the right way.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When I asked Claude to update my test suite file to match the new tuple return format, it only corrected the first test block and completely forgot to update the other two assertions. Had I accepted it blindly, `pytest` would have immediately crashed on the high and low test conditions. I verified this omission through a quick code review of the diff in my workspace window and subsequently prompted Claude to fix the remaining methods.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I determined a bug was successfully resolved by running automated test suites with pytest and manually executing gameplay scenarios within the Streamlit application. I systematically verified that edge cases, such as entering numbers out of range or resetting the application after a game-over screen, behaved predictably. Every state mutation was double-checked using the local developer debug menu to ensure numbers synced accurately.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran the automated verification suite using the command `python -m pytest tests/` in my terminal after refactoring the evaluation logic. This test suite targeted the `check_guess` module and successfully logged three passing assertions for win, high, and low conditions. It proved that extracting the arithmetic computations from the UI layer into a separate module preserved code functional integrity.
- Did AI help you design or understand any tests? How?
Claude helped me understand why the initial unit test suite was failing before applying the fixes. It identified that the started testing infrastructure expected a raw string back, whereas the actual application structure returned a combined state tuple containing both the comparison flag and a display emoji message. This insight guided me to update the test suite assertions to inspect only the first element of the tuple.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit works like a script that reads and reruns from top to bottom every single time a user interacts with a button, checkbox, or input field on the page. Because it refreshes completely, regular variables reset back to their default starting values instantly on every click. Session state acts like a persistent memory bank that stays intact across these restarts, allowing the app to remember crucial data like your current score, match history, and active game status.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I want to reuse the strategy of modularization by decoupling primary application computational logic from user interface rendering modules right from the start. Keeping helper functions inside an independent file makes tracking logic flows significantly easier and drastically simplifies writing automated tests. Additionally, committing changes in logical increments rather than large bulk saves is a Git Habit I will maintain.
- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I will feed the AI assistant file code blocks in smaller, isolated chunks rather than broad multi-file requests to prevent small errors in the generated layout. I will also be much more precise and strict when reviewing code diff implementations to catch missing lines or skipped function updates earlier in the cycle. This will save time by catching partial code generations before they break the local build.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project made me realize that AI-generated code often looks visually convincing but can hide critical logic design flaws, superficial edge-case handling, and severe state synchronization bugs. It taught me that as a human developer, my job is to act as a critical inspector who carefully audits, tests, and refactors AI suggestions rather than blindly trusting them.
