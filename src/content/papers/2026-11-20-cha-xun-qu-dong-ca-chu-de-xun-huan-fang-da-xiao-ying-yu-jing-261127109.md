---
title: Recurrent Amplification and Exact Nonexpansiveness Criteria for Query-Driven
  Erasure
title_zh: 查询驱动擦除的循环放大效应与精确非扩张判定准则
authors:
- Haozhe Wang
affiliations:
- School of Mathematics and Statistics, Ningxia University
arxiv_id: '2611.27109'
url: https://arxiv.org/abs/2611.27109
pdf_url: https://arxiv.org/pdf/2611.27109
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: 线性注意力 · 稳定性判定
tags:
- linear_attention
- QED
- spectral_norm
- recurrent_stability
- long_context
one_liner: 推导线性注意力查询驱动擦除的状态放大条件与线性时间单步非扩张判定准则
practical_value: '- 长上下文LLM推理场景（如电商长文本商品理解、Agent长会话记忆）可复用本文O(d)复杂度的单步非扩张判定准则，在线性注意力推理阶段实时校验状态稳定性，避免长序列误差累积爆炸

  - 若业务采用QED类线性注意力优化推理速度，需控制query正交分量的相邻序列一致性，高对齐度的连续query会触发状态放大，长序列搜索/推荐query理解场景需额外加方向归一化约束

  - 长上下文Agent的记忆模块若基于线性注意力实现，可参考本文周期放大结论，对重复输入（如用户多次检索同品类商品）做特殊截断处理，避免记忆状态扰动放大导致推荐结果漂移'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
线性注意力是长上下文大模型降本提速的核心技术，QED（查询驱动擦除）通过引入查询正交分量优化擦除机制，但此前仅验证单步谱特性稳定，未考虑序列级状态转移乘积的扰动累积效应，长序列下易出现隐式状态放大导致推理偏差，亟需明确稳定性边界与低成本校验方法。
### 方法关键点
- 构造固定key/query投影的周期token序列，证明单步谱半径<1的前提下仍可能出现周期乘积谱半径>1的放大效应
- 针对带通道衰减的秩一擦除操作，推导O(d)时间复杂度的精确单步谱范数非扩张判定准则，无需全量SVD计算
- 提出独立均匀token采样下的均方增长充分条件，量化随机输入场景的状态稳定性
### 关键结果
- 合成实验：32维输入下QED修正使周期乘积谱半径从0.17升至1.26，1536步相干序列的查询风险较初始值放大3913倍
- 准则验证：1800个随机算子的判定结果与SVD完全一致，最大误差仅1.22e-14
- 预训练回放：Qwen3.5-0.8B-Base上0.24修正强度下，4096 token重复文本的终端增益从0.99938升至1.3977
### 核心结论
线性注意力的单步稳定性无法保证长序列状态稳定，query正交分量的跨步方向耦合是长序列扰动放大的核心诱因
