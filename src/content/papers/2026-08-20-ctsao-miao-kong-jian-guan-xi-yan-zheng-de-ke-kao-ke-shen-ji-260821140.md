---
title: A Modular Agent for Reliable and Auditable Spatial Relation Verification in
  CT Scans
title_zh: CT扫描空间关系验证的可靠可审计模块化Agent
authors:
- Simon Vincent Abel
- Heiko Hillenhagen
- Michael Götz
- Timo Ropinski
- Ayhan Can Erdur
- Daniel Santak Wolf
affiliations:
- Ulm University
- Ulm University Hospital
- Technical University of Munich
- TUM University Hospital
arxiv_id: '2608.21140'
url: https://arxiv.org/abs/2608.21140
pdf_url: https://arxiv.org/pdf/2608.21140
published: '2026-08-20'
collected: '2026-08-29'
category: Agent
direction: 医学Agent · 多模块可解释空间推理
tags:
- Modular Agent
- Spatial Reasoning
- Medical VLM
- Interpretability
- Auditable Reasoning
one_liner: 将CT空间关系验证拆分为多阶段可解释模块，精度较端到端Qwen2-VL提升42.5个百分点
practical_value: '- 涉及空间类推理的业务场景（如广告素材元素合规校验、AR商品摆放合理性检测）可借鉴「语义解析+感知检测+规则计算」的拆分架构，大幅降低大模型幻觉，同时实现推理过程可审计

  - 需要强可控性、可解释性的业务（如推荐理由生成、搜索结果合规校验）可复用「大模型做语义解析+小模型做垂直感知任务+硬规则做最终判定」的混合范式，平衡精度与可控性

  - 多模块Agent架构可保留所有中间步骤输出，适合需要溯源、满足监管合规要求的业务场景，避免端到端黑箱模型的不可控风险'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
医疗领域VLM在空间推理任务上存在明显幻觉，无法可靠锚定图像中的空间关系，现有端到端方案缺乏可解释性与可审计性，易影响放射诊断准确性。
### 方法关键点
采用模块化Agent架构，将CT轴向切片二分类空间关系验证任务拆分为3个独立阶段：将自然语言查询转化为结构化关系元组；用YOLO检测器定位查询涉及的解剖结构；基于目标中心坐标通过确定性几何规则输出最终判定。
### 关键结果
在MIRP空间QA基准测试中，最优混合配置准确率达94.1%、F1达94.2%，较直接prompt Qwen2-VL的精度高出42.5个百分点，同时保留可解释中间表示与可审计推理链路。
