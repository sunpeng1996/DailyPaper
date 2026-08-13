---
title: 'Power law graph attention: exact generalization of scaled dot-product attention,
  empirical collapse at inference'
title_zh: 幂律图注意力：缩放点积注意力的精确泛化与推理坍缩研究
authors:
- Burc Gokden
affiliations:
- Fromthesky Research Labs LLC
arxiv_id: '2608.10288'
url: https://arxiv.org/abs/2608.10288
pdf_url: https://arxiv.org/pdf/2608.10288
published: '2026-08-09'
collected: '2026-08-12'
category: LLM
direction: LLM注意力机制优化 · 推理加速
tags:
- Scaled Dot-Product Attention
- Power Law Graph Attention
- Inference Optimization
- KV Cache
- Regularization
one_liner: 提出精确包含SDPA的幂律图注意力机制，发现其推理时算子近似输入无关可直接缓存
practical_value: '- 推理加速trick：业务侧部署自定义注意力类的LLM/推荐模型时，可先验证中间交互算子的输入波动幅度，若波动低于1e-5量级可直接预缓存固定算子，替换推理时动态计算路径，无精度损失下降低推理时延

  - 排序模型优化：可将PLGA的可学习幂律双线性交互思路引入电商召回/排序的注意力模块，既保留原生SDPA的成熟优化能力，又能提升个性化匹配的表达能力

  - 训练正则复用：NOTEARS DAG正则可直接复用到图注意力类的推荐模型训练中，约束用户-物品交互的有向无环结构，降低长尾场景的过拟合风险'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Transformer核心依赖的缩放点积注意力（SDPA）采用固定双线性交互形式，表达能力上限明确；而动态可学习注意力机制普遍存在推理计算开销大、难以部署的痛点，亟需兼顾表达扩展性与推理效率的新型注意力架构。

### 方法关键点
- 提出Power Law Graph Attention（PLGA），将SDPA的固定单位双线性算子替换为输入驱动的可学习双线性算子，通过元素级幂律变换从严格正的交互张量生成匹配算子，在算子为单位矩阵时可精确等价于SDPA
- 配套PLDR-LLM纯解码器架构，引入RoPE位置编码与NOTEARS形式的DAG正则约束交互张量结构，保证位置依赖的有效性
- 针对推理阶段观察到的算子输入不变性，新增G-cache缓存机制，直接用预计算的固定算子替换动态计算路径

### 关键结果
1. 预训练收敛后，PLGA的演绎输出（双线性算子）随输入的相对波动仅为1e-6~1e-11，浮点精度下可视为常数
2. 采用缓存算子推理与原动态推理效果完全一致，TruthfulQA概率分布指标差异仅为5e-5每样本，块级评分与序列评分选中的答案100%一致

### 最值得记住的一句话
对于自定义注意力模块，优先验证推理时中间算子是否存在输入无关坍缩现象，无损缓存加速的收益远高于训练阶段的妥协性优化
