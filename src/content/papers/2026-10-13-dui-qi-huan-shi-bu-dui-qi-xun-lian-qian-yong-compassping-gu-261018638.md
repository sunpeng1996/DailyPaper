---
title: 'To Align or Not To Align: Check Your COMPASS Before You Train'
title_zh: 对齐还是不对齐：训练前用COMPASS评估模型对兼容性
authors:
- Fabian Gröger
- Petar Damjanović
- Maria Brbić
affiliations:
- EPFL
- University of Basel
- HSLU
arxiv_id: '2610.18638'
url: https://arxiv.org/abs/2610.18638
pdf_url: https://arxiv.org/pdf/2610.18638
published: '2026-10-13'
collected: '2026-10-15'
category: Eval
direction: 模型兼容性评估 · 训练前诊断
tags:
- Model Compatibility
- Cross-Modal Alignment
- Model Merging
- k-NN Overlap
- Transfer Learning
one_liner: 提出COMPASS指标，无需对齐/合并即可低成本估算模型对的跨模态对齐、模型合并兼容性
practical_value: '- 做多模态电商推荐/多模态Agent时，对齐视觉编码器和LLM前可先用COMPASS的局部k-NN重叠预筛选模型对，避免无效试错，降低训练成本

  - 做LoRA合并、多任务推荐模型合并时，可先计算两个checkpoint的局部k-NN重叠，预判合并后效果，无需每次合并完做全量评估

  - 选择预训练模型做下游推荐任务迁移时，可参考ease×ceiling双轴逻辑，既看当前模型匹配度，也看预训练范式和下游任务的适配天花板，避免范式不匹配的无效投入'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前跨模态对齐、多任务模型合并是搭建多模态系统、复用预训练模型能力的核心手段，但候选模型对的兼容性只能在完成完整对齐/合并流程后才能评估，当候选池较大时试错成本极高，缺乏低成本的预诊断方法。

### 方法关键点
- 核心假设：模型表示的局部邻居结构一致性是兼容性的核心信号，比全局表示相似性更鲁棒
- 拆解为两个可低成本计算的维度：ease是待组合模型对在初始状态下的局部k-NN重叠率，代表对齐/合并的难度，数值越高越容易兼容；ceiling是模型所属预训练范式的平均最大重叠率，代表该范式下可达到的兼容性天花板
- 最终COMPASS得分=ease×ceiling，用于模型对排序；还可按两个维度的中位数划分为四个象限，给出对应行动指导：双高的act now直接使用，低ease高天花板的budget-limited可投入更多资源优化，高ease低天花板的ceiling-limited建议更换预训练范式，双低的incompatible直接放弃

### 关键实验
在72组跨模态对齐实验、392组任务算术模型合并实验上验证：跨模态对齐场景下COMPASS和下游检索R@1的皮尔逊相关系数达0.91，模型合并场景和下游平均保留精度的相关系数达0.70，远优于传统全局相似性指标CKA的0.68和0.25，可将评估成本降低两个数量级。

### 核心结论
模型对兼容性的核心信号是局部邻居结构的一致性而非全局表示相似性，预训练范式和目标任务的适配性决定了最终效果的天花板，盲目堆算力无法突破范式带来的上限
