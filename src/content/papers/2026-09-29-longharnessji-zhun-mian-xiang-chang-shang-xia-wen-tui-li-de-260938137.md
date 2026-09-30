---
title: 'LongHarness Bench: Stress-Testing Language Model Harnesses for Long-Context
  Reasoning'
title_zh: LongHarness基准：面向长上下文推理的LM Harness压力测试
authors:
- Quang Hieu Pham
- Thuy Duong Nguyen
- Jocelyn Qiaochu Chen
- Xi Ye
affiliations:
- University of Alberta
- Alberta Machine Intelligence Institute (Amii)
arxiv_id: '2609.38137'
url: https://arxiv.org/abs/2609.38137
pdf_url: https://arxiv.org/pdf/2609.38137
published: '2026-09-29'
collected: '2026-09-30'
category: Eval
direction: 长上下文推理 · LM Harness评测
tags:
- Long-Context-Reasoning
- LM-Harness
- Benchmark
- Efficiency-Evaluation
- Agent-Eval
one_liner: 提出首个同时评测长上下文LM Harness准确性与效率的基准，覆盖4类自适应检索推理任务
practical_value: '- 长上下文业务Agent（用户长会话理解、商品手册解析等）选型时，不能仅看准确率，相同效果下不同Harness成本差可达12倍，优先测试mini-swe-agent这类文件-
  shell类Harness的性价比

  - 多条件用户/商品筛选类任务可复用策略优化思路：先执行覆盖范围最小的过滤条件缩小候选集，再校验剩余条件，能大幅降低检索推理成本

  - RAG/长上下文召回效果验证可复用难例构造方法：加入语义高度相似的干扰样本，测试系统的语义判别与证据链整合能力，避免上线后误匹配

  - 中小尺寸LLM落地时优先搭配适配Harness，实测显示弱基座通过Harness增益可缩小与强基座的效果差距，如GLM-5.3搭配mini-swe-agent后准确率从9.5%升至42.5%'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有长上下文评测仅关注准确率，任务多依赖简单检索或独立片段处理，强模型+Harness组合的准确率已饱和，且无法区分不同Harness的计算成本差异，相同基座不同Harness的资源消耗差可达一个数量级，亟需同时覆盖效果与效率的评测基准。

### 方法关键点
- 设计4类高难度长上下文任务，均要求自适应检索+多步推理，存在多种不同成本的解题策略：约束求解搜索、等价程序对搜索、程序执行追踪、异常备忘录检测，单实例上下文达100K~120K token，包含大量语义相似干扰样本
- 评测同时统计准确率、token消耗、单实例美元成本三个维度，设置3M token总预算，覆盖直接推理与4类SOTA Harness（RLM、OpenCode、mini-swe-agent、ReAct）、5款主流基座

### 关键结果
- 最佳组合（GPT-5.6-sol + mini-swe-agent）仅达68%宏观平均准确率，远低于现有基准的饱和水平，验证了任务难度
- 相同基座下准确率接近的方案成本差可达12.4倍：RLM与mini-swe-agent在异常备忘录检测任务上准确率接近，前者单实例成本7.23美元，后者仅0.583美元
- 弱基座搭配合适Harness可大幅缩小与强基座的差距：GLM-5.3搭配mini-swe-agent后准确率从9.5%升至42.5%，超过GPT-5.6-sol搭配OpenCode的40.5%准确率

**最值得记住的话**：长上下文系统必须作为模型与Harness的组合方案评估，额外推理计算量不必然带来效果提升，效率是与准确率同等重要的核心指标
