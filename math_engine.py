```python
import random
import sympy as sp

x, y, z = sp.symbols('x y z')

def generate_senior_question():
    """Generates Senior Phase (Grades 7–9) structured mathematical expressions with LaTeX formatting."""
    q_type = random.choice(["linear_eq", "pythagoras", "exponent", "ratio"])
    
    if q_type == "linear_eq":
        a = random.randint(2, 6)
        ans = random.randint(1, 10)
        c = a * ans
        return {
            "prompt": "Solve for the unknown variable $x$ in the equation:",
            "latex": f"{a}x = {c}",
            "answer": ans,
            "type": "numeric"
        }
    elif q_type == "pythagoras":
        a, b = random.choice([(3, 4), (5, 12), (6, 8), (9, 12)])
        ans = int((a**2 + b**2)**0.5)
        return {
            "prompt": "Calculate the hypotenuse $c$ using right-triangle properties:",
            "latex": f"c = \\sqrt{{{a}^2 + {b}^2}}",
            "answer": ans,
            "type": "numeric"
        }
    elif q_type == "exponent":
        base = random.randint(2, 5)
        p1, p2 = random.randint(2, 3), random.randint(1, 3)
        ans = base ** (p1 + p2)
        return {
            "prompt": "Simplify and evaluate the exponential expression:",
            "latex": f"{base}^{{{p1}}} \\times {base}^{{{p2}}}",
            "answer": ans,
            "type": "numeric"
        }
    else:
        n, d = random.randint(1, 4), random.randint(5, 9)
        return {
            "prompt": "Find the missing numerator value for $x$:",
            "latex": f"\\frac{{x}}{{{d}}} = \\frac{{{n}}}{{{d}}}",
            "answer": n,
            "type": "numeric"
        }

def generate_fet_question():
    """Generates FET Advanced Phase (Grades 10–12) calculus and quadratic equations."""
    q_type = random.choice(["derivative", "quadratic"])
    
    if q_type == "derivative":
        a = random.randint(2, 5)
        n = random.randint(2, 4)
        expr = a * x**n
        derived = sp.diff(expr, x)
        return {
            "prompt": "Determine the symbolic derivative $\\frac{dy}{dx}$ for:",
            "latex": f"y = {sp.latex(expr)}",
            "answer_str": sp.latex(derived),
            "type": "symbolic"
        }
    else:
        r1, r2 = random.randint(-3, 3), random.randint(1, 4)
        expr = sp.expand((x - r1) * (x - r2))
        return {
            "prompt": "Find the maximum positive root for the quadratic equation:",
            "latex": f"{sp.latex(expr)} = 0",
            "answer": max(r1, r2),
            "type": "numeric"
        }

def generate_speedrun_question(difficulty="Easy"):
    """Generates lightning mental math problems for the arcade speed-run mode."""
    ops = {
        "Easy": ["+", "-"],
        "Medium": ["+", "-", "\\times"],
        "Hard": ["\\times", "\\div"],
        "Expert": ["\\times", "\\div", "^"]
    }
    op = random.choice(ops.get(difficulty, ["+"]))
    
    if op in ["+", "-"]:
        a, b = random.randint(5, 50), random.randint(5, 50)
        ans = a + b if op == "+" else a - b
    elif op == "\\times":
        a, b = random.randint(3, 12), random.randint(3, 12)
        ans = a * b
    elif op == "\\div":
        b = random.randint(2, 10)
        ans = random.randint(2, 10)
        a = b * ans
    else:
        a, b = random.randint(2, 4), random.randint(2, 3)
        ans = a ** b
        op = "^"
        
    latex_eq = f"{a} {op} {b}" if op != "^" else f"{a}^{{{b}}}"
    return {"latex": latex_eq, "answer": ans}

```
