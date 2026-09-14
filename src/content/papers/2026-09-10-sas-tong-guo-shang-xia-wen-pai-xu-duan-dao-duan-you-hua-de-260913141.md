---
title: 'SAS: Simple Attention Sparsification via End-to-End Optimization of Context
  Ranking'
title_zh: SAS：通过上下文排序端到端优化的简单注意力稀疏化方法
authors:
- Zhiwei Li
- Lei Zhu
- Hao Gu
- Xiang Hu
- Yan Wang
- Haitao Mi
- Sirui Han
- Leo Liang
- Zhijiang Guo
affiliations:
- Tencent HY LLM Frontier
- Hong Kong University of Science and Technology (Guangzhou)
- Hong Kong University of Science and Technology
arxiv_id: '2609.13141'
url: https://arxiv.org/abs/2609.13141
pdf_url: https://arxiv.org/pdf/2609.13141
published: '2026-09-10'
collected: '2026-09-14'
category: LLM
direction: LLM 稀疏注意力推理加速
tags:
- Sparse-Attention
- Long-Context-LLM
- Inference-Optimization
- KV-Cache
- Triton-Kernel
one_liner: 通过可微分对数门控实现无蒸馏端到端训练的稀疏注意力，低预算下性能提升显著
practical_value: '- 电商/广告长会话用户建模场景，可直接复用SAS的块级上下文选择逻辑，在低KV缓存预算下保留核心用户行为上下文，降低长序列推荐的LLM推理延迟

  - Agent多轮对话、工具调用场景，采用SAS端到端排序训练方法，无需人工设计上下文截断规则，比蒸馏式稀疏选择任务效果保留度更高

  - 工程侧可直接复用论文开源的融合门控计算的FlashAttention风格Triton kernel，无需重构现有LLM推理链路，快速落地长上下文稀疏加速能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有训练式注意力稀疏方法依赖层间稠密注意力蒸馏做监督，上下文排序目标与最终语言建模损失不对齐，有限注意力预算常浪费在无用单元，长上下文推理的二次复杂度瓶颈无法有效解决，低预算下性能掉点严重。

### 方法关键点
- 将选择器的连续得分作为对数空间门控注入注意力softmax内部，绕过Top-K选择的梯度阻断问题，实现选择器与语言建模损失的端到端反向传播
- 核心设计四件套：对数空间门控注入、softmax归一化门控校准上下文相对重要性、保留连续得分而非二值化掩码训练相对优先级、仅更新选中块降低训练成本
- 实现FlashAttention风格Triton内核，将门控计算融合到tile级qK运算中，避免全注意力矩阵实例化，支持长序列高效训练

### 关键结果
在推理、长上下文理解、Agent三类任务上对比SeerAttention-R、StreamingLLM等基线：1024 token预算下，MATH500领先基线6~7.7个点，GPQA-Diamond领先10.6~15.5个点；8K+长上下文LongBench领先基线3.2个点；Agent任务BFCL最多领先3.5个点，4096预算下基本追平全注意力效果，512K上下文下解码速度最高达全注意力的5.6倍。

最值得记住的结论：注意力稀疏优化的核心不是匹配原模型的层间注意力分布，而是直接端到端对齐最终任务损失，低预算下收益尤其显著。
