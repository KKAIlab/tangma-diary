// 糖妈日记 - 多语言翻译文件
// GDM Diary - Multi-language Translation File
// 対象：在日中国人妊婦（主に）

const translations = {
  // 中文 (Chinese)
  zh: {
    // 应用标题
    appTitle: '糖妈日记',
    appSubtitle: '妊娠期糖尿病管理',

    // 头部问候
    greeting: '你好，准妈妈 ✨',
    todayDate: '今天',

    // 底部导航
    navHome: '首页',
    navStats: '统计',
    navGI: 'GI查询',
    navGuide: '指南',

    // 统计卡片
    statWeekSuccess: '本周达标率',
    statAvgGlucose: '平均餐后',
    statTodayWeight: '今日体重',
    statTodaySteps: '今日步数',

    // 日期选择器
    weekdays: ['周日', '周一', '周二', '周三', '周四', '周五', '周六'],

    // 餐次
    breakfast: '早餐',
    lunch: '午餐',
    dinner: '晚餐',

    // 按钮
    btnAdd: '添加记录',
    btnSave: '保存记录',
    btnCancel: '取消',
    btnExport: '导出数据',
    btnImport: '导入数据',
    btnClear: '清除数据',

    // 表单标签
    labelDate: '日期',
    labelWeight: '体重',
    labelFasting: '空腹血糖',
    labelSteps: '步数',
    labelNotes: '备注',
    labelFoods: '食物内容',
    labelGlucose: '餐后血糖',
    labelTime: '测量时间',

    // 单位
    unitKg: 'kg',
    unitMgdl: 'mg/dL',
    unitMmol: 'mmol/L',
    unitSteps: '步',
    unitCarbs: 'g碳水',

    // 提示信息
    msgSaveSuccess: '✅ 记录保存成功',
    msgSaveError: '❌ 保存失败，请重试',
    msgDeleteConfirm: '确定要删除所有数据吗？',
    msgExportSuccess: '数据导出成功',
    msgImportSuccess: '数据导入成功',

    // 医学术语
    medicalTerms: {
      gdm: '妊娠期糖尿病 (GDM)',
      glucose: '血糖',
      fastingGlucose: '空腹血糖',
      postprandialGlucose: '餐后血糖',
      hba1c: '糖化血红蛋白 (HbA1c)',
      bmi: '体重指数 (BMI)',
      gestationalWeek: '孕周',
      trimester: '孕期',
      macrosomia: '巨大儿',
      hypoglycemia: '低血糖',
      hyperglycemia: '高血糖',
    }
  },

  // 日本語 (Japanese)
  ja: {
    // アプリタイトル
    appTitle: '妊娠糖尿病手帳',
    appSubtitle: '妊娠糖尿病管理アプリ',

    // ヘッダー挨拶
    greeting: 'こんにちは、妊婦さん ✨',
    todayDate: '今日',

    // ボトムナビゲーション
    navHome: 'ホーム',
    navStats: '統計',
    navGI: 'GI検索',
    navGuide: 'ガイド',

    // 統計カード
    statWeekSuccess: '今週の達成率',
    statAvgGlucose: '平均食後血糖',
    statTodayWeight: '今日の体重',
    statTodaySteps: '今日の歩数',

    // 日付セレクター
    weekdays: ['日', '月', '火', '水', '木', '金', '土'],

    // 食事
    breakfast: '朝食',
    lunch: '昼食',
    dinner: '夕食',

    // ボタン
    btnAdd: '記録追加',
    btnSave: '保存',
    btnCancel: 'キャンセル',
    btnExport: 'データ出力',
    btnImport: 'データ取込',
    btnClear: 'データ削除',

    // フォームラベル
    labelDate: '日付',
    labelWeight: '体重',
    labelFasting: '空腹時血糖',
    labelSteps: '歩数',
    labelNotes: '備考',
    labelFoods: '食事内容',
    labelGlucose: '食後血糖値',
    labelTime: '測定時刻',

    // 単位
    unitKg: 'kg',
    unitMgdl: 'mg/dL',
    unitMmol: 'mmol/L',
    unitSteps: '歩',
    unitCarbs: 'g炭水化物',

    // メッセージ
    msgSaveSuccess: '✅ 記録を保存しました',
    msgSaveError: '❌ 保存に失敗しました',
    msgDeleteConfirm: 'すべてのデータを削除しますか？',
    msgExportSuccess: 'データを出力しました',
    msgImportSuccess: 'データを取り込みました',

    // 医学用語（日本の病院で使用される正式名称）
    medicalTerms: {
      gdm: '妊娠糖尿病 (GDM: Gestational Diabetes Mellitus)',
      glucose: '血糖値',
      fastingGlucose: '空腹時血糖値',
      postprandialGlucose: '食後血糖値',
      hba1c: 'ヘモグロビンA1c (HbA1c)',
      bmi: 'ボディマス指数 (BMI)',
      gestationalWeek: '妊娠週数',
      trimester: '妊娠期',
      macrosomia: '巨大児',
      hypoglycemia: '低血糖症',
      hyperglycemia: '高血糖症',
      obstetrician: '産科医',
      prenatalCheckup: '妊婦健診',
      maternalClinic: '産婦人科',
      bloodTest: '血液検査',
      glucoseToleranceTest: '経口ブドウ糖負荷試験 (OGTT)',
      insulinTherapy: 'インスリン療法',
      dietTherapy: '食事療法',
      exerciseTherapy: '運動療法',
    }
  },

  // English
  en: {
    // App title
    appTitle: 'GDM Diary',
    appSubtitle: 'Gestational Diabetes Management',

    // Header greeting
    greeting: 'Hello, Mom-to-be ✨',
    todayDate: 'Today',

    // Bottom navigation
    navHome: 'Home',
    navStats: 'Stats',
    navGI: 'GI Search',
    navGuide: 'Guide',

    // Statistics cards
    statWeekSuccess: 'Weekly Success',
    statAvgGlucose: 'Avg. Postprandial',
    statTodayWeight: 'Today\'s Weight',
    statTodaySteps: 'Today\'s Steps',

    // Date selector
    weekdays: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],

    // Meals
    breakfast: 'Breakfast',
    lunch: 'Lunch',
    dinner: 'Dinner',

    // Buttons
    btnAdd: 'Add Record',
    btnSave: 'Save',
    btnCancel: 'Cancel',
    btnExport: 'Export Data',
    btnImport: 'Import Data',
    btnClear: 'Clear Data',

    // Form labels
    labelDate: 'Date',
    labelWeight: 'Weight',
    labelFasting: 'Fasting Glucose',
    labelSteps: 'Steps',
    labelNotes: 'Notes',
    labelFoods: 'Foods',
    labelGlucose: 'Postprandial Glucose',
    labelTime: 'Measurement Time',

    // Units
    unitKg: 'kg',
    unitMgdl: 'mg/dL',
    unitMmol: 'mmol/L',
    unitSteps: 'steps',
    unitCarbs: 'g carbs',

    // Messages
    msgSaveSuccess: '✅ Record saved successfully',
    msgSaveError: '❌ Failed to save',
    msgDeleteConfirm: 'Delete all data?',
    msgExportSuccess: 'Data exported successfully',
    msgImportSuccess: 'Data imported successfully',

    // Medical terms
    medicalTerms: {
      gdm: 'Gestational Diabetes Mellitus (GDM)',
      glucose: 'Blood Glucose',
      fastingGlucose: 'Fasting Blood Glucose',
      postprandialGlucose: 'Postprandial Glucose',
      hba1c: 'Hemoglobin A1c (HbA1c)',
      bmi: 'Body Mass Index (BMI)',
      gestationalWeek: 'Gestational Week',
      trimester: 'Trimester',
      macrosomia: 'Macrosomia',
      hypoglycemia: 'Hypoglycemia',
      hyperglycemia: 'Hyperglycemia',
    }
  }
};

