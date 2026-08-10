---
title: 'DocMemo: Dynamic Evidence Discovery via Probabilistic Memory-Guided Retrieval
  for Multi-Modal Document Understanding'
title_zh: DocMemo：概率记忆引导的多模态长文档动态检索理解框架
authors:
- Hanshu Yao
- Janfeng Zhong
- Niu Lian
- Jinpeng Wang
affiliations:
- Harbin Institute of Technology, Shenzhen
- Tsinghua Shenzhen International Graduate School, Tsinghua University
arxiv_id: '2608.07067'
url: https://arxiv.org/abs/2608.07067
pdf_url: https://arxiv.org/pdf/2608.07067
published: '2026-08-07'
collected: '2026-08-10'
category: Agent
direction: Agent长文档理解 · 结构化记忆动态检索
tags:
- Agent Memory
- Long Document Understanding
- Thompson Sampling
- Multi-modal Retrieval
- Dynamic RAG
one_liner: 提出三层解耦记忆+贝叶斯信念更新的动态检索框架，多模态长文档理解性能超SOTA，效率提升2.4倍
practical_value: '- 多轮召回/迭代检索场景可复用三层记忆拆分设计：离线存储静态内容库结构先验、在线维护动态候选relevance置信度、会话级存储用户交互轨迹与信息缺口，解决静态top-k召回漏召后无法补救的问题

  - 贝叶斯信念更新+Thompson采样的动态选路策略可直接迁移到推荐冷启动/探索场景：用Beta分布建模候选 relevance 置信度，正反馈按距离衰减传播到邻域候选（如用户点击商品后给同类目/邻近价格带商品加权），天然平衡探索与利用

  - 多轮迭代的权重调度策略可复用：随轮次提升历史置信度权重λ_t，逐步降低对当前query/特征相似度的依赖，减少重复召回的无效开销

  - 自适应粒度访问可借鉴到电商参数问答/商品说明书理解场景：先召回整商品/整页维度信息，匹配到表格/参数密集区域后再调取细粒度内容，平衡精度与推理成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
长多模态文档理解需要跨数十上百页定位稀疏异构证据，现有静态检索一旦初始召回遗漏关键证据无法补救；多轮迭代检索缺乏跨轮状态传播机制，仅靠上下文积累易过载，无法追踪页面相关性的动态变化，在有限证据预算下召回效率极低。

### 方法关键点
- 三层解耦记忆结构：离线构建Document Schema Memory存储文档结构先验；动态Page Belief Memory用Beta分布建模每页 relevance 置信度，随推理反馈实时更新；会话级Question Episodic Memory记录当前query的推理轨迹与信息缺口，避免重复检索
- 贝叶斯页信念更新机制：推理后标记的有用/无用页直接更新Beta分布参数，正反馈还会按距离衰减传播到邻域页，利用长文档内容局部聚集的特性降低漏召
- 动态检索策略：结合Thompson采样平衡高置信页利用与低置信页探索，随迭代轮次逐步提升历史信念权重，配合自适应粒度访问，信息密集区域补充细粒度视觉切片降低信息损失

### 关键实验
在MMLongBench-Doc、LongDocURL、PaperTab三个长文档VQA基准上测试，相比最强Agent基线，准确率分别提升3.7、8.8、15.0个百分点，整体平均准确率达77.6%；相比基线SimpleDoc，平均迭代次数降至0.41倍，整体效率提升2.4倍；消融实验显示移除三层记忆或贝叶斯更新会导致整体准确率下降2.5~3.0个百分点。

最值得记住的结论：将多轮检索从无状态的上下文积累转化为结构化记忆引导的动态证据探索，是用有限预算提升长序列召回/推理效果的核心思路。
