---
title: Conformal Calibration Transfer
title_zh: 共形校准迁移
authors:
- Achref Doula
affiliations:
- Technical University of Darmstadt
- Tongji University
arxiv_id: '2609.10737'
url: https://arxiv.org/abs/2609.10737
pdf_url: https://arxiv.org/pdf/2609.10737
published: '2026-09-09'
collected: '2026-09-12'
category: Other
direction: 共形预测 · 跨域无标注校准迁移
tags:
- Conformal Prediction
- Calibration Transfer
- Domain Adaptation
- Distribution Shift
- Uncertainty Estimation
one_liner: 面向跨域场景的无标注共形校准框架TCC及两种互补校正方法，提供有限样本覆盖保证
practical_value: '- 跨域推荐、多模态推荐场景下可复用TCC框架，无需目标域标注即可实现预测结果校准，解决分布偏移导致的置信度失真问题

  - 推荐系统排序阶段的置信度校准可采用weighted-TCC重加权方法，在分布偏移较小时提升校准效率，无需额外标注成本

  - LLM Agent跨场景部署时，可借鉴TCC-KS的无标注偏差校正思路实现输出不确定性校准，降低错误决策率'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
共形预测将点预测转换为带覆盖率保证的集合预测，前提是校准集与部署数据满足可交换性；但实际场景中常仅源域有标注校准数据，目标域无标注，二者仅通过无标注配对数据关联（如多模态切换、传感器更换），原有共形校准无法直接复用。
### 方法关键点
Transported Conformal Calibration (TCC)框架首先用无标注配对数据学习映射，将源域标注校准集迁移到目标域，再通过两种互补的无标注方法校正迁移残留偏差：
1. TCC-KS：用无标注不确定性代理检测分布偏差，保守调整校准参数
2. weighted-TCC：对迁移后的校准样本重加权使其贴合目标域分布，权重稳定时校准效率更高
框架同时提供适配可观测偏差程度的有限样本目标域覆盖保证。
### 关键结果
在CIFAR-100-C、Tiny-ImageNet-C、SEN12MS数据集上，无需目标域标注校准数据即可实现可靠的目标域覆盖率迁移，配套无标注诊断工具可准确判断校正触发时机
