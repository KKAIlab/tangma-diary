# 知食奶爸 ZHISHI PAPA · 从怀孕到育儿的健康饮食科普 🌿

<p align="center"><img src="assets/images/logo.svg" width="96" alt="知食奶爸 Logo"></p>

> 「知食，也是知识」——由一位外科医生、医学生化学博士，同时也是陪太太走过妊娠糖尿病的奶爸打造的健康饮食科普网站，覆盖备孕、孕期、产后、辅食、宝宝餐桌五个阶段。

**🌐 网站地址**：https://kkailab.github.io/tangma-diary/

**🩸 血糖记录工具**（品牌前身「糖妈日记」应用，老用户数据不受影响）：https://kkailab.github.io/tangma-diary/app/

## ✍️ 怎么发布新文章（最重要）

**不需要写代码。** 在 GitHub 网页上（手机也行）：

1. 打开 [`_posts` 文件夹](./_posts) → **Add file → Create new file**
2. 文件名：`2026-07-15-wenzhang-mingzi.md`（日期-英文短名.md）
3. 粘贴模板写内容：

```markdown
---
title: 文章标题
date: 2026-07-15
categories: [孕期]        # 五选一：备孕 / 孕期 / 产后 / 辅食 / 宝宝餐桌
tags: [控糖, 食谱]        # 随意
description: 一句话摘要
---

正文，直接写 Markdown。
```

4. 点 **Commit changes** → 约1分钟后自动上线 🎉

详细图文教程见网站上的 [写作指南](https://kkailab.github.io/tangma-diary/write/)。

## 📁 目录结构

```
├── _config.yml        # 站点配置：名称、简介、作者、分类（有中文注释）
├── _posts/            # ✍️ 文章都在这里，一篇一个 .md 文件
├── assets/images/     # 文章图片
├── about.md           # 「关于我」页面（个人IP主页，记得完善）
├── write.md           # 写作指南页面
├── index.html         # 首页
├── archive.md         # 全部文章归档页
├── categories/        # 5个分类页
├── _layouts/ _includes/ assets/css/   # 页面模板和样式
├── app/               # 旧版血糖记录工具（原样保留）
├── scripts/           # 食物数据库构建脚本（开发用）
└── docs/legacy/       # 旧版应用的文档存档
```

## 🎨 常用自定义

| 想改什么 | 改哪里 |
|----------|--------|
| 网站名称、简介、作者、社交账号 | `_config.yml`（有中文注释） |
| 「关于我」页面 | `about.md` |
| 配色、字体 | `assets/css/main.css` 顶部的 `:root` 变量 |
| 分类增删 | `_config.yml` 的 `nav_categories` + `categories/` 里加对应页面 |

## 🛠️ 技术说明

- [Jekyll](https://jekyllrb.com/) 静态站点，GitHub Pages 自动构建，无需服务器
- 已内置 SEO 标签（jekyll-seo-tag）、RSS 订阅（`/feed.xml`）、站点地图（`/sitemap.xml`）
- 本地预览（可选）：

```bash
gem install jekyll jekyll-feed jekyll-seo-tag jekyll-sitemap webrick
jekyll serve
# 打开 http://127.0.0.1:4000/tangma-diary/
```

## ⚠️ 内容声明

本站内容为健康科普，仅供参考，不能替代医生、注册营养师的专业建议。

## 📄 许可证

MIT License
