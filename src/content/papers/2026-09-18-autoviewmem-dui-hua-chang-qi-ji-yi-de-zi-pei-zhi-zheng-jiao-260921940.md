---
title: 'AutoViewMem: Self-Configuring Orthogonal Views for Conversational Long-Term
  Memory'
title_zh: AutoViewMem：对话长期记忆的自配置正交语义视图框架
authors:
- Zijie Cao
- Xijun Qu
- Zhicheng Gu
- Xiaoshu Chen
- Duanyang Yuan
- Yanning Hou
- Sihang Zhou
- Jianxing Gong
- Jian Huang
- Yang Mei
affiliations:
- National University of Defense Technology
arxiv_id: '2609.21940'
url: https://arxiv.org/abs/2609.21940
pdf_url: https://arxiv.org/pdf/2609.21940
published: '2026-09-18'
collected: '2026-09-21'
category: Agent
direction: Agent 长时记忆 · 多视图语义组织
tags:
- Long-term Memory
- Conversational Agent
- Multi-view Memory
- Retrieval
- Memory Consolidation
one_liner: 通过写时自生成低重叠语义视图组织对话记忆，大幅提升长时交互的检索与个性化效果
practical_value: '- 可复用写时语义解耦思路：对电商用户行为/对话数据，提前按低重叠语义视图（偏好、消费能力、场景需求等）拆分存储记忆，避免混合表征导致的RAG检索噪声，提升个性化推荐召回准确率

  - 可直接复用DPP视图选择方法：在自定义用户画像维度/记忆分类时，用DPP自动选择低重叠维度集，替代人工枚举的固定schema，降低运营成本，适配不同用户的差异化行为特征

  - 离线记忆合并策略可迁移：用相似度聚类+LLM裁决的方式合并冗余的用户行为/记忆记录，既降低向量库存储成本，又避免冲突信息干扰检索，适配长周期用户画像更新场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有对话长时记忆系统多采用固定粒度或静态schema存储，当对话中同时混杂偏好、事件、约束、时间更新等异构信息时，混合表征会产生语义干扰，导致top-K检索对噪声敏感，相关证据排序靠后，无法支撑长周期个性化交互需求。

### 方法关键点
- 在线流程：每积累50轮对话，LLM自动生成10个候选语义视图，通过DPP选择低重叠的10个活跃视图集，指导写时结构化提取记忆，每个记忆携带标签、时间戳、来源provenance，写入统一向量索引
- 离线 consolidation：先通过哈希去重，再构建相似度图（cos≥0.9建边）聚类，用LLM按包含、互补、独立三类规则合并冗余记忆，保留来源可追溯
- 检索阶段：直接采用标准top-K语义检索，无需额外路由逻辑，仅对检索结果按provenance去重后输入LLM

### 关键实验
在LoCoMo（1540个长对话QA）、PersonaMem-32k（589道个性化选择题）两个基准上，以Qwen3-8B/14B为底座，对比Mem0、MemGAS、MemoryBank等基线：
1. LoCoMo上Qwen3-14B底座，LLM-Judge得分达0.853，领先最强基线Mem0的0.765
2. PersonaMem-32k上Qwen3-14B底座，准确率达69.10%，领先最强基线A-mem的63.33%，超过全上下文oracle 13.92个百分点
3. 检索无正例率仅5.14%，显著低于所有消融变体

### 核心结论
长时记忆检索效果的瓶颈不仅是粒度设计，写前的语义解耦、降低混合表征的语义干扰，对提升检索准确率的收益远高于复杂的查时路由逻辑。
