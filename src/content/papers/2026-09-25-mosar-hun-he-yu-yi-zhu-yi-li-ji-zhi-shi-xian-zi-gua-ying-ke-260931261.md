---
title: 'MoSAR: Mixture of Semantic Attention Regimes for Learning Adaptive and Approximable
  Attention Geometries'
title_zh: MoSAR：混合语义注意力机制实现自适应可近似的注意力几何
authors:
- Michele Paolicelli
- Alessandro Petruzzelli
- Alessandro Franceso Maria Martina
- Cataldo Musto
- Giovanni Semeraro
affiliations:
- Università degli Studi di Bari Aldo Moro
arxiv_id: '2609.31261'
url: https://arxiv.org/abs/2609.31261
pdf_url: https://arxiv.org/pdf/2609.31261
published: '2026-09-25'
collected: '2026-09-28'
category: LLM
direction: LLM高效长上下文 · 自适应注意力几何
tags:
- Self-Attention
- Long-Context LLM
- Adaptive Routing
- RoPE
- Efficient Inference
one_liner: 提出内容感知路由的混合注意力机制，兼顾长上下文建模效果与推理效率
practical_value: '- 可将混合语义衰减范式迁移到长用户行为序列的推荐注意力建模中，无需预设固定滑动窗口，让模型自适应选择有效历史长度，减少计算量同时保留长序列收益

  - 推理阶段top-1路由离散化trick可直接复用：训练时用软路由保证效果，推理时转硬路由剪枝注意力矩阵，适配电商搜推大模型的低延迟部署要求

  - 注意力成本正则项可用于搜推大模型蒸馏/压缩，通过显式加权惩罚长距离注意力，在效果损失可控的前提下降低在线推理的KV cache占用与计算开销'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有高效注意力方案多预设固定稀疏模式（如滑动窗口），无法适配不同token、上下文的语义依赖差异；RoPE等位置编码无显式单调距离衰减，长上下文推理的二次复杂度仍是LLM落地的核心瓶颈，尤其无法满足电商/Agent场景下长用户行为、长对话的建模需求。

### 方法关键点
- 预定义短/中/全局3种语义注意力regimes，每种包含无衰减平台区、平滑衰减过渡区、固定低分值底区，避免硬截断的语义断层问题
- RoPE后新增轻量MLP路由层，分别对query和key做内容感知路由，输出不同regime的加权系数，query与key的regime组合得到最终距离衰减曲线
- 支持成本感知训练变体MoSAR-Cost，加入注意力reach正则项，显式引导模型选择更短注意力范围，平衡效果与效率
- 推理可做top-1硬路由离散化，直接根据路由结果构造注意力支持域，无需提前计算QK相似度即可剪枝低价值长距离交互

### 关键实验
基于5亿参数Gemma2架构从头预训练，训练上下文长度2048，对比RoPE、ALiBi、固定窗口等8个基线：训练长度2048下MoSAR PPL比RoPE低2%，预期计算成本仅为全注意力的22.1%；长度外推到8192时PPL比RoPE低19.6%，优于所有基线；推理top-1硬路由仅带来3.5%~5.4%的PPL损失，8192长度下注意力支持域密度仅为全注意力的10.4%，计算量呈亚二次增长。

### 核心结论
注意力稀疏性不需要提前人为预设，可通过内容感知路由学习自适应的距离衰减几何，在效果损失极小的前提下大幅降低长上下文计算开销。
