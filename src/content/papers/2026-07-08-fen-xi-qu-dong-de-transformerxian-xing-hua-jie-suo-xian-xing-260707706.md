---
title: 'The Key to Going Linear: Analysis-Driven Transformer Linearization'
title_zh: 分析驱动的Transformer线性化：解锁线性推理复杂度的核心方案
authors:
- Anna Kuzina
- Paul N. Whatmough
- Babak Ehteshami Bejnordi
affiliations:
- Qualcomm AI Research
arxiv_id: '2607.07706'
url: https://arxiv.org/abs/2607.07706
pdf_url: https://arxiv.org/pdf/2607.07706
published: '2026-07-08'
collected: '2026-07-09'
category: LLM
direction: LLM推理优化 · 线性注意力改造
tags:
- Linear_Attention
- Long_Context_Inference
- KV_Cache
- Transformer_Optimization
- Post-hoc_Linearization
one_liner: 冻结骨干前提下证明Delta型线性注意力更适配软注意力，辅以轻量结构调整大幅缩小性能差距
practical_value: '- 长上下文Agent/生成式推荐的LLM推理优化可优先选用Delta型线性注意力（如GDN）替换软注意力，效果优于GLA、核化线性注意力等方案

  - 固定KV cache预算时，可直接复用「8个sink token+剩余分配给滑动窗口」的策略，以极小成本提升电商长对话导购、长序列推荐等场景的效果

  - 线性化改造时优先给Q/K/V加短卷积而非LoRA，相同参数量下知识类、上下文类任务表现更稳定，适合推荐系统底层LLM轻量化

  - 算力受限场景可采用混合架构：仅保留10%-20%难线性化层的全注意力，其余替换为线性注意力，兼顾推理效率与任务精度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
因果自注意力的二次计算成本与KV cache膨胀是长上下文LLM推理的核心瓶颈，现有后处理线性化方案多混杂LoRA、蒸馏等多种干预因素，无法明确哪种线性状态更新机制能最大程度保留预训练模型性能。
### 方法关键点
1. 采用严格冻结骨干的实验范式：仅训练线性注意力新增参数，隔离不同线性机制的近似能力，排除其他因素干扰
2. 理论推导证明：软注意力天然依赖键相关的秩1正交投影，Delta型更新（GDN）天然实现该几何校正，纯门控累积（GLA）缺失该结构导致近似误差更大
3. 针对性引入轻量结构补全：固定64 token cache预算下拆分8个sink token+56个滑动窗口的混合路径，给Q/K/V加短卷积适配投影偏移
### 关键实验结果
在LLaMA3.1、Qwen3系列（0.6B~32B）上验证，仅用10M训练token、64 cache token的设置下，5-shot MMLU精度达59.17，比LoLCAT、Liger-GLA等基线高4~12个百分点；32k上下文下推理内存比FlashAttention2低40%以上无OOM；混合架构保留20%全注意力层时精度接近原生模型。
> 最值得记住的结论：Delta型线性注意力是预训练Transformer后处理线性化的最优基础组件，辅以极小结构调整即可兼顾长上下文推理效率与性能
