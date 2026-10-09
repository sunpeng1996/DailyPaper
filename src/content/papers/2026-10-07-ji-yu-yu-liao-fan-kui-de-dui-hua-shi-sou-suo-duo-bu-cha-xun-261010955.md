---
title: Learning Multi-Step Query Rewriting via Corpus Feedback for Conversational
  Search
title_zh: 基于语料反馈的对话式搜索多步查询改写方法
authors:
- João Coelho
- Hong Wang
- Jie Yuan
- Zhuoer Wang
- Samson Koelle
- Wei Niu
affiliations:
- INESC-ID
- Carnegie Mellon University
- Amazon
arxiv_id: '2610.10955'
url: https://arxiv.org/abs/2610.10955
pdf_url: https://arxiv.org/pdf/2610.10955
published: '2026-10-07'
collected: '2026-10-09'
category: QueryRec
direction: 对话式搜索 · 多步查询改写
tags:
- QueryRewriting
- ConversationalSearch
- ReinforcementLearning
- GRPO
- RetrievalFeedback
- Agent
one_liner: 无需人工改写标注，基于强化学习训练多步查询改写Agent，依托检索反馈迭代优化提升对话搜索效果
practical_value: '- 对话搜索/电商客服导购场景可直接复用三类 typed 改写操作（意图补全/同义词改写/HyDE伪文档）+ stop 动作的设计，替代单步改写流程，适配不同检索后端

  - 训练无需人工标注改写对，仅用检索排序指标做GRPO强化学习 reward，可大幅降低业务场景下query改写模型的标注成本，冷启动阶段可以先蒸馏大模型的合法动作轨迹做SFT再RL

  - 电商搜索场景中，多步改写可优先跑前3步即可拿到大部分收益，后续边际收益极低，可通过截断控制推理成本，也可在 reward 中加入 step penalty
  进一步优化成本效率

  - 伪文档生成不需要零-shot生成，可基于前序步骤召回的语料词汇做改写，既避免幻觉又提升检索匹配度，适配电商商品标题/详情页的特定术语匹配需求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有对话式查询改写（CQR）多为单步生成，改写完成前看不到语库的实际内容，无法适配目标语料的实体、词汇表达，固定规则的伪相关反馈也无法自适应调整改写策略，且大部分方法依赖人工标注的改写对，落地成本高。

### 方法关键点
- 将CQR建模为多轮序列决策问题，Agent每步可选择4种动作：`<intent>`（补全对话上下文生成自包含查询）、`<rephrase>`（生成词汇变体解决匹配gap）、`<hyde>`（生成回答类伪文档做doc-doc匹配）、`<stop>`（终止迭代），每步改写的召回结果会作为后续决策的上下文
- 训练分两阶段：先蒸馏大模型的合法动作轨迹做SFT解决冷启动，再用GRPO做强化学习，仅用排序激励型检索 reward（RIRS）做优化，无需任何人工改写标注，reward仅看最终改写的召回排序结果
- 每步最多召回top5片段截断到128token，总迭代步长上限5步

### 关键实验
在TopiOCQA、QReCC数据集上和ConvSearch-R1等SOTA单步改写方法对比，TopiOCQA上MRR达41.4，比最优基线提升3.6个百分点，nDCG@3达40.6，提升4.4个百分点；QReCC上MRR达57.2，提升0.7个百分点，nDCG@3达55.8，提升1个百分点。零-shot迁移到TREC CAsT数据集无需额外训练，性能超过基线，且适配BM25、稠密向量等多种检索后端。

### 核心结论
多步改写的性能收益核心来自「先做意图补全、再做词汇适配、最后生成语料grounded伪文档」的自适应策略，而非单纯的模型容量提升。
