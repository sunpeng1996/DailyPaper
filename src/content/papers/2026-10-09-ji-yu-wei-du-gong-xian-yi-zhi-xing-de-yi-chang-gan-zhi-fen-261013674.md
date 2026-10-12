---
title: 'Not All Dimensions Are Equal: Outlier-Aware Attention Linearization with Grouped
  Quadratic Kernels'
title_zh: 基于维度贡献异质性的异常感知分组二次核注意力线性化方法
authors:
- Weiqi Sun
- Qianyue Wu
- Wenjia Wang
- Tianyang Hu
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Beijing Normal University, Zhuhai
- National University of Singapore
arxiv_id: '2610.13674'
url: https://arxiv.org/abs/2610.13674
pdf_url: https://arxiv.org/pdf/2610.13674
published: '2026-10-09'
collected: '2026-10-12'
category: LLM
direction: LLM高效推理 · 注意力线性化优化
tags:
- Attention Linearization
- Transformer Optimization
- Inference Efficiency
- Outlier-aware
- Quadratic Kernel
one_liner: 异常感知注意力线性化OAL按维度贡献分组构造二次核，降低线性化误差适配预训练模型
practical_value: '- 做LLM4Rec、电商Agent长上下文推理时，可采用OAL替换模型中间层注意力，结合LoRA微调，在精度损失可控的前提下降低长序列推理延迟，适配用户长行为序列建模、长Query理解场景

  - 维度贡献异质性的思路可迁移到推荐系统用户/物品表征建模，对高贡献维度单独分配拟合参数、低贡献维度共享参数，在不损失召回/排序效果的前提下降低模型参数量

  - 文中基于贡献度统计+bootstrap稳定性校验的异常维度识别方法，可直接复用到推荐模型特征重要性评估、冗余特征剪枝环节，提升特征迭代效率'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有softmax注意力线性化方法普遍采用全局统一的近似参数，忽略了QK点积中仅占约5.5%的高贡献异常维度贡献了60%以上的近似误差的异质性特征，导致预训练模型转换后效果掉点严重，限制了长上下文低延迟推理的业务落地。
### 方法关键点
- 统计每个维度对QK点积的贡献度，采用bootstrap校验识别稳定的高贡献异常维度，按贡献度相似性对维度分组
- 采用Hadamard乘积形式的二次核近似，支持维度专属线性系数与跨维度二次交互，推理复杂度随序列长度线性增长
- 同组维度共享核系数，异常维度单独分组，既保留差异化拟合能力又将参数量控制在O(G²)（G为分组数，通常2-5）
- 核参数先基于预训练注意力输出离线校准，再结合LoRA联合微调适配下游任务
### 关键实验
在Qwen2.5-0.5B、Llama-3.2-1B上对比DiJiang、Performer、SpectraFormer等基线：
1. 冻结注意力参数场景下，OAL相对SOTA基线DiJiang降低输出相对MSE约8.9%
2. 替换中间层注意力+LoRA微调后，Qwen2.5-0.5B的WikiText-103困惑度从全局二次核的31.71降至27.50，PIQA、HellaSwag、ARC-E等下游任务准确率全面领先
### 核心结论
注意力维度贡献存在显著异质性，针对高贡献维度做差异化处理可通过极小的参数开销大幅提升线性化近似精度，是预训练模型高效转换的可行路径
