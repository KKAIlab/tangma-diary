---
layout: page
title: 写作指南
permalink: /write/
description: 如何在「知食奶爸」网站发布新文章——手机和电脑都可以，3分钟学会
---

这个网站的发布方式非常简单：**在 GitHub 上新建一个 Markdown 文件，保存后约 1 分钟自动上线。** 手机浏览器也能操作。

## 发布一篇新文章（3步）

### 第 1 步：新建文件

打开 [`_posts` 文件夹](https://github.com/KKAIlab/tangma-diary/tree/main/_posts)，点击 **Add file → Create new file**。

文件名必须是这个格式（英文小写，用 `-` 连接）：

```
2026-07-15-wenzhang-biaoti.md
```

- 前面是发布日期 `年-月-日`
- 后面是文章的英文短名（会成为网址的一部分）

### 第 2 步：粘贴模板，开始写

把下面的模板粘贴进去，改成你的内容：

```markdown
---
title: 这里写文章标题
date: 2026-07-15
categories: [孕期]
tags: [控糖, 食谱]
description: 一句话摘要，会显示在首页卡片和搜索结果里
---

正文从这里开始，直接写字就行。

## 用两个井号做小标题

- 用短横线做列表
- 第二条

**两个星号包住的字会加粗**

> 大于号开头的是重点提示框

| 表格 | 也可以 |
|------|--------|
| 食物 | 建议量 |
```

**categories 只能填这五个之一**（对应网站分类）：`备孕`、`孕期`、`产后`、`辅食`、`宝宝餐桌`

**tags 随意填**，几个都行，比如 `[控糖, 早餐, 食谱]`。

### 第 3 步：保存发布

拉到页面底部（手机版点右上角 **Commit changes**），点绿色按钮提交。等 1 分钟左右，刷新网站首页就能看到新文章了 🎉

## 插入图片

1. 打开 [`assets/images` 文件夹](https://github.com/KKAIlab/tangma-diary/tree/main/assets/images)，点 **Add file → Upload files** 上传图片
2. 在文章里这样引用：

```markdown
![图片说明](/tangma-diary/assets/images/你的图片名.jpg)
```

> 💡 更省事的办法：直接在 GitHub 的编辑框里把图片**拖进去/粘贴进去**，它会自动生成图片链接。

## 修改或删除文章

在 [`_posts` 文件夹](https://github.com/KKAIlab/tangma-diary/tree/main/_posts) 里点开对应文件，点铅笔图标 ✏️ 编辑，保存后同样自动更新。删除文件即下架文章。

## 常见问题

**文章没显示出来？**
- 检查文件名是否是 `2026-07-15-xxx.md` 格式，日期不能是未来的日期
- 检查开头的 `---` 是否成对（上下各一行）
- 等 2 分钟再刷新，GitHub 构建需要一点时间

**想改网站名称、简介、分类？**
编辑仓库根目录的 `_config.yml` 文件，里面有中文注释。

**想改「关于我」页面？**
编辑根目录的 `about.md`。
