---
title: How Much Is an AI Token Worth? Scaling Laws for Wild AI-Generated Web Text
title_zh: 野生AI生成网页文本的缩放定律与AI token价值评估
authors:
- Jenna Russell
- Ben Glickenhaus
- Katherine Thai
- John Wieting
- Mohit Iyyer
- Max Spero
- Bradley Emi
affiliations:
- University of Maryland
- Pangram Labs
arxiv_id: '2609.40295'
url: https://arxiv.org/abs/2609.40295
pdf_url: https://arxiv.org/pdf/2609.40295
published: '2026-09-29'
collected: '2026-10-01'
category: LLM
direction: LLM预训练 · 缩放定律优化
tags:
- Scaling Law
- Pre-training Data
- AI Generated Text
- Data Filtering
- Token Value
one_liner: 提出适配野生AI网页文本的缩放定律，量化AI token价值与预训练算力损耗
practical_value: '- 训练垂直领域小LLM（如电商文案、客服模型）且标注人类数据不足时，可少量混入AI生成文本补充，当TPP h<10时能有效降低loss

  - 训练面向人类用户的LLM时，务必过滤预训练数据中的野生AI文本，当前31%的网页AI占比下，不过滤需多付出1.6倍算力才能达到同等效果

  - 做LLM效果验证时，需拆分人类/AI生成文本的验证集分别评测，混合验证集（22.3%AI占比）会掩盖95.5%的AI文本带来的效果下降

  - 若训练目标是处理Agent交互的AI生成内容，训练数据中可混入90%以上的AI文本，能获得最优效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前网页中AI生成文本占比快速提升，2026年8月已达31.1%，现有Chinchilla等缩放定律将AI与人类token等效，无法准确预测真实预训练效果；过往研究要么聚焦递归训练的模型坍塌场景，要么使用人工curated的合成数据，均不符合互联网中野生AI文本（多模型生成、面向人类读者、无标注混入人类数据）的实际场景。
### 方法关键点
- 构建83B token的WildAI数据集，标注AI/人类来源、主题、格式标签，覆盖2021-2026年的Common Crawl数据
- 预训练800个参数范围19.9M~973M的模型，控制AI/人类token比例、人类token per parameter（TPP h）等变量
- 提出新的缩放定律，包含AI token的饱和收益项与对数增长损害项，无AI文本时可退化为Chinchilla定律
### 关键结果
在C4、FineWeb等人类文本测试集上，新定律预测3.6倍更大模型的效果时，RMSE比最优现有定律低41%，比Chinchilla低80%；2026年31.1%的AI占比下，不过滤AI文本需要多花1.6倍算力才能达到同人类子集训练的效果，2028年预测占比51%时需3倍算力；当TPP h<10时加入AI token可降低loss，高于20（Chinchilla最优点）时加入AI立刻有损，重复人类文本效果优于加入AI文本；22.3%AI占比的混合验证集会掩盖95.5%的AI文本带来的有害效果。

除非训练数据极度短缺或目标是处理AI生成文本，否则预训练时过滤野生AI文本的收益远大于保留。
