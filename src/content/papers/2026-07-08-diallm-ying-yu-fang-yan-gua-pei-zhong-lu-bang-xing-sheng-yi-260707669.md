---
title: 'DiaLLM: An Investigation into the Robustness-Generation Gap in English Dialect
  Adaptation'
title_zh: DiaLLM：英语方言适配中鲁棒性-生成差异研究
authors:
- Jordan Painter
- Dipankar Srirag
- Adarsh Kappiyath
- Diptesh Kanojia
- Aditya Joshi
- Lu Yin
affiliations:
- University of Surrey, UK
- University of New South Wales, Australia
arxiv_id: '2607.07669'
url: https://arxiv.org/abs/2607.07669
pdf_url: https://arxiv.org/pdf/2607.07669
published: '2026-07-08'
collected: '2026-07-09'
category: LLM
direction: LLM方言适配 · 对齐策略对比
tags:
- LLM Adaptation
- Dialect Generation
- Alignment Strategy
- Continual Pretraining
- SFT
one_liner: 通过多组件对照实验揭示LLM英语方言理解与生成能力的解离特性，开源相关资源
practical_value: '- 做多区域口语化/本地化内容生成时，优先选择显式定向风格适配方案，用户偏好优于通用对齐策略

  - 风格类生成任务中避免过度优化单一风格奖励指标，极端优化会导致人类偏好显著下降，需设计多维度奖励函数

  - 风格化生成效果评估不能仅依赖自动benchmark，需补充人工评估，对齐带来的生成质量提升无法被自动指标捕获'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM已具备方言理解能力，但仅能生成偏向美式的标准英语，方言生成能力缺失，且方言鲁棒性与生成能力的关联机制不明确。
### 方法关键点
构建DiaLLM框架，基于国际英语语料库对3类开源LLM执行持续预训练，对照测试隐式/显式两类后训练范式、3种对齐策略在澳式、印度、北英三种英语方言上的适配效果。
### 关键结果
1. 方言鲁棒性与生成能力完全解离：自动benchmark得分由持续预训练+SFT决定，对齐对生成质量的优化无法被benchmark捕捉
2. 显式定向方言适配的输出方言识别率比通用对齐高21%，人类偏好更优
3. 过度优化单一方言奖励的方案人类偏好比最优方案低18%，无单一对齐方法可适配所有场景
