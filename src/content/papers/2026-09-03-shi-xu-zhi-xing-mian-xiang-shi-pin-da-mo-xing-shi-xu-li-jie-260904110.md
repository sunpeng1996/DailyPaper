---
title: 'The Shape of Time: Video-Token Contrast for Temporal Understanding in VideoLMs'
title_zh: 时序之形：面向视频大模型时序理解的视频Token对比方法
authors:
- Yumeng Shi
- Quanyu Long
- Yin Wu
- Wenya Wang
affiliations:
- Nanyang Technological University
arxiv_id: '2609.04110'
url: https://arxiv.org/abs/2609.04110
pdf_url: https://arxiv.org/pdf/2609.04110
published: '2026-09-03'
collected: '2026-09-05'
category: Training
direction: 多模态大模型 · 时序理解训练优化
tags:
- VideoLM
- Contrastive Learning
- Temporal Understanding
- Counterfactual Training
- Representation Learning
one_liner: 提出无需修改架构的视频Token对比训练目标VT-Contrast，增强VideoLM时序表示能力
practical_value: '- 短视频推荐、直播内容理解等时序敏感的多模态业务场景，可直接复用该对比训练思路，无需修改原有模型架构，在现有训练流程中新增时序反例对比损失即可提升时序语义理解准确率

  - 电商商品教程视频理解、用户行为序列建模等涉及事件顺序识别的场景，可借鉴Kendall tau距离量化时序差异的方法，给不同混乱程度的反例分配不同权重，优化对比损失效果

  - 多模态大模型微调时，可优先选择高层最后一帧的Token施加监督信号，能以极低的额外计算成本强化时序信息融合效果，兼顾性能与训练效率'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有VideoLM仅针对生成文本做监督，未直接约束视频Token表征的时序属性，模型易依赖对象、场景、语言先验等捷径输出时序相关答案，无法真正捕获事件的时序演进规律，在需要区分顺序相反的相似事件（如开门/关门、组装/拆卸）时表现不佳。
### 方法关键点
1. 提出表征级时序反事实训练目标VT-Contrast，无需修改模型架构，兼容各类VideoLM训练任务；
2. 选择高层网络的最后一帧视频Token作为监督位置，此时序信息已完成融合且未进入语言生成阶段，监督效率更高；
3. 构建对比学习对：将时序保留的正样本与同视频重排的反例做对比，用Kendall tau距离量化时序差异并给反例分配权重，优化对比损失。
### 关键结果
跨多个公开时序理解基准测试集，实现VideoLM时序理解性能的全面提升
