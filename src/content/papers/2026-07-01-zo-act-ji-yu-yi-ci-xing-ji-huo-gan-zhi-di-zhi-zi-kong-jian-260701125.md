---
title: 'ZO-Act: Efficient Zeroth-Order Fine-Tuning via One-Shot Activation-Informed
  Low-Rank Subspaces'
title_zh: ZO-Act：基于一次性激活感知低秩子空间的高效零阶微调
authors:
- Xun Dong
- Yibo Xu
- Naigang Wang
- Xin Li
- Penghang Yin
- Zi Yang
affiliations:
- University at Albany, SUNY
- IBM T. J. Watson Research Center
arxiv_id: '2607.01125'
url: https://arxiv.org/abs/2607.01125
pdf_url: https://arxiv.org/pdf/2607.01125
published: '2026-07-01'
collected: '2026-07-02'
category: Training
direction: LLM零阶微调 · 低秩参数化
tags:
- Zeroth-Order Optimization
- Low-Rank Adaptation
- LLM Fine-tuning
- Quantization
- Activation-aware
one_liner: 基于输入激活构造固定低秩子空间约束零阶扰动，实现内存友好的高效LLM零阶微调
practical_value: '- 业务侧需在边缘/低显存设备微调垂直域LLM（如商品文案生成Agent、query理解小模型）时，可直接复用ZO-Act方案，无需反向传播，显存仅需推理级，支持INT4量化模型微调，大幅降低适配门槛

  - 可将激活感知低秩子空间思路迁移到LoRA优化：初始化时用少量校准样本激活的SVD生成LoRA右矩阵并冻结，仅训系数矩阵，进一步降低参数量和训练方差，适合推荐场景小样本快速适配

  - 低方差零阶优化思路可迁移到黑盒优化场景：如推荐排序策略调优、广告出价优化等无法求导的场景，用业务指标为损失，基于低秩子空间约束扰动维度，降低调参方差'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
零阶（ZO）优化无需反向传播，仅靠前向损失评估即可微调LLM，显存占用仅为推理级，适合低资源、量化模型部署场景，但现有方法要么扰动全量参数，要么采用随机低秩子空间，存在梯度估计方差极高、收敛慢、效果差的问题，远达不到一阶微调的性能。
### 方法关键点
- 初始化阶段用少量校准样本做一次前向传播，对每个线性层的输入激活做SVD，取Top-r右奇异向量作为固定低秩子空间基，全程冻结
- 权重更新仅参数化子空间对应的系数矩阵B，扰动和优化都仅在低维系数空间进行，有效维度从mn降到rn（r远小于m）
- 支持Adam等动量优化器直接作用于显式的系数变量，天然支持量化模型微调（原低比特权重全程冻结）
### 关键结果
在Llama-3-8B、OPT-13B、INT4量化Llama-3-8B上验证，对比MeZO、ZO-Muon、AGZO等SOTA零阶基线：
- 语言理解任务上，Llama-3-8B的RTE准确率比SOTA ZO-Muon高5.8个点，CB准确率高19.7个点
- 常识推理任务平均准确率达70.8%，比次优AGZO高2.6个点
- 显存占用仅16.1GB（INT4版本仅5.8GB），运行速度优于所有基线，初始化开销仅1.5秒

最值得记住的一句话：LLM层梯度的主要分量集中在输入激活的Top奇异向量张成的子空间，基于该子空间约束零阶扰动，能以极小的可控偏差换取梯度估计方差的大幅降低，是低资源LLM微调的极优方案。
