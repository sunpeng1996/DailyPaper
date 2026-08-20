---
title: 'RoE-FND: Synergizing LLMs with Experiential Learning for Effective and Generalizable
  Evidence-Based Fake News Detection'
title_zh: RoE-FND：融合LLM与经验学习的高泛化证据型假新闻检测
authors:
- Yuzhou Yang
- Qichao Ying
- Sheng Li
- Zhiyin Zhu
- Zhenxing Qian
- Xinpeng Zhang
affiliations:
- Fudan University
- Hohai University
arxiv_id: '2608.15210'
url: https://arxiv.org/abs/2608.15210
pdf_url: https://arxiv.org/pdf/2608.15210
published: '2026-08-15'
collected: '2026-08-20'
category: LLM
direction: LLM推理增强 · 经验库驱动内容检测
tags:
- FakeNewsDetection
- ExperientialLearning
- SelfReflection
- RetrievalAugmented
- ZeroShotLLM
one_liner: 提出结合反思经验库与双路径推理的RoE-FND框架，无需微调LLM即可实现高泛化假新闻检测
practical_value: '- 电商内容风控（虚假宣传、刷量评论/直播话术识别）场景可复用「正反双路径推理+经验库裁决」范式，无需微调LLM即可快速适配新违规类型

  - 构建领域规则/经验库时，可参考「无约束推理-真值引导推理对比提炼分歧」的方法，低成本生成可复用的推理指南，替代人工标注规则

  - 跨场景泛化要求高的分类任务，可借鉴该无微调的检索增强推理框架，大幅降低新数据集适配的训练成本与周期'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有假新闻检测方案要么依赖标注数据训练泛化性差，要么直接用LLM推理易被看似合理的错误理由误导，缺乏系统性暴露推理偏差的经验机制。
### 方法关键点
1. 离线构建反思经验库：对比同一新闻的无约束推理结果与真值标签引导的条件推理结果，提炼两类输出的核心分歧作为可复用推理指南存入经验库
2. 在线推理阶段：先生成正反两个伪标签引导的对立推理结果，定位核心分歧后检索最相关的经验条目，裁决证据更充分的结论作为最终输出，全程无需微调LLM参数
### 关键结果
在CHEF、Snopes、PolitiFact等3个文本数据集与FakeTT、FakeSV两个多模态数据集上性能优于所有基线，跨数据集泛化能力显著领先现有方案
