---
title: 'ArmorOCR: Grounded Adversarial Visual Perception via Observation-Transferred
  Self-Distillation'
title_zh: ArmorOCR：基于观测迁移自蒸馏的接地对抗视觉感知OCR方法
authors:
- Linhan Cao
- Siyuan Li
- Jun Lan
- Liangbo He
- Guannan Li
- Xiaolei Huang
- Jun Jia
- Shuheng Zhou
- Huijia Zhu
- Weiqiang Wang
affiliations:
- Ant Group
- Shanghai Jiao Tong University
- East China Normal University
arxiv_id: '2608.20122'
url: https://arxiv.org/abs/2608.20122
pdf_url: https://arxiv.org/pdf/2608.20122
published: '2026-08-20'
collected: '2026-08-21'
category: Multimodal
direction: 多模态大模型 · 鲁棒OCR感知优化
tags:
- LMM
- OCR
- Adversarial Robustness
- Self-Distillation
- Benchmark
one_liner: 构建首个接地对抗OCR基准AdvSpot，提出两阶段训练框架提升多模态模型对抗OCR鲁棒性
practical_value: '- 电商场景商品图、广告图的异形艺术字、干扰纹理文本识别可复用OPSD自蒸馏方案，无需额外标注即可提升异形文本识别准确率

  - 多模态Agent的视觉文本感知模块可接入ArmorOCR两阶段训练流程，提升复杂海报、宣传物料的OCR鲁棒性

  - 业务侧对抗OCR效果验证可直接复用AdvSpot基准的13类对抗文本类型，搭建自有场景的鲁棒性评测集

  - 涉及多任务对齐的OCR优化可复用GRPO带任务条件奖励的强化学习方案，同时兼顾定位、识别等多指标平衡'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
多模态大模型（LMM）原生OCR能力对人类可识别但带干扰的对抗视觉文本（如艺术字、纹理干扰字）识别、定位准确率极低，现有OCR基准无覆盖对抗场景的区域级标注评测集，无法系统性评估和优化鲁棒性。

### 方法关键点
1. 构建AdvSpot基准：含390张带区域级标注的对抗OCR图像，覆盖5大类13细类对抗文本类型，是首个接地对抗OCR评测基准
2. 提出ArmorOCR两阶段训练框架：第一阶段用On-Policy Self-Distillation（OPSD）从增强变换后的特权观测中蒸馏对抗OCR感知能力；第二阶段用带定位、识别、全匹配、VQA多任务条件奖励的Group Relative Policy Optimization（GRPO）优化接地OCR感知能力

### 关键结果
在AdvSpot、其他对抗OCR基准、通用OCR基准上均实现稳定提升：对抗OCR感知能力显著提升的同时，通用OCR能力保持行业竞争力
