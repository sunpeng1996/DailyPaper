---
title: 'RAMP: Robust Ad Recommendation Under Limited Personalized-Feature Availability
  via Masking and Alignment Pathways'
title_zh: RAMP：个性化特征受限场景下基于掩码与对齐通路的鲁棒广告推荐
authors:
- Dairui Liu
- Zhongyi Lu
- Roger Zhe Li
- Changhong Jin
- Jitao Lu
- Xinyang Shao
- Bichen Shi
- Mete Sertkan
- Aghiles Salah
- Aonghus Lawlor
affiliations:
- University College Dublin
- Huawei Ireland Research Center
arxiv_id: '2607.17473'
url: https://arxiv.org/abs/2607.17473
pdf_url: https://arxiv.org/pdf/2607.17473
published: '2026-07-20'
collected: '2026-07-21'
category: RecSys
direction: 隐私合规广告推荐 · CTR/CVR预估
tags:
- CTR Prediction
- CVR Prediction
- Privacy Preserving
- Knowledge Distillation
- Dual Tower
- Ad Recommendation
one_liner: 提出双通路加预测对齐架构，在无个性化特征时显著提升CTR/CVR预测精度
practical_value: '- 针对合规场景下非授权流量的CTR/CVR预估，可直接复用双通路掩码训练思路，给个性化/非个性化流量分设独立参数塔，避免跨流量梯度负迁移

  - 可借鉴训练阶段新增专属非个性化通路+logit级对齐的蒸馏方案，仅训练时新增通路，推理无额外开销，适配线上低延迟服务要求

  - 架构为模型无关设计，可直接套在现有DeepFM/DCN/FCN等CTR/CVR backbone上，不需要重构现有链路，改造ROI极高

  - 工业验证显示非个性化场景AUC提升0.1%即可带来总广告价值超3%的增益，可作为隐私合规场景优化的核心参考指标'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
全球隐私法规（GDPR、个人信息保护法等）收紧后，约20%以上的非授权流量无法获取用户ID、行为、属性等个性化特征，常规CTR/CVR模型在这类流量上性能暴跌，现有隐私方案如联邦学习改造复杂度高、知识增强依赖外部数据，缺乏低侵入的模型侧优化方案。

### 方法关键点
- 个性化通路设计双独立参数塔，共享embedding层，训练时通过流量掩码分别让Tower A仅学习个性化样本、Tower B仅学习非个性化样本，避免梯度冲突
- 新增仅用非个性化特征训练的独立通路，全程复用共享embedding，无需额外特征输入
- 引入蒸馏风格的logit级对齐损失，最小化非个性化通路与个性化通路Tower B的预测logit差，将个性化通路学到的高阶特征知识迁移到非个性化分支，推理时仅保留双塔结构，无额外开销

### 关键实验结果
覆盖4个数据集（Avazu、TaobaoAd、CriteoPrivateAd、华为工业数据集），对比18种SOTA CTR/CVR基线，非个性化场景下AUC最高提升0.87%、LogLoss最高下降1.61%，个性化场景下性能与SOTA持平，工业A/B测试总广告价值（TAV）提升超3%。

### 核心结论
隐私合规场景下，仅通过训练侧的通路拆分、掩码训练和蒸馏对齐，无需推理额外开销，即可有效补回非授权流量的性能损失。
