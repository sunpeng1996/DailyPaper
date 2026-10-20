---
title: Improving OCR Accuracy Through Multi-Classifier Verification of Visually Similar
  Characters
title_zh: 基于多分类器验证视觉相似字符的OCR准确率提升方法
authors:
- Nuzhat Khan
- Ab Al-Hadi Ab Rahman
- Mohamad Anuar Kamaruddin
- Muhammad Paend Bakht
- Sana Fatima
- Farhad Khodadadi
- Ibrahim Yousef Alshareef
affiliations:
- Faculty of Electrical Engineering, Universiti Teknologi Malaysia
- School of Industrial Technology, Universiti Sains Malaysia
- School of Business, Maynooth University
arxiv_id: '2610.22726'
url: https://arxiv.org/abs/2610.22726
pdf_url: https://arxiv.org/pdf/2610.22726
published: '2026-10-15'
collected: '2026-10-20'
category: Other
direction: OCR后处理 · 视觉相似字符纠错
tags:
- OCR
- Character Correction
- Post-processing
- Binary Classifier
- Alphanumeric Recognition
one_liner: 无字典依赖的字符级后处理框架CVM，适配主流OCR引擎修正视觉相似字符错误
practical_value: '- 电商场景下商品SKU编码、快递单号、防伪码等非词典类字符串的OCR纠错可直接复用CVM的无字典二分类器架构，无需修改现有OCR引擎，接入成本极低

  - 处理商品图片、资质文件的内容理解Agent可针对高频易混字符（如数字/字母混排的编码）训练专属二分类器做后处理，降低纠错误判率

  - 独立插拔的模块化架构可迁移到推荐系统的召回/排序后处理链路，针对特定badcase定制子模型修正，无需改动核心排序/召回模型'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
OCR系统对视觉相似字符（如O/0、Z/2、S/5）的区分误差长期存在，现有预处理、词级后处理均无法解决字符级视觉歧义问题，且依赖词典校验的方法不适用于非词汇类数据（如序列号、车牌、编码）。
### 方法关键点
字符级后处理框架CVM为每对视觉易混字符训练独立的二分类Random Forest校验器，无需依赖字典校验，支持直接接入现有OCR pipeline，无需修改底层识别模型。
### 关键结果
在Tesseract、EasyOCR、TrOCR三个主流OCR引擎、10种不同复杂度字体上测试，OCR准确率提升3.95~14.81个百分点，视觉相似字符错误修正率达87.3%，误修正率仅2.3%。
