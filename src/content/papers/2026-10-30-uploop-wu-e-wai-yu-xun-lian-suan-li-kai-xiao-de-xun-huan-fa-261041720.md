---
title: 'UpLoop: Training Looped Transformers via Upcycling at No Extra Pretraining
  Compute'
title_zh: UpLoop：无额外预训练算力开销的循环Transformer训练方法
authors:
- Cheng Liang
- Tengfei Zhang
- Ya Zhang
- Yanfeng Wang
- Zhouhan Lin
affiliations:
- Shanghai Jiao Tong University
- University of Science and Technology of China
arxiv_id: '2610.41720'
url: https://arxiv.org/abs/2610.41720
pdf_url: https://arxiv.org/pdf/2610.41720
published: '2026-10-30'
collected: '2026-11-02'
category: Training
direction: LLM预训练优化 · 循环Transformer
tags:
- Looped-Transformer
- Pretraining-Optimization
- Training-Efficiency
- Reasoning
- Transformer
one_liner: 在参数、训练token、总FLOPs均与稠密基线对齐的前提下，通过阶段式训练提升循环Transformer性能
practical_value: '- 训练垂域小参数LLM（如电商导购Agent、推荐prompt生成模型）时，可复用UpLoop的算力调度策略：前期用浅层结构节省FLOPs，后期叠加中间块循环提升推理能力，在不增加总训练算力的前提下提升模型效果

  - 做推理增强场景（如复杂用户query理解、多步商品导购决策）时，可采用中间块共享权重循环架构，无需新增参数量即可获得更高推理深度，相比全量加深层数节省推理成本

  - 模型迭代时可复用深度增长的层复制机制，基于已训练好的浅层checkpoint直接复制层扩展深度，无需从头训练，大幅节省迭代周期和算力成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Looped Transformer通过共享权重重复计算提升推理深度，无需新增参数即可强化推理能力，但多轮迭代会显著提升训练FLOPs，现有方案无法在与标准稠密Transformer完全相同的参数、训练token、总训练FLOPs预算下实现效果增益。

### 方法关键点
- 采用四阶段预训练调度，执行深度按`L/4→L/2→L→L+(r-1)m`逐步提升，L为基准稠密模型深度，m为中间共享块层数，r为循环次数
- 深度增长阶段复制已训练层（含权重和Adam状态）初始化更深结构，复制后层独立训练
- 最终阶段选中中间m层作为共享块重复执行，仅增加执行深度不新增参数
- 前期浅层训练节省的算力完全覆盖后期循环的额外开销，总训练资源与稠密基线完全对齐

### 关键结果
在370M/760M/1.3B三个参数量级的OLMo 2架构上基于FineWeb-Edu预训练，与相同算力预算的稠密基线对比：1.3B参数下22个下游任务平均得分从22.99提升至27.52，零样本常识推理平均准确率从54.91%提升至56.47%，GSM8K微调后零样本准确率从8.72%提升至12.05%。

### 核心结论
预训练算力无需均匀分配，前期浅层训练节省的开销可支撑后期重复迭代训练，在零额外成本前提下提升模型推理能力。
