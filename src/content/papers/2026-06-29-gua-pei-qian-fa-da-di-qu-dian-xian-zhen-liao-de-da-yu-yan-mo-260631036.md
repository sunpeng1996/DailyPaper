---
title: Teaching LLMs to Recommend and Defer in Underrepresented Epilepsy Care
title_zh: 适配欠发达地区癫痫诊疗的大语言模型推荐与自动转诊框架
authors:
- Shreyas Rajesh
- Kartik Sharma
- Tonmoy Monsoor
- Mehmet Yigit Turali
- Richard Idro
- Juliana Kayaga
- Robert Sebunya
- Tracy Tushabe Namata
- Jessica Nichole Pasqua
- Vwani Roychowdhury
affiliations:
- University of California, Los Angeles
- Makerere University
- St. Francis Hospital Nsambya
arxiv_id: '2606.31036'
url: https://arxiv.org/abs/2606.31036
pdf_url: https://arxiv.org/pdf/2606.31036
published: '2026-06-29'
collected: '2026-07-07'
category: Agent
direction: 多Agent LLM领域自适应与不确定性决策
tags:
- Multi-Agent
- Prompt Learning
- Uncertainty Estimation
- Bayesian Averaging
- Domain Adaptation
one_liner: 提出无参数多Agent prompt学习框架MANANA与贝叶斯prompt平均方法 实现本地化诊疗推荐与低置信案例自动转诊
practical_value: '- 多Agent自学习prompt架构可直接复用：Predictor产出候选、Inspector做错误归因、Architect仅聚合跨案例高频规则更新记忆，避免单Agent自修正的先验偏差问题，适合区域化电商商品推荐、下沉市场文案生成等需适配本地化规则的场景

  - 贝叶斯prompt平均（BPA）的不确定性估计方法可迁移：将多轮迭代产生的prompt轨迹作为模型集成池，按验证集表现加权得到置信度，低成本实现低置信案例人工审核触发，适合医美/医药类商品推荐、广告素材合规判定等高风险推荐场景

  - 小样本领域适配思路可复用：无需LLM参数更新，仅从少量本地标注样本中提取跨案例高频规则修正prompt，在分布偏移场景下表现优于TextGrad、DSPy等通用prompt优化方法，适合冷启动业务的快速适配'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有医疗LLM多基于高收入地区数据训练，在资源匮乏地区（如乌干达癫痫诊疗）存在开药规则、药品可得性的显著分布偏移，直接调用的推荐错误率高；同时稀缺的专科医生资源需要系统能自动识别低置信案例转诊，避免误诊风险。

### 方法关键点
- 提出MANANA无参数prompt学习框架，包含3个Agent角色：Predictor基于当前记忆输出3个候选用药方案，Inspector对比医生真实处方输出错误归因与候选规则，Architect仅将跨≥2个案例的高频规则更新到记忆，避免单案例过拟合；分为单规则集的MANANA-Single与多专家Agent的MANANA-Multi两个变体
- 提出贝叶斯prompt平均（BPA）：将迭代过程中产生的所有prompt状态作为集成模型，按验证集表现加权得到每个推荐方案的置信度，实现高置信案例自动处理、低置信案例触发转诊

### 关键结果
在乌干达两个独立采集的儿科癫痫队列（共699名患者、2549次就诊）上测试，对比经典ML模型、直接prompt、TextGrad、DSPy、ExpeL等基线：
- MANANA-Multi在单药治疗场景Top-3准确率达97%，跨队列迁移场景比基线高4-8个百分点
- BPA支持选择性预测：Top25%高置信案例Top-1准确率达99%，Top50%高置信案例Top-1准确率达95%，剩余低置信案例可转诊给专科医生

### 核心结论
无需LLM参数更新，仅通过多Agent协作从少量本地样本中提取高频规则修正prompt，结合prompt轨迹的贝叶斯集成，就能实现分布偏移场景下的高可靠推荐与可控风险的人机协作
