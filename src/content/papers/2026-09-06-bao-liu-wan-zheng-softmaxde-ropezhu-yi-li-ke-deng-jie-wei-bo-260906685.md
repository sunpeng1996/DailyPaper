---
title: RoPE attention is an exact forward-pass gradient step with softmax intact
title_zh: 保留完整softmax的RoPE注意力可等价为前向传播精确梯度步
authors:
- Julie Huang
- Maggie Chlon
- Leon Chlon
affiliations:
- Hassana Labs
- Oxford University
arxiv_id: '2609.06685'
url: https://arxiv.org/abs/2609.06685
pdf_url: https://arxiv.org/pdf/2609.06685
published: '2026-09-06'
collected: '2026-09-09'
category: LLM
direction: 大模型基础结构 · RoPE注意力机制解析
tags:
- RoPE
- Attention
- Softmax
- KV Cache
- Transformer
one_liner: 推导保留完整softmax的RoPE注意力前向梯度步等价表示，量化KV缓存复用校正误差
practical_value: '- 推理优化：KV缓存复用可直接套用论文给出的精确误差公式，定量设置误差阈值决定缓存刷新时机，在推荐/Agent大模型低延迟部署场景下平衡推理速度与精度

  - RoPE相关微调：做LLM4Rec的LoRA微调时，可基于RoPE前向梯度步的特性调整注意力层梯度裁剪阈值，减少梯度爆炸风险，提升微调稳定性

  - 轻量模型实现：对精度容忍度较高的电商个性化文案生成、搜索query补全等场景，可基于论文给出的线性化softmax误差量化结果，用线性近似替代原softmax降低推理开销'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
过往注意力等价梯度步的研究多基于线性注意力假设，丢失了softmax的非线性特性，也未覆盖工业界广泛使用的RoPE位置编码，既无法解释RoPE注意力的实际运行机制，也难以为KV缓存复用、轻量推理等工程问题提供定量指导。
### 方法关键点
- 引入指数积分的φ₁函数（指数一阶差商），在完整保留softmax、RoPE旋转结构、投影偏置的前提下，推导得到RoPE-softmax注意力的精确有效权重矩阵表示，证明其输出等价于查询条件二次目标的单位梯度步结果
- 建立RoPE位置旋转与有限差分的精确关联，解释RoPE位置编码的底层数学逻辑
- 推导KV缓存中复用锚查询有效矩阵的精确误差公式，证明不存在全局通用的仿射查询读出器
### 关键实验
基于Qwen2.5-0.5B第23层验证：①等价表示重构精度极高，float64下MSE低至9.6×10⁻³⁰，与原生FP32实现的MSE仅7.01×10⁻¹⁴，等价性严格成立；②复用锚查询矩阵的相对RMSE为2.6~2.8倍于锚点输出baseline，13/14的注意力头单头相对RMSE在0.728~0.933区间。
### 核心结论
RoPE-softmax注意力的前向传播本质是查询条件下的精确梯度更新，KV缓存复用的误差可被精确定量计算，无需完全依赖经验调优。
