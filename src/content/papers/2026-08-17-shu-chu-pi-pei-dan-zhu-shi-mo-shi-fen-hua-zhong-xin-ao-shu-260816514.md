---
title: 'Matched Outcomes, Divergent Gaze: How Foveated MLLMs Search Compared to Humans'
title_zh: 输出匹配但注视模式分化：中心凹输入多模态大模型与人类视觉搜索对比
authors:
- Mohamed Amine Kerkouri
- Marouane Tliba
- Aladine Chetouani
- Ulas Bagci
- Alessandro Bruno
affiliations:
- F-initiatives (Paris, France)
- Université Sorbonne Paris Nord
- Northwestern University
- IULM University (Milan, Italy)
arxiv_id: '2608.16514'
url: https://arxiv.org/abs/2608.16514
pdf_url: https://arxiv.org/pdf/2608.16514
published: '2026-08-17'
collected: '2026-08-22'
category: Multimodal
direction: 多模态大模型 · 人类行为对齐评估
tags:
- MLLM
- Foveated Vision
- Visual Search
- Eye Movement
- Human Alignment
one_liner: 对比相同中心凹输入下MLLM与人类视觉搜索行为，发现结果对齐但时序注视过程存在本质差异
practical_value: '- 多模态导购/商品搜索Agent评估：不能仅看检索结果准确率，需补充注视时序、扫描路径等行为维度指标，避免结果正确但交互逻辑不符合人类浏览习惯

  - 目标检出类业务（如电商图违规识别、商品同款检索）：零-shot通用MLLM性能已优于人类，可直接落地降低人工成本

  - 广告/商品图热点优化场景：MLLM输出的空间注视点分布和人类匹配度高，可低成本替代初步人类眼动实验，快速评估内容吸引力'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
当前MLLM的视觉人类对齐评估多聚焦结果匹配，未验证相同中心凹输入条件下，MLLM的视觉搜索时序过程是否和人类一致，限制了其作为人类视觉模型、注意力对齐工具的可靠性。
### 方法关键点
在COCO-Search18目标导向搜索数据集上，给3款通用MLLM输入与人类完全匹配的逐次注视中心凹视图，从目标存在判断、目标获取效率、注视过程三个维度对比MLLM和人类的眼动扫描路径差异。
### 关键结果
目标判断和获取效率上MLLM匹配甚至超过人类，目标检出率接近天花板，首次扫视命中目标的概率高于人类；但注视过程和人类存在本质差异，MLLM扫描路径呈现低熵、大幅、高自一致性特征，自匹配度远高于人类间的匹配度，仅空间注视点分布和人类匹配，无退化策略可实现时序过程的人类级对齐。
