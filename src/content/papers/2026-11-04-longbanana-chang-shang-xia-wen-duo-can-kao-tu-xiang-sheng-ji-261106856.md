---
title: 'LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference
  Image Synthesis'
title_zh: LongBanana：长上下文多参考图像生成专家验证基准
authors:
- Haoxiang Cao
- Yuxuan Zhang
- Penghui Du
- Bo Li
- Jiajiong Cao
- Yingying Fan
- Zimeng Wu
- Yifu Luo
- Mingzhe Zheng
- Junwen Miao
affiliations:
- South China Normal University
- University of British Columbia
- KlingAI Research
- Tsinghua University
- University of Waterloo
arxiv_id: '2611.06856'
url: https://arxiv.org/abs/2611.06856
pdf_url: https://arxiv.org/pdf/2611.06856
published: '2026-11-04'
collected: '2026-11-09'
category: Agent
direction: Agent驱动多模态图像生成基准构建
tags:
- Long-Context
- Image Synthesis
- Agent
- Benchmark
- Multi-Reference
- Evaluation
one_liner: 首个专家设计验证的长上下文多参考图像生成基准，配套Agent生成优化框架
practical_value: '- 电商多素材合成广告场景可复用RPR（ReAct-Plan-Exec-Reflect）Agent工作流，提升跨参考图的内容一致性与约束满足度

  - 多模态生成效果评估可借鉴实体关系图接地的原子化checklist设计，拆解实体、关系、全局约束三类评测项，降低人工评估主观性

  - 长上下文任务的专家标注流程可复用15%双标注+二次加权kappa的校验方案，低成本保证标注质量'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有Agent驱动的图像生成缺乏针对长上下文多参考场景的标准化评测体系，无法系统验证多证据检索、抗干扰、实体关系绑定、多素材融合等核心能力，难以支撑电商广告生成等落地场景的效果校验。
### 方法关键点
采用3×3分类体系构建90项专属评测任务，单任务包含约32张参考图、20条约束、50个评测项，基于实体关系图接地的评估框架，将评测维度拆解为内容保真度、关系绑定、全局约束满足三类；配套提出LongBanana-Gen Agent框架，支持RPR工作流优化长周期生成效果。
### 关键结果
共包含4670个专家标注原子评测项，15%双标注子集精确匹配率达89.4%，二次加权kappa为0.83；RPR工作流相比直接生成显著提升多参考证据接地能力与错误修复效果
