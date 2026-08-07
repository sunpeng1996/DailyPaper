---
title: 'EmoWorld: A Decoupled Affective Field for Controllable Emotional Video Generation'
title_zh: EmoWorld：面向可控情绪视频生成的解耦情感场框架
authors:
- Bingyuan Wang
- Baistan Zhyldyzbekov
- Kunyu Feng
- Zeyu Wang
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- The Hong Kong University of Science and Technology
arxiv_id: '2608.06231'
url: https://arxiv.org/abs/2608.06231
pdf_url: https://arxiv.org/pdf/2608.06231
published: '2026-08-06'
collected: '2026-08-07'
category: Multimodal
direction: 多模态生成 · 可控情绪视频生成
tags:
- Video Generation
- Diffusion Model
- Controllable Generation
- Emotion Steering
- DiT
one_liner: 基于冻结Video DiT实现情绪三要素解耦控制，无需微调即可跨多主干适配多种生成场景
practical_value: '- 冻结大模型+解耦控制向量注入的架构可复用在电商商品/广告素材的可控风格生成场景，无需微调底座大幅降低成本

  - 一次性预提取属性方向+可复用cue库的预处理流程，可迁移到营销文案/素材的多风格（如喜庆、高级感）批量生成

  - 多控制模块独立可调的设计思路，可借鉴到推荐系统多目标（如点击率、情绪种草度）解耦优化，规避目标冲突'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视频生成器将全局氛围、情感语义线索、时间演进三类情感要素耦合在单一文本条件中，无法实现精细化可控情绪调整，无法满足营销内容、交互场景创作的定制化需求。
### 方法关键点
基于冻结的Flow-Matching Video DiT构建EmoWorld框架：
1. 一次性准备阶段：从几何保持一致的中性/情绪编辑全景图中提取层专属情绪方向与可复用线索库
2. 推理阶段：通过三个独立模块实现控制：VAS向隐状态注入氛围方向，SAS提取可独立缩放的prompt残差处理语义线索，TAS跨去噪与时间维度插值残差场控制情绪演进
### 关键结果
在Wan2.2底座上，VAS将目标情绪对齐度提升19%、时间波动降低48%；SAS将情绪对齐度提升37%、情感线索检出率提升36%；TAS将过渡单调性提升15%；支持27类情绪、文生视频/图生视频场景，可跨多Video DiT底座迁移，无需更新参数即可支持相机条件合成。
