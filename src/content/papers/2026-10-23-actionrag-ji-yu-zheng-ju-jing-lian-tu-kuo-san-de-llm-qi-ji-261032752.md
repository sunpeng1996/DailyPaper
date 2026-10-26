---
title: 'ActionRAG: Evidence-Refining Graph Diffusion for Long-Term Memory in LLM Agents'
title_zh: ActionRAG：基于证据精炼图扩散的LLM Agent长期记忆架构
authors:
- Navyansh Mahla
- Sashank Vandrangi
affiliations:
- Actioneer, Mountain View, USA
arxiv_id: '2610.32752'
url: https://arxiv.org/abs/2610.32752
pdf_url: https://arxiv.org/pdf/2610.32752
published: '2026-10-23'
collected: '2026-10-26'
category: Agent
direction: Agent 长期记忆 · 图RAG优化
tags:
- RAG
- GraphRAG
- LLM Agent
- Long-term Memory
- Graph Diffusion
one_liner: 提出融合分层实体解析与查询时图扩散的RAG架构，大幅提升Agent长期记忆检索精度与成本效率
practical_value: '- 索引阶段分层实体解析trick可直接复用：电商/推荐场景构建用户行为/商品知识图谱时，先做实体类型对齐再做实体归一，可减少节点错配、降低图谱冗余

  - 双通道（实体+三元组）检索+局部图扩散重排架构可迁移到长周期用户兴趣召回：从用户历史行为构建兴趣图谱，查询时同时召回兴趣实体和交互三元组，用图扩散补全多跳关联兴趣，提升长周期推荐准确性

  - 高置信度原始结果保护+hub节点惩罚策略可用于广告/推荐召回排序：避免热门商品/热点内容过度挤占上下文，平衡相关性与新颖性

  - 工程上局部子图扩散可在线部署：p99检索延迟低于500ms（消费级硬件），无需大算力GPU，适配toC实时Agent业务需求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent长期记忆方案存在两大核心缺陷：一是索引阶段实体拆分/合并错误导致事实碎片化，二是检索阶段仅依赖初始语义相似度，忽略关联事实的结构信号，在多跳推理、事实冲突解决、长周期记忆召回场景下精度不足，且全图检索的成本和延迟无法满足在线业务需求。

### 方法关键点
- 离线索引：采用分层实体解析pipeline，先对齐实体类型标签，再做模糊匹配归一，保留所有事实的来源provenance，定期对多源同一事实做摘要更新，降低图谱冗余
- 在线检索：双通道并行召回Top-K实体和Top-KT三元组，构建查询绑定的局部子图，避免全图计算
- 证据精炼：使用接收者归一化的图扩散算法重排三元组得分，同时保护高相似度原始检索结果，新增hub节点惩罚的三元组补全机制，补全初始检索漏掉的关联事实
- 全程无额外LLM调用，所有检索计算仅依赖嵌入和图运算

### 关键实验
在MemoryAgentBench (MAB) 8项确定性任务上测试，对比HippoRAG-v2、GraphRAG、BM25 RAG等10+基线：平均准确率达55.1，比最强检索基线HippoRAG-v2高5.4个点；在冲突解决、测试时学习任务上分别领先10.5、20.6个点；单query平均成本低于0.001美元，p99检索延迟仅440.7ms（消费级Apple Silicon设备）。

### 核心结论
不要把初始检索的相似度得分当作最终结果，利用局部子图的结构信号做二次精炼，能以极低的额外成本大幅提升长周期记忆的召回质量。
