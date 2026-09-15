---
title: 'AlayaVista: Streaming World Modeling from Panoramic States to Perspective
  Video'
title_zh: AlayaVista：从全景状态到透视视频的流式世界建模
authors:
- Jiaming Tan
- Mingliang Zhai
- Zhen Li
- Yuwei Wu
- Chuanhao Li
- Kaipeng Zhang
affiliations:
- Alaya Lab
- Beijing Institute of Technology
- The University of Tokyo
arxiv_id: '2609.14462'
url: https://arxiv.org/abs/2609.14462
pdf_url: https://arxiv.org/pdf/2609.14462
published: '2026-09-12'
collected: '2026-09-15'
category: Other
direction: 流式视频世界建模 · 全景-透视视图生成
tags:
- WorldModel
- PanoramicVideo
- StreamingGeneration
- VideoSynthesis
- 3DScene
one_liner: 提出解耦全景演化与透视生成的可控流式视频世界模型，配套1318小时4K全景数据集MUGEN
practical_value: '- 电商虚拟逛街、AR试逛场景可借鉴全景状态+按需透视渲染的架构，降低实时渲染算力开销

  - 多视角商品内容生成可复用全景预训练+局部视图精修的Pipeline，降低多视角素材采集成本

  - 流式内容生成场景可参考分块自回归生成+少步蒸馏的优化方案，降低端到端延迟'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有交互式视频世界模型存在表征权衡：透视视图模型仅处理局部视角，长序列推理易丢失屏外内容；全景/显式3D方案算力开销高，难以兼顾低延迟、高画质与全局场景一致性。

### 方法关键点
提出AlayaVista架构，解耦全景场景演化与透视视图生成流程：
1. 输入单张透视图像，用预训练全景扩展模型生成360度场景先验，将场景演化建模为相机条件的全景隐状态迭代；
2. 隐式视口渲染器将全景隐状态映射为请求的透视视频隐向量，再经透视精修模块完成去伪影、超分；
3. 适配分块自回归生成，对全景生成、透视精修做少步蒸馏适配流式输出；配套构建MUGEN数据集，含1318小时≥4K分辨率真实全景视频，带语义/几何标注。

### 关键结果
在画质、相机可控性、长时序稳定性、端到端流式效率上均优于基线方案，平衡了空间覆盖度、输出质量与计算效率
