---
title: Objective-Specialized Residual Streams in Manifold-Constrained Hyper-Connections
title_zh: 流形约束超连接下的目标专属残差流优化方法
authors:
- Shantanu Agarwal
- Ruchita V. Maitri
- Zhiqi Huang
- Vivek Datla
- Alfy Samuel
affiliations:
- Capital One
arxiv_id: '2611.24567'
url: https://arxiv.org/abs/2611.24567
pdf_url: https://arxiv.org/pdf/2611.24567
published: '2026-11-18'
collected: '2026-11-19'
category: RecSys
direction: 多目标检索 · mHC残差流专业化
tags:
- mHC
- Multi-Objective Learning
- Hybrid Retrieval
- Residual Stream
- Transformer
one_liner: 为mHC多残差流分配专属训练目标，提升多目标检索性能并揭示分层specialization规律
practical_value: '- 电商多目标召回场景（需同时覆盖语义匹配、关键词匹配、属性匹配等互补目标）可直接复用该设计，给不同mHC流分配专属目标，仅增加0.41%（n=2流）~2.25%（n=4流）参数即可获得稳定效果提升

  - 工程实现可直接复用论文给出的mHC初始化方案，路由参数单独使用10倍于backbone的学习率训练，既不破坏预训练权重泛化性，又能在单epoch内快速完成专业化适配

  - 线上多目标融合阶段无需调整流权重，专业化模型在稀疏/稠密检索全融合区间效果均优于非专业化mHC，可灵活适配不同业务对召回准确率、召回率的偏好

  - 推理时可直接将跨流混合矩阵固定为单位矩阵，完全保留专业化收益的同时降低路由计算开销，适配搜索推荐低延迟推理要求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有mHC（流形约束超连接）将Transformer单残差流扩展为多并行流，但所有流统一向共享目标优化，未能充分释放多流适配互补任务的潜力；多目标检索（如稀疏lexical匹配+稠密语义匹配）的传统联合训练方案存在任务梯度干扰、表征空间冲突问题，难以同时实现两类互补目标的最优效果。

### 方法关键点
- 基于预训练ModernBERT改造mHC结构，给不同残差流分配专属训练目标：n=2/4流时前半部分流对应稀疏检索目标，后半部分对应稠密检索目标，输出层仅从对应流读取表征
- 保留mHC的read gate、write gate、跨流混合矩阵三层路由机制，初始化时保证与原Transformer功能完全对齐，路由参数单独设置更高学习率训练，避免破坏预训练权重
- 训练时稀疏、稠密目标分别计算对比损失，仅回传梯度到对应分配的流，减少跨任务梯度干扰

### 关键实验
在13个BEIR公开检索数据集上测试，对比单流联合模型、非专业化mHC（所有流共享同一训练目标）基线：Base规模下n=2流平均nDCG@10从0.4310提升至0.4486，n=4流从0.4410提升至0.4529；Large规模下n=4流从0.4573提升至0.4748；固定跨流混合矩阵为单位矩阵时收益无损失，说明效果提升完全来自目标专属的read/write路由设计。

### 最值得记住的结论
mHC多残差流的专业化收益核心来自顶层（最后10层）的目标专属路由，底层仍可共享通用表征，完美平衡多任务共享计算与专属能力的需求。
