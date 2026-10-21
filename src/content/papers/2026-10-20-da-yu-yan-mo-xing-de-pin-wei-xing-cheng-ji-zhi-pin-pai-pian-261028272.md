---
title: 'How Language Models Learn Taste: Brand Preference in LLMs'
title_zh: 大语言模型的品味形成机制：品牌偏好来源研究
authors:
- Tapan Parikh
affiliations:
- Cornell Tech
arxiv_id: '2610.28272'
url: https://arxiv.org/abs/2610.28272
pdf_url: https://arxiv.org/pdf/2610.28272
published: '2026-10-20'
collected: '2026-10-21'
category: LLM
direction: LLM偏好形成 · 训练阶段影响
tags:
- LLM Preference
- DPO
- Brand Recommendation
- Preference Alignment
- Training Pipeline
one_liner: 揭示LLM命名与推荐的品牌偏好差异来源，证实DPO阶段会隐性迁移通用偏好
practical_value: '- 做电商生成式推荐/AI导购时，可通过DPO注入通用「品味偏好」（如小众/品质品牌倾向），无需显式标注大量品牌样本，大幅降低标注成本

  - 品牌营销侧可针对性优化品牌的语义关联（如绑定「高品质/小众专业/高性价比」等属性标签），适配LLM的隐性偏好判定逻辑，提升被推荐概率

  - LLM应用的偏好对齐阶段，需警惕训练数据中未显式存在的隐性偏好迁移，避免推荐结果不符合平台业务定位（如过度推荐高溢价小众品牌流失大众用户）

  - 开发多轮交互AI导购时，注意多轮对话会将LLM输出非头部品牌的概率提升58pct，可针对性做干预校准保证推荐结果匹配业务目标'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM已广泛应用于电商导购、商品推荐场景，但输出品牌偏好存在明显矛盾：命名品类时优先输出头部市场品牌，推荐时却倾向小众专业品牌，其偏好来源与形成机制尚不明确，直接影响生成式推荐的可信度与业务适配性。

### 方法关键点
- 设计42个品类的多轮问答范式，区分`Name`/`Choose`/`Recommend`/两轮`Picked`四种提问场景，统计不同场景下的品牌输出概率
- 覆盖102款公开/商用LLM，同时跟踪OLMo 3 7B、OLMo 3.1 32B、Tulu 3 8B三条公开训练管线的全阶段（预训练/SFT/DPO/RL）checkpoint，定位偏好形成的具体阶段
- 结合训练数据检索与跨品类验证，排除显式品牌样本学习的可能性，验证偏好的隐性迁移特性

### 关键结果数字
- 26/42品类下，LLM两轮推荐的首选品牌与命名品类时的首选品牌不一致，头部品牌的推荐占比从命名时的89%降至两轮推荐时的31%
- 预训练阶段已存在「推荐场景绑定小众品牌」的关联，SFT阶段对品牌偏好无显著影响，DPO阶段会将小众品牌的选择概率提升11~24个百分点，RL阶段无明显变化
- DPO训练数据中几乎不存在显式品牌对比样本，偏好迁移可跨品类生效，如酱料选择中pesto的选择占比从预训练的5%提升至DPO后的67%

### 核心结论
LLM的品牌推荐结果与品牌本身的曝光量关联较弱，更大程度取决于品牌是否匹配DPO阶段对齐的隐性「品味」偏好
