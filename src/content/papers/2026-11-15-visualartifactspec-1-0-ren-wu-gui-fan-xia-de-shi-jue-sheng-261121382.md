---
title: 'VisualArtifactSpec 1.0: Evaluating Visual Artifacts under Task Specifications'
title_zh: VisualArtifactSpec 1.0：任务规范下的视觉生成产物评估基准
authors:
- Shuyi Ouyang
- Xiaojun Tang
- Zijian Zou
- Xintong Zhang
- Mingli Song
- Guannan Zhang
- Hongwei Xue
affiliations:
- Zhejiang University
- Alibaba Group Accio Team
arxiv_id: '2611.21382'
url: https://arxiv.org/abs/2611.21382
pdf_url: https://arxiv.org/pdf/2611.21382
published: '2026-11-15'
collected: '2026-11-18'
category: Eval
direction: 多模态Agent · 视觉生成产物评估
tags:
- Evaluation Benchmark
- Multimodal Agent
- Visual Generation
- Task Specification
- Artifact Assessment
one_liner: 推出覆盖4类视觉产物的211任务基准VAS，拆分双维度评估跨媒介Agent创作能力
practical_value: '- 电商多模态生成（主图、详情页、商品短视频、推介PPT）效果评估可复用双维度框架，拆分硬性约束校验和主观质量打分，避免合规性漏判

  - 自研视觉类Agent工具链时，可直接复用VAS标注的211个任务做离线评测，快速对齐不同模型+工具组合的能力边界

  - 面向不同受众/场景的生成需求，可借鉴任务专属评分锚点设计思路，把模糊的质量要求拆解为可落地的量化评判标准'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视觉生成评估基准多局限于单一媒介，无法系统衡量Agent跨媒介通用创作能力，也缺少对不同受众、场景适配性的评估维度。
### 方法关键点
推出VAS 1.0基准，覆盖演示文稿、静态图、动画视频、网页界面4类视觉产物共211个创建/修改任务，每个任务明确目标、素材、约束、交付物要求；评估拆分两个独立维度：①Task Fulfillment 校验显性要求和功能合规性 ②Artifact Performance 从内容、结构、视觉、交付四方面打分，配套任务专属评分锚点统一评判标准。
### 关键结果
9种模型+工具链配置的总分在42.12~70.52之间，最高分与最低分的差距中73.4%来自Artifact Performance维度的差异。
