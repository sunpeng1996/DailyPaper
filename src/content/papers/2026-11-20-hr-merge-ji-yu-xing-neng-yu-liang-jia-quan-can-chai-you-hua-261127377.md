---
title: 'HR-Merge: Model Merging with Headroom-Weighted Residual Refinement'
title_zh: HR-Merge：基于性能余量加权残差优化的无训练模型合并框架
authors:
- Jiakang Huang
- Xueyan Zhang
- Renyi Cai
- Jingcheng Niu
- Jiaru Li
- Yining Wang
- Josh Zhang
- Jiahe Jiang
- Jinman Zhao
- Gerald Penn
affiliations:
- University of British Columbia
- University of Toronto
- University of California, Los Angeles
- Technische Universität Darmstadt
- Northwestern University
arxiv_id: '2611.27377'
url: https://arxiv.org/abs/2611.27377
pdf_url: https://arxiv.org/pdf/2611.27377
published: '2026-11-20'
collected: '2026-11-23'
category: Training
direction: 多任务无训练模型合并 · 残差优化
tags:
- Model Merging
- LoRA
- Multi-Task Learning
- LLaMA-3
- CLIP
one_liner: 可兼容任意基合并方法的无训练包装器，通过性能余量加权残差重合并提升多任务模型效果
practical_value: '- 现有多场景LoRA合并流程可直接套入HR-Merge包装器，无需额外训练、不改动原有合并逻辑，即可优化短板场景效果，且自带保底机制不会出现负向，上线风险极低；

  - 性能余量（headroom）的指标设计可复用至多任务模型优化：用单任务实际掉点比例作为任务权重，优先优化损失大的任务，比余弦相似度等权重侧proxy更直接有效；

  - fail-closed的参数选择机制可借鉴到所有算法迭代场景：优化项的候选权重包含0，无增益时自动回退基线，省去大量AB实验的成本。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多任务模型合并方法对所有任务采用统一规则，导致任务间掉点不均，短板任务效果损失严重，且多数优化方案需要额外训练成本，落地风险高。
### 方法关键点
- 两阶段无训练框架：第一阶段直接运行任意基合并方法得到初始模型，完全兼容现有合并逻辑；
- 性能余量（headroom）加权：计算每个任务单专家验证准确率与初始合并模型准确率的差值占比作为权重，自适应温度缩放后分配残差优化优先级；
- 残差重合并：复用基合并算子处理加权后的残差（单任务向量减初始合并更新量），避免直接加和导致的跨任务干扰；
- 保底选择机制：验证集选择残差项的加权系数，候选集包含0，确保最终模型效果不会低于基合并方法。
### 关键结果
在LLaMA-3 8B 6个NLI任务LoRA合并场景下，将TIES基线的归一化准确率从93.29提升至94.29，其中短板任务QNLI准确率从83.63提升至90.02；在3个CLIP backbone、最多20个视觉任务的全微调/LoRA合并场景下，所有配置下均提升或保持基线准确率，DC-Merge基线平均提升0.64个归一化准确率点，所有提升均通过McNemar显著性检验。
### 核心结论
模型合并损失的效果并未消失，而是残留在单任务与合并模型的权重差中，用验证集实际掉点量指导优化比权重相似度等间接指标更有效。
