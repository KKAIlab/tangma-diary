# Google Drive 云端同步配置指南

## 📋 概述

糖妈日记现已支持 Google Drive 云端同步功能！您可以将数据自动备份到 Google Drive，实现多设备无缝同步。

## 🎯 功能特点

- ✅ **自动备份**：每次保存数据时自动上传到 Google Drive
- ✅ **多设备同步**：手机、平板、电脑数据实时同步
- ✅ **智能恢复**：打开应用时自动检查云端更新
- ✅ **数据安全**：数据存储在您自己的 Google Drive，完全私密
- ✅ **离线可用**：无网络时使用本地数据，有网络时自动同步

## ⚙️ 配置步骤

### 第一步：创建 Google Cloud 项目

1. 访问 [Google Cloud Console](https://console.cloud.google.com/)
2. 点击顶部的项目选择器，创建新项目
3. 项目名称：`tangma-diary` （可自定义）
4. 点击"创建"

### 第二步：启用 Google Drive API

1. 在项目仪表板中，点击"启用 API 和服务"
2. 搜索"Google Drive API"
3. 点击"Google Drive API"
4. 点击"启用"

### 第三步：创建 OAuth 2.0 客户端ID

1. 在左侧菜单选择"凭据"（Credentials）
2. 点击"+ 创建凭据" → "OAuth 客户端ID"

3. **首次使用需要配置同意屏幕**：
   - 点击"配置同意屏幕"
   - 用户类型选择"外部"
   - 填写基本信息：
     - 应用名称：`糖妈日记`
     - 用户支持电子邮件：您的邮箱
     - 开发者联系信息：您的邮箱
   - 点击"保存并继续"
   - 作用域：不需要添加，直接"保存并继续"
   - 测试用户：添加您自己的Gmail账号
   - 完成配置

4. **创建 OAuth 客户端ID**：
   - 应用类型：选择"Web 应用"
   - 名称：`tangma-diary-web`
   - 已获授权的 JavaScript 来源：
     ```
     https://kkailab.github.io
     ```
     如果您使用本地测试，还需要添加：
     ```
     http://localhost
     http://127.0.0.1
     ```
   - 已获授权的重定向 URI：
     ```
     https://kkailab.github.io/tangma-diary/
     ```
   - 点击"创建"

5. **保存凭据信息**：
   - 创建成功后会显示客户端ID和客户端密钥
   - 复制 **客户端ID**（格式类似：`xxxxx.apps.googleusercontent.com`）

### 第四步：配置应用代码

打开 `index.html`，找到 Google API 配置部分（约在第 854 行）：

```javascript
const GOOGLE_CONFIG = {
    // TODO: 请替换为您自己的 OAuth 客户端ID
    CLIENT_ID: 'YOUR_CLIENT_ID.apps.googleusercontent.com',  // ← 替换这里
    API_KEY: 'YOUR_API_KEY',  // ← 可选，留空也可以
    DISCOVERY_DOCS: ['https://www.googleapis.com/discovery/v1/apis/drive/v3/rest'],
    SCOPES: 'https://www.googleapis.com/auth/drive.file',
    FILE_NAME: 'tangma-diary-data.json',
    FILE_MIME_TYPE: 'application/json'
};
```

替换为您的客户端ID：

```javascript
const GOOGLE_CONFIG = {
    CLIENT_ID: '123456789-abc123def456.apps.googleusercontent.com',  // ← 您的客户端ID
    API_KEY: '',  // 可以留空
    DISCOVERY_DOCS: ['https://www.googleapis.com/discovery/v1/apis/drive/v3/rest'],
    SCOPES: 'https://www.googleapis.com/auth/drive.file',
    FILE_NAME: 'tangma-diary-data.json',
    FILE_MIME_TYPE: 'application/json'
};
```

### 第五步：部署并测试

1. 将修改后的代码推送到 GitHub
2. 等待 GitHub Pages 部署完成（通常1-2分钟）
3. 访问您的应用
4. 进入"指南"页面 → "数据管理"
5. 点击"连接 Google Drive"
6. 授权应用访问您的 Google Drive
7. 连接成功后，点击"立即备份"测试上传功能

## 🧪 测试验证

### 测试备份功能：
1. 添加一条新记录
2. 数据会自动备份到 Google Drive
3. 查看控制台，应显示"✅ 自动备份到 Google Drive 成功"

### 测试多设备同步：
1. 在设备A添加记录
2. 在设备B打开应用
3. 应提示"检测到云端有更新的数据"
4. 确认恢复，数据同步成功

### 测试手动恢复：
1. 清除本地所有数据
2. 点击"恢复数据"
3. 数据从 Google Drive 恢复成功

## 📂 数据存储位置

数据文件保存在您的 Google Drive 根目录：
```
我的云端硬盘/
  └─ tangma-diary-data.json
```

您可以：
- ✅ 在 Google Drive 中查看此文件
- ✅ 下载此文件作为额外备份
- ✅ 将此文件分享给他人（导入到他们的应用）
- ❌ 不要手动编辑或删除此文件

## 🔒 隐私说明

- **数据安全**：数据存储在您自己的 Google Drive，只有您可以访问
- **权限范围**：应用仅请求访问由应用创建的文件权限（`drive.file`）
- **数据加密**：传输过程使用 HTTPS 加密
- **第三方访问**：我们无法访问您的数据，数据完全归您所有

## ❓ 常见问题

### Q1: 配置后仍无法连接？
**A**: 检查以下几点：
1. 客户端ID是否正确复制（包含完整的 `.apps.googleusercontent.com`）
2. 已获授权的来源是否包含您的域名
3. 浏览器是否禁用了第三方Cookie
4. 尝试清除浏览器缓存后重试

### Q2: 提示"未验证的应用"？
**A**: 这是正常的，因为应用处于测试模式：
1. 点击"高级"
2. 点击"前往 tangma-diary（不安全）"
3. 这是您自己创建的应用，完全安全

### Q3: 同步失败怎么办？
**A**:
1. 检查网络连接
2. 查看浏览器控制台的错误信息
3. 尝试断开连接后重新连接
4. 检查 Google Drive 存储空间是否充足

### Q4: 可以使用多个Google账号吗？
**A**: 可以，但：
- 每个设备只能连接一个账号
- 切换账号需要先断开当前连接
- 不同账号的数据是独立的，不会互相同步

### Q5: 配置需要付费吗？
**A**:
- **Google Cloud** 免费额度足够个人使用
- **Google Drive** 使用您的免费存储空间（15GB）
- **应用本身** 完全免费开源

## 🛠️ 开发者说明

### API 权限范围
使用最小权限原则：
```javascript
SCOPES: 'https://www.googleapis.com/auth/drive.file'
```
只能访问应用创建的文件，无法访问用户的其他文件。

### 文件操作
- 首次上传：POST 创建文件
- 后续更新：PATCH 更新文件
- 文件搜索：按名称查找
- 文件下载：使用 `alt=media` 参数

### 错误处理
- Token 过期：自动提示重新登录
- 网络错误：静默失败，不影响本地保存
- 上传失败：仅记录日志，不干扰用户操作

## 📞 需要帮助？

如果遇到配置问题，请：
1. 查看浏览器控制台的错误信息
2. 提交 Issue 到 GitHub 仓库
3. 附上详细的错误描述和截图

---

**配置完成后，您就可以享受多设备无缝同步的便利了！** 🎉
