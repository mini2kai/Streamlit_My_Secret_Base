import bcrypt

# 为用户生成密码哈希
def generate_hash(password):
    # 使用bcrypt直接生成哈希值
    password_bytes = password.encode('utf-8')
    hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')

# 为配置文件中的用户生成哈希密码
if __name__ == "__main__":
    # 为alice用户生成哈希密码
    alice_hash = generate_hash("zeke#0419")
    print(f"Alice的密码哈希: {alice_hash}")
    
    # 为bob用户生成哈希密码
    bob_hash = generate_hash("bob123")
    print(f"Bob的密码哈希: {bob_hash}")
    
    print("请将这些哈希值复制到config.yaml文件中")