---
title: Does LLM Pre-Training Typically Occur at the Edge of Stability?
title_zh: LLM预训练是否通常处于稳定性边缘？
authors:
- Yuhang Cai
- Haodong Wen
- Haofeng Huang
- Deyi Liu
- Yiyuan Ma
- Kaifeng Lyu
affiliations:
- UC Berkeley
- Tsinghua University
- ByteDance Seed
arxiv_id: '2610.36778'
url: https://arxiv.org/abs/2610.36778
pdf_url: https://arxiv.org/pdf/2610.36778
published: '2026-10-27'
collected: '2026-10-28'
category: Training
direction: LLM预训练优化 · 稳定性分析
tags:
- LLM Pretraining
- Edge of Stability
- Hessian
- AdamW
- Optimization
one_liner: 发现LLM预训练存在EoC和EoS两种二次近似失效模式，给出随机训练场景通用EoS定义
practical_value: '- 微调电商垂域LLM/推荐侧LLM时，优先将batch size匹配至临界batch规模，确保训练进入EoS区获得最优收敛效果，避免过小batch带来的损失劣化

  - LR衰减幅度超过阈值后训练会脱离EoS进入稳定区，此时无需额外调整正则项，可直接按计划调低LR降低调参成本

  - 若训练中出现loss持续震荡不降，可检查当前LR是否超过临界阈值，若进入超EoS不稳定区及时调小LR，可降低最终验证损失0.2~0.3'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有稳定性边缘（EoS）分析仅针对全批量训练场景，仅考虑正曲率导致的二次近似失效，未覆盖LLM预训练主流的随机自适应优化范式，负曲率带来的二次近似失配问题也被长期忽略，无法解释实际训练中理论预测与真实动态的偏差。
### 方法关键点
- 提出凸性边缘（EoC）概念：训练过程中持续存在的负曲率会导致二次近似动态无论LR取何值都会发散，但真实训练动态仍保持稳定，用saddleness（负曲率最大绝对值/正曲率最大特征值）量化EoC程度
- 去除负曲率影响后，给出适配随机训练+自适应优化器的通用EoS定义：小幅提升LR会导致二次近似动态发散但真实动态无明显变化时，训练处于EoS
- 设计可扩展的EoC/EoS检测方法，仅通过Hessian向量乘积实现，无需显式构造Hessian，支持最大787M规模LLM的全训练过程检测
### 关键实验
在104M/344M/787M规模GPT模型（覆盖FineWeb等5个公开文本数据集）的3000+训练检查点上验证：EoC普遍存在（saddleness<0.1）；EoS仅在batch size高于对应阈值、LR未进入衰减后期时出现；当LR超过最优范围2~4倍时会进入超EoS不稳定区，最终验证损失上升0.2~0.3。
### 核心结论
LLM预训练默认处于EoC+EoS的双边缘状态，二次近似不能直接用于实际训练的稳定性判定。
