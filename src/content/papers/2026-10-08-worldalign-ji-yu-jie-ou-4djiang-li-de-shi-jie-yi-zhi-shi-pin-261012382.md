---
title: 'WorldAlign: Decoupled 4D Reward for World-Consistent Video Generation'
title_zh: WorldAlign：基于解耦4D奖励的世界一致视频生成方法
authors:
- Jing He
- Kaixin Ding
- Xingye Tian
- Guibao Shen
- Wenhang Ge
- Xin Tao
- Pengfei Wan
- Ying-Cong Chen
affiliations:
- 香港科技大学（广州）
- 香港科技大学
- KlingAI
- 香港大学
arxiv_id: '2610.12382'
url: https://arxiv.org/abs/2610.12382
pdf_url: https://arxiv.org/pdf/2610.12382
published: '2026-10-08'
collected: '2026-10-10'
category: Other
direction: 视频生成 · 4D时空一致性优化
tags:
- Video Generation
- 4D Consistency
- Reward Framework
- Decoupled Alignment
- VLM-as-Judge
one_liner: 提出语义分离动静区域的解耦4D奖励框架，无人工标注即可提升视频生成时空一致性
practical_value: '- 解耦静态背景/动态主体的分治评估思路，可迁移到电商商品展示短视频生成场景，分别校验背景一致性、商品外观/动作合理性，降低生成内容崩坏率

  - VLM-as-judge 结合样本专属检查清单的无标注奖励构建方法，可复用在推荐场景AIGC物料（文案、短视频、虚拟直播内容）的自动质量评估，减少人工标注成本

  - 无需人工偏好标注的在线后训练优化范式，可迁移到生成式推荐大模型的增量微调，在不损伤原有生成能力的前提下定向提升特定维度生成质量'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视频生成的几何感知后训练多依赖静态场景假设，动态场景下静态一致性反馈不可靠，动态一致性也缺乏有效评估，难以保障生成视频的4D时空一致性（包含静态3D结构连贯、动态主体运动/外观合理两大要求）。
### 方法关键点
1. 提出解耦4D奖励框架，语义分割静态区域与动态主体，分别对齐适配的世界先验给出反馈
2. 静态区域采用语义引导的掩膜重投影对齐几何先验，新增相机运动奖励避免生成近静态结果
3. 动态主体引入VLM作为动态世界先验，基于样本专属检查清单构建VLM-as-judge奖励，覆盖动态性、物理合理性、形状纹理一致性维度；无需人工偏好标注即可开展在线后训练
### 关键结果
在Wan2.1、Wan2.2两个预训练图像转视频生成器上验证，相比现有方法同时提升静态、动态一致性，且不会抑制整体或主体运动。
