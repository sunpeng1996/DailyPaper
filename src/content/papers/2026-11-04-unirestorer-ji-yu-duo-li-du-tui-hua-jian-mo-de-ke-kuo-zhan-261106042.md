---
title: 'UniRestorer++: Scalable Universal Image Restoration with Multi-Granularity
  Degradation Modeling'
title_zh: UniRestorer++：基于多粒度退化建模的可扩展通用图像修复框架
authors:
- Jingbo Lin
- Zhilu Zhang
- Fan Li
- Renjing Pei
- Wenbo Li
- Hang Xu
- Hongzhi Zhang
- Wangmeng Zuo
arxiv_id: '2611.06042'
url: https://arxiv.org/abs/2611.06042
pdf_url: https://arxiv.org/pdf/2611.06042
published: '2026-11-04'
collected: '2026-11-06'
category: Multimodal
direction: 多模态图像修复 · MoE分层路由优化
tags:
- MoE
- Image Restoration
- Multi-Granularity Routing
- OOD Generalization
- Benchmark
one_liner: 提出多粒度退化建模的可扩展图像修复框架，效果优于vanilla MoE，覆盖50类退化场景
practical_value: '- 多粒度分层MoE路由思路可迁移至多场景推荐/广告排序，通过分层路由平衡场景专业化与OOD鲁棒性，缓解多目标优化冲突

  - 分层场景组+专属专家的扩容策略可复用在多模态内容理解模型扩容，避免单纯加宽加深backbone带来的性能饱和问题

  - 区域感知路由逻辑可借鉴到电商主图瑕疵修复、商品图像质量优化等业务场景，实现非均匀损伤的分区域精准处理'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
通用图像修复单模型需覆盖多种退化场景，现有单纯加宽加深backbone易出现性能饱和，退化感知方法依赖精准退化估计，OOD/真实场景下估计误差会导致效果骤降，缺乏可靠的规模化扩容策略。

### 方法关键点
1. 构建多粒度退化层级，逐层细化退化组并配置专属修复专家，将模型容量扩容与退化场景专业化绑定；2. 双路由机制：退化估计路由选择层级内根到叶路径，粒度估计路由选择路径内对应层级，平衡细粒度专业化与退化估计误差鲁棒性；3. 空间稠密退化表示支持区域感知路由，适配空间非均匀的退化场景；4. 构建CDD-50基准，覆盖单退化到5种组合退化共50类场景。

### 关键结果数字
模型扩容时PSNR呈近似对数线性增长，OOD/真实数据扩容收益远超vanilla MoE，在全量基准上达到SOTA，具备真实图像零样本泛化、少样本迁移能力。
