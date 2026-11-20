---
title: 'Persona Lenses: What Makes a Vision-Language Model See Through Its Persona''s
  Eyes?'
title_zh: Persona Lens：如何让多模态模型模拟特定用户的网页注视行为
authors:
- Yoonho Shin
affiliations:
- LG Uplus
arxiv_id: '2611.25508'
url: https://arxiv.org/abs/2611.25508
pdf_url: https://arxiv.org/pdf/2611.25508
published: '2026-11-19'
collected: '2026-11-20'
category: RecSys
direction: 多模态用户建模 · 网页注视行为预测
tags:
- VLM
- Persona Modeling
- Gaze Prediction
- Prompt Engineering
- User Simulation
one_liner: 提出三类适配不同规模VLM的Persona透镜，提升用户画像在网页注视模拟的生效程度
practical_value: '- 小参数（4B/9B级）VLM做用户行为模拟时优先选weight lens，无需额外页面处理步骤，对训练外用户兴趣泛化性好，可降低推理成本

  - 强用户属性区分需求场景可选text lens，需额外新增无关属性过滤逻辑，避免非注视相关的画像特征干扰预测结果

  - 大参数（30B+）VLM无需额外透镜模块，直接通过基础prompt注入用户画像即可达到可观的属性区分效果，可简化工程链路'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
当前VLM模拟用户网页注视行为时，prompt注入的用户画像仅能部分生效，缺乏量化画像生效程度的方案，也无适配不同模型规模的优化手段。
### 方法关键点
1. 设计单属性差异的MatrAIx persona对，量化画像对注视结果的影响程度；
2. 提出三类persona透镜：text lens（两步prompt先输出兴趣区域再预测注视）、pixel lens（页面兴趣区域打标注入）、weight lens（注视停留奖励门控保持扫描路径自然）。
### 关键结果
在Qwen3-VL 4B/32B、Qwen3.5 9B上测试：32B模型无透镜即可实现良好的persona区分度；4B/9B模型中weight lens可区分训练外的兴趣persona，无新页面额外处理开销；text lens区分度最高但对无关属性敏感；pixel lens区分度稍低但不受无关属性干扰
