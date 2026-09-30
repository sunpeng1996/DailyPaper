---
title: Pretraining Latent Information Feedback Transformers with Teacher Supervision
title_zh: 带教师监督的隐式信息反馈Transformer预训练方法
authors:
- Dor Tirosh
- Ido Amos
- Mor Geva
affiliations:
- Tel Aviv University
- The Hebrew University of Jerusalem
arxiv_id: '2609.38149'
url: https://arxiv.org/abs/2609.38149
pdf_url: https://arxiv.org/pdf/2609.38149
published: '2026-09-29'
collected: '2026-09-30'
category: Training
direction: LLM预训练 · 隐状态反馈架构
tags:
- Transformer
- Pretraining
- Latent Feedback
- Teacher Forcing
- State Propagation
one_liner: 利用外部预训练LM的token分布作为监督，实现带隐状态反馈的Transformer并行预训练
practical_value: '- 优化多轮导购Agent/会话推荐的状态跟踪：可复用LIFT的隐状态反馈设计，无需显式输出Chain-of-Thought即可携带多轮交互的推理信息，提升复杂查询应答准确率

  - 小规格业务LLM提速提效：预训练小模型时仅增加约3%参数的SwiGLU融合层，用现成大模型的top-k token分布作为监督信号，可在同等训练成本下提升推理、多步计算类任务表现

  - 长序列用户行为建模优化：可借鉴状态反馈思路，将上一步的深层输出分布反馈到输入层，减少长序列行为的重复计算，提升召回/排序阶段的长序列处理效率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
原生Transformer为纯前向结构，深层特征无法反馈至浅层，仅靠输出token传递跨步骤信息的通道过窄，导致模型需重复计算中间结果、丢弃候选续例；现有反馈方法要么训练时需串行滚动计算成本极高，要么采用迭代近似存在质量-效率权衡，无法兼顾预训练并行性与反馈能力。

### 方法关键点
- 架构新增轻量SwiGLU融合层，将输入token与上一步状态（输出logits取top-k后经温度缩放softmax得到的token分布）融合为输入表示，新增参数仅占1B模型的3%，占比随模型规模增大而降低
- 训练采用教师强制策略，用冻结的外部预训练LM（教师）并行输出的token分布作为状态监督信号，训练目标同时包含next token预测损失和与教师状态的KL对齐损失，完全保留预训练的序列并行性
- 训练最后10%阶段切换为模型自生成状态监督，缓解训练-推理分布偏移；同时加入前缀状态dropout，支持推理时Prompt并行预填充

### 关键结果
- 合成S5状态跟踪任务上，2层LIFT仅用1/8训练步数即可实现长度12序列100%准确率，同等规模 vanilla Transformer即使训练8倍步数，在长度≥12时准确率接近随机
- 135M~1B参数规模预训练中，同等token预算下LIFT相比基线Perplexity降低5~5.5%，在33/36个下游任务上胜出，算术、模式延续等过程性任务优势最大，性能超过训练2倍token的同规模Transformer
- 与基于Jacobi迭代的反馈Transformer相比，同等token/计算预算下LIFT效果更优，训练峰值内存更低

### 核心结论
利用外部预训练LM的输出分布作为隐状态监督信号，可在完全保留预训练并行性的前提下，赋予Transformer跨步骤隐状态反馈能力，显著提升token效率和推理能力
