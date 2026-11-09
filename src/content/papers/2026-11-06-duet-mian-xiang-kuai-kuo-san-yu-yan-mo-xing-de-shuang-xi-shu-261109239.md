---
title: 'DUET: Dual-Sparse Inference for Block Diffusion Language Models'
title_zh: DUET：面向块扩散语言模型的双稀疏推理加速框架
authors:
- Siyuan Yan
- Shen Gu
- Xiaoxing Ma
- Chun Cao
- Jingwei Xu
affiliations:
- State Key Laboratory for Novel Software Technology, Nanjing University
arxiv_id: '2611.09239'
url: https://arxiv.org/abs/2611.09239
pdf_url: https://arxiv.org/pdf/2611.09239
published: '2026-11-06'
collected: '2026-11-09'
category: LLM
direction: 扩散大模型 · 推理效率优化
tags:
- Diffusion LLM
- Inference Optimization
- KV cache
- Sparse Attention
- Block Diffusion
one_liner: 无需训练的双稀疏推理框架，同时优化块扩散LLM的历史KV与查询计算，最高实现4.72×步级加速且效果无明显损失
practical_value: '- 做基于扩散LLM的生成式推荐（比如商品文案生成、Semantic ID生成、多轮推荐话术生成）场景时，可直接复用Duet的双稀疏策略，在32K长上下文下实现2倍以上端到端加速，无需微调模型不影响生成质量

  - KV缓存优化可迁移到普通LLM的长上下文推荐场景：块级复用高相关历史KV子集的思路，能大幅降低长用户行为序列下的推荐Prompt推理开销，实测256个相关KV就能覆盖85%以上注意力权重

  - 早期查询剪枝的trick可复用：在迭代生成类任务（比如多轮改写Query、分步生成推荐理由）中，可在Transformer浅层预测待更新位置，仅传递活跃查询到深层，减少无效计算'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
块扩散语言模型（BDLM）采用迭代去噪并行生成，比自回归模型更适合长文本、可控生成场景（比如电商长文案、多轮推荐话术），但推理开销极高：一是每轮去噪都要全量注意力过历史前缀，上下文越长开销越大；二是每轮都要把当前生成块所有位置走完整个Transformer，而每轮仅少量位置会更新，冗余度极高。现有稀疏优化要么仅剪枝查询要么仅剪枝KV，加速收益有限。

### 方法关键点
- 前缀KV稀疏：每个生成块首次去噪时，基于查询与历史KV的相似度选出固定大小的高相关历史子集，整个块的迭代去噪过程复用该子集的KV缓存，无需每次全量遍历历史，256大小的子集即可覆盖85%以上注意力权重
- 早期查询稀疏：指定Transformer浅层为选择层，每轮去噪时仅在浅层跑全量计算，用原解码规则预测本轮待更新的活跃查询位置，仅把活跃位置传递到深层计算，非活跃位置直接旁路，无需走注意力、FFN/MoE模块
- 全程无需训练/微调，完全兼容现有BDLM的解码逻辑，不会改变生成轨迹

### 关键实验结果
在LLaDA2.1-mini和SDAR-8B-Chat-b32两个主流BDLM上验证，对比FOCUS、LoSA等基线，32K上下文下：LLaDA2.1-mini获得1.34×端到端加速、2.83×步级加速，LongBench Macro-F1仅损失0.38%；SDAR-8B获得2.41×端到端加速、4.72×步级加速，长、短上下文任务效果均与稠密推理持平。

### 核心经验
块扩散模型迭代生成过程中历史注意力高度集中且跨步稳定，待更新位置可在Transformer浅层高精度预测，这两个观察可推广到绝大多数迭代式生成任务的效率优化。
