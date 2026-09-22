---
title: 'Beyond Linear Context: Graph-Guided Evidence Navigation for Long-Novel Reasoning
  with a Local 9B Language Model'
title_zh: 图谱引导证据导航：本地9B大模型的长篇文本长上下文推理方法
authors:
- Wenji Fu
affiliations:
- Southwestern University of Finance and Economics
arxiv_id: '2609.22939'
url: https://arxiv.org/abs/2609.22939
pdf_url: https://arxiv.org/pdf/2609.22939
published: '2026-09-19'
collected: '2026-09-22'
category: RAG
direction: 检索增强 · 图谱引导长上下文推理
tags:
- Knowledge Graph
- Long-Context Reasoning
- RAG
- Small Language Model
- Question Answering
one_liner: 基于冻结知识图谱的证据导航方案提升本地9B大模型长上下文推理表现，超近期窗口基线7.69pp
practical_value: '- 电商商品/内容的长图文详情、用户评论、售后记录可构建领域KG替代普通向量RAG，优先召回KG 2-core区域的高价值证据，提升多跳咨询问题（如某材质商品是否适合敏感肌）的回答准确率

  - 搭建RAG系统时需单独统计「知识召回率」（即用户问题的答案在检索库中的覆盖比例），该指标对最终效果的影响远大于检索排序策略，避免把建库缺陷误判为检索算法问题

  - 多模态Agent处理长上下文任务（如全店商品售后问题解答）时，可采用BM25+稠密检索+图谱排序的 reciprocal rank 融合策略，在小上下文窗口限制下获得最优召回效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有长上下文大模型按线性顺序处理输入，存在中间位置信息遗忘、注意力资源被无效内容占用的问题，跨篇章多跳证据链推理效果差；且大模型长上下文推理成本高，小模型受窗口限制无法处理超长文本，需要更高效的证据组织方式降低推理成本、提升小模型长上下文推理能力。
### 方法关键点
- 长文本2-pass构建冻结知识图谱：Pass1过滤冗余内容保留核心信息片段，Pass2抽取实体、关系及对应证据原文，合并实体变体后经过孤立节点占比<60%、边密度≥0.5等质量门控，保留完整原文本作为无损侧车
- 设计5种可审计的图谱导航策略，最优G5融合策略：基于问题选项生成查询，采用BM25、稠密检索、图谱排序的 reciprocal rank 融合得到最多6条候选证据，在固定上下文预算下输入模型
- 全程冻结Qwen3.5-9B模型（关闭推理能力）与图谱，黄金标注证据段落仅用于事后评估，不参与检索、排序过程
### 关键实验
- 数据集采用DetectiveQA，包含30部中文侦探小说、234道多选推理题，拆分两个建库队列（legacy流水线164题、新流水线70题）
- 对比基线：近期窗口输入（B1）、全本压缩（B2）、普通向量RAG（B3）、仅问题输入（Q0）
- 核心结果：G5策略准确率达53.85%，较B1高7.69pp，较B2高2.56pp，较B3高2.14pp；在无原文本无法回答的Q0-hard子集上准确率达42.86%；黄金证据在KG 2-core区域富集2.35倍，新旧建库流水线的线索召回率分别为16%、73%，差异远大于方法间差异

RAG系统的效果瓶颈首先是建库的知识召回率，其次才是检索排序策略，混淆二者会导致优化方向完全错误。
