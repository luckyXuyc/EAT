#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import streamlit as st
import random

st.set_page_config(page_title="今天吃什么", layout="centered")

st.title("🎲 今天吃什么")
st.markdown("---")

# 默认列表
default = ["川味轩", "粤味茶餐厅", "兰州拉面", "黄焖鸡米饭",
           "寿司之家", "韩式石锅拌饭", "必胜客", "肯德基",
           "海底捞", "小龙坎", "老乡鸡", "真功夫"]

# 会话状态里保存餐厅列表
if "rst" not in st.session_state:
    st.session_state.rst = default.copy()

# 输入框：新增餐厅
new = st.text_input("手动添加餐厅（回车即可）:")
if new and new not in st.session_state.rst:
    st.session_state.rst.append(new)

# 多行文本框：直接批量编辑
edited = st.text_area("当前餐厅列表（每行一家，可任意删改）:",
                      value="\n".join(st.session_state.rst))
st.session_state.rst = [x.strip() for x in edited.splitlines() if x.strip()]

# 抽奖按钮
if st.button("🎯 随机抽一家！", type="primary"):
    choice = random.choice(st.session_state.rst)
    st.success(f"**今晚就吃：{choice}**")