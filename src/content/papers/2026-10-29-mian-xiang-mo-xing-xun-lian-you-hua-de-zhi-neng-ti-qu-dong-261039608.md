---
title: 'From Intent to Improvement: Agentic Dataset Search for Better Model Training'
title_zh: 面向模型训练优化的智能体驱动数据集搜索框架
authors:
- Qiaosheng Chen
- Kaijia Huang
- Fanqi Zhou
- Gong Cheng
affiliations:
- Nanjing University
- State Key Laboratory for Novel Software Technology, Nanjing University
arxiv_id: '2610.39608'
url: https://arxiv.org/abs/2610.39608
pdf_url: https://arxiv.org/pdf/2610.39608
published: '2026-10-29'
collected: '2026-10-30'
category: Agent
direction: 智能体信息检索 · 训练数据获取
tags:
- Agentic_IR
- Dataset_Search
- LLM_Agent
- Hybrid_Retrieval
- Training_Data_Acquisition
one_liner: 提出契约管控的AgenticDS数据集检索框架，大幅提升检索精度与下游模型训练效果
practical_value: '- 契约管控的三模块（Planner/Engineer/Critic）智能体检索架构可直接复用：LLM仅负责语义决策，检索、过滤、排序逻辑用确定性代码实现，既保留自然语言理解的灵活性，又大幅降低幻觉，适配电商多约束（价格、品类、物流、用户标签）的商品/内容检索场景

  - 混合检索+有界KG扩展的召回策略可迁移：先做BM25+Dense的混合召回，再按预设路径做KG多跳扩展，搭配路径衰减、热度惩罚过滤噪声，可解决冷启动item元信息稀疏的召回问题

  - 检索效果与下游业务效果挂钩的评估范式可参考：不仅看NDCG、MAP等检索指标，还做控制变量的检索到业务落地的全链路验证，避免检索指标上涨但业务效果下跌的错位问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有百万级ML资源平台的数据集搜索依赖文本相似度匹配，无法满足用户融合语义训练目标与硬约束（任务类型、许可证、训练阶段）的查询需求：传统检索无法处理元信息稀疏的数据集，也不能校验约束满足情况；无约束的LLM Agent检索存在幻觉，无法保证返回的数据集能真正提升下游模型训练效果，检索相关性和训练效用脱节的问题突出。
### 方法关键点
- 采用契约管控的三模块智能体架构：Planner将自然语言查询编译为带约束、允许KG遍历路径、验收标准的结构化搜索计划；Engineer仅执行确定性算子，完成Dense+BM25混合检索、有界KG多跳扩展、带约束的预排序，全链路保留证据来源；Critic基于结构化证据包打分，要么输出最终排序要么输出仅支持局部修复的诊断，避免LLM篡改检索语义
- 多源证据分组融合：采用分组归一化的RRF融合不同证据分支的结果，平衡文本检索、KG扩展的权重，避免单一证据源噪声
- 约束柔性处理：明确违反硬约束的候选直接过滤，元信息缺失的候选保留不丢弃，兼顾召回率和准确率
### 关键实验
- 构建HuDS-Bench基准，包含200个自然语言查询、24908条分级标注，覆盖4类不同查询场景
- 对比15个基线系统，NDCG@10比最强稠密-稀疏混合基线高25.7%，比商用LLM Agent高18.9%
- 控制变量的搜索-训练全链路验证显示，返回的数据集在数学、代码、医疗三个领域的下游训练准确率均为最优，弱基础模型的增益更显著
- 推理成本比商用LLM Agent低59%~82%，速度是Codex Agent的5.8倍
### 核心结论
关系型证据是条件增益而非加性增益，知识图谱扩展的收益来自配套的证据校验而非本身，检索精度的提升必须落地到下游业务效果才有实际价值
