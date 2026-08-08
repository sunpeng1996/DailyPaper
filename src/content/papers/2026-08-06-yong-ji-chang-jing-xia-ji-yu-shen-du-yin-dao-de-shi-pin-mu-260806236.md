---
title: Depth-Guided Video Object Counting in Crowded Scenes
title_zh: 拥挤场景下基于深度引导的视频目标计数
authors:
- Yuanjing Xu
- Xinyan Liu
- Weidong Chen
- Zixuan Zou
- Linhao Zhang
- Zhuangzhe Meng
- Antoni B. Chan
- Weigang Zhang
affiliations:
- Harbin Institute of Technology (Weihai)
- City University of Hong Kong
- University of Science and Technology of China
- Harbin Institute of Technology Qingdao Research Institute
arxiv_id: '2608.06236'
url: https://arxiv.org/abs/2608.06236
pdf_url: https://arxiv.org/pdf/2608.06236
published: '2026-08-06'
collected: '2026-08-08'
category: Other
direction: 视频目标计数 · RGB-D多模态融合
tags:
- Object Counting
- RGB-D
- Cross-Attention
- Occlusion Handling
- Video Understanding
one_liner: 融合深度特征、RGB-D跨注意力与跨帧去重框架，搭配新数据集提升拥挤场景视频目标计数精度
practical_value: '- 电商直播密集商品/实体计数、线下门店人流统计场景，可借鉴深度+RGB跨注意力方案解决遮挡漏检问题

  - 跨帧序列实体计数类任务可复用其统一去重流水线，降低重复计数误差

  - 多模态目标检测任务可参考其RGB-D特征融合思路，引入额外模态信息提升复杂场景鲁棒性'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有视频目标计数方法仅依赖RGB信息，在拥挤、高遮挡场景下区分能力不足，漏检、重复计数问题严重，无法适配复杂场景下的目标统计需求。

### 方法关键点
1. 提出DG-Det检测器，融合深度特征设计多尺度RGB-D cross-attention模块，新增显式遮挡预测分支，强化空间感知能力；
2. 搭建通用后处理流水线，内置统一跨帧去重逻辑，消除不同帧重复计数误差；
3. 开源包含多类别、深度标注的RGB-D视频目标计数数据集RGBD-VideoCount，支撑后续相关研究。

### 关键结果
相比现有基线方法，MAE下降62.01%，RMSE也取得一致性提升，代码与数据集均已对外开源。
