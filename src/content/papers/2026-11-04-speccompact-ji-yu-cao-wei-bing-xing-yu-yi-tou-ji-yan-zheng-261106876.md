---
title: 'SpecCompact: Accelerating LLM Agent Context Compaction with Slot-Parallel
  Semantic Speculative Verification'
title_zh: SpecCompact：基于槽位并行语义投机验证的LLM Agent上下文压缩加速框架
authors:
- Yulu An
- Yifei Feng
- Xiangyang Yin
affiliations:
- New York University
arxiv_id: '2611.06876'
url: https://arxiv.org/abs/2611.06876
pdf_url: https://arxiv.org/pdf/2611.06876
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: Agent 上下文管理效率优化
tags:
- LLM Agent
- Context Compaction
- Speculative Decoding
- Semantic Verification
- Parallel Inference
one_liner: 采用小模型槽位并行生成+大模型语义校验框架，实现最高5.63倍的Agent上下文压缩加速
practical_value: '- 电商/客服/导购类Agent的上下文压缩可直接复用结构化槽位拆分思路，将用户需求、约束、历史交互等拆为独立槽位并行生成，在信息损失可接受的前提下大幅降低压缩延迟，提升交互流畅度

  - 语义投机验证范式可迁移至生成式推荐的商品摘要生成、Query改写场景，用小模型批量draft内容，大模型仅做语义校验+局部修复，平衡生成质量与推理成本

  - 工程优化点可直接复用：共享前缀KV cache减少长上下文重复prefill开销、draft buffering批量生成降低模型调用次数、行感知停止规则避免无效解码，适配所有长文生成类推理场景

  - 若业务可接受极小信息损失换延迟优化，该方案在ROUGE-L仅下降0.6个点的前提下可实现2倍以上压缩加速，性价比优于传统串行摘要方案'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM Agent长周期交互会累积大量历史上下文，直接推理延迟极高；传统上下文压缩依赖大模型串行生成摘要，延迟严重影响用户体验。现有token级投机解码不适配摘要场景的语义灵活性，单序列语义投机仍为串行生成，未解决速度瓶颈。
### 方法关键点
- 核心观察：结构化摘要的不同槽位（目标、约束、进展、决策、下一步、关键上下文）无强依赖，独立生成的信息保留率比串行整体生成更高
- 离线阶段：用目标大模型生成的槽位摘要做SFT，微调小尺寸draft模型，对齐大模型的槽位生成风格
- 在线推理：多槽位并行独立生成，每个槽位的draft行提交给大模型做语义校验，符合要求则接受，不符合则大模型生成局部修复内容，校验通过内容作为前缀继续生成
- 系统层优化：独立槽位调度重叠计算、共享前缀KV cache减少重复prefill成本、draft buffering批量生成降低调用开销、行感知停止规则避免无效解码
### 关键结果
- 实验数据集覆盖AppWorld、τ3 Agent基准，LongBench长文本摘要基准，对比Hermes、OpenClaw两类主流Agent压缩方案
- 相对Hermes基线，Gemma4-31B作为目标模型时实现2.49~5.63×压缩加速，Qwen3.5-122B作为目标模型时实现1.36~2.41×加速
- 信息损失极小：Qwen3.5上ROUGE-L仅比大模型直接生成低0.6个点，部分场景指标更高；Hermes实际部署用户研究中实现8.68×中位数加速，39.3%用户偏好其输出

结构化摘要的槽位独立性是优化上下文压缩效率的核心抓手，语义级投机验证比token级投机更适合措辞灵活、仅要求信息准确的生成场景
