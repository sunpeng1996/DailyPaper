---
title: 'ContextBias: Controlled Evaluation of Bias Persistence Under Context Shift
  in Text-to-Image Models'
title_zh: ContextBias：文本生成图像模型上下文偏移下偏见持久性可控评估
authors:
- Shaghayegh Kolli
- Sina Emami
- Moreno D&#39;Incà
- Pouyan Nejadi
- Nicu Sebe
- Massimiliano Mancini
- Jana Diesner
affiliations:
- Technical University of Munich
- University of Trento
- Orreco
- Munich Center for Machine Learning (MCML)
- Munich Data Science Institute (MDSI)
arxiv_id: '2608.29847'
url: https://arxiv.org/abs/2608.29847
pdf_url: https://arxiv.org/pdf/2608.29847
published: '2026-08-29'
collected: '2026-09-02'
category: Eval
direction: 文生图模型 偏见持久性可控评估
tags:
- Text-to-Image
- Bias Evaluation
- Context Shift
- Benchmark
- Stereotype Detection
one_liner: 提出文生图偏见可控评估框架ContextBias与基准ContextBench，验证职业刻板印象不随上下文偏移消失
practical_value: '- 电商文生图营销素材生成场景下，可复用ContextBias的变量控制方法，测试不同场景prompt下生成内容的刻板偏见，规避违规或用户不适风险

  - 多模态推荐系统的生成内容偏见校验环节，可直接复用ContextBench的分层prompt设计逻辑，拆分身份/服饰/场景等维度分别评估偏差

  - Agent调用文生图工具的输出校验流程中，可借鉴核心结论：职业/身份关联属性不会随场景prompt变化消失，需单独增加属性合规校验规则，不能依赖场景prompt修正偏见'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
文生图模型学习到的概念关联易催生刻板偏见，现有评估多基于无上下文场景，无法验证上下文偏移下偏见的稳定性，缺乏可控的变量隔离评估手段。
### 方法关键点
1. 推出ContextBias可控评估框架，配套ContextBench基准，覆盖92类职业、1656条语义可控prompt，通过固定职业、变换场景上下文实现变量隔离
2. 对4个SOTA文生图模型生成的66240张图像开展量化偏见评估
### 关键结果
- 语义无关上下文不会抑制职业关联属性，跨角色属性集中度反而上升（合并BI +0.047）
- 人口统计学特征、职业服饰、专属工具在三类上下文场景下均高度稳定，仅场景构图、camera framing对上下文敏感
- 现有无上下文评估会遗漏大量跨场景持续存在的刻板偏见
