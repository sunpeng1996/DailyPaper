---
title: 'GraphNIAH: A Benchmark for Long-Context Reasoning over Real-World Graphs'
title_zh: GraphNIAH：面向真实世界图结构的长上下文推理基准
authors:
- Minh-Nam Tran
- Abulhair Saparov
affiliations:
- Purdue University
arxiv_id: '2610.41704'
url: https://arxiv.org/abs/2610.41704
pdf_url: https://arxiv.org/pdf/2610.41704
published: '2026-10-30'
collected: '2026-11-02'
category: Eval
direction: 长上下文LLM评测 · NIAH基准构建
tags:
- Long-Context LLM
- NIAH Benchmark
- Graph Reasoning
- Multi-hop Reasoning
- Evaluation
one_liner: 提出基于真实学术引用关系的动态NIAH基准，支持非线形多跳长上下文推理且无标注污染
practical_value: '- 定制业务私有NIAH评测集时，可复用GraphNIAH动态生成、基于cutoff后真实数据、无人工标注的设计思路，用电商场景的商品关联图、用户行为路径等数据构建专属评测集，彻底避免基准污染问题

  - 开发商品关联检索、用户行为路径归因、长会话推荐Agent时，要注意当前LLM在多跳路径深度≥16时会倾向于提前终止返回负结果的缺陷，可通过prompt强制要求全路径遍历，或外挂独立图检索模块补全路径搜索能力

  - 优化长上下文RAG系统时，可参考GraphNIAH的复杂度控制变量（问题深度、关联规模、干扰类型），量化RAG在不同干扰下的多跳信息聚合准确率，针对性优化召回、重排策略'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有NIAH（大海捞针）长上下文评测基准存在四大共性缺陷：依赖合成数据导致泛化性不足、复用公开数据集易出现基准污染、依赖人工标注难以动态扩展、仅支持线性单路径多跳推理，无法匹配真实场景中需在多路径图结构中搜索推理的需求，难以准确衡量LLM在学术检索、商品关联推理、用户行为路径分析等真实任务中的表现。

### 方法关键点
- 数据源采用Semantic Scholar中晚于被评测LLM知识cutoff日期的论文引用关系，从根源避免基准污染，全流程自动生成无需人工标注，可随新数据发布动态更新
- 从真实引用图中采样符合无标度分布的子图，转换为长上下文QA样本，支持三类任务：YES/NO可达性判断、多选可达性判断、可达节点计数，覆盖非线形多跳图推理核心场景
- 可通过控制问题深度（路径节点数）、子图规模、上下文长度、干扰内容类型等变量，精细化量化LLM长上下文推理能力边界

### 关键结果
评测8款前沿LLM（GPT-5.6系列、Gemini3系列、Qwen3.5系列）：
1. 问题深度达16/32时，GPT-5.6、Qwen3.5系列的YES/NO判断准确率降至随机猜测水平，普遍倾向于直接返回NO
2. 可达性计数任务难度最高，4款模型无法答对任意计数题，其余模型准确率随子图规模从100升至250时最高下降54pct
3. 干扰内容类型、推理努力程度对准确率无显著稳定提升，仅GPT-5.6-LUNA高推理模式下准确率提升10pct，但推理成本升高30%、耗时增加4.7倍

### 核心结论
当前LLM在处理长上下文非线形多跳推理任务时，往往会在遍历到答案前就提前停止搜索，即使所有必要信息都已存在于上下文中
