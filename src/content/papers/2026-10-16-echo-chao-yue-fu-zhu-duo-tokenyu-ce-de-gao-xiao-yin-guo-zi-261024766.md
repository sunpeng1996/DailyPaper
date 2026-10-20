---
title: 'ECHO: Efficient Causal Self-Recursion Beyond Auxiliary Multi-Token Prediction'
title_zh: ECHO：超越辅助多token预测的高效因果自递归框架
authors:
- Yuxuan Zhou
- Junyuan Shang
- Tianyu Wang
- Chunrui Zheng
- Zichang Liu
- Wenbin Chang
- Shuohuan Wang
- Dianhai Yu
affiliations:
- ERNIE Team, Baidu
- Independent Researcher
arxiv_id: '2610.24766'
url: https://arxiv.org/abs/2610.24766
pdf_url: https://arxiv.org/pdf/2610.24766
published: '2026-10-16'
collected: '2026-10-20'
category: Training
direction: LLM训练优化 · 多token预测与推理加速
tags:
- Multi-Token Prediction
- Speculative Decoding
- LLM Pretraining
- Inference Acceleration
- Dynamic Sampling
one_liner: 复用LLM主干最后层做多token预测，结合动态采样降本并提效果与推理速度
practical_value: '- 电商智能客服、商品文案生成等生成类业务，可直接复用ECHO设计替代额外训练的drafter，无需新增参数，在高熵开放回复场景下获得更高的推测解码接受率，降低推理延迟与成本

  - 垂类大模型预训练时，引入DDS动态深度采样策略，仅用一半多token预测训练开销即可获得全深度训练的下游效果，还能额外提升模型推理、代码类任务表现，适合电商垂类LLM定制训练

  - 生成式推荐、Semantic ID序列预测等场景，可借鉴主干层共享思路，避免新增多预测头带来的参数与计算开销，多horizon监督信号直接作用于主干，相比辅助MTP方案效果更优'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多token预测（MTP）均为辅助任务，需额外新增专用预测模块，多horizon监督信号无法直接作用于LLM主干，训练成本随预测深度线性上升；推理阶段后训练的drafter容易过拟合小样本数据，高熵开放生成场景下与主干对齐差、接受长度低，加速效果受限。
### 方法关键点
- **主干最后层共享**：递归复用LLM主干的最后解码层和输出头预测所有horizon的未来token，仅新增轻量融合层，多horizon监督信号直接作用于主干生成参数，无额外预测模块开销。
- **动态深度采样（DDS）**：训练时按衰减概率采样预测深度（如深度1/2/3采样概率0.6/0.3/0.1，期望深度仅1.5），降低平均训练开销，同时减少深层监督噪声对主干的负面影响。
### 关键结果
- 预训练阶段：ECHO-1.5(3)仅用MTP-3一半的训练开销，14个下游基准平均得分36.34，与全深度训练的ECHO-3（36.36）基本持平，推理、代码类任务相对MTP-1基准最高提升2.37分。
- 推理阶段：无需额外训练drafter，支持深度外推，接受长度随服务深度线性提升，高熵开放场景下接受长度比EAGLE3、DFlash等后训练drafter高1~2token，解码加速效果更显著。
- 微调后优势进一步扩大：SFT后相对MTP-1基准，推理代码类任务提升1.93分，QA类提升1.04分，效果在双倍token预算、重复训练下均稳定。
### 核心结论
将多token预测从辅助任务转化为自回归目标的一部分，可同时实现训练降本、下游效果提升、推理加速三重收益。
