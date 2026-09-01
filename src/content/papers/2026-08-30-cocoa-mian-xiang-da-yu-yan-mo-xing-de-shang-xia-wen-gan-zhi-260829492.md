---
title: 'CoCoA: Context-Conditional Cultural Alignment for Large Language Models'
title_zh: CoCoA：面向大语言模型的上下文感知文化对齐框架
authors:
- Kyungdon Lee
- Wei Xu
- Alan Ritter
- Dong-Ho Lee
- JinYeong Bak
affiliations:
- Sungkyunkwan University
- Georgia Institute of Technology
- University of Southern California
arxiv_id: '2608.29492'
url: https://arxiv.org/abs/2608.29492
pdf_url: https://arxiv.org/pdf/2608.29492
published: '2026-08-30'
collected: '2026-09-01'
category: LLM
direction: 大语言模型 · 文化对齐与偏差缓解
tags:
- Cultural Alignment
- Bias Mitigation
- LoRA
- Contrastive Learning
- Multi-Objective Optimization
one_liner: 通过双上下文训练与梯度协调实现LLM上下文感知的文化偏差缓解
practical_value: '- 出海电商/内容推荐的本地化适配可复用双上下文训练范式：有明确地域/文化提示的场景（如「韩国特色零食」）强化本地实体偏好，无提示场景保持中立，避免文化同质化

  - 多目标训练的梯度冲突可借鉴目标感知PCGrad方法：根据每个目标距离预设值的差距动态调整投影权重，避免不同优化目标互相干扰，可迁移到推荐同时优化点击率与多样性的场景

  - 实体偏好得分计算可采用PMI风格的先验校正：减去实体在预训练语料中的基线概率，弱化热门实体的天然排序优势，提升上下文对排序的贡献，适合搜索/推荐的相关性得分校准

  - 文化/地域适配优先采用LoRA微调方案，仅更新小部分参数即可达成目标，对通用能力影响极小，适合出海业务快速适配不同区域需求，训练与部署成本低'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM普遍存在西方中心的文化偏差，传统去偏方法追求全局统一中立，会导致文化同质化——既在有明确文化提示的场景下无法输出符合本地文化的内容，又消解了合理的文化关联信息，出海业务（电商、内容推荐、Agent）中这类偏差会直接影响用户体验甚至引发文化冲突，需要上下文感知的文化对齐方案。

### 方法关键点
- 双上下文训练构造：每个训练样本配对「带明确文化提示的grounded上下文」和「无文化提示的neutral上下文」，同时配对本地实体与西方实体，让模型学习不同上下文下的偏好差异
- 三部分损失函数：① 对齐损失：有文化提示时用对比损失强化本地实体排序高于西方实体；② 校准损失：无文化提示时最小化两类实体的得分差保持中立；③ 漂移正则：约束无提示场景的实体得分差接近原始模型，避免对齐过程干扰中立行为
- 目标感知梯度协调：用改进的PCGrad方法，根据两个目标当前距离预设目标的差距动态调整梯度投影权重，解决多目标训练的梯度冲突，仅更新LoRA参数不改动基础模型权重

### 关键结果
在CAMeL、Camellia两个实体级文化偏差基准（覆盖7个文化组、10种语言），4个主流LLM上测试，相比原始模型平均文化偏差分数（CBSg）从43降到24，无提示场景的中立度保持在50.2（50为完全中立），通用能力在MMLU等5个基准上下降不超过0.38个百分点，显著优于BiasEdit、BiasUnlearn等传统去偏基线。

最值得记住的一句话：文化对齐不能追求全局统一去偏，而是要让模型学会根据上下文是否存在文化提示动态切换偏好策略，既满足本地化需求又避免不必要的文化倾向。
