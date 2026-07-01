---
title: Trimming the Long-Tail of Visual World Modeling Evaluation
title_zh: TailOR：面向视觉世界建模评估的长尾场景评测基准
authors:
- Bingxuan Li
- Yining Hong
- Cheng Qian
- Hyeonjeong Ha
- Jiateng Liu
- Zhenhailong Wang
- Yue Guo
- Yunzhu Li
- Heng Ji
affiliations:
- University of Illinois Urbana-Champaign
- Stanford University
- Columbia University
arxiv_id: '2606.24256'
url: https://arxiv.org/abs/2606.24256
pdf_url: https://arxiv.org/pdf/2606.24256
published: '2026-06-22'
collected: '2026-07-01'
category: Eval
direction: 多模态世界模型评测 · 长尾场景
tags:
- Benchmark
- Long-tail Evaluation
- Visual World Model
- Multimodal Reasoning
- Physical Interaction
one_liner: 发布覆盖三类物理交互场景的Tailor-Bench，量化现有视觉世界模型的长尾泛化能力缺陷
practical_value: '- 多模态生成场景（如电商商品宣传视频/AR展示内容生成）可复用三级场景设计框架，分层验证模型在非常规/违背常识场景下的生成合规性，降低错误内容上线风险

  - 多模态导购Agent的物理推理能力评测可借鉴该基准的任务设计逻辑，区分模型是靠记忆答对还是真正理解物理规则，避免给用户输出错误的商品使用/搭配建议

  - 推荐系统的长尾效果评测可迁移该基准的分布偏移性能测试方法，量化头部热门item到冷门小众item的召回/排序性能衰减幅度，定位长尾优化方向'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视觉世界模型（图像/视频生成）仅在常见物理交互场景下表现优异，缺少稀有/违背约束的长尾场景评测维度，无法验证模型是真正掌握物理规则，还是仅拟合表层视觉模式。
### 方法关键点
提出Tailor-Bench评测基准，设计三级递进难度场景：1）Regular：常规工具-任务对，测试基础能力；2）Unconventional：替换为属性兼容的非常规工具，测试功能泛化能力；3）Impossible：使用属性违反的工具，测试约束感知能力。同时设置预测生成、描述生成两种任务范式，统一评测协议。
### 关键结果
现有模型性能从Regular到Unconventional、Impossible场景大幅衰减，图像模型核心缺陷是状态变化生成错误，视频模型额外存在时序一致性问题，证明当前模型物理规则泛化能力严重不足。
