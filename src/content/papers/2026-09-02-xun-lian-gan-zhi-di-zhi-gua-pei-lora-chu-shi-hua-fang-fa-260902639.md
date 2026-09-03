---
title: 'TaRA: Training-Aware Low-Rank Adaptation Initialization'
title_zh: 训练感知低秩适配（LoRA）初始化方法TaRA
authors:
- Taehyeon Kim
- Eunhyeok Park
affiliations:
- Pohang University of Science and Technology (POSTECH)
arxiv_id: '2609.02639'
url: https://arxiv.org/abs/2609.02639
pdf_url: https://arxiv.org/pdf/2609.02639
published: '2026-09-02'
collected: '2026-09-03'
category: Training
direction: LoRA初始化 · 参数高效微调
tags:
- LoRA
- PEFT
- Initialization
- LLM Fine-tuning
- SVD
one_liner: 通过对齐全参数微调梯度方向的LoRA初始化方法，以极小开销大幅提升PEFT效果
practical_value: '- 做LLM4Rec、垂域Agent微调时，可直接替换现有LoRA初始化逻辑为TaRA，相同参数预算下无需改训练流程即可提升下游任务（比如商品文案生成、推荐prompt对齐）效果

  - 业务场景校准成本极低：仅需256条甚至32条业务样本即可完成初始化校准，总训练时间仅增加4-5%，性价比极高

  - 显存紧张场景可使用FP8精度收集激活、梯度协方差统计量，几乎不损失效果的前提下降低初始化阶段显存开销

  - 跨品类推荐、泛化Agent等分布偏移场景，可给协方差矩阵加入Ledoit-Wolf收缩正则，提升TaRA的OOD鲁棒性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LoRA是当前参数高效微调（PEFT）的主流方案，但现有初始化方法（随机初始化、基于预训练权重SVD的PiSSA、基于单步梯度的LoRA-One等）均未对齐全参数微调的训练动态，低秩瓶颈导致优化轨迹偏移，收敛效果差，相同rank下性能天花板低，低rank场景下性能损失尤其明显。

### 方法关键点
- 核心优化目标：让LoRA初始化后的局部梯度行为尽可能和全参数微调的梯度对齐，基于二阶泰勒展开和K-FAC Fisher近似，推导得出最优低秩解需要同时纳入激活协方差、梯度协方差和预训练权重三类信息
- 实现流程：用小批量校准集做一次前向后向传播，收集各层输入激活和权重梯度，计算协方差矩阵后对Σ_G W0 Σ_X做SVD分解，取前r个奇异分量逆投影回原空间初始化LoRA的A、B矩阵，同时修正残差权重保证初始输出和原预训练模型完全一致
- 工程兼容设计：协方差矩阵加1e-2倍均值奇异值的对角阻尼保证数值稳定，支持低精度协方差收集、极小校准集适配

### 关键实验结果
- 覆盖数学推理、代码生成、常识推理三类任务，对比基线包括原始LoRA、PiSSA、CorDA、LoRA-One：r=128时GSM8K-D准确率比次优方法高1.05%，平均任务得分高0.85%；r=32时平均得分比次优高0.98%，低rank下收益更显著
- 初始化开销仅占总训练时间的4-5%，校准集最小32条即可获得稳定效果，FP8精度收集统计量几乎无精度损失

最值得记住的一句话：LoRA初始化的核心不是拟合预训练权重或单步梯度，而是对齐全参数微调的局部训练动态，能在不增加推理开销的前提下稳定提升PEFT效果。
