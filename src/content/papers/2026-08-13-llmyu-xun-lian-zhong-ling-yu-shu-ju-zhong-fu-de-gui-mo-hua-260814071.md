---
title: Scaling Domain Data Repetition in LLM Pretraining
title_zh: LLM预训练中领域数据重复的规模化规律研究
authors:
- Jingwei Li
- Xinran Gu
- Rui Dai
- Xintong Hao
- Chengyin Xu
- Yan Wu
- Shuran Zheng
- Jingzhao Zhang
affiliations:
- Tsinghua University
- ByteDance Seed
arxiv_id: '2608.14071'
url: https://arxiv.org/abs/2608.14071
pdf_url: https://arxiv.org/pdf/2608.14071
published: '2026-08-13'
collected: '2026-08-17'
category: Training
direction: LLM预训练 · 数据复用策略
tags:
- LLM Pretraining
- Data Repetition
- Scaling Law
- Domain Adaptation
- Training Efficiency
one_liner: 固定token-参数比下大模型领域数据最优重复次数随规模上升，可通过小代理模型快速调参
practical_value: '- 训练电商/推荐领域垂直LLM时，可采用和目标大模型相同TPP的小代理模型扫描最优重复次数，结果可直接复用，大幅降低调参成本

  - 不同领域最优重复次数与该领域验证损失强负相关，商品文案、用户评论等简单垂直场景（验证损失低）可重复5-6次，复杂领域可适当降低重复次数

  - 固定总领域数据占比时，替换部分独特数据为重复数据仅影响领域内性能，跨域通用能力波动小于1%，优质数据不足时可放心复用

  - 学习率衰减越晚/采用恒定学习率，模型可容忍的重复次数越高，数据稀缺场景可延长学习率保持阶段占比，提升重复数据利用率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM规模化训练时，总token预算通常随参数规模等比增长以维持最优tokens-per-parameter ratio（TPP），但高质量垂直领域数据获取难度远高于通用网页数据，在训练集中的占比会随总token规模上涨被稀释。重复利用现有优质领域数据是缓解稀释的核心方案，但过度重复易引发过拟合，现有研究多基于固定总token预算的设定，不符合工业界固定TPP的训练范式，得出的重复规律无法直接复用。
### 方法关键点
- 采用工业界主流的固定TPP训练范式，总训练token数随模型参数规模等比增长，变量仅包含高质量领域独特数据占比α、重复次数e，剩余token填充无重复通用网页数据
- 覆盖Code、Math、Wiki、医疗4类典型高质量领域，同时评估领域内验证损失、跨域（ArXiv、新闻）验证损失，量化重复的收益与泛化影响
### 关键结果
- 最优重复次数与领域最小验证损失皮尔逊相关系数达-0.944，强负相关：Math最优重复5-6次，Code最优4-5次，Wiki、医疗最优仅3-4次
- 固定TPP下，最优重复次数与模型规模正相关（相关系数0.4），与独特领域数据占比几乎无关（相关系数0.018）
- 固定总领域数据占比时，用重复数据替换独特数据仅影响领域内性能，跨域性能波动<1%，几乎无负面影响
### 核心结论
固定TPP下，小代理模型调试出的领域数据最优重复次数，可直接保守复用给同TPP的更大模型，不会出现过拟合
