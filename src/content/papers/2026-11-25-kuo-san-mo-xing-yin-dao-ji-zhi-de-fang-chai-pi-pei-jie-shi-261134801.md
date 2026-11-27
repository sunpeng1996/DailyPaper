---
title: Guidance as Variance Matching
title_zh: 扩散模型引导机制的方差匹配解释与无调参实现方法
authors:
- Ali Backour
- Artem Lukoianov
- Frank Permenter
- Tommi Jaakkola
- Justin Solomon
- Vincent Sitzmann
affiliations:
- Massachusetts Institute of Technology
- Toyota Research Institute
arxiv_id: '2611.34801'
url: https://arxiv.org/abs/2611.34801
pdf_url: https://arxiv.org/pdf/2611.34801
published: '2026-11-25'
collected: '2026-11-27'
category: Other
direction: 生成模型优化 · 扩散引导机制
tags:
- Diffusion Model
- Guidance
- Variance Matching
- Generative Model
- Hyperparameter-free
one_liner: 提出扩散模型引导的方差匹配解释，给出无调参闭形式引导尺度计算方法
practical_value: '- 用扩散模型生成电商商品图、营销文案、虚拟模特素材时，可直接复用方差匹配闭形式规则计算引导尺度，省去人工调参成本

  - 跨模态生成商品短视频、口播音频等营销内容时，无需为不同模态单独调优引导超参，匹配对应模态数据方差即可得到最优效果

  - 业务用到生成模型融合时，可参考负引导尺度结论，实现双向风格迁移满足不同营销场景的差异化内容需求'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
扩散模型的Guidance能大幅提升生成样本质量，但内在机制长期不明确，现有引导尺度需要大量人工调参，跨模态适配成本极高。

### 方法关键点
1. 发现现有Guidance实际不优化后验均值预测，而是通过提升预测方差匹配真实数据分布方差来优化样本质量；
2. 方差匹配引导（VMG）闭形式规则可通过匹配引导后预测方差与真实数据方差直接计算最优引导尺度，无需调参；
3. 给出Guidance的误差重缩放解释，支持负引导尺度、不同参考模型对应不同最优尺度两个新假设。

### 关键结果
在11个跨模态SOTA模型（图像/视频/音频/运动/世界模型）上无需调参即可复现人工最优引导尺度，Spearman相关系数达0.96；SD 3.5 Medium上用户偏好度优于人工设计的引导尺度schedule。
