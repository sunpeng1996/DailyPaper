---
title: 'RippleMem: From Isolated Retrieval to Associative Recollection for Long-Term
  Agent Memory'
title_zh: RippleMem：面向LLM Agent长期记忆的关联式回忆检索系统
authors:
- Jingbo Ji
- Lingyi Li
- Xilong Cheng
- Yuhao Zhou
- Wenji Zhang
- Yuting Tan
- Yunxiao Qin
affiliations:
- Communication University of China
- Zhilian Yinghe Technology Co., Ltd.
- State Key Laboratory of Media Convergence and Communication
arxiv_id: '2608.13334'
url: https://arxiv.org/abs/2608.13334
pdf_url: https://arxiv.org/pdf/2608.13334
published: '2026-08-13'
collected: '2026-08-14'
category: Agent
direction: Agent 长期记忆关联检索优化
tags:
- LLM Agent
- Long-Term Memory
- Associative Retrieval
- Memory Graph
- RAG
one_liner: 提出事件中心的关联回忆式Agent长期记忆系统，提升跨会话证据召回精度同时大幅降低建图成本
practical_value: '- 电商客服Agent、个性化推荐Agent的长期用户记忆模块，可复用「富线索事件记忆单元+语义/结构双关联记忆图」的写路径设计，替代现有平铺记忆存储，提升跨会话用户偏好/历史行为召回完整度

  - 现有RAG系统召回分散多片段证据时，可借鉴「初始锚点召回→锚点关联扩展→证据补全」的读路径逻辑，解决单步检索漏召回关联证据的问题，尤其适合需综合用户多轮历史交互的个性化生成场景

  - 记忆图构建环节可复用其稀疏建图策略：仅对新插入记忆的Top-N近邻做语义/结构化关联打分，保留高置信度边，相比全量建图成本降低30倍，适合大规模用户记忆库的在线增量更新场景

  - 对话推荐、长期用户画像存储业务可直接复用其记忆单元schema（事件重述+向量+参与者/地点/时间线索），降低跨会话信息冲突、指代消解的处理成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent长期记忆系统存在三大痛点：全上下文方法长语境搜索噪声大、平铺检索返回孤立不完整记录、图存储系统建图成本高且压缩事件上下文，当回答query的证据分散在多个跨会话交互中时，极易漏召回关键支撑信息导致回答错误。

### 方法关键点
- 写路径：将交互历史转为富线索的事件记忆单元，每个单元包含标准化事件重述、语义向量、参与者/地点/时间三类结构化线索；构建事件为中心的稀疏记忆图，边分为语义关联（向量余弦相似度）和结构关联（参与者/地点的Jaccard重合度+时间间隔衰减得分）两类，仅保留高置信度边降低存储成本。
- 读路径：采用自适应关联回忆机制，首先通过语义+词汇+结构化线索混合召回初始证据锚点，再以锚点为中心沿记忆图做有限跳扩展，匹配待补全的证据目标，迭代召回遗漏的支撑信息，最后做多源证据去重排序得到最终上下文。

### 关键实验
在LoCoMo、LongMemEval-S两个长期对话记忆基准上测试，对比Mem0、Zep、SimpleMem、RF-Mem等10+SOTA基线；LoCoMo上LLM-as-a-Judge准确率较最强基线提升3.95%，LongMemEval-S上最高提升11.87%，记忆图构建成本相比传统图基线降低约30倍，同时回答上下文token数仅为同类方法的1/5左右。

### 核心洞见
长期记忆的核心瓶颈不是存储容量，而是如何从分散的交互痕迹中召回完整的可回答证据集合，已召回的记忆不仅是回答上下文，更是补全遗漏证据的线索。
