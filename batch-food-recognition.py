#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
糖妈日记 - 批量食物识别脚本
使用Claude Vision API识别食物照片并生成标签数据库
"""

import os
import json
import base64
from pathlib import Path
from anthropic import Anthropic

# 配置
PHOTOS_DIR = "./food-photos"  # 食物照片目录
OUTPUT_FILE = "./food-tags-database.json"  # 输出数据库文件
API_KEY = os.getenv("ANTHROPIC_API_KEY")  # 从环境变量读取API密钥

# 初始化Claude客户端
client = Anthropic(api_key=API_KEY)

# 食物识别提示词模板
RECOGNITION_PROMPT = """
你是一位专业的营养师，专门为妊娠期糖尿病（GDM）患者提供饮食建议。

请识别图片中的食物，并按照以下JSON格式返回：

{
  "name": {
    "zh": "中文名称",
    "ja": "日语名称",
    "en": "英文名称"
  },
  "aliases": ["别名1", "别名2"],
  "category": "主食/蛋白质/蔬菜/水果/坚果",
  "nutrition": {
    "carbs": 碳水化合物含量(g/100g),
    "protein": 蛋白质含量(g/100g),
    "fat": 脂肪含量(g/100g),
    "fiber": 膳食纤维含量(g/100g),
    "calories": 热量(kcal/100g)
  },
  "gi": GI值(数字),
  "recommendation": {
    "level": "强烈推荐/推荐/适量/谨慎/避免",
    "reason": "推荐理由",
    "tips": "食用建议"
  }
}

注意事项：
1. 如果图片中有多种食物，请分别识别每种食物
2. 营养数据要准确，基于权威营养数据库
3. GI值要基于国际GI数据库
4. 推荐理由要结合GDM患者需求
5. 食用建议要具体实用

请只返回JSON格式的数据，不要添加任何其他文字。
"""


def encode_image(image_path):
    """将图片编码为base64"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def get_image_media_type(image_path):
    """根据文件扩展名返回媒体类型"""
    ext = Path(image_path).suffix.lower()
    media_types = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp"
    }
    return media_types.get(ext, "image/jpeg")


def recognize_food(image_path):
    """
    使用Claude Vision API识别单张食物照片

    Args:
        image_path: 图片文件路径

    Returns:
        dict: 识别结果（JSON格式）
    """
    print(f"🔍 正在识别：{image_path}")

    try:
        # 编码图片
        image_data = encode_image(image_path)
        media_type = get_image_media_type(image_path)

        # 调用Claude Vision API
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2048,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": media_type,
                                "data": image_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": RECOGNITION_PROMPT
                        }
                    ],
                }
            ],
        )

        # 提取响应文本
        response_text = message.content[0].text

        # 解析JSON
        food_data = json.loads(response_text)

        print(f"✅ 识别成功：{food_data['name']['zh']}")

        return food_data

    except Exception as e:
        print(f"❌ 识别失败：{str(e)}")
        return None


def add_tags(food_data):
    """
    根据营养数据自动添加标签

    Args:
        food_data: 食物数据

    Returns:
        dict: 添加标签后的食物数据
    """
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
    gi_value = food_data.get("gi", 0)
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

    food_data["gi"] = {
        "value": gi_value,
        "level": gi_level,
        "color": gi_color.replace("#", "")
    }

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

    food_data["carbLevel"] = {
        "value": carb_level,
        "color": carb_color.replace("#", ""),
        "recommendation": "推荐食用" if carbs < 10 else "适量食用" if carbs <= 20 else "控制摄入"
    }

    food_data["tags"] = tags
    food_data["categoryIcon"] = category_icons.get(category, "🍽️")

    return food_data


