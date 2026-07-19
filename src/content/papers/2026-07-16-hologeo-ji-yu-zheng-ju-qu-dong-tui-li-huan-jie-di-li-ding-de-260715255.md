---
title: 'HoloGeo: Mitigating Landmark Bias in Geo-localization via Evidence-Driven
  Reasoning'
title_zh: HoloGeo：基于证据驱动推理缓解地理定位中的地标偏差
authors:
- Pengcheng Zhou
- Xuanyu Liu
- Yanchen Yin
- Bobo Li
- Shengqiong Wu
- Mong-Li Lee
- Wynne Hsu
affiliations:
- National University of Singapore
- Shandong University of Science and Technology
- University of Oxford
arxiv_id: '2607.15255'
url: https://arxiv.org/abs/2607.15255
pdf_url: https://arxiv.org/pdf/2607.15255
published: '2026-07-16'
collected: '2026-07-19'
category: Multimodal
direction: 多模态推理 · 视觉偏差缓解
tags:
- VLM
- Bias Mitigation
- Multimodal Reasoning
- Geo-localization
- Reinforcement Learning
one_liner: 提出地标偏差量化指标与评测基准，构建证据驱动推理框架提升地理定位鲁棒性
practical_value: '- 可借鉴BI/BH偏差量化指标的设计逻辑，度量推荐场景中热门item、头部商家带来的bias对排序模型的影响

  - 多维度奖励引导模型均衡关注多源特征的思路，可用于缓解推荐系统马太效应，避免模型依赖头部特征产生伪相关

  - 可参考LandmarkBias-3K的构建逻辑，构造推荐系统特定bias的测试集，量化模型鲁棒性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前VLM驱动的图像地理定位方案普遍存在地标偏差，易忽略非地标类地理特征、产生伪相关，导致定位精度下降，且缺乏统一的偏差量化与评测基准。
### 方法
1. 设计Bias Intensity (BI)、Bias Harmfulness (BH)两个量化指标，刻画地标特征对模型推理的影响，同时构建LandmarkBias-3K专用偏差评测基准；
2. 基于标注了结构化无偏多证据推理链的BF-30K数据集，提出HoloGeo证据驱动推理框架，通过多维度奖励引导模型均衡关注多元视觉特征，实现多证据联合推理。
### 结果
在IM2GPS3K、YFCC4K通用基准上保持优秀性能的同时，在LandmarkBias-3K上的表现显著优于现有开源VLM，验证了其地理空间推理的鲁棒性。
