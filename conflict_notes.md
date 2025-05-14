## Context

Am avut un conflict în fișierul `main.py` între ramurile `feature-a` și `feature-b`, deoarece ambele au modificat funcția `main()` pe aceleași linii.

## Conținutul original:
```python
def main():
    print("Hello, CI/CD! Aplicația funcționează corect.")

Am decis să păstrez ambele mesaje, pentru că oferă context diferit și este util să vedem clar comportamentul ambelor ramuri în versiunea finală.

def main():
    print("Hello, CI/CD! Aplicația funcționează corect branch feature-a and feature-b.")
