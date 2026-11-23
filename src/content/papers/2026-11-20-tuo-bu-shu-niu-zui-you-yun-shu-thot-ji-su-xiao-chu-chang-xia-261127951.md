---
title: 'Topology Hub Optimal Transport: Eliminating Long Context Dilution at Flash
  Speed'
title_zh: 拓扑枢纽最优运输（THOT）：极速消除长上下文注意力稀释问题
authors:
- Dylan Forde
arxiv_id: '2611.27951'
url: https://arxiv.org/abs/2611.27951
pdf_url: https://arxiv.org/pdf/2611.27951
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: 长上下文大模型 · 线性注意力优化
tags:
- LongContext
- OptimalTransport
- Attention
- Sinkhorn
- TritonKernel
- CausalLM
one_liner: 提出线性时间THOT长上下文注意力，262K序列零样本召回最高达98.83%，性能远超FlashAttention
practical_value: '- 长上下文RAG/电商导购Agent场景可复用bounded-support容量门控思路，用sparsemax或阈值ReLU替换softmax分配注意力权重，避免百万token下无关信息稀释核心用户意图/商品特征，实测可将长序列召回精度从个位数提升至95%以上

  - 电商用户超长行为序列建模（如近1年浏览/购买记录）可复用THOT的hub-and-spoke拓扑结构，将O(L²)自注意力降为线性复杂度，同时保证长跨度历史行为的信息召回率

  - 工程侧可直接复用论文的split-factor Triton内核优化方案：BF16 Tensor Core计算+FP32电位混合精度，在L4卡上4K序列下前向+反向速度比FlashAttention快3.27倍，适配线上低延迟推理场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有长上下文模型依赖稀疏/结构化Attention规避O(L²)开销，但全局softmax会将概率分散到海量无关token上，序列越长关键信息检索精度越低；同时传统Hub OT注意力存在有限步Sinkhorn残差高、反向显存开销大、全序列运算违反因果性四大落地障碍。
### 方法关键点
- 采用sparsemax（O(L log L)）或免排序token级阈值ReLU（O(L)）做容量门控，将无关distractor的分配容量直接置零，从根源解决注意力稀释问题
- 提出1+2退火行闭合Sinkhorn调度：1次无梯度非周期预热+2次可导二分迭代+最终行归一化，仅3次迭代即可消除行边际误差，精度比非退火方案高1~1.44pp
- 设计单参考块精确伴随算子，搭配分块Triton内核实现，反向仅需2次D维稀疏遍历，编译器临时变量缩小4倍，运算速度提升2.2倍
- 推出严格因果的分块THOT变体，块内仅使用前缀log-sum-exp运算，完全无未来信息泄漏，适配自回归生成场景
### 关键实验
在合成绑定检索、WikiText-103多针检索、WikiText-4K语言建模任务上测试，对比FlashAttention、Latent Softmax、softmax门控Hub OT等基线：262K序列下零样本绑定检索精度，sparsemax THOT达97.4%（无门控监督）、98.83%（轻监督），softmax门控版本仅3.52%；65K WikiText多针检索精度100%，FlashAttention仅0.78%；4K序列下前向+反向速度1.34ms，比cuDNN FlashAttention快3.27倍。
### 核心结论
解决长上下文注意力稀释的核心是从归一化根源入手，用精确零稀疏的容量门控替代全局softmax，而非仅依赖结构调整。
