---
title: 'LoRA-TSD: Tangent-Space Spectral Descent for LoRA via Muon-Style Updates'
title_zh: LoRA-TSD：基于Muon风格更新的LoRA切空间谱下降优化器
authors:
- Dmitrii Andriianov
- Andrey Veprikov
- Aleksandr Beznosikov
affiliations:
- BRAIn Lab
- SB AI Lab
- Innopolis University
arxiv_id: '2609.02734'
url: https://arxiv.org/abs/2609.02734
pdf_url: https://arxiv.org/pdf/2609.02734
published: '2026-09-02'
collected: '2026-09-03'
category: Training
direction: 参数高效微调 · LoRA训练优化
tags:
- LoRA
- Muon
- Optimization
- PEFT
- Riemannian Optimization
one_liner: 提出基于切空间谱下降的LoRA专属优化器LoRA-TSD，精度超越现有LoRA优化器且对适配秩鲁棒
practical_value: '- 业务场景微调大模型（如电商文案生成、推荐系统prompt对齐、Agent工具调用能力微调）时，可替换原有AdamW/LoRA+优化器，直接提升微调精度，低秩下稳定性提升更明显

  - LoRA-TSD的因子化实现无需实例化全量权重矩阵，和现有LoRA训练框架兼容，改造成本极低，retraction操作比传统截断SVD快最高2.8倍，训练速度损失可忽略

  - 若当前业务LoRA微调对rank选择敏感，切换LoRA-TSD可大幅降低rank调优成本，小rank下仍能保持较高精度，有效节省训练显存'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LoRA优化器独立更新A、B两个低秩因子，忽略二者乘积形成的低秩矩阵流形几何特性，导致权重空间的更新缩放错位、对适配秩参数高度敏感，泛化效果不稳定；同时现有基于流形的LoRA优化方法依赖截断SVD操作，计算开销大难以落地。

### 方法关键点
- 将每步LoRA更新建模为固定秩矩阵流形的切向量，在切空间内执行Muon风格的谱范数最陡下降，平衡更新的奇异方向避免少数方向主导训练
- 设计LoRA原生的因子化retraction机制，仅通过A、B的梯度即可计算切空间投影，无需实例化全量m×n权重矩阵，比传统截断SVD retraction快最高2.8倍
- 理论证明Frobenius范数版本的LoRA-TSD等价于LoRA-Pro，首次给出LoRA-Pro和LoRA-TSD二者的全局收敛保证

### 关键实验
在Llama-3.2-1B、Llama-3.1-8B、Qwen3-32B三个模型的6个常识/NLI基准测试上，对比AdamW、LoRA-Pro、LoRA-Muon、Riemannion等9个基线：1B模型平均准确率达82.49%，超出第二名0.89个点；8B模型平均准确率达89.7%，超出第二名0.8个点；11个测试场景下精度超越全参数Muon微调，且在不同LoRA rank下精度波动最小，对秩参数鲁棒性最优。

**最值得记住的一句话**：LoRA优化的核心约束是低秩乘积的流形几何，基于切空间的谱更新比独立因子更新在精度、鲁棒性上都有显著优势。
