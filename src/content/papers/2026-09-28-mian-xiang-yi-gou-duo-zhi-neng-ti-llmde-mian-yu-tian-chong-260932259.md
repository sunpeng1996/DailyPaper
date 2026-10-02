---
title: Prefill-Free Cross-Family KV Cache Transfer for Heterogeneous Multi-Agent LLMs
title_zh: 面向异构多智能体LLM的免预填充跨模型族KV缓存迁移
authors:
- Vincent-Daniel Yun
- Woosang Lim
- Haneul Yoo
- Sungjoo Yoo
- Murali Annavaram
- Sai Praneeth Karimireddy
affiliations:
- University of Southern California
- Seoul National University
- New York University
arxiv_id: '2609.32259'
url: https://arxiv.org/abs/2609.32259
pdf_url: https://arxiv.org/pdf/2609.32259
published: '2026-09-28'
collected: '2026-10-02'
category: MultiAgent
direction: 多智能体通信 · KV缓存复用优化
tags:
- KV Cache
- Multi-Agent
- LLM Inference
- Heterogeneous LLM
- Cache Transfer
one_liner: 提出HeteroFold实现异构多智能体跨模型族免预填充KV缓存迁移，32K上下文速度较原生预填充提10.7倍
practical_value: '- 多Agent混合部署场景可复用Token Alignment思路，通过字符边界对齐不同模型族Tokenizer输出，解决跨模型语义传递的token不匹配问题，适配电商场景大中小模型分工的通信需求

  - 长上下文处理可复用Recolor统计对齐+输出感知校准的设计，在冻结业务模型的前提下实现上下文缓存跨模型复用，大幅降低商品详情、用户长行为序列的重复预填充开销

  - 跨模型KV映射可采用多层邻接层拼接+低秩校正后折叠为仿射映射的方案，推理无额外模块开销，适配搜索推荐线上高吞吐低延迟的部署要求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
异构多智能体系统常混合部署不同家族、不同参数量的LLM来平衡能力与成本，但文本通信模式下接收方需要重复预填充发送方已处理过的共享上下文，产生大量冗余计算，上下文越长预填充延迟越高；现有KV缓存复用方案仅支持同模型族，无法适配跨模型族的Tokenizer、层数、KV表征差异。
### 方法关键点
- Token Alignment（TA）：通过共享字符边界对齐不同Tokenizer的输出，解决跨模型token对应关系不匹配问题
- 层对齐：按相对深度匹配发送方与接收方的层，拼接发送方匹配层前后各4层的KV特征，适配模型深度差异
- Recolor映射：通过Procrustes对齐将发送方KV特征的均值、协方差映射为接收方的统计分布，保留接收方KV原生分布特性
- 输出感知校准：分别优化Key校正（匹配原生注意力分布）和Value校正（匹配原生输出），校正后的低秩参数折叠为固定仿射映射，推理无额外开销，收发模型全程冻结
### 关键实验
在Llama-3.1、Qwen3、Ministral-3三个模型族的6个跨模型迁移方向上测试，对比Dense Latent、KV Ridge等SOTA基线；32K上下文下Llama-3.1-8B→Ministral-3-14B迁移速度较原生预填充提升10.7倍，较SOTA基线快1.18-1.47倍；所有长上下文benchmark性能最优，多智能体HIDDENBENCH任务准确率超过文本通信模式。
### 核心结论
跨模型KV缓存迁移不能仅优化KV重构误差，更要对齐接收方的注意力模式与输出分布，才能在免预填充的同时保证任务效果。
