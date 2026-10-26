---
title: 'TutorCaseBench: A Case-Grounded Benchmark for Evaluating LLM Tutors in Supporting
  Students with Challenging Behaviors'
title_zh: 《TutorCaseBench：面向行为障碍学生LLM辅导场景的案例驱动评估基准》
authors:
- Yeon Su Park
- Chanyoung Park
- Tae Soo Kim
- Seungju Kim
- Hyunwoo Kim
- Daho Jung
- Jinsung Yoon
- Juho Kim
affiliations:
- KAIST
- Seoul National University
- Google Cloud AI Research
- Korea Institute for Curriculum and Evaluation
- SkillBench
arxiv_id: '2610.30828'
url: https://arxiv.org/abs/2610.30828
pdf_url: https://arxiv.org/pdf/2610.30828
published: '2026-10-22'
collected: '2026-10-26'
category: Eval
direction: LLM性能评估 · 教育场景专属基准
tags:
- LLM
- Benchmark
- Evaluation
- AI Tutor
- Open Data
one_liner: 构建了基于教育学真实案例的LLM辅导评估基准，覆盖5类学生挑战行为场景，数据完全开源
practical_value: '- 做垂直场景Agent性能评估时，可复用「先基于领域定性研究生成场景、对话、评估rubric再分生成/选择两类任务测试」的流水线，比如电商客服Agent的难搞用户场景评估

  - 可参考结论：当前LLM策略选择能力远强于场景适配生成能力，做垂直Agent时可优先用检索+排序选预设策略再做轻量改写的架构，降低生成错误率

  - 开源的923组多轮对话+评估rubric的构建方法可迁移到电商客服、导购Agent的负向用户反馈场景评测集构建'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有LLM教育辅导评估基准完全忽略有学习/行为障碍学生的常见挑战行为场景，无法衡量LLM辅导的情感适配、行为干预能力。

### 方法关键点
1. 基于教育学、教育心理学、特殊教育的定性案例研究，搭建流水线将已归档的学生类别转化为特定场景、师生对话和基于证据的评估rubric
2. 基准覆盖5类学生挑战行为，包含923段对话，设置开放回复生成（1560个测试项）、多选策略选择（2537个测试项）两类评估任务

### 关键结果数字
- 11个SOTA LLM测试中，最强模型的开放回复满足评估标准的比例仅为55.8%
- 所有模型的策略选择准确率均显著高于场景化回复生成的达标率，开源模型的两类任务差距更明显
