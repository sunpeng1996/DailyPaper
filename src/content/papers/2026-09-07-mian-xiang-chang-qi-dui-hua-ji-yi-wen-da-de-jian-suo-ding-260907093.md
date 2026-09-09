---
title: 'Where to Look and What to Use: Retrieve-Localize-Generate for Long-Term Conversational
  Memory Question Answering'
title_zh: 面向长期对话记忆问答的检索-定位-生成框架MemLoc
authors:
- Yifan Wang
- Xinkui Lin
- Yongxiu Xu
- Shen Gao
- Ruochen Yang
- Kun Huang
- Yubin Wang
- Jie Wu
- Wei Liu
- Jian Luan
affiliations:
- University of Electronic Science and Technology of China
- Institute of Information Engineering, CAS
- University of Chinese Academy of Sciences
- Xiaomi Inc.
- Tsinghua University
arxiv_id: '2609.07093'
url: https://arxiv.org/abs/2609.07093
pdf_url: https://arxiv.org/pdf/2609.07093
published: '2026-09-07'
collected: '2026-09-09'
category: Agent
direction: Agent 长对话记忆管理优化
tags:
- Long-term Memory
- RAG
- Conversational QA
- Policy Optimization
- Multi-granularity Retrieval
one_liner: 提出Retrieve-Localize-Generate三阶段MemLoc框架，解决长期对话记忆QA的证据分散与lost-in-the-middle问题
practical_value: '- 电商个性化咨询/用户画像召回场景可复用多粒度召回设计：将用户历史行为/对话拆分为会话、轮次、事件、关键词、时间等多粒度，用熵值加权自适应选择最优召回粒度，结合跨会话语义+时间图传播，解决跨周期用户行为关联难的问题

  - 证据ID锚点方案可直接迁移到生成式推荐/对话场景：召回后先提取query相关片段并分配唯一ID，生成时用ID作为引导信号，既保留完整上下文避免语义漂移，又有效缓解lost-in-the-middle效应，提升生成内容的事实一致性

  - SHPO自优化训练策略可降低Agent记忆模块的标注成本：无需额外人工标注，仅通过对比同一query的正确/错误推理轨迹生成hint迭代优化，可低成本提升Agent的证据定位能力，适配小样本业务场景

  - 多粒度召回的消融结论可直接复用：事件级+轮次级粒度组合召回效果最优，纯会话级粒度召回噪声高，时间粒度需结合语义使用，可直接套用到用户历史行为召回架构'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
长对话记忆问答是个性化智能客服、对话Agent的核心能力，现有RAG方案存在两大痛点：一是相关证据分散在时间跨度大的不同会话，单粒度召回难以建模跨会话依赖，导致证据不完整；二是召回会话存在大量噪声，触发LLM的lost-in-the-middle效应，而传统过滤/压缩方案容易丢失信息或语义漂移，严重影响回答准确率。
### 方法关键点
- 三阶段Pipeline：采用Retrieve→Localize→Generate架构，逐步缩小证据范围，平衡召回覆盖率和精准度
- 检索模块：每个会话拆分为会话、轮次、摘要、关键词、事件、时间6种粒度，基于熵值自适应选择最优粒度做内部路由，再构建跨会话语义+时间边的记忆图，通过Personalized PageRank做全局传播，召回Top-K候选会话
- 定位模块：先做单会话内证据片段提取去噪，再做跨会话重排去冗余，输出证据片段ID作为生成锚点；Locator先在多跳QA数据集做SFT冷启动，再通过SHPO策略自优化，仅对比同query的正确/错误推理轨迹生成hint，无需额外标注
- 生成模块：用证据ID作为轻量锚点引导LLM定位关键片段，既保留完整上下文，又缓解lost-in-the-middle效应
### 关键实验
在4个长记忆QA基准（LongMemEval-S/M、LoCoMo、Long-MT-Bench+）上对比12种基线（RAPTOR、Mem0、MemGAS等），8B版本MemLoc的GPT-4o-Judge得分在4个基准上分别达到68.4、54.2、57.4、77.42，均为SOTA，F1最高较基线提升5.16，检索Recall@3最高达87.97，同时token消耗处于合理区间。
### 核心结论
长记忆管理的核心是先粗粒度关联跨上下文依赖，再细粒度定位证据，用轻量锚点引导生成比盲目压缩上下文效果更优。
