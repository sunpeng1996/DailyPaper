---
title: 'InfluMatch: Frontier-Quality KOL Search at 4B-Model Cost'
title_zh: InfluMatch：用4B参数模型实现前沿效果的KOL搜索系统
authors:
- Krittanon Kaewtawee
- Petmongkon Pornpichitsuwan
- Natchaya Temyingyong
- Nutnicha Laplamoon
- Wachiravit Modecrua
- Krittin Pachtrachai
- Touchapon Kraisingkorn
affiliations:
- Amity AI Holdings Co.,Ltd.
arxiv_id: '2607.05968'
url: https://arxiv.org/abs/2607.05968
pdf_url: https://arxiv.org/pdf/2607.05968
published: '2026-07-07'
collected: '2026-07-08'
category: RecSys
direction: 级联检索优化 · 低成本KOL智能匹配
tags:
- KOL Matching
- Cascade Retrieval
- SimPO
- Reranking
- Low Cost LLM
one_liner: 基于三级级联小模型流水线，以1/35成本实现比肩前沿大模型的泰语KOL搜索效果
practical_value: '- 可直接复用「粗召回→低成本LLM rerank过滤到Top10→高成本LLM推理」三级级联架构，比直接给全量候选跑大模型效果高14个P@5点，同时token消耗降低50%以上，适合电商达人匹配、广告素材检索等多模态检索排序场景。

  - Rerank阶段采用SimPO pairwise偏好训练+单Yes token log概率打分的方案，推理延迟极低，泛化性远超pointwise标注训练的模型，甚至能比肩前沿大模型的排序效果，可直接落地到工业级排序链路。

  - 不要盲目迷信离线pointwise指标：pointwise SFT+GRPO微调虽然离线准确率更高，但端到端排序效果反而不如未微调的基座模型，优先采用相对偏好标注做训练，更贴合真实排序需求。

  - 4B级小模型足够支撑工业级检索排序核心环节，针对性微调后性价比远高于调用前沿大模型API，适合成本敏感的业务场景。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有泰语KOL匹配方案存在明显缺陷：关键词结构化搜索语义匹配能力差，纯dense召回P@5仅54.5%接近随机水平；全量候选调用前沿大模型打分虽然准确，但成本高、延迟高，无法支撑大规模落地，亟需低成本、高准确率的方案适配自由形态的多维度营销需求。

### 方法关键点
- 三级级联架构：第一阶段dense召回取Top50候选，优先保障召回率；第二阶段4B参数点wise reranker，以单Yes token的log概率作为打分依据，过滤到Top10候选，推理成本极低；第三阶段4B参数推理器按多维度规则给每个候选打分+生成泰语解释，输出最终排序。
- 训练策略：Reranker采用SimPO做pairwise偏好微调（LoRA），直接优化排序目标；推理器实测用未微调的基座效果最好，pointwise SFT+GRPO微调虽然离线指标高，但端到端效果反而下降。
- 数据构造：合成符合真实营销场景的泰语brief，配套5个固定维度的匹配规则，人工标注pointwise分数、binary匹配结果、pairwise偏好三类标签。

### 关键实验结果
实验基于11条全标注query（每条对应50个KOL标注）、31条Top10标注query，对比基线包括纯召回、前沿大模型Kimi-K2.6、全量候选直接推理等方案：完整级联方案P@5达94.1%，比肩Kimi-K2.6的91.8%，输出token量少35倍，单A100上50个KOL的查询仅需20s；rerank+推理比直接给全50个候选做推理高14个P@5点。

### 最值得记住的一句话
可迁移的监督信号存在于相对偏好判断中，而非绝对标注分数，盲目追求离线pointwise指标反而会损害端到端排序效果。
