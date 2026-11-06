---
title: 'CORE: Coarse-to-Fine Search with Context Management for Deep Research'
title_zh: CORE：面向深度研究Agent的粗到细搜索与上下文管理框架
authors:
- Hoang Tran Vuong
- Ngoc Quan Pham
- Hung Bui
- Fatih Porikli
- Dat Quoc Nguyen
affiliations:
- Qualcomm AI Research
- Qualcomm Vietnam Company Limited
arxiv_id: '2611.07859'
url: https://arxiv.org/abs/2611.07859
pdf_url: https://arxiv.org/pdf/2611.07859
published: '2026-11-05'
collected: '2026-11-06'
category: Agent
direction: Agent 搜索工具与上下文管理优化
tags:
- Agent
- Retrieval
- Context Management
- ColBERT
- RAG
one_liner: 训练免调的深度研究Agent搜索框架，多基准下取得SOTA回答准确率与证据召回
practical_value: '- 检索侧可复用ColBERT等晚交互重排器的token级相似度矩阵做相关片段提取，无额外编码开销，同时提升相关性、降低返回token量，可直接迁移到电商搜索结果摘要、商品详情动态截取场景

  - 跨搜索的片段级去重机制，避免冗余信息占用LLM上下文窗口，适合多轮对话导购Agent、多步搜索型推荐系统的上下文管理模块

  - 训练免调的harness设计与Agent完全解耦，迭代检索逻辑无需修改Agent侧代码或重训模型，大幅降低业务侧迭代成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
深度研究Agent依赖多轮搜索积累证据，现有搜索harness存在核心矛盾：检索需要长上下文保证语义匹配准确性，但返回长文本会占用Agent有限的上下文窗口，稀释关键证据、提升推理成本；现有方案要么依赖额外LLM做摘要增加开销，要么细粒度检索丢失上下文导致匹配效果下降。

### 方法关键点
- 两阶段粗到细搜索：先基于AgentIR-4B做粗召回取Top300长passage，再用Reason-ModernColBERT重排，复用重排阶段的token级相似度矩阵定位passage内最高相关片段，无额外编码开销，仅返回精准snippet给Agent
- 上下文管理：支持Agent针对已召回片段发起上下文扩展，仅对目标文档内的passage做语义匹配返回相邻上下文，无需全库重搜；同时实现跨搜索的片段级去重，仅保留首次出现的完整snippet，重复内容替换为精简引用
- 完全训练免调：兼容任意Agent模型，无需修改Agent结构或重训即可接入

### 关键实验
在3个基准（BrowseComp-Plus含10万文档、BrowseComp-Wikipedia含600万文档、BrowseComp-PlusCM含5.53亿文档）上对比Tongyi DeepResearch、OpenResearcher两个SOTA harness，搭配3种Agent（GPT-5.4、Qwen3.8-27B、通义深度研究30B）均取得最优结果：在5.53亿文档超大规模语料上，搭配GPT-5.4时回答准确率达68.42%，比次优基线高12.28个点，证据召回高4.79个点，同时峰值上下文token量更低。组件分析显示粗到细搜索单独提升准确率8.23个点，上下文管理再提升9.28个点。

### 核心结论
把证据定位的负担从Agent侧转移到搜索侧，用检索工具的专业能力精简返回内容，比依赖Agent自身处理冗余上下文效率更高、效果更好。
