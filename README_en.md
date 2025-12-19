# GDM Diary 📱

> Gestational Diabetes Mellitus (GDM) Management App
> Helping expectant mothers track blood glucose and maintain healthy pregnancy

[![语言: 中文](https://img.shields.io/badge/语言-中文-red)](./README.md)
[![Language: English](https://img.shields.io/badge/Language-English-blue)](./README_en.md)
[![言語: 日本語](https://img.shields.io/badge/言語-日本語-green)](./README_ja.md)

## 🌟 Features

### ✅ Free & Privacy-First
- ❌ No account required
- ❌ No data uploaded to servers
- ✅ All data stored locally in your device
- ✅ Completely free, no ads

### 📝 Easy Recording
- **Record entire day with one submission**
  - Input breakfast, lunch, and dinner at once
  - Add weight, fasting glucose, steps, and notes simultaneously
- Track food intake, blood glucose, and measurement time
- Backfill historical data

### 📊 Data Analysis
- Automatic weekly success rate calculation
- Average postprandial glucose
- Blood glucose trend charts
- Meal-specific glucose analysis

### 🏥 Japan Healthcare Support
- **Built-in Japanese medical terminology reference**
  - Common terms used in Japanese obstetrics clinics
  - Romaji pronunciation guide
  - Chinese and English translations
- Compliant with Japanese GDM management standards
- Japanese prenatal checkup schedule reference

### 🌐 Multilingual Support
- 🇨🇳 中文 (Simplified Chinese)
- 🇯🇵 日本語 (Japanese)
- 🇬🇧 English
- One-click language switching

### 💾 Data Management
- Export data as JSON files
- Import to other devices
- Regular backups recommended

---

## 🚀 Getting Started

### Online Version (Recommended)
**URL**: https://kkailab.github.io/tangma-diary/

1. Open the URL in your browser
2. Add to home screen (PWA supported)
3. Start using immediately

### Add to Home Screen

#### iPhone (Safari)
1. Open the app in Safari
2. Tap the Share button (bottom of screen)
3. Select "Add to Home Screen"
4. Tap "Add"
5. App icon appears on home screen

#### Android (Chrome)
1. Open the app in Chrome
2. Tap the menu (⋮) in top right
3. Select "Add to Home screen"
4. Tap "Add"

---

## 📖 Usage Examples

### Scenario 1: Morning Record

```
【After waking up】
1. Open the app
2. Date: Today (automatic)
3. Weight: 67.5 kg
4. Fasting glucose: 92 mg/dL

【2 hours after breakfast】
5. Breakfast section:
   - Foods: Brown rice, egg, broccoli
   - Postprandial glucose: 112 mg/dL
   - Measurement time: 08:30

6. Tap "Save" button
→ All data saved at once
```

### Scenario 2: Record Full Day at Once

```
【Before bed, record the entire day】
1. Date: Today
2. Daily data:
   - Weight: 67.3 kg
   - Fasting glucose: 88 mg/dL
   - Steps: 7200
   - Notes: Feeling good, walked 30 minutes

3. Breakfast:
   - Foods: Brown rice, natto, miso soup
   - Glucose: 110 mg/dL
   - Time: 07:30

4. Lunch:
   - Foods: Chicken breast, vegetables, brown rice
   - Glucose: 118 mg/dL
   - Time: 12:30

5. Dinner:
   - Foods: Fish, tofu, brown rice
   - Glucose: 108 mg/dL
   - Time: 18:30

6. Tap "Save" button
→ Entire day's data saved!
```

---

## 🏥 Japanese GDM Management Standards

This app follows the Japan Society of Obstetrics and Gynecology guidelines:

| Measurement | Target Value | Notes |
|------------|--------------|-------|
| Fasting Glucose | < 92 mg/dL | Before breakfast (after 8h fasting) |
| 1-hour Postprandial | < 140 mg/dL | 1 hour after meal start |
| 2-hour Postprandial | < 120 mg/dL | 2 hours after meal start |
| HbA1c | < 5.8% (NGSP) | Reflects 3-month average glucose |

---

## 💡 Detailed Features

### 📅 Recordable Data

#### Daily Metrics
- ⚖️ Weight (kg)
- 🩸 Fasting Blood Glucose (mg/dL)
- 👣 Steps
- 📝 Notes (symptoms, special conditions)

#### Meal Records
For each meal:
- 🍚 Food items (multiple entries supported)
- 🩸 Postprandial Glucose (mg/dL)
- ⏰ Measurement Time

### 📊 Statistics Features

- **Weekly Success Rate**: Percentage of glucose readings within target range
- **Average Postprandial Glucose**: Mean of all post-meal readings
- **Glucose Trend Chart**: Visualize daily changes
- **Meal-Specific Analysis**: Patterns for breakfast, lunch, dinner

### 🏥 Japanese Medical Terminology Reference

Included term categories:
1. **Medical Facilities**: OB/GYN, General Hospital, Clinic
2. **Tests**: Prenatal checkup, Blood test, OGTT
3. **Glucose-Related**: Fasting glucose, Postprandial glucose, HbA1c
4. **Treatments**: Diet therapy, Exercise therapy, Insulin therapy
5. **Common Phrases**: Making appointments, describing symptoms

Each term includes:
- ✅ Japanese characters
- ✅ Romaji pronunciation
- ✅ Chinese translation
- ✅ English translation
- ✅ Additional notes (target values, etc.)

---

## ⚠️ Important Information

### Data Storage
- All data is stored in browser localStorage
- Data will be lost if browser cache is cleared
- **Weekly backups recommended**

### Backup Method
1. "Guide" → "Data Management"
2. Tap "📤 Export Data"
3. Save JSON file to safe location
   - Cloud storage (Google Drive, iCloud, etc.)
   - Email to yourself
   - Copy to PC

### Data Restoration
1. "Guide" → "Data Management"
2. Tap "📥 Import Data"
3. Select saved JSON file

---

## 🆘 FAQ

### Q1: Do I need to register?
**A**: No registration required. Just open the browser and start using.

### Q2: Where is my data stored?
**A**: All data is stored locally on your device (browser localStorage). Nothing is uploaded to servers.

### Q3: Can I sync across devices?
**A**: Use export/import features to transfer data between devices. Automatic sync is not supported.

### Q4: Can I use it without knowing English?
**A**: Yes, Chinese and Japanese languages are supported. Use the language switcher in the top right.

### Q5: Can I share data with my doctor?
**A**: Yes, use "Export Data" to download a JSON file that can be emailed or shown directly.

### Q6: Does it work offline?
**A**: Yes, once accessed, it works offline (PWA functionality).

### Q7: Works on both iPhone and Android?
**A**: Yes, compatible with all major browsers: Chrome, Safari, Edge, Firefox.

---

## 🎯 For Chinese Women in Japan

This app was developed specifically for **Chinese women diagnosed with GDM in Japan**.

### Problems Solved

1. **Language Barrier**
   - Unfamiliar with Japanese medical terminology
   - Difficulty understanding prenatal checkups
   - Can't interpret test results

2. **Recording Burden**
   - Daily glucose testing is tedious
   - Multiple entries are time-consuming
   - Hard to maintain consistency

3. **Doctor Communication**
   - Can't effectively share data
   - Unable to ask questions in Japanese

### App Advantages

✅ **Japanese medical terminology reference** overcomes language barriers
✅ **One-time entry for full day** reduces recording burden
✅ **Data export feature** enables smooth doctor communication
✅ **Free & privacy-protected** for peace of mind

---

## 📞 Support & Feedback

### Report Issues
If you find bugs or problems:
- **GitHub Issues**: https://github.com/KKAIlab/tangma-diary/issues

### Feature Requests
To suggest new features:
- Create an Issue on GitHub

### Contribute
This is an open-source project. Pull requests are welcome!

---

## 📜 License

MIT License - Free to use, modify, and distribute

---

## ❤️ From the Developer

Managing gestational diabetes is challenging, but crucial for both mother and baby's health.

We hope this app helps Chinese women in Japan manage their health and approach childbirth with confidence.

**Wishing you a healthy pregnancy and a joyful meeting with your baby!** 🤰✨

---

**Version**: v2.0 (Multilingual Edition)
**Last Updated**: 2025-12-19
**Website**: https://kkailab.github.io/tangma-diary/

---

## 🔗 Related Links

- [中文版说明](./README.md)
- [日本語版 README](./README_ja.md)
- [使用指南（中文）](./新功能使用指南.md)
- [快速测试流程（中文）](./快速测试.md)
