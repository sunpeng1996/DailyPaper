---
title: 'Your Prompt Should Do More: Effects of Retrieval Instructions in Embedding
  Models'
title_zh: 嵌入模型检索指令生效机制与查询侧干扰鲁棒性优化研究
authors:
- Amanda Myntti
- Jenna Kanerva
- Veronika Laippala
- Filip Ginter
affiliations:
- University of Turku, Finland
- TurkuNLP
- Ellis Institute Finland
arxiv_id: '2610.10508'
url: https://arxiv.org/abs/2610.10508
pdf_url: https://arxiv.org/pdf/2610.10508
published: '2026-10-07'
collected: '2026-10-08'
category: RAG
direction: RAG · 嵌入模型指令跟随优化
tags:
- Dense Retrieval
- Embedding Model
- Instruction Tuning
- Hard Negative Mining
- RAG
- Robustness
one_liner: 发现嵌入模型对查询侧语义干扰鲁棒性差，提出查询侧负样本微调方案大幅提升指令跟随能力
practical_value: '- 电商/搜索的检索嵌入微调时，可加入查询侧同义改写硬负样本，仅需少量数据就能大幅降低召回语义相似但不符合用户意图的结果的概率，比如避免搜"跑鞋男"召回"跑鞋女"

  - 评估带指令的嵌入模型时，不要仅依赖MTEB等标准基准，需补充带查询侧干扰项的业务相关测试集，才能真实反映线上效果

  - 微调时混合训练任务导向检索和通用语义匹配任务，在获得指令跟随能力提升的同时，不会大幅损失通用检索性能，避免灾难性遗忘'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有带指令的嵌入模型在MTEB等标准隔离评测上表现优异，但实际业务场景的候选池常存在与查询语义高度相似但不符合任务要求的内容，标准评测无法反映模型真实指令跟随能力，甚至很多模型对无关指令、乱码指令也能产出不错的分数，指令对查询嵌入的影响机制尚不明确。

### 方法关键点
- 定义3个量化指标衡量指令效果：相似度提升（加指令后查询与正样本的相似度变化）、位移（加指令前后查询嵌入的余弦距离）、定向性（指令引发的嵌入移动指向正样本的程度）
- 构造查询侧干扰项：用LLM生成每个查询的同义改写作为硬负样本，测试模型能否忽略语义相似干扰、按指令召回正确结果
- 提出微调方案：训练时加入查询侧干扰项作为负样本，同时混合语义匹配任务避免通用检索能力下降

### 关键结果
- 测试8个主流开源嵌入模型，加入同义干扰项后QA任务Recall@1从平均0.106暴跌至0.006，几乎完全失效
- 对Qwen/Qwen3-Embedding-0.6B微调后，带同义干扰的SQuAD任务Recall@1从0.014提升至0.470，多语言翻译检索Recall@1从0.102提升至0.569，无干扰的标准检索性能仅下降不到2%，MMTEB通用任务性能几乎无损失

最值得记住的结论：现有嵌入模型的标准评测大幅高估了真实场景下的指令跟随能力，加入查询侧语义相似硬负样本的微调和评测是提升业务鲁棒性的核心手段
