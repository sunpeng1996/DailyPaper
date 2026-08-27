---
title: Adaptive Hierarchical Representation Alliance for Multimodal Learning
title_zh: 面向多模态学习的自适应分层表征联盟方法
authors:
- Chunlei Meng
- Pengbin Feng
- Jacqueline J. Pang
- Chih-Ting Liao
- Rong Fu
- Zhaolu Kang
- Zhongxue Gan
- Chun Ouyang
affiliations:
- Fudan University
- University of Southern California
- J.P. Morgan Chase
- University of New South Wales
- Peking University
arxiv_id: '2608.22863'
url: https://arxiv.org/abs/2608.22863
pdf_url: https://arxiv.org/pdf/2608.22863
published: '2026-08-24'
collected: '2026-08-27'
category: Multimodal
direction: 多模态学习 · 分层表征融合
tags:
- Multimodal Learning
- Hierarchical Representation
- Expert Framework
- Cross-modal Alignment
- Robustness
one_liner: 提出分层共享-私有专家框架AHRA，解决多模态语义粒度不匹配问题，提升噪声/缺模态场景下模型效果
practical_value: '- 多模态召回/排序场景可复用分层共享-私有专家架构，分别提取文本深语义、视觉/音频浅中层特征，避免细粒度特征损失

  - 可借鉴稀疏控制软门控机制筛选各模态任务相关私有token，降低噪声模态（如用户模糊上传图、背景杂音）对推荐效果的影响

  - 缺模态场景（如商品只有图无文案、用户评价只有文字无晒图）可复用层级共融合模块的跨语义层选择逻辑，提升模型鲁棒性'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有多模态模型默认各模态任务相关信息出现在相同语义深度，仅在最后一层隐空间对齐，经层间CKA分析发现存在语义粒度不匹配问题：文本需要更深层上下文抽象，视觉/音频的区分性感知信息多在浅中层，易造成细粒度私有特征丢失，噪声、缺模态场景下可靠性差。

### 方法关键点
AHRA为分层共享-私有专家框架，每个模态在不同语义层级拆分共享、私有流，分别用共享对齐、私有去相关正则约束；跨模态专家路由共享信息，稀疏控制软门控（前景检测）引导模态专属专家增强任务相关私有token；层级共融合模块完成层内专家协同、层间语义选择。

### 关键结果
在图文分类、多模态意图识别、三模态情感分析共6个基准数据集上效果一致超过强基线，噪声、缺模态场景下鲁棒性显著提升。
