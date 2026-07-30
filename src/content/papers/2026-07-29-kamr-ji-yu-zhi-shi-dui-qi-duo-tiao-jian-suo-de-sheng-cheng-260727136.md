---
title: 'KAMR: Grounding Generation via Knowledge-Aligned Multi-hop Retrieval'
title_zh: KAMR：基于知识对齐多跳检索的生成事实锚定
authors:
- Xiaochen Wang
- Yuan Zhong
- Haoyu Wang
- Ting Wang
- Fenglong Ma
affiliations:
- The Pennsylvania State University
- University at Albany, SUNY
- Stony Brook University, SUNY
arxiv_id: '2607.27136'
url: https://arxiv.org/abs/2607.27136
pdf_url: https://arxiv.org/pdf/2607.27136
published: '2026-07-29'
collected: '2026-07-30'
category: RAG
direction: Graph RAG · 多跳知识检索优化
tags:
- RAG
- Multi-hop Retrieval
- Knowledge Graph
- Contrastive Learning
- Graph RAG
one_liner: 区分锚定/关联三元组，用弱监督预训练优化两阶段多跳检索，提升Graph RAG多跳推理性能
practical_value: '- 电商/商品知识图谱多跳召回可复用两阶段检索逻辑：先召回和用户query强语义对齐的锚定三元组（如用户搜「xx品牌精华适合肤质」时先召回「xx品牌-旗下产品-xx精华」），再沿知识图谱邻域扩展关联三元组（如「xx精华-适用肤质-干皮」），避免漏召回语义弱相关但推理必需的事实

  - 缺少query-三元组对齐标注时，可复用弱监督数据集构造方法：掩码领域知识三元组的单个元素，用LLM生成对应query，构造对比训练样本，无需人工标注即可训练领域专属知识检索器

  - 电商导购Agent的多轮推理RAG模块可复用双对比损失设计：pair级损失优化query和局部三元组的匹配（锚定召回），element级损失优化query和三元组元素的匹配（关联扩展），平衡语义相关性和结构连通性，提升复杂用户query的回答准确率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Graph RAG的多跳检索大多基于全局语义匹配独立打分三元组，易遗漏和用户query语义弱对齐但推理必需的关联事实；同时多数多跳基准仅提供最终答案标注，缺乏query-三元组对齐的监督信号，导致检索器训练难度大，多跳推理链的召回完整度偏低，制约下游生成准确率。
### 方法关键点
- 显式区分两类三元组：和query有2个元素匹配、强语义对齐的**锚定三元组**，和query仅1个元素匹配、需和锚定三元组结构连通的**关联三元组**
- 弱监督数据集构造：掩码三元组的单个元素得到3组局部三元组，用LLM生成对应query，无需人工标注即可构造query-局部三元组对齐训练集
- 双对比预训练损失：pair级InfoNCE损失对齐query和局部三元组，优化锚定三元组召回；element级InfoNCE损失对齐query和三元组单个元素，优化关联三元组召回
- 两阶段推理：先全局检索top-M锚定三元组，再沿知识图谱邻域迭代扩展关联三元组，直到达到检索预算
### 关键结果
在PathQuestion 2/3跳、CWQ共4个基准，3类LLM backbone（Qwen3-8B、LLaMA2-7B、ChatGPT-3.5）上对比14个基线模型；PathQuestion 3跳数据集上，KAMR(N=2)的Triplet Recall达94.09%、Path Recall达85.78%，较最优基线分别提升14.91pct、26.43pct；CWQ数据集上搭配ChatGPT-3.5时，KAMR(N=1)的F1达42.70%，较最优语义检索基线高0.13pct。
### 核心结论
多跳知识检索不能仅依赖全局语义匹配，需区分强对齐的锚点事实和弱对齐的关联事实，用结构约束补全语义匹配的盲区。
