---
title: Say Less, Hallucinate Less? Diagnosing and Restoring Object Coverage in Preference-Optimized
  Vision-Language Models
title_zh: 少输出就少幻觉？偏好优化视觉语言模型的物体覆盖问题诊断与修复
authors:
- Hansang Lee
affiliations:
- Department of Computer Science, Seoul Women’s University
arxiv_id: '2611.23179'
url: https://arxiv.org/abs/2611.23179
pdf_url: https://arxiv.org/pdf/2611.23179
published: '2026-11-17'
collected: '2026-11-18'
category: Multimodal
direction: 多模态大模型 · 幻觉与输出覆盖优化
tags:
- LVLM
- Preference Optimization
- Hallucination
- Object Coverage
- DPO
one_liner: 发现偏好优化降LVLM幻觉的同时降低物体覆盖，提出无训练的基模型引导类别修复方案
practical_value: '- 多模态商品理解/直播文案生成场景下，不要盲目上线PO方案降幻觉，需同时评估物体覆盖度与F1，避免丢失商品关键属性、关联物品信息

  - 可直接复用EOS logit bias调优trick，通过调整EOS生成概率控制输出长度，在幻觉率和召回率之间做快速 tradeoff，无需重新训练模型

  - 无训练的基模型引导修复方案可直接迁移到业务：用已对齐的基模型高置信度输出补全PO模型的缺失类别，兼顾低幻觉和高覆盖，适配快速迭代需求'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
Preference Optimization（PO）是降低大视觉语言模型（LVLM）物体幻觉的标准方案，但现有PO方法在降幻觉的同时会显著降低输出的物体类别覆盖度，并未带来CHAIR指标上set-level物体F1的显著提升。
### 方法关键点
1. 测试通过调整EOS logit bias控制生成停止时机的效果，验证PO的降幻觉收益大部分可通过基模型早停复现；
2. 提出无训练的base-guided object-category restoration方案，将基模型高置信度独有的物体类别追加到PO模型输出后，无需额外训练。
### 关键结果
仅基模型早停即可复现3个PO checkpoint 58%~86%的CHAIRi增益；调整负EOS bias仅能恢复2%~9%的丢失召回；修复后3个PO checkpoint在COCO留出集上的召回与基模型差距小于1个点，且独特物体幻觉率低于基模型。
