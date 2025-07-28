# Copilot Instructions for DSA Workspace

## Overview
This workspace contains Python scripts for practicing Data Structures and Algorithms (DSA), organized by topic and difficulty. There are no build systems, test frameworks, or external dependencies; scripts are run directly with Python.

## Directory Structure
- `basic practice/`: Foundational Python scripts (e.g., patterns, number operations, prime checks).
- `advance pattern/`: More complex pattern generation scripts.
- `cc que/`: Coding challenge questions and solutions.
- Top-level files: Miscellaneous practice scripts and notes.

## Key Patterns & Conventions
- **Script-based workflow**: Each file is a standalone script. No imports between scripts; functions are defined and executed in the same file.
- **Naming**: Filenames and function names are descriptive of their purpose (e.g., `check_prime_num.py`, `PrimeNum`).
- **Input/Output**: Most scripts use `input()` for user input and `print()` for output. Some code is commented out for alternate approaches or explanations.
- **Prime Number Example**: See `basic practice/check_prime_num.py` for two approaches to prime checking (fast and slow), with clear comments and function separation.

## Developer Workflow
- **Run scripts**: Use `python <script_path>` to execute any script. No compilation or build steps required.
- **Debugging**: Add print statements or comment/uncomment code blocks for testing different logic.
- **No external dependencies**: All code uses only Python's standard library.

## Project-Specific Practices
- **Commented alternatives**: Many files contain multiple approaches, with unused code commented out for reference.
- **No test automation**: Manual testing via script execution and user input.
- **No class-based architecture**: All logic is function-based or procedural.

## Example: Prime Number Check
- Fast approach uses early returns and skips even numbers.
- Slow approach iterates through odd numbers only.
- Both approaches are documented and easy to switch between by commenting/uncommenting code blocks.

## Recommendations for AI Agents
- When adding new scripts, follow the descriptive naming and function-based structure.
- When updating existing scripts, preserve commented alternatives and explanatory comments.
- Reference similar scripts for consistent logic and style.
- Avoid introducing external dependencies or complex architectures.

## Key Files
- `basic practice/check_prime_num.py`: Prime number logic and conventions.
- `advance pattern/`: Pattern generation examples.
- `cc que/`: Coding challenge solutions.

---
For questions or unclear conventions, ask the user for clarification or examples from existing scripts.
