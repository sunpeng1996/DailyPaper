---
title: Dense Structural Compression of Transformers via Gauge-Correct Channel Removal
title_zh: 基于规范校正通道移除的Transformer稠密结构压缩方法
authors:
- Jed A. Duersch
- Naïm Es-Sebbani
- Nathanaël Haas
- Zied Bouraoui
affiliations:
- Université d'Artois
- CNRS
- CRIL UMR 8188
arxiv_id: '2609.07264'
url: https://arxiv.org/abs/2609.07264
pdf_url: https://arxiv.org/pdf/2609.07264
published: '2026-09-07'
collected: '2026-09-09'
category: Training
direction: Transformer训练优化 · 模型压缩
tags:
- Transformer
- Model Compression
- Structured Pruning
- GaugeLasso
- Training Optimization
one_liner: 提出GaugeLasso训练时动态压缩Transformer，保留稠密张量实现更高GPU推理效率
practical_value: '- 垂直域小模型落地：电商/推荐场景下的文案生成、Query理解等小规格垂直LLM，可复用GaugeLasso动态压缩框架，在保证效果的前提下降低推理成本，适配高并发请求

  - 排序模型结构优化：搜索/推荐的Transformer类排序模型训练时，可复用通道效用评估逻辑，诊断各层维度的冗余/饱和情况，指导异构层结构设计，效率远高于手动调参

  - 训练提速：训练大规格推荐/LLM模型时，可加入动态通道移除逻辑，随着训练推进自动缩小模型尺寸，实现1.6~5倍的训练后期提速，降低训练成本'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
Transformer推理成本中稠密矩阵乘占比极高，现有后剪枝、NAS等方法要么无法保留稠密张量导致GPU利用率低，要么受限于规范自由度（gauge freedom）导致通道剪枝不稳定；且手工设计的同构层结构普遍存在冗余，远大于推理所需的最小结构，亟需训练时动态压缩的方法，在保证效果的同时提升推理效率。

### 方法关键点
- 提出GaugeLasso对称组Lasso惩罚，对规范连接的张量两侧同时施加惩罚，解决传统乘积范数惩罚受规范自由度影响的不稳定问题，收敛到规范平衡点时组范数可直接衡量单通道的推理效用/计算量比值
- 采用效率校准逻辑，按通道移除后释放的FMA数量动态调整惩罚权重，保证不同结构轴的惩罚力度统一
- 实现动态训练框架：自适应惩罚强度锚定损失目标，定期用规范Sinkhorn迭代平衡张量尺度，信任丢弃机制移除效用低于阈值的通道，全程保留稠密张量无需稀疏掩码或训练重启，训练步速随模型压缩自动提升

### 关键实验
在4类任务上验证效果：多项式长除法任务实现148~255倍计算量压缩且精度无损；字符级语言建模任务，压缩后模型在同等FMA下比手工基线PPL低1.6%；训练后期步速提升1.6~5倍；同等压缩比下效果远优于后剪枝、CoFi等现有方法，后剪枝在语言建模任务同等FMA下PPL高22%。

> 最值得记住的结论：训练时持续施加结构压力得到的高效异构架构，远优于从完全训练的模型中后剪枝得到的结构；统计类任务下发现的高效架构可重新训练复现效果，精确算法类任务则必须依靠训练时的持续压力才能收敛。
