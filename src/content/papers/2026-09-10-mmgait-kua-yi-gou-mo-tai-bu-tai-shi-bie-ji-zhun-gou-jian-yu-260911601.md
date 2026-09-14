---
title: 'MMGait: Benchmarking and Unifying Gait Recognition across Heterogeneous Modalities'
title_zh: MMGait：跨异构模态步态识别基准构建与统一框架
authors:
- Saihui Hou
- Chenye Wang
- Qingyuan Cai
- Aoqi Li
- Yongzhen Huang
arxiv_id: '2609.11601'
url: https://arxiv.org/abs/2609.11601
pdf_url: https://arxiv.org/pdf/2609.11601
published: '2026-09-10'
collected: '2026-09-14'
category: Multimodal
direction: 多模态识别 · 跨模态统一建模
tags:
- Multimodal
- Cross-Modal Retrieval
- Benchmark
- Multi-Modal Fusion
- Unified Modeling
one_liner: 构建覆盖5类异构模态的步态识别基准MMGait，提出支持任意模态组合的统一识别框架OmniGait++
practical_value: '- 多模态商品召回/表征场景可复用「模态专属前端+共享ID编码器」架构，降低多模态任务适配成本

  - 异构模态融合场景可借鉴anchor-guided fusion思路，无需严格模态对齐即可支持任意数量模态输入

  - 跨模态检索任务评测可参考impostor-augmented协议，提升评测结果鲁棒性'
score: 3
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有步态识别研究以RGB为核心，无法覆盖步行行为的异构光度、几何、运动多维度特征，且不同模态、模态配对、融合配置需单独训练模型，扩展性差。
### 方法关键点
1. 构建大规模多传感器基准MMGait，序列级对齐可见光、红外、深度、LiDAR、雷达5类模态数据，覆盖外观、轮廓、几何、运动、人体结构多维度特征；
2. 提出统一步态识别框架OmniGait++，采用模态专属前置网络+共享身份编码器结构，通过anchor引导的融合模块聚合任意数量模态，无需帧级同步，单个checkpoint覆盖单模态、跨模态、多模态三类识别任务。
### 关键结果
OmniGait++在多数通用场景下性能与任务专属专家模型持平，可扩展支持固定配对模型无法实现的多模态高基数融合，验证了异构模态下统一识别的可行性。
