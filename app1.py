#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import streamlit as st
import random

st.set_page_config(page_title="今天吃什么", layout="centered")
st.title("🎲 今天吃什么")
st.markdown("---")

# ===== 1. 默认“店→菜品”字典 =====
# 想固化新菜单就改这里
default_menu = {
    "老李家烧烤": ["羊肉串", "烤韭菜", "烤馒头片", "腰子"],
    "重庆小面": ["豌杂面", "牛肉面", "肥肠面", "素小面"],
    "粥员外": ["皮蛋瘦肉粥", "南瓜粥", "海鲜粥", "八宝粥"],
    "田老师红烧肉": ["红烧肉饭", "狮子头饭", "卤肉饭", "鸡腿饭"],
    "必胜客望京店": ["超级至尊比萨", "海鲜至尊比萨", "烤鸡翅", "意面"],
    "肯德基湖光中路店": ["吮指原味鸡", "香辣鸡腿堡", "黄金鸡块", "葡式蛋挞"],
    "喜茶": ["多肉葡萄", "芝芝莓莓", "烤黑糖波波", "满杯橙橙"],
    "蜜雪冰城": ["冰鲜柠檬水", "杨枝甘露", "草莓圣代", "四季春茶"]
}

# ===== 2. 会话状态初始化 =====
if "menu" not in st.session_state:
    st.session_state.menu = default_menu.copy()

# ===== 3. 侧边栏：增删店铺/菜品 =====
with st.sidebar:
    st.header("🛠 菜单管理")
    # 新增店铺
    new_shop = st.text_input("新增店铺名").strip()
    if st.button("添加店铺") and new_shop and new_shop not in st.session_state.menu:
        st.session_state.menu[new_shop] = []
    # 选择要编辑的店铺
    shop_opts = list(st.session_state.menu.keys())
    if shop_opts:
        edit_shop = st.selectbox("选择要编辑的店铺", shop_opts)
        dishes = st.session_state.menu[edit_shop]
        # 显示并允许批量改菜品
        dish_txt = st.text_area("菜品（每行一个）", value="\n".join(dishes))
        st.session_state.menu[edit_shop] = [d.strip() for d in dish_txt.splitlines() if d.strip()]
        # 删除店铺
        if st.button("删除该店铺"):
            del st.session_state.menu[edit_shop]
            st.rerun()

# ===== 4. 主界面：两级随机 =====
if st.session_state.menu:
    if st.button("🎯 随机抽！", type="primary"):
        shop = random.choice(list(st.session_state.menu.keys()))
        dishes = st.session_state.menu[shop]
        if dishes:                       # 店里有菜品
            dish = random.choice(dishes)
            st.success(f"**今晚去 → {shop}**  点这个 → **{dish}**")
        else:                            # 店里没录菜品
            st.warning(f"**{shop}** 还没录菜品哦，先去侧边栏加几道！")
else:
    st.info("菜单是空的，先在侧边栏添加店铺吧～")