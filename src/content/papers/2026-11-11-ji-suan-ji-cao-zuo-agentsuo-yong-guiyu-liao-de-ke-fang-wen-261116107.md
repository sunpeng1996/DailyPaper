---
title: 'Trained on What Screen Readers Cannot Read: Accessibility Debt in the GUI
  Corpora Behind Computer-Use Agents'
title_zh: 计算机操作Agent所用GUI语料的可访问性债务问题研究
authors:
- Obada Kraishan
- Kulsawasd Jitkajornwanich
affiliations:
- Texas Tech University
arxiv_id: '2611.16107'
url: https://arxiv.org/abs/2611.16107
pdf_url: https://arxiv.org/pdf/2611.16107
published: '2026-11-11'
collected: '2026-11-13'
category: Agent
direction: 计算机操作Agent 训练数据质量评估
tags:
- Computer-Use Agent
- GUI Corpus
- Accessibility
- Training Data Quality
- Android
one_liner: 量化2份安卓GUI语料的内容描述覆盖率缺口，揭示计算机操作Agent的训练数据标注偏差
practical_value: '- 做GUI交互Agent训练时，优先筛选带有效内容描述的GUI元素，避免用无标注输入控件做训练样本，提升Agent操作准确率

  - 自研Agent训练语料时，可参考论文的5套编码规则校验内容描述覆盖率，同时剔除placeholder类无效标注，降低数据噪声

  - 做Agent操作基准测试时，需注意现有语料存在的元素选择偏差，避免基准结果高估实际落地性能'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
计算机操作Agent依赖GUI截图+可访问性树语料训练，语料的标注缺口会直接导致Agent操作能力缺陷，现有研究缺乏对这类缺口的量化分析。
### 方法关键点
针对2017年Rico、2024年AndroidControl两份安卓GUI语料，共1737万+界面元素，用6套编码规则量化需标注元素的内容描述覆盖率，同时匹配2.6万+任务操作的触达元素分析选择偏差。
### 关键结果数字
- Rico语料需标注元素的有效描述覆盖率仅17.74%，AndroidControl为57.27%，差值稳定在39.5个百分点
- 两类语料中输入控件的标注率最低，分别为2.20%、27.21%
- 旧语料的占位符描述占比是新语料的5倍（10.25% vs 1.95%）
- 任务演示中带描述的无文本可点击图形被选中的概率比其他元素高9个百分点
