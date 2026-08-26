---
title: Structurally-bounded Agentic Graph Exploration for Evidence-Grounded Scholarly
  DeepSearch
title_zh: 结构约束的智能体图探索实现可审计证据的学术深度搜索
authors:
- Rima Hazra
- Sayan Layek
- Somnath Banerjee
- Soumen Chakrabarti
- Animesh Mukherjee
affiliations:
- National University of Singapore
- TCG CREST
- Indian Institute of Technology Kharagpur
- Singapore Institute of Technology
- Indian Institute of Technology Bombay
arxiv_id: '2608.24809'
url: https://arxiv.org/abs/2608.24809
pdf_url: https://arxiv.org/pdf/2608.24809
published: '2026-08-25'
collected: '2026-08-26'
category: Agent
direction: Agent 结构化检索优化
tags:
- Agentic Search
- Citation Graph
- Natural Language Inference
- Personalized PageRank
- Information Retrieval
one_liner: 用1.5跳引文图+claim级剪枝+时效感知游走做学术搜索，比闭源研究Agent召回高3倍成本降2/3
practical_value: '- 可借鉴固定探索边界的思路替代开放循环Agent，比如电商商品关联推荐先固定1.5跳商品共现/点击图再剪枝排序，大幅降低工具调用成本和不可控性

  - claim级蕴含剪枝trick可迁移到内容/商品关联度判断，从商品详情/评价提取核心卖点，用小模型做卖点蕴含打分过滤弱关联推荐边，比直接语义相似度更准确

  - 时效性感知的个性化随机游走排序可复用，给用户兴趣种子后在商品/内容图上做带新鲜度权重的PPR，平衡相关性和时效性，适配新品推荐场景

  - 子查询拆分+多检索结果取交集的种子召回方法可用于搜索Query理解，拆分多意图子Query后召回结果取交集，提升种子召回的相关性覆盖'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有深度研究Agent采用开放循环搜索模式，终止条件由模型自主判断，存在错误累积、证据选择不可审计、工具调用成本高的问题，学术搜索等对证据可信度要求高的场景亟需可控、可追溯的检索方案。
### 方法关键点
- 仅种子阶段调用外部搜索：将原Query拆分为5个关键词式子Query，每个子Query召回同时满足相关性和时效性的top m篇论文作为种子，后续运算全在固定图内完成
- 1.5跳引文图扩展与剪枝：将种子扩展为1.5跳引文邻域，从每篇论文提取4-5条核心claim，用微调的科学领域蕴含模型计算引用边的支撑度，剪枝无支撑的边和孤立节点
- 时效感知图排序：用带时效性衰减权重的个性化PageRank或SALSA对剪枝后的图排序，返回top k结果
### 关键实验
在50万篇2016-2026年arXiv论文数据集上测试，对比GPT/Claude深度研究Agent、Spector2-Deepwalk基线：ICLR数据集上Recall@50提升3倍，token消耗减少62%，端到端耗时降低58%，单query成本从~$2降至$0.37，证据剪枝决策与人类专家一致性达84%。
### 最值得记住的一句话
把开放探索的Agent问题转化为固定图上的剪枝排序问题，用结构约束替代模型自主决策，既能提升效果又能大幅降低成本、提升可审计性。
