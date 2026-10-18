---
title: 'PAIR: Bridging Perception and Action in Vision-Language-Action Models'
title_zh: PAIR：视觉-语言-动作模型的感知与动作桥接框架
authors:
- Kaixi Feng
- Guoheng Sun
- Ang Li
affiliations:
- University of Maryland, College Park
arxiv_id: '2610.09016'
url: https://arxiv.org/abs/2610.09016
pdf_url: https://arxiv.org/pdf/2610.09016
published: '2026-10-05'
collected: '2026-10-18'
category: Agent
direction: VLA Agent 感知动作表示对齐
tags:
- VLA
- Representation Alignment
- Robot Agent
- Action Generation
- Autoencoder
one_liner: 提出PAIR共享感知-动作表示框架，显著提升连续动作VLA模型的任务执行表现
practical_value: '- 搭建多模态导购Agent、线下实体机器人导购系统时，可复用桥接模块思路，对齐用户多模态Query表示与动作生成隐空间，避免仅靠端到端损失导致的中间信息丢失，提升决策准确率

  - 训练涉及序列决策的业务模型（如电商投放动作序列生成、推荐全链路决策链优化）时，可先用掩码自编码器编码领域专家的历史决策序列生成隐令牌，与输入特征对齐后注入初始生成阶段，降低优化难度

  - 推理阶段可完全移除训练用的自编码器模块，仅保留轻量化桥接模块，不会增加线上推理延迟，适合低延迟业务场景落地'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有连续动作VLA模型的感知表示到动作表示的过渡为隐式，仅靠最终动作预测损失监督，易丢失任务关联的动作结构信息，效果上限低。
### 方法关键点
1. 训练阶段引入Masked Action Autoencoder编码专家动作块，得到时间对齐的Action Latent Tokens；
2. Bridge Module提取视觉-语言表示的任务相关特征，与Action Latent Tokens对齐生成同时保留任务信息、专家动作结构的Bridge Tokens；
3. 将Bridge Tokens投影后注入初始Action Tokens，为后续动作优化提供高质量起点，推理阶段移除自编码器，无额外推理开销。
### 关键结果
LIBERO-Plus数据集上VLA-Adapter成功率从59.1%提升至64.2%；CALVIN数据集上VLA-Adapter平均完成序列长度从4.42升至4.53；7项真实世界任务中OpenVLA-OFT成功率从51.4%提升至65.0%
