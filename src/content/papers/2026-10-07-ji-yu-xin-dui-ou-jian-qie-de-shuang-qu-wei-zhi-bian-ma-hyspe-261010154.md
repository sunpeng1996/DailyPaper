---
title: 'HySPE: Positional Encoding via Symplectic Dual Shears'
title_zh: 基于辛对偶剪切的双曲位置编码HySPE：支持超长上下文零样本外推
authors:
- Zhongping Ji
arxiv_id: '2610.10154'
url: https://arxiv.org/abs/2610.10154
pdf_url: https://arxiv.org/pdf/2610.10154
published: '2026-10-07'
collected: '2026-10-08'
category: LLM
direction: LLM位置编码 · 长上下文外推
tags:
- Positional Encoding
- RoPE
- Long Context
- Transformer
- Symplectic Geometry
one_liner: 提出基于辛对偶剪切的双曲位置编码HySPE，实现16倍上下文零样本外推，推理延迟与RoPE相当
practical_value: '- 做用户长行为序列建模的推荐系统、长对话Agent大模型，可直接替换现有RoPE编码，无需调整其他架构即可获得16倍以上的长度外推能力，避免长序列截断导致的信息损失

  - 可复用「算子对角化+分块坐标重锚定」的数值稳定优化方案，解决自定义注意力衰减、长序列特征变换中的指数溢出问题，无需降低数值精度

  - 自适应居中分块调度的工程思路可复用在KV cache优化、长序列推理加速场景，在保证计算正确性的前提下将内核开销压缩到和原生算子持平的水平'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RoPE作为当前主流的位置编码方案，基于辛群椭圆分支的旋转构造，超过预训练长度后会出现相位混叠、注意力熵崩溃问题，现有长上下文优化方案要么是各向同性衰减效果差，要么存在数值溢出、推理延迟高的缺陷，无法兼顾效果、稳定性、推理效率。
### 方法关键点
- 利用辛群Sp(2,R)的双曲分支构造对称对偶剪切算子，每个通道对配备两个独立的谱衰减率，实现各向异性的距离过滤，天生具备长序列衰减的归纳偏置
- 通过算子对角化到不变特征基、分块坐标重锚定的方案，彻底消除绝对位置因子导致的指数数值溢出问题，数值精度误差控制在1e-7级别
- 设计自适应居中分块调度策略，减少SDPA内核调用开销，推理效率与原生RoPE对齐
### 关键实验结果
- TinyShakespeare数据集：预训练长度256，16倍零样本外推到4096时，HySPE-UltraLong PPL稳定在4.81，而RoPE PPL劣化到131.2
- WikiText-103数据集：预训练长度512，16倍零样本外推到8192时，HySPE尾PPL较RoPE降低83.9%
- 推理效率：RTX 4090上4096长度前向延迟7.21ms，与缓存RoPE的7.20ms几乎一致

基于辛群双曲分支的位置编码可以在不增加推理开销、不引入额外可学习参数的前提下，实现远超过预训练长度的零样本外推，是长上下文序列建模的高性价比替代方案
