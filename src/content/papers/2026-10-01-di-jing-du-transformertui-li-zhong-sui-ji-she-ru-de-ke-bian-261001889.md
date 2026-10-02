---
title: 'Stochastic Rounding in Low-Precision Transformer Inference: A Variable-Precision
  Emulation Study of a Small GPT-2'
title_zh: 低精度Transformer推理中随机舍入的可变精度仿真研究
authors:
- Yohan Chatelain
- Pablo de Oliveira Castro
affiliations:
- Krembil Centre for Neuroinformatics, CAMH
- Université Paris-Saclay, UVSQ, LI-PaRAD
arxiv_id: '2610.01889'
url: https://arxiv.org/abs/2610.01889
pdf_url: https://arxiv.org/pdf/2610.01889
published: '2026-10-01'
collected: '2026-10-02'
category: LLM
direction: LLM低精度推理 · 舍入策略优化
tags:
- Stochastic Rounding
- Low-Precision Inference
- Transformer
- GPT-2
- Quantization
one_liner: 提出可变精度随机舍入算法，验证Transformer分层差异化舍入策略可优化低精度推理精度
practical_value: '- 部署LLM驱动的推荐/Agent服务时，可采用分层舍入策略：MLP层用SR降低长累积误差，输出层用RN避免softmax损失上升，6位尾数精度下可将PPL损失从121%降至15%，兼顾延迟和精度

  - 自研量化推理框架时，可复用VPSR算法实现任意虚拟精度的随机舍入仿真，比传统MCA方案快70倍，无需等待硬件支持即可快速验证不同精度、舍入策略的业务效果

  - 长序列推荐/多轮Agent场景下，大维度MLP投影、长序列注意力累积等长线性运算优先用SR减少系统性误差，短维度输出层用RN控方差，可在降精度压成本的同时最小化业务指标损失'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前Transformer低精度推理默认使用就近舍入(RN)，但动态随机舍入(SR)的收益仅在训练梯度量化中被验证，推理阶段不同层对舍入策略的敏感度差异未被系统性研究。低精度下RN的长累积误差会导致精度骤降，而全网络用SR又会引入方差损失，缺乏可落地的分层舍入策略指导。

### 方法关键点
- 提出可变精度随机舍入(VPSR)算法，支持任意虚拟精度的舍入仿真，证明其决策过程可在硬件浮点中精确执行，无需扩展精度开销，集成到PRISM库后比传统MCA随机舍入仿真快最高70倍
- 理论推导两类误差边界：线性投影层SR的误差包络为$O(\sqrt{n}u)$，远优于RN的$O(nu)$，长MLP投影层差距更明显；输出softmax层的损失分解为漂移项、曲率项、方差惩罚项，验证非均匀噪声会被softmax放大，均匀噪声无损失
- 实验采用控制变量法，固定数值格式仅调整舍入规则，对DistilGPT-2分层配置舍入策略，排除其他量化优化的干扰

### 关键实验
数据集为WikiText-2，Baseline为全精度RN推理、同精度全网络RN。核心结果：t=6位尾数精度下，MLP层用SR仅带来15%PPL上升，同精度RN为121%；输出Head层用SR损失高于RN；混合策略（MLP用SR、Head用RN）仅带来10%PPL上升，比同精度全RN降低28%精度损失。

### 核心结论
Transformer低精度推理舍入策略无需全局统一，长累积运算用SR控漂移、输出层用RN控方差，可在不增加硬件成本的前提下大幅降低低精度推理的精度损失
