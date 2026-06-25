import hashlib
from database import create_connection

MAX_ATTEMPTS = 3


def hash_password(password: str) -> str:
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, email, password, phone, role="User"):
    """Register a new user securely."""
    conn = create_connection()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        hashed_pw = hash_password(password)
        cursor.execute("""
            INSERT INTO users (username, email, password, phone, role)
            VALUES (?, ?, ?, ?, ?)
        """, (username, email, hashed_pw, phone, role))
        conn.commit()
        print(f"✅ User '{username}' registered successfully!")
        return True
    except Exception as e:
        print(f"❌ Registration failed: {e}")
        return False
    finally:
        conn.close()


def login_user(username, password):
    """Authenticate user with login attempt limit."""
    conn = create_connection()
    if conn is None:
        return None
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, password, role, failed_attempts, is_locked FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if not user:
            print("❌ User not found.")
            return None

        user_id, uname, stored_pw, role, attempts, is_locked = user

        if is_locked:
            print("🔒 Account locked due to too many failed attempts. Please reset password.")
            return None

        if hash_password(password) == stored_pw:
            cursor.execute("UPDATE users SET failed_attempts = 0 WHERE id = ?", (user_id,))
            conn.commit()
            print(f"✅ Welcome, {uname}! (Role: {role})")
            return {"id": user_id, "username": uname, "role": role}
        else:
            attempts += 1
            locked = 1 if attempts >= MAX_ATTEMPTS else 0
            cursor.execute("UPDATE users SET failed_attempts = ?, is_locked = ? WHERE id = ?", (attempts, locked, user_id))
            conn.commit()
            remaining = MAX_ATTEMPTS - attempts
            if locked:
                print("🔒 Account locked! Use 'Forgot Password' to reset.")
            else:
                print(f"❌ Wrong password. Attempts left: {remaining}")
            return None
    except Exception as e:
        print(f"❌ Login error: {e}")
        return None
    finally:
        conn.close()


def forgot_password(username, new_password):
    """Reset password and unlock account."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
        if not cursor.fetchone():
            print("❌ User not found.")
            return False
        hashed_pw = hash_password(new_password)
        cursor.execute("""
            UPDATE users SET password = ?, failed_attempts = 0, is_locked = 0
            WHERE username = ?
        """, (hashed_pw, username))
        conn.commit()
        print("✅ Password reset successfully. Account unlocked.")
        return True
    except Exception as e:
        print(f"❌ Error resetting password: {e}")
        return False
    finally:
        conn.close()