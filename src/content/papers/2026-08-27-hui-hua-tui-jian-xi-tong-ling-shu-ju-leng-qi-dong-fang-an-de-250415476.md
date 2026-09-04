---
title: An Empirical Study on Zero-Data Bootstrapping for Conversational Recommender
  Systems
title_zh: 会话推荐系统零数据冷启动方案的系统性实证研究
authors:
- Rohan Surana
- Junda Wu
- Zhouhang Xie
- Yu Xia
- Nathan Kallus
- Julian McAuley
affiliations:
- University of California, San Diego
- Netflix Inc.
- Cornell University
arxiv_id: '2504.15476'
url: https://arxiv.org/abs/2504.15476
pdf_url: https://arxiv.org/pdf/2504.15476
published: '2026-08-27'
collected: '2026-09-04'
category: RecSys
direction: 会话推荐 · 零数据冷启动
tags:
- Conversational Recommender System
- Zero-Data Bootstrapping
- Synthetic Training Data
- Active Learning
- LLM Fine-tuning
one_liner: 系统性验证基于非对话域信号合成数据实现会话推荐零数据冷启动的可行路径
practical_value: '- 新域上线会话推荐无对话数据时，可直接复用「非对话信号（商品评论/属性/交互数据）→ 主动选样 → Teacher LLM合成对话
  → 目标模型微调」的完整流程，跳过人工标注对话的高成本环节

  - 选样阶段优先使用JS多样性或Fisher信息准则，比随机选/按热度选的数据效率提升20%以上，同等LLM调用预算下下游召回率更高，不要依赖热度 heuristic
  选样本

  - 小参数量LLM（1.5B-3B级别）用合成数据Full-SFT收益远高于LoRA，Qwen2.5-1.5B在低资源场景下Recall@1相对提升可达207.8%，小模型冷启动优先选全量微调

  - 低资源场景下（真实对话量<1k），合成数据效果优于稀缺真实对话，还可和真实对话混合训练进一步提效，冷启动阶段优先堆合成数据，不用等少量真实对话积累'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
会话推荐系统（CRS）传统依赖大量域内对话数据，标注成本高、隐私风险大，新域完全无对话数据时冷启动难度极高；直接调用通用大模型做零样本CRS又存在成本高、延迟高、域知识陈旧的问题，行业亟需无对话训练数据的CRS落地路径，但此前缺乏系统性的方案验证。

### 方法关键点
- 落地三段式零数据CRS启动流程：1）从非对话种子数据（商品评论、元数据、用户-商品交互）中用信息论准则主动筛选高价值样本；2）用Teacher LLM基于选中样本合成对话训练数据；3）用合成数据微调目标CRS模型，支持LoRA/Full-SFT两种微调范式
- 选样阶段设计两种无监督准则：JS多样性优先覆盖样本分布，Fisher信息优先选择对模型参数增益最高的样本，两者效果均优于随机/热度选样
- 合成数据阶段仅需复用少量通用对话风格模板，不需要域内对话参考，生成「用户查询+推荐列表」的配对训练数据

### 关键结果
在ReDial（1万条对话）、INSPIRED（1千条对话）两个标准CRS数据集上测试，对比零样本、无域信号的随机合成数据等基线：域信号锚定的合成数据比零样本基线Recall@1最高提升207.8%，比无域信号的合成数据提升150%+；主动选样比随机选样在同等预算下Recall提升15%-25%；低资源场景下纯合成数据效果优于仅用稀缺真实对话训练的模型，混合训练可再提升10%以上。

最值得记住的结论：零数据启动CRS的核心不是用大模型随便生成对话，而是必须把合成过程锚定到域内的非对话信号上，才能获得可用的落地效果。
