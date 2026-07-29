---
title: Rethinking Expert Training for Model Merging with Prompt Learning
title_zh: 基于提示学习的模型融合专家训练策略优化
authors:
- Christos Georgakilas
- Aniello Panariello
- Samir El Karrat Moreno
- Simone Calderara
- Dimosthenis Karatzas
- Joost van de Weijer
affiliations:
- Computer Vision Center, Barcelona, Spain
- Universitat Autònoma de Barcelona, Barcelona, Spain
- AImageLab, University of Modena and Reggio Emilia, Italy
arxiv_id: '2607.24465'
url: https://arxiv.org/abs/2607.24465
pdf_url: https://arxiv.org/pdf/2607.24465
published: '2026-07-27'
collected: '2026-07-29'
category: Training
direction: 大模型训练 · 多专家模型融合优化
tags:
- Model Merging
- Prompt Learning
- LoRA
- Expert Training
- Multi-task Learning
one_liner: 提出两阶段双调专家DTE训练策略，显著提升多领域专家模型融合的效果与兼容性
practical_value: '- 多场景/垂直域专家模型融合时，可先做prompt tuning再微调LoRA等小参数，降低参数更新幅度，减少跨场景权重干涉

  - 跨域多任务模型部署前，可用DTE策略训练各场景专家，无需修改现有融合逻辑即可提升最终合并模型效果

  - 业务侧多垂直域小模型合并成本高时，可优先尝试固定backbone仅合并各域独立prompt的基线方案，落地成本低'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有模型融合研究多聚焦融合流程优化，默认专家来自全参数微调，跨任务权重干涉严重，导致融合后性能衰减。
### 方法关键点
1. 验证固定 backbone 仅独立学习各任务 prompt 的基线方案，可完全规避权重融合的干涉问题，效果优于传统融合基线；
2. 提出 Dual-Tuned Experts (DTE) 两阶段训练策略：先学习任务专属 prompt，再微调 encoder 小参数，大幅降低任务专属参数更新幅度，提升专家融合兼容性。
### 关键结果
在多类 CLIP 架构、全微调/LoRA 专家场景下，DTE 可稳定提升各类标准融合方法的合并后性能，对异构专家集合融合依然有效。
