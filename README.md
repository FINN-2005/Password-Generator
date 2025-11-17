# Password-Generator

A minimal, secure password generator using Python’s `secrets` module.

# Description

This script creates cryptographically secure passwords using Python’s built-in `secrets` module.
You can customize the password length and choose whether to include symbols.
The character set includes uppercase letters, lowercase letters, digits, and optional punctuation.

The generator is short, simple, and suitable for creating strong passwords for general use.

# Installation

- Just clone the repo, no extra dependencies required.

# Usage

- just run the file
  ```bash
  python main.py
  ```
- or import it
  ```python
  from password_generator import generate_password
  
  print(generate_password())            # 16 chars, includes symbols
  print(generate_password(32))          # 32 chars
  print(generate_password(20, False))   # no symbols
  ```
