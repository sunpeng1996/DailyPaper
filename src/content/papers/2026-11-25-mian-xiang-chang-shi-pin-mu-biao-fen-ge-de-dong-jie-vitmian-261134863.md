---
title: 'Focus Only on What''s Important: Training-Free Focus Maps for Frozen Vision
  Transformers in Long-Video Object Segmentation'
title_zh: 面向长视频目标分割的冻结ViT免训练聚焦映射方法
authors:
- Harsha Karipineni
- Rajesh Reddy Chintha
affiliations:
- Independent Researcher
arxiv_id: '2611.34863'
url: https://arxiv.org/abs/2611.34863
pdf_url: https://arxiv.org/pdf/2611.34863
published: '2026-11-25'
collected: '2026-11-27'
category: Other
direction: 长视频分割 · 冻结ViT免训练优化
tags:
- VisionTransformer
- VideoSegmentation
- Training-Free
- TokenMerging
- ComputationOptimization
one_liner: 提出免训练动态聚焦映射策略，在极小精度损失下降低长视频分割场景冻结ViT的计算开销
practical_value: '- 动态算力分配思路可迁移到生成式推荐/多模态内容理解场景：仅对高价值对象（如用户感兴趣的商品、核心query语义单元）保留全精度计算，非核心区域执行降采样/Token合并降本

  - 免训练适配冻结大模型的策略可复用：无需微调基座即可实现计算优化，避免业务场景下微调基座的数据成本与效果波动风险

  - 工程优化可参考其验证逻辑：算力优化不能仅看理论FLOPs下降，必须端到端测试包含启动、稳态全链路的实际延迟收益

  - 动态优先级调度逻辑可迁移到Agent感知模块：仅对环境中高关注度目标保留全量特征计算，降低边缘侧Agent的感知算力开销'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
冻结ViT作为视觉编码器在长视频目标分割任务中精度优异，但计算开销高；现有免训练Token合并策略全局统一降采样，会丢失跟踪目标的关键特征，长视频下快速运动场景效果暴跌。
### 方法关键点
免训练聚焦映射策略对分割模型预测的目标区域保留全分辨率Token，非目标区域执行粗粒度合并；通过速度偏移+块匹配的掩码联合预测、相机补偿异常检测，解决长视频下目标快速运动出框的丢失问题，无目标时回退到通用合并策略。
### 关键结果
LVOS V2验证集上，ViT-S配置下比ALGM 0.98高2.76 J&F，编码器FLOPs降低16%，仅比全量编码器低1.0 J&F；ViT-B配置下比ALGM 0.95高3.89 J&F；DAVIS 2017验证集上精度仅比全量编码器低0.19（ViT-S）/0.12（ViT-B）J&F；稳态实际延迟降低3%-8%。
