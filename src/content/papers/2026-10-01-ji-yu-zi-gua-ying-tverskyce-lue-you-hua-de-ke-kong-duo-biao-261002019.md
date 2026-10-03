---
title: Controllable Multi-label Video Safety Detection via Adaptive Tversky Policy
  Optimization
title_zh: 基于自适应Tversky策略优化的可控多标签视频安全检测
authors:
- Guangyu Yang
- Jingbiao Mei
- Mingsheng Sun
- Jinghong Chen
- Yingtong Bu
- Pengda Qin
- Da Chen
- Bill Byrne
affiliations:
- University of Cambridge
- Xiaohongshu Inc.
- AntGroup
- Tencent Company, China
- University of Bath
arxiv_id: '2610.02019'
url: https://arxiv.org/abs/2610.02019
pdf_url: https://arxiv.org/pdf/2610.02019
published: '2026-10-01'
collected: '2026-10-03'
category: Other
direction: 多模态视频内容审核 · 训练优化
tags:
- VLM
- Reinforcement Learning
- Multi-label Classification
- Content Moderation
- Precision-Recall Tradeoff
one_liner: 提出自适应Tversky策略优化框架，实现多标签视频安全检测的可控精度-召回权衡
practical_value: '- 电商短视频/直播内容审核场景可复用ATPO的多标签建模思路，替代现有二元分类方案，同时识别多种违规类型

  - 不同违规类别可通过ATR动态调整FP/FN惩罚权重，满足差异化的精度/召回要求，比如高危违规优先保障召回，低危违规优先保障精度

  - 自适应奖励函数设计思路可迁移到推荐多目标优化场景，实现不同业务目标权重的动态调整'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
短视频社交平台快速发展，用户接触有害内容概率大幅提升；现有视频安全检测方案普遍将任务简化为二元分类，忽略违规内容天然的多标签属性，且静态训练目标无法适配不同审核管线、不同违规类别差异化的精度-召回权衡需求。
### 方法关键点
提出基于强化学习的多标签视频安全检测框架ATPO，设计自适应Tversky奖励（ATR）机制，训练过程中动态调整假阳性、假阴性的惩罚权重，支持可控的精度-召回trade-off。
### 关键结果
在SafeWatch-Bench、XD-Violence数据集上取得显著多标签性能提升，SafeWatch-Bench-Real数据集Jaccard Index从40.66提升至75.44；可灵活调整精度-召回工作点，适配异构部署场景的策略要求。
