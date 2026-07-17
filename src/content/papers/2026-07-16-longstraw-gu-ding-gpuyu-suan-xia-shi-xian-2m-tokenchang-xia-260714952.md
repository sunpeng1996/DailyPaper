---
title: 'LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget'
title_zh: 《LongStraw：固定GPU预算下实现2M+token长上下文RL训练》
authors:
- Changhai Zhou
- Kieran Liu
- Yuhua Zhou
- Qian Qiao
- Jun Gao
- Harry Zhang
- Irvine Lu
- Nolan Ho
- Lucian Li
- Andrew Lei
affiliations:
- MindLab
- Fudan University
arxiv_id: '2607.14952'
url: https://arxiv.org/abs/2607.14952
pdf_url: https://arxiv.org/pdf/2607.14952
published: '2026-07-16'
collected: '2026-07-17'
category: Training
direction: 长上下文RL训练 · 固定GPU资源优化
tags:
- LongContext
- GRPO
- RLHF
- MemoryOptimization
- MoE
- LoRA
one_liner: 通过共享前缀无梯度预计算+响应串行重放设计，固定GPU预算下实现2M+token长上下文GRPO训练
practical_value: '- 做电商/搜索Agent长轨迹RL训练时，可复用「共享长前缀无梯度预计算+仅保留必要状态+短响应串行重放」的思路，大幅降低GPU内存占用，无需大规模集群即可开展百万token级长轨迹训练。

  - 对于混合架构（循环+全注意力）或MoE大模型的长上下文微调/RL训练，可参考其分层状态存储策略：循环层状态常驻GPU，稀疏注意力/MoE前缀状态落CPU、按层按需加载，平衡显存占用与传输开销。

  - 开展GRPO等多响应RL训练时，可复用其组大小优化逻辑：组大小从2提升到8仅增加0.21GB峰值显存，优先拉长响应串行处理维度而非扩容GPU集群，可显著降低硬件成本。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前大模型推理已能支持百万级token上下文，但RL后训练（尤其是GRPO这类需要基于同一前缀生成多响应打分回传的任务）大多还停留在256K token以下，依赖长度泛化能力落地，对于需要累积长轨迹的Agent场景瓶颈突出；传统长上下文训练需要堆砌大量GPU，小团队很难开展相关探索。

### 方法关键点
- 核心架构拆分长前缀与短响应计算：共享长前缀仅做一次无梯度前向，只保留后续响应必须的模型特定状态（如Qwen的GDN循环状态、KV分片，GLM的MLA latent页、DSA索引页），丢弃所有临时激活缓存。
- 响应分支串行重放：每次仅在autograd下处理一个短响应分支，梯度累加后统一执行一次optimizer step，将活计算图的内存占用从全序列降低到单响应长度。
- 多架构适配：分别支持混合循环+全注意力的Qwen3.6-27B、压缩注意力+MoE的GLM-5.2两种主流大模型架构，适配不同的状态存储与并行策略。

### 关键结果
- 8张H20 GPU上，Qwen3.6-27B可完成2.1M token上下文、组大小2/8的GRPO训练，组大小从2提升到8仅增加0.21GB峰值显存，压力测试最高支持4.46M token上下文。
- 32张H20 GPU上，验证了GLM-5.2全78层的2.1M token端到端执行路径。

最值得记住的一句话：固定预算下长上下文RL训练的实际上下文上限核心取决于张量生命周期与物理所有权管理，而非仅靠稀疏性优化。
