# Speak Pseudocode2C

**Speak Pseudocode2C** is a framework designed to convert customized pseudocode into C code. The main objective of this tool is to simplify coding for beginners by allowing them to express algorithms in pseudocode, which is then translated into C source code. By abstracting away the complexities of a programming language, this approach makes coding more accessible and helps maintain engagement with the subject.

This project utilizes **Natural Language Processing (NLP)** to robustly interpret spoken pseudocode, making it possible to generate source code line-by-line as the user describes the algorithm verbally.

## Key Features

- **Simplified Pseudocode to C Translation:** Users can speak pseudocode, which the system simultaneously converts to C language source code.
- **Static Stub-Based Approach:** This framework relies on a static stub-based architecture that maps pseudocode constructs to equivalent C constructs.
- **Natural Language Processing (NLP) Integration:** NLP is used to identify programming constructs and differentiate between action words (commands) and narration (comments).
- **Support for Control Structures:** The framework understands different programming constructs such as loops, conditional statements, and functions.

## Problem Statement

For beginners, programming languages like C can be difficult to grasp due to their syntax and strict rules. This tool makes programming more accessible by allowing users to interact with the code in a more intuitive way, using spoken pseudocode rather than traditional text-based coding. As pseudocode is simpler, it encourages users to focus on algorithmic thinking without getting bogged down by syntax.

## How it Works

- Users speak the pseudocode line-by-line.
- The first word of each spoken line is treated as an **action word**, which triggers specific programming constructs (e.g., "if," "while," "print").
- Any other narration or comments are ignored and added as comments in the C code.
- The NLP system interprets the user’s speech and maps it to a corresponding C code block, constructing the final source code step-by-step.

## Published Paper

This project is based on a research paper published by IEEE. You can read the full paper here:  
[Speak Pseudocode2C: A Framework to Convert Customized Pseudocode to C Code](https://ieeexplore.ieee.org/document/9824336)

## Installation and Usage

To run the application:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/speak-pseudocode2c.git
2. Go to the Final Approach folder. Run a pipreqs and install all the dependencies of the project.
3. Run the project:

  ```bash
  python3 main.py
