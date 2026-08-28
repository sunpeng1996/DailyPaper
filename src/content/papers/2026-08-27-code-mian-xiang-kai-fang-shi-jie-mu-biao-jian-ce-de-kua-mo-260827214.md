---
title: 'CODE: Cross-Modal Calibration and Dynamic Suppression for Open World Object
  Detection'
title_zh: CODE：面向开放世界目标检测的跨模态校准与动态抑制
authors:
- Hao Xu
- Zhaoning Shi
- Hehe Jin
- Bo Ma
affiliations:
- Beijing Institute of Technology
arxiv_id: '2608.27214'
url: https://arxiv.org/abs/2608.27214
pdf_url: https://arxiv.org/pdf/2608.27214
published: '2026-08-27'
collected: '2026-08-28'
category: Multimodal
direction: 多模态开放世界目标检测推理优化
tags:
- Open-World-Object-Detection
- Cross-Modal-Matching
- OOD-Detection
- Inference-Optimization
- OWL-ViT
one_liner: 针对开放世界目标检测两大痛点，提出推理端优化框架CODE，OWL-ViT下U-mAP、K-mAP超SOTA2.6、2.3个点
practical_value: '- 电商搜图、多模态商品分类场景可复用「全局视觉原型校准文本驱动预测」trick，缓解单向文本到视觉匹配的语义歧义

  - 新物品召回、未知物体识别等OOD场景可借鉴「置信度边际动态抑制」替代硬阈值惩罚，避免边界样本过杀

  - 推理端免训练优化思路可直接落地，无需调整多模态基座预训练权重就能快速提升下游任务性能，适配快迭代业务'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
基于多模态基座的开放世界目标检测（OWOD）存在两大核心痛点：单向文本到视觉匹配易引发语义歧义，固定离群点惩罚会过度抑制已知类别决策边界附近的未知物体。
### 方法关键点
推理时统一框架CODE包含三个互补模块：
1. 跨模态联合置信度校准：注入全局视觉原型，校准文本驱动的已知类别预测
2. 不确定性引导的通用目标性增强：从局部视觉响应度量分类犹豫度，强化潜在未知物体的识别权重
3. 基于置信度边际的动态离群抑制：用边际感知调整替代固定抑制规则，保留模糊的分布外样本
### 关键结果
基于OWL-ViT L/14基座在真实世界检测基准Task1上，U-mAP达21.7、K-mAP达40.8，分别超出此前SOTA2.6、2.3个百分点。
