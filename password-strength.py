import re

# List of common weak passwords
COMMON_PASSWORDS = {
    "password", "admin", "123456", "qwerty", "abc123", 
    "letmein", "welcome", "passw0rd", "123123", "iloveyou"
}

def check_password_strength(password):
    """
    Checks the strength of a password and assigns a strength percentage.
    """

    password = password.strip()

    # **Check for common passwords first**
    if password.lower() in COMMON_PASSWORDS:
        return False, "Password is too common and easily guessable. Choose a more unique one."

    check_criteria = []
    strength_score = 0
    total_criteria = 5  

    if len(password) < 8:
        check_criteria.append("Password must contain at least 8 characters.")
    else:
        strength_score += 1

    if not re.search(r"[A-Z]", password):
        check_criteria.append("Password should have at least one uppercase letter.")
    else:
        strength_score += 1

    if not re.search(r"[a-z]", password):
        check_criteria.append("Password should have at least one lowercase letter.")
    else:
        strength_score += 1

    if not re.search(r"[0-9]", password):
        check_criteria.append("Password should have at least one number.")
    else:
        strength_score += 1

    if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>?/]", password):
        check_criteria.append("Password should have at least one special character.")
    else:
        strength_score += 1

    # Calculate strength percentage
    strength_percentage = (strength_score / total_criteria) * 100

    if check_criteria:
        return False, f"Weak Password ({int(strength_percentage)}% Strength):\n" + "\n".join(check_criteria)
    return True, f"Strong Password! ({int(strength_percentage)}% Strength)"

if __name__ == "__main__":
    user_password = input("Please enter a password to check its strength: ")
    status, message = check_password_strength(user_password)  
    print(message)
