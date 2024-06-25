# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import streamlit as st


def calculate_password(serial_number):
    # 截取后七位数字
    last_seven_digits = serial_number[-7:]

    # 将所有非数字字符替换为'0'
    cleaned_last_seven = ''.join(['0' if not c.isdigit() else c for c in last_seven_digits])

    # 转换为整数，乘以10，再转换为十六进制
    hex_number = hex(int(cleaned_last_seven) * 10)

    # 分解十六进制数为高位和低位
    high_part, low_part = (hex_number[2:].zfill(16)[:8]), hex_number[2:].zfill(16)[8:]

    # 进行异或操作
    xor_result = int(low_part, 16) ^ int('aaaa', 16)

    # 合并高位和经过异或操作的低位，转换回十六进制
    final_hex = f'{high_part}{format(xor_result, "x")}'

    # 转换成十进制表示形式
    decimal_representation = int(final_hex, 16)

    return decimal_representation


# 创建Streamlit应用程序
st.title("密码计算器")
serial_input = st.text_input("请输入您的序列号（最多16位数字）", max_chars=16)

if st.button("计算密码"):
    password = calculate_password(serial_input)
    st.write(f"计算得到的密码为：{password}")