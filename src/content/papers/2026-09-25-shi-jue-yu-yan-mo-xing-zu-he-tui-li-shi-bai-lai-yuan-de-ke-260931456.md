---
title: 'Diagnosing the Sources of Compositional Failure in Vision-Language Models:
  A Controlled Analysis'
title_zh: 视觉语言模型组合推理失败来源的可控诊断分析
authors:
- Mona Gandhi
- Cenk Merih Olcay
- Kuan-Chieh Lo
- Santiago Castro
- Christopher W. Myers
- Srinivasan Parthasarathy
affiliations:
- The Ohio State University
- Netflix Research
arxiv_id: '2609.31456'
url: https://arxiv.org/abs/2609.31456
pdf_url: https://arxiv.org/pdf/2609.31456
published: '2026-09-25'
collected: '2026-09-28'
category: Eval
direction: 多模态VLM · 组合推理能力评估
tags:
- VLM
- Compositional Reasoning
- Evaluation Framework
- Multimodal
- Skill Decomposition
one_liner: 提出COMPASS可控评估框架，拆分量化VLM组合推理失败的多维度独立影响因素
practical_value: '- 做多模态商品理解（如图文商品属性抽取、场景化推荐）时，可复用COMPASS的技能拆分思路，分别量化物体检测、属性绑定、关系推理三个子任务的误差，快速定位业务badcase根因

  - 多模态召回/排序模型迭代时，可参考「自负载增加导致单技能退化、跨类型特征提供正向上下文」的结论，构造负例时优先增加同类型原语密度，无需刻意叠加多类无关特征

  - 搭建电商多模态Agent的能力评测体系时，可借鉴对照实验设计，拆分组合推理成本与单组件识别成本，避免评测指标过于笼统无法定位模型短板'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有VLM在组合推理任务上性能差的根源未被量化，传统基准仅评估整体组合任务表现，无法拆分组合推理集成成本与单组件识别成本的独立影响。
### 方法关键点
提出COMPASS可控评估框架，通过匹配扰动下组合式描述与拆分后描述的性能对比，量化组合集成的独立成本；进一步通过定向扰动实验，拆分物体检测、属性绑定、关系推理三类子技能的性能影响因子。
### 关键结果
在87K图文对上的测试显示，组合集成成本仅为整体性能下降的部分原因；274K图文对的子技能分析表明，单技能性能下降主要受自身原语数量（自负载）影响，跨类型原语大多提供正向上下文，该规律在对比学习编码器、专项训练组合推理模型、非对比架构三类主流VLM中均成立。
