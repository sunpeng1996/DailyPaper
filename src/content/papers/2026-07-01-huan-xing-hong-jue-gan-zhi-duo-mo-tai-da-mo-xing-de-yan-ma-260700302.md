---
title: Wake up for Touch! Mask-isolated Tactile Alignment Learning in MLLMs
title_zh: 唤醒触觉感知：多模态大模型的掩码隔离触觉对齐学习
authors:
- Yoonhyung Park
- Minji Kim
- Sungwon Moon
- Jiyoung Lee
affiliations:
- Ewha Womans University
arxiv_id: '2607.00302'
url: https://arxiv.org/abs/2607.00302
pdf_url: https://arxiv.org/pdf/2607.00302
published: '2026-07-01'
collected: '2026-07-04'
category: Multimodal
direction: 多模态大模型 · 模态扩展与对齐
tags:
- MLLM
- Multimodal Alignment
- Catastrophic Forgetting
- Modality Expansion
- Parameter Efficient Tuning
one_liner: 提出参数分区的Splash框架，为MLLM无推理开销新增触觉模态且不遗忘原有能力
practical_value: '- 多模态扩展场景可复用参数空间分区思路：量化预训练参数重要度，冻结核心参数、仅更新休眠参数做新模态对齐，避免灾难性遗忘，无需新增LoRA等组件带来额外推理开销

  - 电商商品属性建模可借鉴逻辑：对仅靠视觉难以区分的材质属性（如面料柔软度、表面防滑性），可结合触觉数据做多模态对齐，提升商品属性打标、选品推荐的准确率

  - 模态扩展时优先选择无推理开销的参数更新方案，避免部署阶段算力成本上升，适配高并发的推荐/搜索业务场景'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
MLLM新增触觉模态时存在零和权衡：小参数模型预算有限，要么牺牲原有视觉语言推理能力学习触觉感知，要么保留原有能力但触觉效果差，且易出现灾难性遗忘。
### 方法关键点
1. 提出Splash掩码隔离触觉对齐框架，先量化每个预训练参数的重要度，将参数空间划分为休眠子空间和关键子空间
2. 冻结关键子空间锚定原有通用视觉知识，仅更新隔离的休眠子空间完成触觉与LLM的对齐，无需新增推理组件
### 关键结果
在SSVTP、TVL、TacQuad等视觉触觉基准上取得SOTA性能，LLM部分无额外推理开销，同时完全保留原有通用能力
