---
title: 'ScholarCatalyst: A Benchmark for Retrieving Papers That Inspire New Research'
title_zh: ScholarCatalyst：面向启发性科研文献检索的基准数据集
authors:
- Sohyeon Kim
- Yoonho Lee
- Bo Liu
- Dayoon Ko
- Rulin Shao
- Seungone Kim
- Graham Neubig
- Pang Wei Koh
- Aakanksha Chowdhery
- Akari Asai
affiliations:
- Stanford University
- Seoul National University
- University of Washington
- Carnegie Mellon University
- MIT
arxiv_id: '2610.02202'
url: https://arxiv.org/abs/2610.02202
pdf_url: https://arxiv.org/pdf/2610.02202
published: '2026-10-01'
collected: '2026-10-02'
category: Eval
direction: 检索评测 · 科研启发型文献检索
tags:
- Retrieval
- Benchmark
- LLM Agent
- Scientific Literature
- RAG
one_liner: 基于184位研究者一手标注构建科研启发型文献检索基准，验证当前检索与Agent系统性能瓶颈
practical_value: '- 构建领域类检索标注数据集时，可复用其仅输入内容ID的自动化预标注流水线，先由LLM生成候选集、预标注标签，再由专家校验，大幅降低标注成本，适配电商好物灵感、用户决策理由等难标注场景

  - 搭建检索增强类Agent系统时，优先优化底层召回的候选覆盖度，而非盲目堆叠复杂Agent推理逻辑；论文验证在召回覆盖不足时，Agent检索效果甚至弱于直接embedding检索，该结论可直接复用在导购Agent、科研辅助Agent的架构设计中

  - 做灵感类检索（如电商「随便逛逛」、灵感好物推荐）时，不能仅以语义相似度为召回目标，可参考其启发式相关性的标注逻辑，挖掘跨语义、跨品类的高价值候选，避免召回结果同质化

  - 在开放、模糊的检索场景下，慎用Query改写、HyDE等传统优化手段，论文验证这类方法对启发型检索效果提升有限甚至负向，这类场景优先优化embedding空间的相关性建模'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前AI科研辅助系统多聚焦已明确子问题的工程落地，无法像人类研究者一样从海量文献中挖掘能启发开放式研究问题的关键工作；现有科研检索基准均基于公开引用关系或显式信息需求构建，无法捕捉未被引用、但能提供核心启发的文献，缺乏对应能力的评测标准。
### 方法关键点
- 搭建自动化标注流水线，仅需输入论文arXiv ID即可生成预标注的研究问题初稿、候选文献集，大幅降低专家标注成本，支持基准持续更新
- 邀请184位2025-2026年顶会论文的核心作者，标注其项目启动阶段的研究问题对应的启发型文献（catalyst paper），包含未在最终论文中引用的潜在启发文献
- 任务定义为给定项目早期研究问题，从项目启动前发表的191K篇CS领域文献中召回启发型文献，设置核心研究问题（CoreQ）、子领域特定问题（SubQ）两类查询
### 关键实验结果
对比BM25、SPECTER2、Qwen3-Embedding等9类检索模型，以及grep检索、工具调用、深度研究三类LLM Agent：
1. 最优预训练数据截止时间合规的embedding模型Recall@20仅0.48，领域专用检索模型性能比通用模型低16个百分点以上
2. 三类Agent的Recall@20最高仅0.42，弱于直接embedding检索
3. 训练数据可能包含测试集论文的Claude Fable 5.1，Recall@20也仅0.51
### 核心结论
启发型检索的核心瓶颈是候选召回覆盖度，而非上层的Agent推理或reranking能力，语义相似度不等于实际启发价值
