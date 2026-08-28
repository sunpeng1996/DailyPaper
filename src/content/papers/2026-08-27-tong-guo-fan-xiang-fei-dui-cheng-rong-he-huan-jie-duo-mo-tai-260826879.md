---
title: Mitigating Strong-Modality Collapse in Multimodal Learning via Inverted Asymmetric
  Fusion
title_zh: 通过反向非对称融合缓解多模态学习中的强模态坍塌
authors:
- Mary Ogbuka Kenneth
- Foaad Khosmood
- Abbas Edalat
affiliations:
- Imperial College London
- California Polytechnic State University, San Luis Obispo
arxiv_id: '2608.26879'
url: https://arxiv.org/abs/2608.26879
pdf_url: https://arxiv.org/pdf/2608.26879
published: '2026-08-27'
collected: '2026-08-28'
category: Multimodal
direction: 多模态融合 · 强模态坍塌优化
tags:
- Multimodal Fusion
- Knowledge Distillation
- Asymmetric Fusion
- Modality Collapse
one_liner: 提出反向非对称融合IAF解决多模态融合强模态坍塌问题，较最优单模基线最高提升8.25%
practical_value: '- 做多模态推荐/多模态搜索时，可优先保留用户行为、商品标题等核心强模态特征不强制跨模态对齐，避免主模态信息损失

  - 商品图片、短视频音频等弱模态可先用模态感知知识蒸馏预增强，再以主模态为锚做单向注意力融合，提升多模态特征质量

  - 多模态召回/排序模型上线前可新增通路隔离验证环节，检测强模态性能是否下降，提前规避融合反降问题'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有早融合、晚融合、对称注意力融合等多模态融合方法常出现强模态性能下降（定义为强模态坍塌），甚至无法超过最优单模态基线，大幅限制多模态模型的实际收益。
### 方法关键点
1. 提出反向非对称融合（IAF）：不强制模态间双向注意力，主模态特征直接透传不修改，弱模态以主模态为上下文锚点做单向注意力融合；
2. 融合前置步骤：用模态感知知识蒸馏对弱模态做预训练增强，提升弱模态表征质量。
### 关键结果
在3个不同模态主导的基准数据集验证：IAF可100%保留强模态的单模态精度上限，而对称融合会使MultiHuSE数据集的强模态精度最多下降18.5%；IAF较最优单模态基线最高提升8.25%
