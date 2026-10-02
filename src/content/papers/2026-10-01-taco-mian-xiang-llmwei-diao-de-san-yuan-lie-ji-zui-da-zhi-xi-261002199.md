---
title: 'TACO: Ternary Absolute-max Column-wise One-sparse Optimizer for LLM Fine-Tuning'
title_zh: TACO：面向LLM微调的三元列级最大值单稀疏优化器
authors:
- Jichao Jiang
- Cristian McGee
- El Houcine Bergou
- Hanqin Cai
- Aritra Dutta
affiliations:
- University of Central Florida
- Mohammed VI Polytechnic University
arxiv_id: '2610.02199'
url: https://arxiv.org/abs/2610.02199
pdf_url: https://arxiv.org/pdf/2610.02199
published: '2026-10-01'
collected: '2026-10-02'
category: Training
direction: 低内存LLM全参数微调优化器
tags:
- LLM Fine-tuning
- Optimizer
- Memory Efficiency
- Full Parameter Tuning
- Sparse Gradient
one_liner: 以极低优化器内存开销实现LLM全参数微调，精度速度接近AdamW
practical_value: '- 电商/推荐域垂直LLM微调（如query改写、商品文案生成、生成式推荐prompt调优）可直接替换AdamW为TACO，单张80G
  H100即可完成32B参数模型全参数微调，无需多卡集群，降低训练成本

  - 梯度稀疏设计思路可迁移到推荐大模型训练：仅保留每列梯度Top-k大值用FP8存储，可大幅降低优化器内存开销，精度损失可控

  - 无Muon微调Adam预训练模型的性能掉点问题，迁移通用预训练LLM到业务场景时无需额外适配优化器超参数，默认配置可跨模型规模生效'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM全参数微调时AdamW等传统优化器的状态内存开销极高，13B参数模型仅优化器动量状态就需约104GB内存，现有内存优化方案要么牺牲精度、要么与Adam预训练模型存在更新几何不匹配导致性能掉点，亟需兼顾内存效率、精度、训练速度的优化器方案。

### 方法关键点
- 基于维度归一化1→1算子范数推导精确最速下降方向，每列仅保留绝对值最大的梯度的符号作为更新，天然产生三元、列级单稀疏更新规则，无需后处理梯度剪枝
- 仅为每列维护FP8精度的Top16梯度大值EMA历史作为稀疏状态，代替传统AdamW的两个FP32动量矩阵，优化器状态复杂度从O(mn)降至O(n)
- 理论证明收敛性符合非凸优化要求，且与AdamW共享连续几何结构，微调Adam预训练模型无优化器不匹配问题，同时符合µP缩放规则，学习率可跨模型规模迁移

### 关键实验
在OPT、Qwen3、Llama、Mistral等5个模型族、SST-2/RTE/BoolQ等8个下游任务上对比基线，OPT-13B任务上，TACO持久优化器状态比AdamW8bit低174×（从27.7GB降至0.16GB），峰值训练内存降低2.9×（从80.6GB降至27.5GB），精度和训练吞吐量接近AdamW；单张80G H100可完成32B参数模型全参数微调。

最值得记住的一句话：优化几何原生带来的稀疏性，比后处理梯度剪枝能更好地兼顾内存效率、精度和训练稳定性。
