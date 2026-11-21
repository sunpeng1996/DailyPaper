---
title: 'ScaleWorld: High-Resolution World Generation through Shared Prediction and
  Refinement'
title_zh: ScaleWorld：基于共享预测与细化的高分辨率世界生成方法
authors:
- Yansong Qu
- Wesker Zheng
- Quanjian Song
- Zhiyuan Zhang
- Xiao Cao
- Shengchuan Zhang
- Liujuan Cao
affiliations:
- 厦门大学
- 东南大学
- 香港城市大学
- 新加坡国立大学
arxiv_id: '2611.26615'
url: https://arxiv.org/abs/2611.26615
pdf_url: https://arxiv.org/pdf/2611.26615
published: '2026-11-19'
collected: '2026-11-21'
category: Multimodal
direction: 多模态世界生成 · 共享骨干多任务优化
tags:
- WorldModel
- VideoGeneration
- KV Cache
- KnowledgeDistillation
- BackboneSharing
one_liner: 提出单共享骨干因果视频模型，统一低分辨率预测与高分辨率细化，降低高分辨率世界生成的计算与内存开销
practical_value: '- 共享骨干+分任务独立KV缓存的架构，可迁移至生成式推荐多任务（如候选生成+文案渲染、召回+排序）场景，大幅降低推理显存与部署成本

  - 任务非对称on-policy蒸馏（TA-OPD）方法，可解决多任务联合训练的干扰问题，适合用单个大模型承载多类推荐/广告生成需求

  - 低分辨率预测后做高分辨率细化的级联生成思路，可复用在电商商品高清图/短视频生成、推荐场景高清内容渲染场景，降低生成算力开销'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
高分辨率视频世界生成可输出细粒度场景结构与纹理，但直接生成的计算、内存开销极高，现有方案需独立的预测、细化双模型，部署复杂度高。
### 方法关键点
1. 单个共享骨干统一低分辨率世界预测与高分辨率细化任务，每个视频chunk先完成低分辨率预测，再基于预测结果做单步高分辨率细化，无需独立细化模型
2. 维护两套独立因果状态：长时低分辨率历史KV缓存用于预测，短时高分辨率历史KV缓存用于细化，支撑高效流式生成
3. 提出任务非对称on-policy蒸馏（TA-OPD），在各自采样和历史策略下做局部速度匹配，将专业教师的能力迁移至共享学生模型，解决多任务蒸馏的干扰问题
### 关键结果
实现960p 12FPS的流式高分辨率世界生成，相较独立双模型方案计算、内存效率显著提升
