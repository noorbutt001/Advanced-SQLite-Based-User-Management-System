from database import create_connection
from auth import hash_password


def view_profile(user_id):
    """View profile of logged-in user."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, email, phone, role, created_at FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        if user:
            print("\n========== 👤 USER PROFILE ==========")
            print(f"ID         : {user[0]}")
            print(f"Username   : {user[1]}")
            print(f"Email      : {user[2]}")
            print(f"Phone      : {user[3]}")
            print(f"Role       : {user[4]}")
            print(f"Created At : {user[5]}")
            print("=====================================\n")
        else:
            print("❌ User not found.")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        conn.close()


def update_profile(user_id, email=None, phone=None, password=None):
    """Update user profile fields."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        fields, values = [], []

        if email:
            fields.append("email = ?")
            values.append(email)
        if phone:
            fields.append("phone = ?")
            values.append(phone)
        if password:
            fields.append("password = ?")
            values.append(hash_password(password))

        if not fields:
            print("⚠️ No fields to update.")
            return

        values.append(user_id)
        query = f"UPDATE users SET {', '.join(fields)} WHERE id = ?"
        cursor.execute(query, values)
        conn.commit()
        print("✅ Profile updated successfully.")
    except Exception as e:
        print(f"❌ Error updating profile: {e}")
    finally:
        conn.close()


def delete_account(user_id):
    """Delete the user account."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        print("🗑️ Account deleted successfully.")
    except Exception as e:
        print(f"❌ Error deleting account: {e}")
    finally:
        conn.close()