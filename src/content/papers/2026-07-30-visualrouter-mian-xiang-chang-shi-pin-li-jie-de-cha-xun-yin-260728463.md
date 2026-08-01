---
title: 'VisualRouter: Query-Grounded Visual Sampling for Long Video Understanding'
title_zh: VisualRouter：面向长视频理解的查询引导视觉采样框架
authors:
- Haiyue Zhang
- Yi Bin
- Xun Jiang
- Zeyu Ma
- Duo Peng
- Guoqing Wang
- Yang Yang
- Heng Tao Shen
arxiv_id: '2607.28463'
url: https://arxiv.org/abs/2607.28463
pdf_url: https://arxiv.org/pdf/2607.28463
published: '2026-07-30'
collected: '2026-08-01'
category: Multimodal
direction: 多模态长视频理解 · LVLM帧采样优化
tags:
- LVLM
- Long-Video-Understanding
- Frame-Sampling
- Training-Free
- Multimodal
one_liner: 训练免调即插即用的查询感知长视频帧采样框架，分策略适配全局/局部查询，大幅提升LVLM长视频理解性能
practical_value: '- 电商直播/长商品视频理解场景可直接复用查询分桶策略，全局查询（如「该直播介绍了几款产品」）用关联+覆盖混合采样，局部查询（如「第三款产品的价格是多少」）用事件感知采样，降低LVLM输入token量同时提升准确率

  - 训练免调、即插即用的架构设计可直接集成到现有多模态内容理解链路，无需重新训练LVLM，落地成本极低

  - 可迁移至多模态搜索召回的帧特征提取环节，针对用户query类型动态选择采样帧，提升长视频内容的检索匹配精度'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
LVLM长视频理解受限于视觉token量大、上下文窗口有限，现有采样方法要么冗余高、时序覆盖不足，要么采用固定策略不区分查询类型，效果难以满足需求。

### 方法关键点
1. 推出训练免调、即插即用的VisualRouter框架，先将查询分为全局/局部两类，适配不同采样策略；
2. 全局查询采用关联度+覆盖度混合采样，兼顾query相关信息与时序完整性；
3. 局部查询采用事件感知采样，先做事件分割、按段分配帧配额、再段内选帧，平衡有限帧下的关联度、覆盖度、多样性。

### 关键结果
相较均匀采样，搭配Qwen2.5-VL-7B时在Video-MME、LongVideoBench、MLVU上分别提升5.2%、7.7%、11.6%，效果优于同设置下所有现有免训练采样方法。
