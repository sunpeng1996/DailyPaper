---
title: 'SpectralShift: Effective Context Window Extension of Gated DeltaNet via Spectral
  Reparameterization'
title_zh: SpectralShift：基于谱重参数化的Gated DeltaNet上下文窗口扩展方法
authors:
- Zian Liu
- Yiwen Hu
- Zican Dong
- Tian Xie
- Wayne Xin Zhao
- Yucheng Ding
- Ran Tao
- Bryan Dai
affiliations:
- Renmin University of China
- IQuest Research
- Microsoft Research Asia
arxiv_id: '2609.14320'
url: https://arxiv.org/abs/2609.14320
pdf_url: https://arxiv.org/pdf/2609.14320
published: '2026-09-13'
collected: '2026-09-15'
category: LLM
direction: LLM长上下文优化 · 线性注意力扩展
tags:
- Linear Attention
- Gated DeltaNet
- Context Window Extension
- Spectral Reparameterization
- Continual Pretraining
one_liner: 通过谱重参数化调整GDN的alpha投影初始化与学习率，高效扩展线性注意力模型上下文窗口
practical_value: '- 构建处理全量用户行为序列、长会话历史的推荐/客服Agent时，若采用GDN类线性注意力架构，可直接复用SpectralShift的alpha投影重参数化+学习率缩放方案，无需修改模型结构即可快速扩展上下文窗口，训练成本几乎无增加

  - 做长序列用户建模（如用户近1年的点击/交互序列）的线性注意力召回/排序模型，可借鉴其谱动力学分析思路，通过调整状态衰减的慢谱带宽平衡长程信息保留与短程上下文切换能力，避免长序列下历史信息过度遗忘

  - 跨长度迁移的模型训练场景，可复用其平方根长度缩放因子(L_ref/L_tar)^0.5的设计，用于参数初始化缩放和对应模块的学习率调整，提升跨长度训练的稳定性与下游效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有线性注意力（如GDN）的上下文扩展方法通常直接进行增量预训练，忽略了线性注意力状态转移的谱特性，导致长上下文下信息保留能力不足，且容易损失短上下文通用能力，无法满足长文档理解、长会话Agent、长序列用户建模等场景需求。

### 方法关键点
- 从转移矩阵谱角度明确GDN长程信息检索的两个核心条件：足够宽的慢谱带匹配目标依赖长度，同时保留快衰减模式用于状态清理和上下文切换
- 对alpha投影做重参数化：将alpha投影围绕全局均值的偏差按(L_ref/L_tar)^0.5缩放，重塑衰减谱，提升慢传播能力
- 训练阶段对alpha投影的学习率也按相同因子缩放，避免训练过程破坏调整好的谱结构

### 关键实验
基于1.5B/20B规模的GDN-MoE模型，从8K上下文分别扩展到32K/64K/128K，对比朴素增量预训练基线：
- 128K上下文下RULER平均分达55.18，相对基线提升5.35%，通用能力与基线基本持平
- 兼容DroPE/YaRN/ABF等所有主流位置编码方案，在纯GDN模型上也能稳定生效，32K扩展下RULER得分相对基线提升约65%

### 最值得记住的结论
线性注意力的长上下文能力不由单一最大记忆时长决定，而是由与目标依赖长度匹配的慢谱带宽度决定，扩展上下文窗口时需同时兼顾慢谱信息保留与快谱上下文切换能力。