// 日本医疗系统专用术语对照表
// Japanese Medical System Terminology Reference
const japanMedicalReference = {
  title: {
    zh: '🏥 日本医疗术语对照表',
    ja: '🏥 日本の医療用語対照表',
    en: '🏥 Japanese Medical Terminology Reference'
  },

  categories: [
    {
      name: {
        zh: '常用医疗机构',
        ja: '医療機関',
        en: 'Medical Facilities'
      },
      terms: [
        { ja: '産婦人科', zh: '妇产科', en: 'Obstetrics & Gynecology', romaji: 'sankafujinka' },
        { ja: '総合病院', zh: '综合医院', en: 'General Hospital', romaji: 'sougoubyouin' },
        { ja: 'クリニック', zh: '诊所', en: 'Clinic', romaji: 'kurinikku' },
        { ja: '助産院', zh: '助产院', en: 'Midwifery Clinic', romaji: 'josanin' },
      ]
    },
    {
      name: {
        zh: '检查项目',
        ja: '検査項目',
        en: 'Medical Tests'
      },
      terms: [
        { ja: '妊婦健診', zh: '产检', en: 'Prenatal Checkup', romaji: 'ninpu kenshin' },
        { ja: '血液検査', zh: '血液检查', en: 'Blood Test', romaji: 'ketsueki kensa' },
        { ja: '尿検査', zh: '尿检', en: 'Urine Test', romaji: 'nyou kensa' },
        { ja: '超音波検査', zh: '超声波检查', en: 'Ultrasound', romaji: 'chouonpa kensa' },
        { ja: '経口ブドウ糖負荷試験', zh: '口服葡萄糖耐量试验 (OGTT)', en: 'Oral Glucose Tolerance Test (OGTT)', romaji: 'keikou budoutou fuka shiken' },
        { ja: '血糖値測定', zh: '血糖值测定', en: 'Blood Glucose Test', romaji: 'kettou chi sokutei' },
      ]
    },
    {
      name: {
        zh: '血糖相关',
        ja: '血糖値関連',
        en: 'Blood Glucose'
      },
      terms: [
        { ja: '空腹時血糖値', zh: '空腹血糖值', en: 'Fasting Blood Glucose', romaji: 'kuufuku ji kettou chi', note: {zh: '正常值: <92 mg/dL', ja: '正常値: <92 mg/dL'} },
        { ja: '食後血糖値', zh: '餐后血糖值', en: 'Postprandial Glucose', romaji: 'shokugo kettou chi', note: {zh: '正常值: 1小时<140, 2小时<120 mg/dL', ja: '正常値: 1時間後<140, 2時間後<120 mg/dL'} },
        { ja: 'ヘモグロビンA1c', zh: '糖化血红蛋白', en: 'HbA1c', romaji: 'hemogurobinA1c', note: {zh: '目标值: <5.8%', ja: '目標値: <5.8%'} },
        { ja: '低血糖', zh: '低血糖', en: 'Hypoglycemia', romaji: 'teikettou', note: {zh: '<70 mg/dL', ja: '<70 mg/dL'} },
        { ja: '高血糖', zh: '高血糖', en: 'Hyperglycemia', romaji: 'koukettou' },
      ]
    },
    {
      name: {
        zh: '治疗方式',
        ja: '治療方法',
        en: 'Treatment Methods'
      },
      terms: [
        { ja: '食事療法', zh: '饮食疗法', en: 'Diet Therapy', romaji: 'shokuji ryouhou' },
        { ja: '運動療法', zh: '运动疗法', en: 'Exercise Therapy', romaji: 'undou ryouhou' },
        { ja: 'インスリン療法', zh: '胰岛素治疗', en: 'Insulin Therapy', romaji: 'insurin ryouhou' },
        { ja: '血糖自己測定', zh: '血糖自我监测', en: 'Self-Monitoring of Blood Glucose (SMBG)', romaji: 'kettou jiko sokutei' },
      ]
    },
    {
      name: {
        zh: '妊娠并发症',
        ja: '妊娠合併症',
        en: 'Pregnancy Complications'
      },
      terms: [
        { ja: '妊娠糖尿病', zh: '妊娠期糖尿病', en: 'Gestational Diabetes Mellitus (GDM)', romaji: 'ninshin tounyoubyou' },
        { ja: '妊娠高血圧症候群', zh: '妊娠高血压综合征', en: 'Pregnancy-Induced Hypertension', romaji: 'ninshin kouketsuatsu shoukougun' },
        { ja: '巨大児', zh: '巨大儿', en: 'Macrosomia', romaji: 'kyodaiji', note: {zh: '出生体重 >4000g', ja: '出生体重 >4000g'} },
        { ja: '早産', zh: '早产', en: 'Preterm Birth', romaji: 'sousan' },
        { ja: '羊水過多', zh: '羊水过多', en: 'Polyhydramnios', romaji: 'yousui kata' },
      ]
    },
    {
      name: {
        zh: '营养指导',
        ja: '栄養指導',
        en: 'Nutritional Guidance'
      },
      terms: [
        { ja: '炭水化物', zh: '碳水化合物', en: 'Carbohydrates', romaji: 'tansuikabutsu' },
        { ja: '食物繊維', zh: '膳食纤维', en: 'Dietary Fiber', romaji: 'shokumotsu sen\'i' },
        { ja: 'カロリー', zh: '卡路里/热量', en: 'Calories', romaji: 'karorii' },
        { ja: 'グリセミック指数', zh: '升糖指数 (GI值)', en: 'Glycemic Index (GI)', romaji: 'gurisemikku shisuu' },
        { ja: '分割食', zh: '分餐制', en: 'Divided Meals', romaji: 'bunkatsu shoku', note: {zh: '少食多餐', ja: '少量頻回食'} },
      ]
    },
    {
      name: {
        zh: '常用表达',
        ja: 'よく使う表現',
        en: 'Common Phrases'
      },
      terms: [
        { ja: '予約をお願いします', zh: '我要预约', en: 'I\'d like to make an appointment', romaji: 'yoyaku o onegai shimasu' },
        { ja: '血糖値が高いです', zh: '血糖值高了', en: 'My blood sugar is high', romaji: 'kettou chi ga takai desu' },
        { ja: '気分が悪いです', zh: '我感觉不舒服', en: 'I don\'t feel well', romaji: 'kibun ga warui desu' },
        { ja: '処方箋をください', zh: '请给我处方', en: 'Please give me a prescription', romaji: 'shohousen o kudasai' },
        { ja: '母子手帳', zh: '母子健康手册', en: 'Maternal and Child Health Handbook', romaji: 'boshi techou' },
      ]
    }
  ],

  // 日本血糖管理标准
  japanGlucoseStandards: {
    title: {
      zh: '📋 日本妊娠期血糖管理标准',
      ja: '📋 日本の妊娠糖尿病管理基準',
      en: '📋 Japanese GDM Management Standards'
    },
    standards: [
      {
        test: { zh: '空腹血糖', ja: '空腹時血糖', en: 'Fasting Glucose' },
        target: '<92 mg/dL (<5.1 mmol/L)',
        note: { zh: '晨起未进食8小时后', ja: '朝食前（8時間絶食後）', en: 'Before breakfast (after 8h fasting)' }
      },
      {
        test: { zh: '餐后1小时血糖', ja: '食後1時間血糖', en: '1-hour Postprandial' },
        target: '<140 mg/dL (<7.8 mmol/L)',
        note: { zh: '从开始进食计时', ja: '食事開始から1時間後', en: '1 hour after starting meal' }
      },
      {
        test: { zh: '餐后2小时血糖', ja: '食後2時間血糖', en: '2-hour Postprandial' },
        target: '<120 mg/dL (<6.7 mmol/L)',
        note: { zh: '从开始进食计时', ja: '食事開始から2時間後', en: '2 hours after starting meal' }
      },
      {
        test: { zh: '糖化血红蛋白', ja: 'HbA1c', en: 'HbA1c' },
        target: '<5.8% (NGSP)',
        note: { zh: '反映近3个月平均血糖', ja: '過去3ヶ月の平均血糖を反映', en: 'Reflects 3-month average' }
      }
    ]
  },

  // 日本产检时间表
  prenatalSchedule: {
    title: {
      zh: '📅 日本产检时间表（参考）',
      ja: '📅 妊婦健診スケジュール（参考）',
      en: '📅 Prenatal Checkup Schedule (Reference)'
    },
    schedule: [
      { weeks: '~23周', frequency: { zh: '每4周一次', ja: '4週に1回', en: 'Every 4 weeks' } },
      { weeks: '24~35周', frequency: { zh: '每2周一次', ja: '2週に1回', en: 'Every 2 weeks' } },
      { weeks: '36周~分娩', frequency: { zh: '每周一次', ja: '毎週1回', en: 'Every week' } }
    ],
    note: {
      zh: '※ GDM患者可能需要更频繁的检查，请遵医嘱',
      ja: '※ 妊娠糖尿病の場合、より頻繁な受診が必要な場合があります',
      en: '※ GDM patients may require more frequent visits'
    }
  }
};

// 导出供使用
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { translations, japanMedicalReference };
}
