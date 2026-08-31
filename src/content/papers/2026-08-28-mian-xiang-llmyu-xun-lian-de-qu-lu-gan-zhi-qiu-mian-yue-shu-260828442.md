---
title: Curvature-Conditioned Multiscale Momentum with Sphere Constraints for LLM Pretraining
title_zh: 面向LLM预训练的曲率感知球面约束多尺度动量优化器
authors:
- Shuchen Zhu
- Yuxin Fang
- Mingze Wang
- Kun Yuan
affiliations:
- ByteDance Seed
- Peking University
arxiv_id: '2608.28442'
url: https://arxiv.org/abs/2608.28442
pdf_url: https://arxiv.org/pdf/2608.28442
published: '2026-08-28'
collected: '2026-08-31'
category: Training
direction: LLM预训练 · 优化器效率提升
tags:
- Optimizer
- LLM Pretraining
- Multiscale Momentum
- Muon
- Sphere Constraint
- MoE
one_liner: 为Muon优化器加入曲率感知平坦方向多尺度动量与球面约束，稳定加速LLM预训练
practical_value: '- 训练垂直领域中小规模LLM时，可直接复用MuonM替换AdamW/Muon，同等计算预算下拿到更低预训练loss，提升商品文案生成、用户query理解等下游任务效果

  - 自研优化器团队可复用平坦方向梯度降噪设计：仅在低曲率平坦方向加慢动量降噪，尖锐方向保留快动量保稳定，避免全参数加动量带来的训练震荡

  - 可借鉴球面约束替代权重衰减的设计，解决多尺度动量带来的参数范数膨胀、有效学习率衰减过快问题，降低学习率等超参调优成本

  - 训练MoE架构垂域大模型时优先尝试该优化器，实验验证其在MoE上也能稳定拿到loss收益，适配推荐/电商场景多专家路由大模型训练'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM预训练计算成本极高，现有AdamW、Muon等优化器依赖梯度归一化仅能部分缓解损失面病态问题，主导最终loss下降的平坦方向训练进度极慢；直接放大平坦方向学习率又会放大梯度噪声，导致训练不稳定，亟需高效动量机制在保证稳定的前提下加速平坦方向训练。

### 方法关键点
- 曲率感知多尺度动量：仅在低曲率平坦方向组合快慢双动量，慢动量（低衰减率）负责梯度降噪，快动量（高衰减率）负责快速适配曲率变化，尖锐方向不引入慢动量避免训练震荡
- 球面约束设计：替换传统权重衰减，对参数施加Frobenius范数球面约束+慢动量平行传输，解决多尺度动量带来的参数范数膨胀、有效学习率塌陷问题
- 低开销实现：通过在线幂迭代估计平坦方向，额外计算开销可忽略，仅需多存储一组慢动量buffer，适配FSDP等分布式训练策略

### 关键实验
在350B token高质量预训练语料上测试，覆盖0.12B~2.3B参数的Dense/MoE架构，对比Muon、MuonS、AdEMAMix、EMA-Nesterov等主流优化器：所有场景下MuonM的terminal loss比Muon低约0.03，比MuonS低约0.02；训练周期越长收益越大，1000TPP下loss优势进一步扩大，且最优学习率随训练周期的衰减幅度仅为Muon的1/4，超参适配性更强。

### 核心结论
仅在平坦方向加慢动量降噪+球面约束防范数膨胀，是几乎无额外成本的LLM预训练加速手段，收益稳定且可叠加在现有成熟优化器之上。
