---
title: Visual Grounding in Zero-Shot Vision-Language Control
title_zh: 零样本视觉语言控制中的视觉对齐（Visual Grounding）能力研究
authors:
- J. de Curtò
- Dayani Plasencia
- Diego Sánchez
- I. de Zarzà
affiliations:
- Barcelona Supercomputing Center
- Universidad Pontificia Comillas
- University of Florida
- University of Illinois Urbana-Champaign
- Luxembourg Institute of Science and Technology
arxiv_id: '2608.06154'
url: https://arxiv.org/abs/2608.06154
pdf_url: https://arxiv.org/pdf/2608.06154
published: '2026-08-06'
collected: '2026-08-08'
category: Multimodal
direction: 多模态VLM · 零样本控制视觉对齐评估
tags:
- VLM
- Visual Grounding
- Zero-shot Control
- Multimodal Evaluation
- Robustness
one_liner: 设计输入消融测试集评估VLM零样本控制的视觉对齐能力，提出对称共识守卫提升决策鲁棒性
practical_value: '- 多模态Agent感知对齐能力评估可复用输入消融方案，通过盲输入、对称翻转、重复输入等测试，快速筛除不依赖感知的虚假高性能模型

  - 多模态决策场景可借鉴对称共识守卫机制，对原始/翻转视图等对称输入做投票校验，大幅降低决策幻觉，提升鲁棒性

  - 多模态系统优先做模块化验证而非端到端黑盒测试，先确认感知模块的输入-输出一致性再串联决策模块，可快速定位问题'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
VLMs被大量用作零样本控制器，但高决策得分可能来自模拟器动态、保守动作先验而非真实视觉感知，缺乏有效评估视觉对齐能力的方案。
### 方法关键点
设计包含盲图像控制、重复输入、车道轴翻转、非视觉基线、管线完整性检查的输入消融测试集，覆盖9个直接动作模型、6个结构化本地VLM、1个VLM-MPC层级架构，在2种实体、3个模拟器下分析32874次带评分调用。后处理阶段设计泄漏可控的对称共识守卫，基于16帧校准数据筛选模型，对原始/翻转视图做2/4 hazard投票。
### 关键结果
直接控制模型表现整体不佳，恒定慢行策略优于脚本几何控制器，无本地VLM满足纵向+横向视觉对齐标准。对称共识守卫在272个留出帧上达0.954平衡准确率，弃权平局场景下覆盖度0.824时平衡准确率升至0.973，离线模块化重放达0.934动作一致性与严格镜像等变性。
