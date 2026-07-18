---
title: Benchmarking Multimodal Large Language Models for Scientific Visualization
  Literacy
title_zh: 多模态大模型科学可视化理解能力基准测试
authors:
- Patrick Phuoc Do
- Chau M. Ta
- Chaoli Wang
affiliations:
- University of Notre Dame
arxiv_id: '2607.15176'
url: https://arxiv.org/abs/2607.15176
pdf_url: https://arxiv.org/pdf/2607.15176
published: '2026-07-16'
collected: '2026-07-18'
category: Eval
direction: 多模态大模型 · 专业可视化能力评测
tags:
- MLLM
- Benchmark
- SciVis
- Visualization Literacy
- Evaluation
one_liner: 构建科学可视化理解评测基准，测试6款MLLM表现并对比485名人类得分
practical_value: '- 电商多模态商品理解场景中，若需解析带专业可视化图表的工业/医疗/美妆类商品内容，可优先选择Gemini类闭源MLLM，当前开源MLLM在复杂可视化理解上表现未达人类基线

  - 搭建多模态Agent处理图表类定量估算、流向判断任务时，需额外增加规则校验模块，规避MLLM细粒度量化判断、编码规则理解的常见错误

  - 构建多模态模型能力评测体系时，可参考本文分任务类型、分可视化技术的细粒度评估框架，避免笼统的性能结论'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有MLLM可视化理解评测多以普通图表为核心，缺乏对科学可视化（SciVis）类专业内容的理解能力评估，无法有效衡量MLLM在专业场景下的多模态表现。
### 方法关键点
选取3款闭源、3款开源共6款MLLM作为评测对象，采用包含18张科学可视化图、49道评测题、覆盖8种可视化技术、11类任务的标准化SciVis评测集，在闭域协议下开展测试，同步对比485名人类参与者的测试结果。
### 关键结果数字
Gemini整体表现最优，得分超过人类均值；所有开源MLLM得分均低于人类基线；模型在科学插图、搜索、空间理解类任务表现最好，在纹理/集成类可视化、定量估算任务表现较差；三类高频错误为细粒度定量估算错误、流向判断错误、编码规则理解错误。
