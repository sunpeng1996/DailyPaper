---
title: 'SMELT: Scaling Laws for Compute-Matched MoE Looped Transformers'
title_zh: SMELT：计算匹配的MoE循环Transformer缩放定律
authors:
- Shaowen Wang
- Ge Zhang
- Kairong Luo
- Yuhao Wu
- Shaofan Liu
- Jiaheng Liu
- Wenhao Huang
- Shen Yan
- Jian Li
affiliations:
- Tsinghua University
- ByteDance Seed
- M-A-P
- TokenWave.AI
arxiv_id: '2609.01343'
url: https://arxiv.org/abs/2609.01343
pdf_url: https://arxiv.org/pdf/2609.01343
published: '2026-08-31'
collected: '2026-09-02'
category: Training
direction: 大模型训练 · MoE循环架构优化
tags:
- MoE
- Looped Transformer
- Scaling Law
- FLOPs Efficiency
- KV cache
one_liner: 提出计算匹配的MoE循环Transformer配方SMELT，同等约束下节省6.8%-18%训练FLOPs
practical_value: '- 自研垂类MoE大模型（如电商商品理解、文案生成大模型）可直接复用SMELT配方：循环中间50%层2次，通过调隐层宽、专家数、GQA头参数对齐FLOPs/参数/KV缓存，无额外成本下提升模型效果

  - 面向长上下文Agent、客服话术生成、代码辅助这类强结构长序列场景，优先选择循环MoE架构，其对长样本、ICL的增益比单纯扩参数/加专家更显著

  - 训练大模型前可参考其缩放定律参数分配逻辑，无需大范围扫参即可近似达到计算最优配置，降低预训练试错成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
过往Looped Transformer研究要么固定参数量放开计算，要么固定计算削减参数量，未同时对齐单token FLOPs、总非嵌入参数量、KV缓存三个部署核心约束，无法判断循环架构的真实结构收益而非资源倾斜带来的增益。
### 方法关键点
- 提出SMELT架构配方：仅循环Transformer中间50%层2次，循环段残差更新缩放1/2避免数值溢出；通过缩小隐层维度抵消循环带来的额外FLOPs，提升专家数补回总参数，调整GQA头大小对齐KV缓存，三项指标与标准MoE基线偏差均<4%
- 覆盖100M~1.6B激活参数（最高54B非嵌入参数）、4个稀疏度级别的完整缩放梯队，分别为基线和SMELT拟合Chinchilla风格缩放定律
### 关键结果
在内部多域语料上预训练，对比标准无循环MoE基线：同等验证损失下节省6.8%~18.0%训练FLOPs；下游任务增益超过验证损失下降的预期，Code域增益最高达20.4%，长样本增益是短样本的1.52倍，ICL增益随示例数提升而扩大
### 核心结论
Looped Transformer的收益并非来自额外计算投入，而是其天然降低注意力沉底、向内容相关Token重分配权重的归纳偏置，尤其适合结构化长序列场景
