---
title: 'Stage-Replay Divergence Follows the KV Cache: Fixed-Prefix Precision Controls
  and Bidirectional Cache Transplantation'
title_zh: 阶段重放偏差与KV Cache关联机制：固定前缀精度控制及双向缓存移植
authors:
- Alexander Boesgaard Lorup
affiliations:
- Openhagen
arxiv_id: '2607.28495'
url: https://arxiv.org/abs/2607.28495
pdf_url: https://arxiv.org/pdf/2607.28495
published: '2026-07-30'
collected: '2026-07-31'
category: LLM
direction: LLM推理优化 · KV Cache 一致性
tags:
- KV Cache
- LLM Inference
- Numerical Precision
- Stage Replay
- Deterministic Inference
one_liner: 验证KV Cache是阶段重放偏差的因果载体，FP32可消除BF16下的预填充与实时缓存轨迹分歧
practical_value: '- 做LLM驱动的电商导购Agent、多轮推荐/智能客服场景，若要求输出可复现，关键推理阶段优先用FP32计算KV Cache，可完全消除BF16下的轨迹漂移问题

  - 多阶段生成式推荐系统（如先做用户意图理解、再生成候选、最后做话术包装）做中间阶段调试或反事实评估时，不能仅复用中间文本做预填充重放，必须缓存对应阶段的完整KV
  Cache才能保证结果可信

  - 工程上拆分长推理链路做断点续推、多节点分布式推理时，直接移植完整KV Cache即可保证后续生成结果与原链路完全一致，无需重跑前置阶段，可大幅降低推理延迟'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
阶段重放是LLM推理诊断、反事实评估、多阶段Agent协作的核心基础技术，此前行业默认输入token完全相同时，一次性预填充生成的状态与实时增量推理的状态等价，但该假设未经过严格验证，会导致多阶段任务的中间干预、评估结果出现系统性偏差。

### 方法关键点
- 基于Qwen2.5-14B微调的多分支推理模型，选择多分支合并后的边界作为重放测试点，严格控制token、角色、注意力掩码、位置ID等所有外部变量完全一致，对比实时缓存、增量重建缓存、一次性预填充缓存的生成结果
- 设计固定前缀2×2交叉实验，在相同token前缀下对比BF16/FP32两种精度下的重放差异
- 设计双向KV Cache移植实验，仅交换缓存、保留其他所有状态，验证KV Cache对生成轨迹的因果性
- 测试集为GPQA Main的200条样本，所有实验采用结果盲选设计避免数据泄露

### 关键结果
BF16下实时缓存与一次性预填充缓存的生成轨迹分歧率达83%（166/200），答案分歧率24.5%，但两类方式的准确率差异仅1个百分点，无统计显著性；FP32下相同前缀完全无生成分歧，Wilson 95%置信上限为1.88%；双向KV Cache移植实验中，所有分歧样本的生成结果100%跟随缓存捐赠方（主checkpoint 24/24，盲测checkpoint 43/43）。

### 核心结论
仅靠输入token一致无法保证LLM重放结果与原实时推理等价，KV Cache是决定后续生成轨迹的充分因果载体
