import string
import sys

COMMON_PASSWORDS_FILE = "common.txt"

def load_common_passwords(filepath: str) -> list:
    """Loads a list of common passwords from a text file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read().splitlines()
    except FileNotFoundError:
            print("[!] Warning: common.txt not found. Skipping common password check.\n")
            return []
    
def analyze_password(password: str) -> dict:
    """Analyzes password and returns character type flags and length."""
    return {
        "has_upper": any(c in string.ascii_uppercase for c in password),
        "has_lower": any(c in string.ascii_lowercase for c in password),
        "has_digit": any(c in string.digits for c in password),
        "has_special": any(c in string.punctuation for c in password),
        "length": len(password)
    }

def calculate_score(analysis: dict) -> int:
     """Calculates a strength score out of 7 based on length and variety."""
     score = 0

     # Points for length
     length = analysis["length"]
     if length > 8: score += 1
     if length > 12: score += 1
     if length > 16: score += 1
     if length > 21: score += 1

     # Points for character variety
     variety = sum([
        analysis["has_upper"],
        analysis["has_lower"],
        analysis["has_digit"],
        analysis["has_special"],
     ])
     if variety > 1: score += 1
     if variety > 2: score += 1
     if variety > 3: score += 1

     return score

def get_strength_label(score: int) -> str:
     """Returns a human-readable strength label based on the score."""
     if score <= 2: return "Very Weak"
     elif score <= 4: return "Weak"
     elif score == 5: return "Moderate"
     elif score == 6: return "Strong"
     else: return "Very Strong"

def print_report(password: str, analysis: dict, score: int) -> None:
     """Prints a report of the password analysis."""
     strength = get_strength_label(score)
     variety = sum([analysis["has_upper"], analysis["has_lower"],
                    analysis["has_digit"], analysis["has_special"]])
     
     print("=" * 40)
     print("       PASSWORD STRENGTH REPORT")
     print("=" * 40)
     print(f"  Password   : {'*' * len(password)}")
     print(f"  Length     : {analysis['length']} characters")
     print(f"  Uppercase  : {'✓' if analysis['has_upper'] else '✗'}")
     print(f"  Lowercase  : {'✓' if analysis['has_lower'] else '✗'}")
     print(f"  Digits     : {'✓' if analysis['has_digit'] else '✗'}")
     print(f"  Special    : {'✓' if analysis['has_special'] else '✗'}")
     print("-" * 40)
     print(f"  Score      : {score} / 7")
     print(f"  Strength   : {strength}")
     print("=" * 40)

def main():
     print("=" * 40)
     print("      PASSWORD STRENGTH CHECKER")
     print("=" * 40)

     password = input("\n Enter your password: ")
     common = load_common_passwords(COMMON_PASSWORDS_FILE)

     # Immediately reject common passwords
     if password in common:
          print("\n [!] This password is too common. Score 0 / 7 - Very Weak")
          print("=" * 40)
          sys.exit()

     analysis = analyze_password(password)
     score = calculate_score(analysis)

     print()
     print_report(password, analysis, score)

if __name__ == "__main__":
     main()