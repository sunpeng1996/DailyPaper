---
title: 'DeepLoop: Depth Scaling for Looped Transformers'
title_zh: DeepLoop：面向循环Transformer的深度缩放优化方法
authors:
- Shuzhen Li
- Yifan Zhang
- Jiacheng Guo
- Quanquan Gu
- Mengdi Wang
affiliations:
- Princeton University
- University of California, Los Angeles
arxiv_id: '2607.13491'
url: https://arxiv.org/abs/2607.13491
pdf_url: https://arxiv.org/pdf/2607.13491
published: '2026-07-14'
collected: '2026-07-17'
category: Training
direction: 循环Transformer · 训练稳定性优化
tags:
- Looped-Transformer
- Residual-Scaling
- DeepNorm
- Training-Stability
- Parameter-Sharing
one_liner: 提出循环感知的残差缩放规则，稳定提升多轮共享Transformer的训练效果
practical_value: '- 落地低资源/端侧推荐小模型时，直接套用DeepLoop缩放规则α=(2N)^(1/2)、β=(8N)^(-1/2)，无需修改架构即可提升循环深度下的训练稳定性与效果

  - 开发多步思考的推荐Agent推理模块时，用该规则解决多轮循环的梯度爆炸/消失问题，不需要额外引入门控或辅助损失

  - 做轻量化生成式推荐模型时，搭配参数共享+DeepLoop方案，可在不增加参数量的前提下通过增加循环轮次提升表达能力，降低部署成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Looped Transformer通过共享少量物理Transformer块多轮执行，可在不增加参数量的前提下提升有效深度，是低资源场景下提升模型能力的重要路径，但原有的DeepNorm残差缩放规则针对无参数共享的标准Transformer设计，多轮共享参数时会因为梯度跨轮次聚合效应导致训练不稳定，无法充分释放循环深度的收益。

### 方法关键点
- 引入访问对齐系数κ_R衡量多轮循环下梯度和输出敏感度的相关性，推导绑定深度下的一阶稳定性约束，最坏对齐场景下残差缩放的指数阈值从DeepNorm的1/4提升到1/2；
- 完全沿用DeepNorm的Post-LN架构，仅修改缩放规则为α=(2N)^(1/2)、β=(8N)^(-1/2)，无额外参数、门控或辅助损失，改造成本极低；
- 可扩展到分层循环推理架构，支持不同模块独立设置缩放系数。

### 关键结果
- 在GPT-2小/中规模语言模型上，R=1（无循环）时与基线效果持平，R=7时小模型验证loss降0.0186，中模型验证loss降0.0278；
- 8项下游任务平均准确率，GPT-2中规模R=7时1-shot准确率达55.20%，比基线高0.58个百分点；
- 应用到分层推理模型HRM上，ARC-AGI任务2票投票准确率从36.50%提升到39.75%，涨幅达3.25个百分点。

**最值得记住的一句话**：循环Transformer的残差缩放需要考虑参数的重复访问次数，而不仅仅是名义上的层数。
