---
title: 'MASCOT: Model-Aware Submodular Coverage for Composite-Attribute Text-to-Image
  Retrieval'
title_zh: MASCOT：面向复合属性文图检索的模型感知子模覆盖方法
authors:
- Aaryan Sharma
- Vishak Prasad C
- Virendra Singh
- Ganesh Ramakrishnan
affiliations:
- Indian Institute of Technology Bombay
arxiv_id: '2608.12532'
url: https://arxiv.org/abs/2608.12532
pdf_url: https://arxiv.org/pdf/2608.12532
published: '2026-08-12'
collected: '2026-08-14'
category: RecSys
direction: 文图检索 · 多属性可控多样性重排
tags:
- Diversification
- Re-ranking
- Text-to-Image Retrieval
- Submodular
- VLM
one_liner: MASCOT重排方法将多属性多样性转化为资源分配问题，解决复合约束下早排召回下降问题
practical_value: '- 电商多属性搜索（如带地域、时效约束的商品/素材检索）场景可复用MASCOT的软分桶+查询感知权重的多样性控制逻辑，替代传统DPP类重排避免早排召回暴跌

  - 多约束下的结果重排可参考将多样性要求转化为资源分配问题的建模思路，无需依赖流形排斥即可精准控制不同属性的覆盖度

  - 复合属性约束的推荐/检索场景可直接复用其开源的子模覆盖优化实现，快速适配业务需求'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
VLM驱动的文图检索仅保障相关性不足，需实现跨地理、时间等复合属性的结果多样性精准控制；现有MS-DPP等基于流形排斥的重排方法，在离散元数据的降多样性任务中早排召回大幅下降，无法满足复合约束场景需求。
### 方法关键点
MASCOT重排框架放弃流形排斥思路，将多属性多样性建模为资源分配问题，把属性投影到由查询驱动重要性加权的软分桶空间，通过子模覆盖优化实现相关性与可控多样性的平衡。
### 关键结果
3个PixelProse降多样性任务平均R@10达88.58%，远超MS-DPP的67.63%；复合约束PP_geo_hour任务下，MS-DPP R@1暴跌至0.23、R@10降至0.4931，MASCOT仍保持R@1=0.7202、R@10=0.9410，且多样性指标优于无约束基线。
