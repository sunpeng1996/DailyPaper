---
title: 'VocaDet: Sample-Driven Open-Vocabulary Object Detection and Segmentation via
  Visual Tokenization and Vector Database Retrieval'
title_zh: VocaDet：基于视觉Token化与向量库的样本驱动开放词汇目标检测分割
authors:
- ZhiXin Sun
affiliations:
- PowerChina Zhongnan Engineering Corporation Limited
arxiv_id: '2607.08541'
url: https://arxiv.org/abs/2607.08541
pdf_url: https://arxiv.org/pdf/2607.08541
published: '2026-07-09'
collected: '2026-07-10'
category: Multimodal
direction: 多模态 · 开放词汇目标检测优化
tags:
- Open-Vocabulary Detection
- Visual Tokenization
- Vector Database
- DINOv3
- Image Segmentation
one_liner: 提出无需重训的样本驱动开放词汇检测分割框架，通过视觉Token与向量库实现可扩展识别
practical_value: '- 电商搜图、货架巡检、直播商品识别场景可复用「连续视觉特征转多粒度离散视觉Token+向量数据库存储」架构，无需重训即可快速新增商品类目识别能力

  - 固定摄像头场景（如线下门店监控、直播间画面捕捉）可直接复用背景过滤机制，剔除高频冗余背景模式，降低检索开销提升推理效率

  - 样本驱动的动态类目扩展方案可迁移到智能Agent的视觉感知模块，无需微调大模型即可支持动态新增自定义识别目标'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有开放词汇目标检测分割方法依赖文本prompt、有限视觉样本或高开销特征匹配流程，难以扩展到规模持续增长的目标库。
### 方法关键点
1. 采用DINOv3作为视觉特征提取器，用自适应敏感度的凝聚式聚类生成多粒度视觉Token，结合去偏位置表示、空间拓扑信息存入向量数据库作为可扩展目标记忆库
2. 推理阶段将查询图像转换为视觉Token，与库中存储的目标记忆高效匹配完成目标定位与分割
3. 新增背景过滤机制，剔除固定摄像头场景下的高频背景模式，减少冗余检索操作
### 关键结果
在UA-DETRAC数据集上无需传统检测器训练即可实现有效开放词汇检测性能，支持随正负样本积累持续扩展识别能力。
