---
title: Balanced Twin Weight Factorization for Efficient MLLMs
title_zh: 面向高效多模态大模型的平衡双权值分解方法
authors:
- Bryan A. Plummer
- Shan Lu
- Keval Doshi
- Noranart Vesdapunt
- Wei Wang
- Jim Thomas
- Kah Kuen Fu
affiliations:
- Amazon
arxiv_id: '2611.21459'
url: https://arxiv.org/abs/2611.21459
pdf_url: https://arxiv.org/pdf/2611.21459
published: '2026-11-16'
collected: '2026-11-17'
category: Training
direction: 多模态大模型 · 权值压缩优化
tags:
- Weight Factorization
- MLLM
- Model Compression
- Low Rank
- Inference Acceleration
one_liner: 提出平衡双权值分解BTWF，同等算力下为多模态大模型带来2-6%性能提升
practical_value: '- 可将BTWF的FCB+BCB权值平衡思路迁移到推荐大模型的LoRA压缩场景，在降低推理延迟的同时减少长尾小维度特征的损失，适配电商广告/商品推荐的长尾分布特性

  - 借鉴Overparameterized Groups（OG）设计，训练阶段给推荐系统核心层（如用户/物品embedding投影层、多模态商品理解层）增加过参数，推理时折叠回原尺寸，无需额外线上资源即可提升模型表现

  - BTWF可作为drop-in模块与现有量化、剪枝、KV cache优化技术结合，在电商多模态推荐、智能导购Agent等场景下用更低的资源成本拿到1-9%的性能增益'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有权值分解（WF）方法虽然能减少模型参数量和FLOPs，但替换大矩阵为多个小矩阵带来的调度开销会导致实际延迟降低幅度远低于FLOPs减少幅度；且现有共享基分解方法在处理尺寸不同的孪生层（如注意力Q/K/V投影、SwiGLU的门控/上投影层）时会天然偏向尺寸更大的层，导致小层重建误差过高、整体性能损失大。

### 方法关键点
- **Factor Component Balancing（FCB）**：按每个孪生层的Frobenius范数归一化重建损失，平衡不同尺寸层对共享基的贡献，解决传统方法的大层偏好问题。
- **Block Contribution Balancing（BCB）**：按因子对所在Transformer块输出的敏感度加权，优先保留对下游任务更有用的因子，有效降低块级输出误差。
- **Overparameterized Groups（OG）**：对低秩敏感层训练时使用高于盈亏平衡点的秩增加模型容量，推理时将因子相乘折叠回原层尺寸，无额外推理成本即可提升性能。

### 关键实验
在6个不同架构的多模态大模型（InternVL3系列、Qwen2-VL/3-VL/3.5、Gemma 4 E2B）、9个图文/视频多模态基准上测试，对比SVD-LLM、AdaSVD、Cat等SOTA权值分解方法：无微调时性能领先2-6%，微调恢复后领先1-3.5%；结合剪枝、量化、Token剪枝时可额外获得1-9%增益，是同类因子分解方法中推理延迟最低的。

权值分解的实际收益不能仅看FLOPs减少幅度，平衡不同层的因子贡献、优先保留对下游输出影响大的因子，才能真正实现模型的“降本增效”。
