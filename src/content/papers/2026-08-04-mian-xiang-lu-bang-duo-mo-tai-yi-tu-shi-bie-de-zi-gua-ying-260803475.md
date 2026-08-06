---
title: Adaptive Modality Reliability Diagnosis and Restoration for Robust Multimodal
  Intent Recognition
title_zh: 面向鲁棒多模态意图识别的自适应模态可靠性诊断与修复
authors:
- Suraj Kumar
- Mohnish Raj
- Soumi Chattopadhayay
- Chandranath Adak
- Ayan Dutta
arxiv_id: '2608.03475'
url: https://arxiv.org/abs/2608.03475
pdf_url: https://arxiv.org/pdf/2608.03475
published: '2026-08-04'
collected: '2026-08-06'
category: Multimodal
direction: 多模态意图识别 · 鲁棒性优化
tags:
- Multimodal Intent Recognition
- Modality Robustness
- Multimodal Fusion
- Uncertainty Estimation
- Representation Restoration
one_liner: 提出PRIME闭环框架，通过模态诊断修复重评估实现鲁棒多模态意图识别
practical_value: '- 多模态用户意图理解场景（如直播导购、短视频评论意图识别）可复用PRIME的样本级模态可靠性诊断逻辑，基于预测置信度、跨模态一致性等指标量化单模态质量，避免直接丢弃噪声模态

  - 缺失/噪声模态修复可借鉴原型条件变分修复模块的设计思路，用可靠模态的信息补全退化模态表征，提升低质量输入下的意图识别准确率

  - 无模态可靠性标注的场景下，可参考「人工构造不同程度模态退化样本+异方差不确定性目标」的方式训练可靠性评估器，降低标注成本'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
多模态意图识别融合文本、语音、视觉信号时，常遇到单模态噪声、缺失、语义冲突、模态占比失衡问题，现有方法仅隐式加权或抑制不可靠模态，未考虑退化模态的可修复性与修复后的可信度。
### 方法关键点
PRIME闭环框架实现样本级模态诊断、修复、重评估全流程：1）通过预测置信度、认知分歧、跨模态一致性、特征退化度四类互补特征，计算每个模态的上下文对数方差表征退化程度；2）无可靠性标注场景下，通过人工构造已知退化程度的模态损坏样本，结合异方差不确定性目标训练可靠性评估器；3）用退化程度控制原型条件变分修复模块，基于互补模态重构退化表征，修复后重新评估可靠性，最终采用逆方差加权完成多模态融合。
### 关键结果
在多模态意图识别基准上，干净数据下性能保持主流水平，在模态缺失、噪声、冲突、失衡场景下鲁棒性显著提升。
