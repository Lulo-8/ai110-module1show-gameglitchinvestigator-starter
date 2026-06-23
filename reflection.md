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

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
