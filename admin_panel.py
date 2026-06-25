from database import create_connection
from utils import export_to_csv


def view_all_users():
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, email, phone, role, created_at FROM users")
        users = cursor.fetchall()
        if not users:
            print("⚠️ No users found.")
            return
        print("\n========== 📋 ALL USERS ==========")
        for u in users:
            print(f"{u[0]} | {u[1]} | {u[2]} | {u[3]} | {u[4]} | {u[5]}")
        print("==================================\n")
    finally:
        conn.close()


def search_users(keyword):
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, username, email, role FROM users 
            WHERE username LIKE ? OR email LIKE ?
        """, (f"%{keyword}%", f"%{keyword}%"))
        results = cursor.fetchall()
        if not results:
            print("❌ No matching users found.")
            return
        print("\n========== 🔍 SEARCH RESULTS ==========")
        for r in results:
            print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]}")
        print("=======================================\n")
    finally:
        conn.close()


def filter_by_role(role):
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, email, role FROM users WHERE role = ?", (role,))
        users = cursor.fetchall()
        if not users:
            print(f"⚠️ No users with role '{role}'.")
            return
        print(f"\n========== 🎭 ROLE: {role} ==========")
        for u in users:
            print(f"{u[0]} | {u[1]} | {u[2]} | {u[3]}")
        print("====================================\n")
    finally:
        conn.close()


def delete_any_user(user_id):
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"🗑️ User ID {user_id} deleted by admin.")
        else:
            print("❌ User not found.")
    finally:
        conn.close()


def export_users():
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, email, phone, role, created_at FROM users")
        data = cursor.fetchall()
        headers = ["ID", "Username", "Email", "Phone", "Role", "Created At"]
        export_to_csv("users_export.csv", headers, data)
    finally:
        conn.close()