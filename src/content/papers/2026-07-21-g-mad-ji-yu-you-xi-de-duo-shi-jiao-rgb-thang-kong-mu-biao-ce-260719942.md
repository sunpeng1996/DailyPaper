---
title: 'G-MAD: A Game-Based Data Generation Framework for Multi-View RGB-T Aerial
  Object Detection'
title_zh: G-MAD：基于游戏的多视角RGB-T航空目标检测数据生成框架
authors:
- Yechan Kim
- JongHyun Park
- Dongho Yoon
- Namhoon Jung
- Moongu Jeon
affiliations:
- LIG Defense&Aerospace
- GIST
arxiv_id: '2607.19942'
url: https://arxiv.org/abs/2607.19942
pdf_url: https://arxiv.org/pdf/2607.19942
published: '2026-07-21'
collected: '2026-07-27'
category: Other
direction: 航空目标检测 · 合成数据生成
tags:
- Synthetic Data Generation
- Object Detection
- RGB-T
- Multi-View
- Dataset Benchmark
one_liner: 基于Arma3游戏构建开源多视角RGB-T航空检测数据生成框架，配套发布大规模基准数据集AMOD
practical_value: '- 稀缺场景数据不足时可借鉴游戏引擎可控生成合成数据的方案，补充训练样本

  - 多模态数据对齐标注成本高的场景可复用引擎级元数据自动标注的思路，降本增效

  - 做可控数据生成时可参考其结构化场景参数配置的设计，覆盖更多边界case'
score: 3
source: huggingface-daily
depth: abstract
---

### 动机
真实航空目标检测数据集存在三大核心缺陷：视角控制能力有限、RGB-T多模态对齐效果差、人工标注成本极高，无法支撑视角变化、多模态融合、合成到真实迁移等方向的可控研究。
### 方法关键点
1. 基于Arma3游戏引擎构建开源G-MAD框架，支持全流程结构化场景参数配置，覆盖资产类别、数量、天气、时间、相机参数、视角采样策略等维度
2. 支持可控多视角相机放置，同步采集可见光/红外对齐数据
3. 直接调用引擎层几何元数据自动生成边界框标注，完全无需人工参与
### 关键结果
基于G-MAD构建并开源了大规模多视角航空RGB-T目标检测基准数据集AMOD，框架代码及数据集已全部对外开放。
