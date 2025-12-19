#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
糖妈日记 - 从公开API构建食物标签数据库
使用USDA、Open Food Facts等免费API获取食物数据
"""

import os
import json
import time
import requests
from typing import Dict, List, Optional

# USDA API配置
USDA_API_KEY = os.getenv("USDA_API_KEY", "DEMO_KEY")  # 免费KEY，每小时1000次请求
USDA_API_URL = "https://api.nal.usda.gov/fdc/v1"

# Open Food Facts API配置
OFF_API_URL = "https://world.openfoodfacts.org/api/v2"

# GI数据（从权威来源整理）
GI_DATABASE = {
    # 主食
    "白米饭": 73, "玄米饭": 55, "糙米饭": 55, "杂粮饭": 50,
    "白面包": 75, "全麦面包": 51,
    "面条": 61, "荞麦面": 54, "乌冬面": 55,
    "米粉": 61, "粉丝": 39,
    "饺子": 75, "包子": 70, "馒头": 88,
    "寿司": 48, "意大利面": 49,

    # 蛋白质
    "鸡蛋": 30, "鸡胸肉": 45, "牛肉": 40, "猪肉": 45,
    "鱼": 40, "鲑鱼": 40, "豆腐": 42, "纳豆": 33,
    "牛奶": 27, "酸奶": 36, "芝士": 0,

    # 蔬菜
    "西兰花": 15, "菠菜": 15, "白菜": 10, "胡萝卜": 39,
    "南瓜": 75, "番茄": 38, "黄瓜": 15, "茄子": 15,
    "青椒": 15, "洋葱": 10, "蘑菇": 10,

    # 水果
    "苹果": 36, "香蕉": 52, "柚子": 25, "橙子": 43,
    "草莓": 40, "蓝莓": 53, "奇异果": 53, "葡萄": 59,
    "梨": 38, "桃子": 42, "西瓜": 76,

    # 坚果
    "核桃": 15, "杏仁": 15, "腰果": 22, "花生": 14,
}

# 常吃食物清单（中英日对照）
COMMON_FOODS = {
    # 主食
    "白米饭": {"en": "white rice cooked", "ja": "白米", "category": "主食"},
    "玄米饭": {"en": "brown rice cooked", "ja": "玄米", "category": "主食"},
    "杂粮饭": {"en": "mixed grain rice", "ja": "雑穀米", "category": "主食"},
    "全麦面包": {"en": "whole wheat bread", "ja": "全粒粉パン", "category": "主食"},
    "白面包": {"en": "white bread", "ja": "食パン", "category": "主食"},
    "乌冬面": {"en": "udon noodles", "ja": "うどん", "category": "主食"},
    "荞麦面": {"en": "soba noodles", "ja": "そば", "category": "主食"},
    "饺子": {"en": "dumplings", "ja": "餃子", "category": "主食"},

    # 蛋白质
    "鸡蛋": {"en": "egg", "ja": "卵", "category": "蛋白质"},
    "鸡胸肉": {"en": "chicken breast", "ja": "鶏むね肉", "category": "蛋白质"},
    "牛肉": {"en": "beef", "ja": "牛肉", "category": "蛋白质"},
    "猪肉": {"en": "pork", "ja": "豚肉", "category": "蛋白质"},
    "鱼": {"en": "fish", "ja": "魚", "category": "蛋白质"},
    "鲑鱼": {"en": "salmon", "ja": "サーモン", "category": "蛋白质"},
    "豆腐": {"en": "tofu", "ja": "豆腐", "category": "蛋白质"},
    "纳豆": {"en": "natto", "ja": "納豆", "category": "蛋白质"},
    "牛奶": {"en": "milk", "ja": "牛乳", "category": "蛋白质"},
    "酸奶": {"en": "yogurt", "ja": "ヨーグルト", "category": "蛋白质"},

    # 蔬菜
    "西兰花": {"en": "broccoli", "ja": "ブロッコリー", "category": "蔬菜"},
    "菠菜": {"en": "spinach", "ja": "ほうれん草", "category": "蔬菜"},
    "白菜": {"en": "napa cabbage", "ja": "白菜", "category": "蔬菜"},
    "胡萝卜": {"en": "carrot", "ja": "人参", "category": "蔬菜"},
    "南瓜": {"en": "pumpkin", "ja": "かぼちゃ", "category": "蔬菜"},
    "番茄": {"en": "tomato", "ja": "トマト", "category": "蔬菜"},
    "黄瓜": {"en": "cucumber", "ja": "きゅうり", "category": "蔬菜"},
    "茄子": {"en": "eggplant", "ja": "なす", "category": "蔬菜"},
    "青椒": {"en": "green pepper", "ja": "ピーマン", "category": "蔬菜"},
    "洋葱": {"en": "onion", "ja": "玉ねぎ", "category": "蔬菜"},

    # 水果
    "苹果": {"en": "apple", "ja": "りんご", "category": "水果"},
    "香蕉": {"en": "banana", "ja": "バナナ", "category": "水果"},
    "柚子": {"en": "grapefruit", "ja": "グレープフルーツ", "category": "水果"},
    "橙子": {"en": "orange", "ja": "オレンジ", "category": "水果"},
    "草莓": {"en": "strawberry", "ja": "いちご", "category": "水果"},
    "蓝莓": {"en": "blueberry", "ja": "ブルーベリー", "category": "水果"},
    "奇异果": {"en": "kiwi", "ja": "キウイ", "category": "水果"},
    "葡萄": {"en": "grape", "ja": "ぶどう", "category": "水果"},

    # 坚果
    "核桃": {"en": "walnut", "ja": "くるみ", "category": "坚果"},
    "杏仁": {"en": "almond", "ja": "アーモンド", "category": "坚果"},
    "腰果": {"en": "cashew", "ja": "カシューナッツ", "category": "坚果"},
    "花生": {"en": "peanut", "ja": "ピーナッツ", "category": "坚果"},
}


def search_usda_food(query: str) -> Optional[Dict]:
    """
    从USDA数据库搜索食物

    Args:
        query: 英文食物名称

    Returns:
        dict: 食物营养数据，如果找不到返回None
    """
    try:
        url = f"{USDA_API_URL}/foods/search"
        params = {
            "api_key": USDA_API_KEY,
            "query": query,
            "pageSize": 1,
            "dataType": ["Foundation", "SR Legacy"]  # 使用基础数据和传统数据
        }

        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()
            if data.get("foods") and len(data["foods"]) > 0:
                food = data["foods"][0]

                # 提取营养成分
                nutrients = {}
                for nutrient in food.get("foodNutrients", []):
                    name = nutrient.get("nutrientName", "").lower()
                    value = nutrient.get("value", 0)

                    if "carbohydrate" in name:
                        nutrients["carbs"] = round(value, 1)
                    elif "protein" in name:
                        nutrients["protein"] = round(value, 1)
                    elif "total lipid" in name or "fat" in name:
                        nutrients["fat"] = round(value, 1)
                    elif "fiber" in name:
                        nutrients["fiber"] = round(value, 1)
                    elif "energy" in name and "kcal" in name.lower():
                        nutrients["calories"] = int(value)

                return nutrients

        return None

    except Exception as e:
        print(f"  ⚠️ USDA查询失败：{str(e)}")
        return None


def search_openfoodfacts(query: str) -> Optional[Dict]:
    """
    从Open Food Facts搜索食物和照片

    Args:
        query: 英文食物名称

    Returns:
        dict: 包含照片URL和营养数据
    """
    try:
        url = f"{OFF_API_URL}/search"
        params = {
            "search_terms": query,
            "page_size": 1,
            "fields": "product_name,image_url,nutriments"
        }

        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()
            if data.get("products") and len(data["products"]) > 0:
                product = data["products"][0]

                result = {
                    "image_url": product.get("image_url"),
                    "nutrients": {}
                }

                nutriments = product.get("nutriments", {})
                if "carbohydrates_100g" in nutriments:
                    result["nutrients"]["carbs"] = round(nutriments["carbohydrates_100g"], 1)
                if "proteins_100g" in nutriments:
                    result["nutrients"]["protein"] = round(nutriments["proteins_100g"], 1)
                if "fat_100g" in nutriments:
                    result["nutrients"]["fat"] = round(nutriments["fat_100g"], 1)
                if "fiber_100g" in nutriments:
                    result["nutrients"]["fiber"] = round(nutriments["fiber_100g"], 1)
                if "energy-kcal_100g" in nutriments:
                    result["nutrients"]["calories"] = int(nutriments["energy-kcal_100g"])

                return result

        return None

    except Exception as e:
        print(f"  ⚠️ Open Food Facts查询失败：{str(e)}")
        return None


def add_tags(food_data: Dict) -> Dict:
    """添加标签"""
    tags = []

    # 类别标签
    category_icons = {
        "主食": "🍚",
        "蛋白质": "🥩",
        "蔬菜": "🥬",
        "水果": "🍎",
        "坚果": "🥜"
    }

    category = food_data.get("category", "其他")
    tags.append({
        "type": "category",
        "label": category,
        "icon": category_icons.get(category, "🍽️"),
        "color": "#FFB84D" if category == "主食" else "#4CAF50"
    })

    # GI标签
    gi_value = food_data.get("gi", {}).get("value", 0)
    if gi_value < 55:
        gi_level = "低GI"
        gi_color = "#4CAF50"
        gi_icon = "✅"
    elif gi_value <= 70:
        gi_level = "中GI"
        gi_color = "#FFA500"
        gi_icon = "⚠️"
    else:
        gi_level = "高GI"
        gi_color = "#F44336"
        gi_icon = "❌"

    tags.append({
        "type": "gi",
        "label": gi_level,
        "icon": gi_icon,
        "color": gi_color
    })

    # 碳水标签
    carbs = food_data.get("nutrition", {}).get("carbs", 0)
    if carbs < 10:
        carb_level = "低碳水"
        carb_color = "#4CAF50"
        carb_icon = "✅"
    elif carbs <= 20:
        carb_level = "中碳水"
        carb_color = "#FFA500"
        carb_icon = "⚠️"
    else:
        carb_level = "高碳水"
        carb_color = "#F44336"
        carb_icon = "❌"

    tags.append({
        "type": "carb",
        "label": carb_level,
        "icon": carb_icon,
        "color": carb_color
    })

    food_data["tags"] = tags
    food_data["carbLevel"] = {
        "value": carb_level,
        "color": carb_color.replace("#", "")
    }

    return food_data


def build_database():
    """构建食物数据库"""
    print("=" * 60)
    print("🍽️  从公开API构建食物标签数据库")
    print("=" * 60)
    print(f"\n📋 将处理 {len(COMMON_FOODS)} 种常吃食物")
    print("-" * 60)

    foods = []

    for idx, (zh_name, info) in enumerate(COMMON_FOODS.items(), 1):
        print(f"\n[{idx}/{len(COMMON_FOODS)}] 🔍 查询：{zh_name}")

        en_name = info["en"]
        ja_name = info["ja"]
        category = info["category"]

        # 从USDA获取营养数据
        nutrients = search_usda_food(en_name)
        if not nutrients:
            print(f"  ⚠️ USDA未找到，尝试Open Food Facts...")
            off_data = search_openfoodfacts(en_name)
            if off_data:
                nutrients = off_data.get("nutrients", {})
                print(f"  ✅ Open Food Facts找到数据")
            else:
                print(f"  ❌ 未找到营养数据，跳过")
                continue
        else:
            print(f"  ✅ USDA找到数据")

        # 构建食物数据
        food_data = {
            "id": f"food_{idx:03d}",
            "name": {
                "zh": zh_name,
                "ja": ja_name,
                "en": en_name.title()
            },
            "aliases": [zh_name, ja_name, en_name],
            "category": category,
            "categoryIcon": {"主食": "🍚", "蛋白质": "🥩", "蔬菜": "🥬",
                           "水果": "🍎", "坚果": "🥜"}.get(category, "🍽️"),
            "nutrition": nutrients,
            "gi": {
                "value": GI_DATABASE.get(zh_name, 50),
                "level": "",
                "color": ""
            }
        }

        # 添加推荐
        carbs = nutrients.get("carbs", 0)
        gi = GI_DATABASE.get(zh_name, 50)

        if gi < 55 and carbs < 15:
            level = "强烈推荐"
            emoji = "💚"
            reason = "低GI、低碳水，对血糖影响很小"
        elif gi < 70 and carbs < 25:
            level = "推荐"
            emoji = "✅"
            reason = "中等GI和碳水，适量食用"
        else:
            level = "谨慎"
            emoji = "⚠️"
            reason = "较高GI或碳水，需要控制摄入量"

        food_data["recommendation"] = {
            "level": level,
            "emoji": emoji,
            "reason": reason,
            "tips": f"建议每餐{category}摄入适量"
        }

        # 添加标签
        food_data = add_tags(food_data)

        foods.append(food_data)

        # 避免API限流
        time.sleep(0.2)

    print("\n" + "=" * 60)
    print(f"✅ 数据库构建完成！成功获取 {len(foods)} 种食物")
    print("=" * 60)

    # 生成数据库
    database = {
        "version": "1.0",
        "description": "糖妈日记 - 食物标签数据库（从USDA+Open Food Facts构建）",
        "createdAt": "2025-12-19",
        "dataSource": ["USDA FoodData Central", "Open Food Facts", "Sydney University GI Database"],
        "totalFoods": len(foods),
        "foods": foods
    }

    # 保存文件
    output_file = "food-tags-database.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(database, f, ensure_ascii=False, indent=2)

    print(f"\n💾 数据库已保存到：{output_file}")
    print(f"\n📊 数据库统计：")
    print(f"   - 总食物数：{len(foods)}")

    for cat in ["主食", "蛋白质", "蔬菜", "水果", "坚果"]:
        count = len([f for f in foods if f["category"] == cat])
        print(f"   - {cat}：{count}")

    print("\n✨ 完成！可以在应用中使用这个数据库了。")


if __name__ == "__main__":
    build_database()
