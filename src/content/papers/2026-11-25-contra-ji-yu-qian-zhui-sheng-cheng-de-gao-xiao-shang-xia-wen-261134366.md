---
title: 'ConTra: A Training Framework for Effective Contextual Retrieval via Prefix
  Generation'
title_zh: ConTra：基于前缀生成的高效上下文检索训练框架
authors:
- Jiajun Hou
- Jingbang Chen
affiliations:
- CUHK-Shenzhen
- SLAI
arxiv_id: '2611.34366'
url: https://arxiv.org/abs/2611.34366
pdf_url: https://arxiv.org/pdf/2611.34366
published: '2026-11-25'
collected: '2026-11-26'
category: RAG
direction: RAG上下文检索 · 前缀生成优化
tags:
- RAG
- Contextual Retrieval
- Reinforcement Learning
- Prefix Generation
- Information Retrieval
one_liner: 通过强化学习训练轻量LLM生成检索chunk上下文前缀，兼顾全链路检索精度与索引效率
practical_value: '- 电商知识库/商品详情页的chunk拆分后，可接入轻量ConTra风格的前缀生成模型，为参数、规格类chunk补充品牌、类目、所属活动等上下文，同时喂给向量召回和重排环节，比单独优化编码器成本低、见效快

  - 可直接复用ConTra的四元奖励设计：用业务已有的冻结召回、重排、事实校验模型提供反馈信号，不需要额外标注大量训练数据，就能快速对齐业务检索目标训练小模型

  - 多阶段排序链路可参考该思路：尽可能让上下游环节共用同一份显式增强特征（如文本标签、前缀），避免隐式向量优化导致的下游环节信息断层，提升全链路收益

  - 前缀长度控制的trick可直接复用：设定无惩罚长度阈值，超过后线性加罚，平衡上下文信息增益和token成本，业务可根据自身算力预算灵活调整阈值'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG上下文检索方案存在两类缺陷：一是将上下文编码进chunk隐式向量，重排环节无法读取上下文信息，导致多阶段链路信息断层；二是用大模型prompt生成显式文本前缀，索引阶段推理成本高，效果也弱于SOTA上下文编码器。业界亟需低成本、能同时提升全链路检索效果的上下文补全方案。

### 方法关键点
- 提出ConTra强化学习训练框架，基于轻量自回归LLM为每个chunk生成专属上下文前缀，前缀与原chunk拼接后同时用于向量召回和重排，一次生成可跨所有查询复用
- 奖励函数融合4个维度：① 召回相似度增益，对齐向量召回目标；② 重排得分增益，对齐重排精细排序目标；③ 事实校验惩罚，用冻结大模型校验前缀真实性，避免幻觉；④ 长度惩罚，控制前缀长度、减少相邻chunk的特征冲突
- 训练数据做两层筛选，仅保留奖励信号差异充足、特定精准前缀比通用描述有明确检索收益的样本，大幅提升训练效率

### 关键实验
- 测试集覆盖公开数据集ConTEB，以及新构建的RealContextBench（含网页搜索、金融分析、会议纪要等5个真实场景+3种干扰文本条件）
- ConTra-2B表现超过Anthropic prompt 9B基线和PPLX-4B上下文编码器，整体nDCG@10最高领先3.15个点；短文档索引速度是9B基线的7.74倍、PPLX-4B的2.15倍，同规模模型RL训练最多降低52.3%总索引时间
- 生成的前缀可直接与现有上下文编码器结合，PPLX-4B召回+ConTra前缀重排的混合方案在金融、会议等场景能进一步提升效果

给检索chunk添加全链路可读取的显式文本前缀，比仅优化隐式向量表示的投入产出比更高
