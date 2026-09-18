---
title: Relational Attention for Data-Efficient Language Modeling
title_zh: 面向数据高效语言建模的关系注意力机制
authors:
- Adrian Brasoveanu
- Ece Takmaz
- Jakub Dotlačil
affiliations:
- UC Santa Cruz
- Utrecht University
arxiv_id: '2609.20530'
url: https://arxiv.org/abs/2609.20530
pdf_url: https://arxiv.org/pdf/2609.20530
published: '2026-09-17'
collected: '2026-09-18'
category: LLM
direction: 小数据语言建模 · 关系注意力
tags:
- Relational-Attention
- Data-Efficient-LLM
- Dual-Attention-Transformer
- Next-Latent-Prediction
- BabyLM
one_liner: 将双注意力Transformer与NextLatent预测目标结合，在小数据语言建模上大幅提升泛化能力
practical_value: '- 垂类电商/Agent等小语料训练场景，可将标准自注意力拆分出1/4-1/2关系注意力头，无需大幅增加参数即可提升结构泛化能力，适配语法规则敏感的文案生成、语义理解任务

  - 采用RoPE-based相对符号替代可学习符号库，零参数成本，可直接用于低资源场景下的LLM轻量化改造

  - 训练阶段加入NextLatent Prediction辅助目标，无需改变推理架构即可提升模型对序列历史的压缩能力，适合长序列用户行为建模、多轮对话上下文理解场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
普通Transformer自注意力纠缠对象级特征与关系信息，小数据场景下 Out-of-Training-Sample 泛化能力差，且无压缩序列历史的内在约束，和人类语言处理的认知规律不符，小数据训练的LLM性能瓶颈明显。

### 方法关键点
- 架构上采用 Dual Attention Transformer (DAT) 替换标准自注意力，并行设置感知注意力头（处理 lexical 特征）和关系注意力头（处理结构/关系信息），两者解耦提升数据效率
- 新增RoPE-based相对符号机制，替换原可学习符号库，无额外参数开销，性能与可学习版本相当
- 训练时加入 Next-Latent Prediction (NextLat) 辅助目标，用轻量动力学模型预测下一层隐状态，迫使隐状态压缩历史信息，训练后丢弃辅助模块，推理无 overhead

### 关键实验
在BabyLM 2026的10M词（strict-small）和100M词（strict）赛道测试，基线为同规模GPT-2：100M词赛道最佳模型总榜排第6/55、NLP任务子集排第3/55，拿到最高EWoK得分59.54，在8/9个benchmark上领先GPT-2；10M词赛道DAT比同参数标准Transformer的BLiMP得分高2.5个百分点，NextLat让(Super)GLUE 5/7任务精度提升。

### 核心结论
小数据场景下，引入关系注意力的归纳偏置性价比远高于单纯扩大模型规模或增加训练数据，训练侧轻量辅助目标可在不增加推理成本的前提下大幅提升泛化能力
