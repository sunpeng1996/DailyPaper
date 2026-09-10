---
title: 'Beyond One-Size-Fits-All: Sample-Adaptive Strategy Routing for Vision Token
  Pruning in MLLMs'
title_zh: 面向多模态大模型视觉Token剪枝的样本自适应策略路由
authors:
- Haiji Liang
- Pengfei Zhou
- Zhenglin Wan
- Wei Wang
- Yang You
- Wangbo Zhao
affiliations:
- National University of Singapore
- InfRec, Cardinal AI Lab
- The Hong Kong University of Science and Technology
arxiv_id: '2609.10346'
url: https://arxiv.org/abs/2609.10346
pdf_url: https://arxiv.org/pdf/2609.10346
published: '2026-09-09'
collected: '2026-09-10'
category: Multimodal
direction: 多模态大模型 · 视觉Token剪枝效率优化
tags:
- MLLM
- Token Pruning
- Adaptive Routing
- Inference Acceleration
- VIP-Router
one_liner: 提出即插即用VIP-Router，为MLLM每个输入自适应选最优视觉Token剪枝策略
practical_value: '- 多模态商品理解、图文推荐场景可直接复用VIP-Router即插即用架构，无需修改原有MLLM权重，仅新增万级参数量即可在降低推理成本的同时避免剪枝带来的效果损失

  - 可迁移该样本自适应路由思路到推荐系统的策略选择场景：将现有多种召回/排序策略作为候选集，用低开销的用户/商品/query特征训练轻量路由模块，替代全局固定策略，提升单样本效果

  - 优化目标可参考论文的cost-aware效用设计，直接将计算成本纳入路由评分，平衡效果与推理开销，适配电商高QPS的线上部署要求'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前MLLM处理单张图像需要数百上千个视觉Token，推理成本极高，是多模态业务落地的核心瓶颈；现有固定视觉Token剪枝策略仅追求平均精度最优，掩盖了样本层面的策略互补性——平均最优策略在超1/3的单样本上效果不如其他剪枝策略，存在巨大优化空间。
### 方法关键点
- 设计VIP-Router轻量路由模块，仅新增约0.017%的骨干参数量，即插即用无需修改原有剪枝算法或MLLM权重
- 用冻结CLIP的视觉/文本编码器提取低开销预览特征，通过文本到视觉的交叉注意力生成query关联的视觉表征，结合保留Token比例特征输入两层MLP预测各候选策略的效用
- 采用cost-aware效用作为优化目标，将策略的正确性与Token成本共同纳入评分，保留全量Token推理作为降级选项，避免剪枝失效导致的效果损失
### 关键实验结果
在剪枝敏感的VTC-Bench Group A数据集上评测，对比4种SOTA固定剪枝策略：全剪枝比例下平均准确率相对提升26.9%，考虑实际Token成本的平均效用相对提升22.0%；跨4种不同MLLM骨干均获得一致效果提升，零样本迁移到4个未见过的基准测试也取得正向收益。

最值得记住的结论：平均最优的固定策略不等于单样本最优，利用策略间的样本级互补性做自适应路由，是低开销提升系统效果与效率的重要路径。
