---
title: 'TAGGRAPH: Tag-Augmented Graphs for Graph Retrieval of Agent Persistent Histories'
title_zh: TAGGRAPH：面向Agent持久历史检索的标签增强图框架
authors:
- Yu-Su Chen
- Yu-Jung Liang
- Pengtao Xie
affiliations:
- University of California, San Diego
arxiv_id: '2609.38353'
url: https://arxiv.org/abs/2609.38353
pdf_url: https://arxiv.org/pdf/2609.38353
published: '2026-09-29'
collected: '2026-10-01'
category: Agent
direction: Agent长记忆检索·图与词法方案对比
tags:
- LLM Agent
- Long-term Memory
- Graph Retrieval
- BM25
- Personalized PageRank
- Memory Evaluation
one_liner: 提出Agent长记忆检索可控对比框架，明确不同检索方案的跨场景表现差异
practical_value: '- 落地Agent长记忆系统时优先测BM25基线，长历史多干扰场景下BM25效果优于多数图检索方案，研发投入产出比更高

  - 图检索的效果瓶颈在标签抽取质量，优先选择能生成高复用度、低冗余标签的模型，可大幅提升检索表现

  - 检索方案选型匹配场景：短紧凑用户记忆（如电商用户偏好快照）用局部标签遍历即可，长多轮交互历史（如客服对话历史）可加PPR扩散提升表现

  - 做检索方案迭代时固定输入表示，不要同时调整抽取和检索模块，避免无法定位收益来源'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM Agent依赖长记忆实现跨会话一致性，现有检索方案多同时调整表示、索引、检索模块，无法明确各组件收益，且多数图检索方案未与强词法基线做公平对比，缺乏跨场景的统一评估框架。

### 方法关键点
- 统一5W+Extra抽取范式：每轮对话抽取为层级化语义标签，构建共享的标签-主题-文件基础图，所有检索方案使用相同抽取结果，实现可控对比
- 两类图检索方案：TagGraph系列（局部遍历，含基础版、停词过滤版、TF-IDF加权版），AdaptiveGraph（新增时序边+Personalized PageRank扩散排序）
- 基线设置：BM25基于相同抽取结果检索，OpenClaw基于原始文本做混合稠密+词法检索作为工业界参考

### 关键实验结果
在两个公开基准上测试：1. LongMemEval-S（长历史多干扰场景）：AdaptiveGraph MRR最高达0.844，同抽取结果的BM25达0.867，OpenClaw达0.880；2. ATANT Core（紧凑叙事场景）：局部TagGraph-Stopwords MRR最高达0.734，AdaptiveGraph因主题稀释比局部方案低0.15左右；3. 标签抽取质量对效果的影响远大于检索算法，标签收敛度高的Gemma比GPT-OSS在同检索方案下MRR高0.29。

### 核心结论
没有普适最优的长记忆检索方案，选型前必须在目标场景测试强词法基线，标签抽取质量是图检索效果的核心瓶颈。
