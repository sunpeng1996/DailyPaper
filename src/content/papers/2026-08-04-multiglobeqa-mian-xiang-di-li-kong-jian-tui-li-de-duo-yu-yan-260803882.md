---
title: 'MultiGlobeQA: A Multilingual and Globally Diverse Benchmark for Geospatial
  Reasoning'
title_zh: MultiGlobeQA：面向地理空间推理的多语言全球多样性基准
authors:
- Martin Böckling
- Elizaveta Nosova
- Heiko Paulheim
- Andreea Iana
affiliations:
- University of Mannheim, Germany
arxiv_id: '2608.03882'
url: https://arxiv.org/abs/2608.03882
pdf_url: https://arxiv.org/pdf/2608.03882
published: '2026-08-04'
collected: '2026-08-06'
category: Eval
direction: LLM地理推理 · 多语言基准评测
tags:
- Geospatial Reasoning
- Multilingual Benchmark
- LLM Evaluation
- Knowledge Graph
- Tool Use
one_liner: 推出覆盖17种语言201个国家的4.6万条地理空间推理评测基准，定位LLM地理推理瓶颈
practical_value: '- 搭建本地化电商/物流相关Agent时，可参考该基准的分层采样方法构建测试集，避免低线/欠发达区域效果滑坡

  - 地理相关Agent能力优先实现拓扑关系/方向类推理，网格索引、形状计算类任务优先走工具调用而非LLM原生推理

  - 地理类场景LLM优化无需优先做知识注入，核心瓶颈在计算能力，优先配套地理计算工具+RAG链路性价比更高'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
LLM存储了大量地理知识，但在导航、物流所需的几何/拓扑空间计算任务上表现不佳，现有地理推理评测基准多为小体量合成数据、单语言、地理覆盖有限，无法准确定位能力瓶颈。

### 方法关键点
推出MultiGlobeQA多语言评测集，包含46060条问答对，覆盖14类空间函数、15种回答格式，基于3个知识图谱生成执行级真实标注；采用收入/人口密度分层采样覆盖201个国家和地区，支持英语及16种高低资源语言的并行问答。

### 关键结果
LLM原生在网格索引、形状计算任务上效果崩塌，拓扑关系、方向类任务表现最优；RAG+工具调用可大幅提升效果，但即使提供黄金事实性能仍不足2/3，核心瓶颈为计算能力而非知识获取；LLM在低收入地区表现显著更差，补充黄金事实反而会拉大性能差距。
