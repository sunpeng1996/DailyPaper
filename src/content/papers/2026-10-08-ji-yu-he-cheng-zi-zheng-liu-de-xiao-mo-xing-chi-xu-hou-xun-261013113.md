---
title: Continually Post-training Small Models via Synthetic Self-distillation
title_zh: 基于合成自蒸馏的小模型持续后训练方法
authors:
- Woosung Koh
- Hyunsoo Lee
- Kyungjae Lee
- Haeju Park
- Dahyun Lee
- Dasol Hwang
- Moontae Lee
affiliations:
- KAIST AI
- LG AI Research
arxiv_id: '2610.13113'
url: https://arxiv.org/abs/2610.13113
pdf_url: https://arxiv.org/pdf/2610.13113
published: '2026-10-08'
collected: '2026-10-12'
category: Training
direction: 小模型持续训练 · 合成自蒸馏
tags:
- Continual Learning
- Self-distillation
- Small Language Model
- Supervised Fine-tuning
- Distribution Alignment
one_liner: 采用同系列稍大模型做分布对齐，解决小模型持续训练的遗忘与习得矛盾
practical_value: '- 做端侧小模型（如端侧搜索推荐、端侧Agent）持续注入领域知识时，优先选同系列稍大模型做对齐器生成训练数据，比跨系列大模型效果更好、计算成本降低60%以上

  - 小模型SFT前加轻量rejection sampling过滤答案错误的样本，可显著减少灾难性遗忘，同时提升目标域效果，无需修改训练逻辑

  - 持续训练时优先控制训练数据与模型原生分布的KL散度，比单纯提升监督数据质量更能平衡新知识习得和旧能力保留'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
小模型是低延迟端侧部署、垂域搜索推荐轻量化推理的核心载体，但现有持续后训练方法（如SDFT）依赖强ICL与指令跟随能力，在小模型上完全失效，存在严重的灾难性遗忘和新知识习得效率低问题；根因验证显示，训练后模型的分布偏移与遗忘程度、习得效果呈强线性负相关，保持分布对齐是核心需求。

### 方法关键点
- 提出SYNTHSELF框架，用同系列稍大模型作为对齐器，将目标域训练样本重写成与小模型原生分布对齐的格式，最小化训练时的分布偏移
- 采用off-policy训练范式，加入rejection sampling过滤对齐器生成的答案错误样本，大幅提升小模型敏感的监督数据质量
- 对齐器选择规则：优先选与基模型分布KL散度最小的同系列稍大模型，而非能力更强但分布差异大的跨系列大模型

### 关键结果
在0.5B、1.5B、3B三个小模型尺度、4个习得数据集（科学、工具使用、医学、多学科科学混合）、14个保留能力基准上测试，对比SFT、SDFT等6种基线：
- 新知识习得效果平均比最优基线高5.7~16.9%p，旧能力遗忘仅1%p左右，接近零遗忘
- 同系列稍大对齐器比跨系列强对齐器的数据生成成本降低62.9%~76.9%，同时效果更优
- 比prompt匹配的SDFT方法习得效果高18.96%p，旧能力保留效果高1.68%p

### 核心结论
小模型持续训练的核心矛盾是分布偏移，保持训练数据与模型原生分布对齐，比单纯追求监督数据的绝对质量更重要。
