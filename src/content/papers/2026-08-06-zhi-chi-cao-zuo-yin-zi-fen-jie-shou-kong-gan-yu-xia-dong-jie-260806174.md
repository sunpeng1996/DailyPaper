---
title: 'Support Operation Factorization: Compositional Readout of Frozen Vision Encoders
  under Controlled Interventions'
title_zh: 支持操作因子分解：受控干预下冻结视觉编码器的组合读出
authors:
- Zhongyao Wang
- Wanli Ouyang
- Taoyong Cui
- Pheng Ann Heng
affiliations:
- Fudan University
- MMLab, The Chinese University of Hong Kong
- Department of Computer Science and Engineering, The Chinese University of Hong Kong
arxiv_id: '2608.06174'
url: https://arxiv.org/abs/2608.06174
pdf_url: https://arxiv.org/pdf/2608.06174
published: '2026-08-06'
collected: '2026-08-08'
category: Multimodal
direction: 多模态 · 冻结视觉编码器组合分析
tags:
- Frozen Vision Encoder
- Compositional Analysis
- Factorization
- Evaluation Protocol
- Disentanglement
one_liner: 提出SO-OPF因子分解读出与单射对齐评估协议，解决冻结视觉编码器组合分析的操作混淆问题
practical_value: '- 多模态商品属性拆解场景可借鉴SO-OPF因子分解思路，规避同一语义槽被多个属性复用的混淆问题，提升属性识别准确率

  - 多模态特征可解释性评估可复用单射对齐留一协议，更精准衡量属性与图像空间位置的绑定效果

  - 商品主图编辑操作（改色、换背景等）的语义识别场景，可直接适配该读出方法，同时提升操作类型与修改位置的识别精度'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
冻结视觉编码器的组合分析需同时识别变化内容与位置，传统因子探针单独对两个维度评分，存在同一预测槽被多个操作复用的「操作洗白」缺陷，聚合评分也混淆了已知网格下的绑定组合能力、平标签下的网格恢复能力两类任务目标。
### 方法关键点
1. 设计基于support×operation网格的单射对齐留一单元评估协议
2. 提出SO-OPF读出方法，将单元能量分解为support salience与竞争性操作后验，实现两个维度完全解耦
### 关键结果
基于冻结DINOv3特征，已知因子分配在Shapes3D-Extended上单射准确率达0.874，全局图像不相交COCO数据集达0.799；平标签下学习分配准确率分别为0.769、0.762；Shapes3D匹配轴感知监督下，比稠密载体的学习分配准确率从0.653提升至0.841，完全消除操作洗白gap；MuJoCo场景下存在性能边界，DINOv3准确率仅0.569，SigLIP2为0.484，存在明显槽坍塌。