def batch_recognize(photos_dir, output_file):
    """
    批量识别食物照片

    Args:
        photos_dir: 照片目录
        output_file: 输出JSON文件路径
    """
    print("=" * 60)
    print("🍽️  糖妈日记 - 批量食物识别")
    print("=" * 60)

    # 确保照片目录存在
    photos_path = Path(photos_dir)
    if not photos_path.exists():
        print(f"❌ 错误：照片目录不存在：{photos_dir}")
        return

    # 获取所有图片文件
    image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".webp"]
    image_files = []
    for ext in image_extensions:
        image_files.extend(photos_path.glob(f"*{ext}"))
        image_files.extend(photos_path.glob(f"*{ext.upper()}"))

    if not image_files:
        print(f"❌ 错误：在 {photos_dir} 中未找到图片文件")
        return

    print(f"\n📷 找到 {len(image_files)} 张照片")
    print("-" * 60)

    # 识别所有食物
    foods = []
    for idx, image_path in enumerate(image_files, 1):
        print(f"\n[{idx}/{len(image_files)}] ", end="")

        food_data = recognize_food(str(image_path))

        if food_data:
            # 添加ID和图片路径
            food_data["id"] = f"food_{idx:03d}"
            food_data["imageUrl"] = f"photos/{image_path.name}"
            food_data["recognitionConfidence"] = 0.95  # 可以根据实际情况调整

            # 自动添加标签
            food_data = add_tags(food_data)

            foods.append(food_data)

    print("\n" + "=" * 60)
    print(f"✅ 识别完成！成功识别 {len(foods)}/{len(image_files)} 种食物")
    print("=" * 60)

    # 生成完整数据库
    database = {
        "version": "1.0",
        "description": "糖妈日记 - 食物标签数据库",
        "createdAt": "2025-12-19",
        "totalFoods": len(foods),
        "foods": foods,
        "categories": [
            {
                "id": "staple",
                "name": "主食",
                "icon": "🍚",
                "color": "#FFB84D",
                "description": "米饭、面条、面包等碳水化合物主要来源"
            },
            {
                "id": "protein",
                "name": "蛋白质",
                "icon": "🥩",
                "color": "#E57373",
                "description": "肉类、蛋类、豆制品等蛋白质来源"
            },
            {
                "id": "vegetable",
                "name": "蔬菜",
                "icon": "🥬",
                "color": "#4CAF50",
                "description": "各类蔬菜，富含膳食纤维"
            },
            {
                "id": "fruit",
                "name": "水果",
                "icon": "🍎",
                "color": "#FF6B9D",
                "description": "各类水果，注意糖分含量"
            },
            {
                "id": "nuts",
                "name": "坚果",
                "icon": "🥜",
                "color": "#8D6E63",
                "description": "坚果、种子类食物"
            }
        ],
        "giLevels": [
            {
                "level": "低GI",
                "range": "< 55",
                "color": "#4CAF50",
                "icon": "✅",
                "recommendation": "推荐"
            },
            {
                "level": "中GI",
                "range": "55-70",
                "color": "#FFA500",
                "icon": "⚠️",
                "recommendation": "适量"
            },
            {
                "level": "高GI",
                "range": "> 70",
                "color": "#F44336",
                "icon": "❌",
                "recommendation": "避免"
            }
        ],
        "carbLevels": [
            {
                "level": "低碳水",
                "range": "< 10g/100g",
                "color": "#4CAF50",
                "icon": "✅",
                "recommendation": "推荐"
            },
            {
                "level": "中碳水",
                "range": "10-20g/100g",
                "color": "#FFA500",
                "icon": "⚠️",
                "recommendation": "适量"
            },
            {
                "level": "高碳水",
                "range": "> 20g/100g",
                "color": "#F44336",
                "icon": "❌",
                "recommendation": "控制"
            }
        ]
    }

    # 保存到文件
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(database, f, ensure_ascii=False, indent=2)

    print(f"\n💾 数据库已保存到：{output_file}")
    print(f"📊 数据库统计：")
    print(f"   - 总食物数：{len(foods)}")
    print(f"   - 主食：{len([f for f in foods if f['category'] == '主食'])}")
    print(f"   - 蛋白质：{len([f for f in foods if f['category'] == '蛋白质'])}")
    print(f"   - 蔬菜：{len([f for f in foods if f['category'] == '蔬菜'])}")
    print(f"   - 水果：{len([f for f in foods if f['category'] == '水果'])}")
    print(f"   - 坚果：{len([f for f in foods if f['category'] == '坚果'])}")


if __name__ == "__main__":
    # 检查API密钥
    if not API_KEY:
        print("❌ 错误：未设置 ANTHROPIC_API_KEY 环境变量")
        print("\n请先设置API密钥：")
        print("export ANTHROPIC_API_KEY='your-api-key-here'")
        exit(1)

    # 运行批量识别
    batch_recognize(PHOTOS_DIR, OUTPUT_FILE)

    print("\n✨ 完成！现在可以在应用中使用这个标签数据库了。")
