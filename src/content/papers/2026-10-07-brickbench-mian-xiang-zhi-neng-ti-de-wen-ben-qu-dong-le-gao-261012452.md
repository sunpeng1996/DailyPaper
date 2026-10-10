---
title: 'BrickBench: Evaluating Agentic Brick Design'
title_zh: 《BrickBench：面向智能体的文本驱动乐高设计评测基准》
authors:
- Peter Kulits
- Yiqing Xu
- R. Kenny Jones
- Cordelia Schmid
- Jiajun Wu
affiliations:
- Stanford University
- Max Planck Institute for Intelligent Systems
- Inria
arxiv_id: '2610.12452'
url: https://arxiv.org/abs/2610.12452
pdf_url: https://arxiv.org/pdf/2610.12452
published: '2026-10-07'
collected: '2026-10-10'
category: Agent
direction: Agent 生成式物理设计任务评测
tags:
- Agent
- Benchmark
- Code Agent
- Generative Design
- Evaluation
one_liner: 开源文本驱动乐高设计Agent评测基准与开发环境，验证现有Agent弱于人类设计水平
practical_value: '- 做电商套装组合、搭配推荐等离散组合生成任务时，可复用「有效性-语义对齐-设计质量」三层评测框架，降低非法结果率

  - 落地受限物料库的Agent生成任务（如给定SKU生成营销方案、组货清单）时，可参考BrickAgent的工具调用反馈循环，让Agent自主校验约束、迭代输出

  - 代码Agent落地时，可借鉴基准的离散物料匹配逻辑，减少多约束协同推理场景下的生成错误'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
代码Agent在离散组合、多物理约束协同推理场景的能力缺乏统一评测基准，现有生成式设计任务大多未覆盖物理可实现性校验，无法对齐人类设计的实用性要求。
### 方法关键点
1. 搭建BrickBench评测集，设置三个难度梯度场景：≤400零件的轻量Model场景、400~4000零件的复杂Set场景、限定固定零件库的Alt-Build场景
2. 配套开源BrickAgent环境，支持Agent编码生成设计、调用工具校验物理可装配性、迭代优化输出
3. 统一从三个维度打分：物理有效性（是否可实际搭建）、语义对齐度（是否符合prompt要求）、设计质量
### 关键结果
当前头部代码Agent可满足90%左右的物理、语义约束要求，但整体设计质量得分仅为人类设计的40%~60%，离散组合推理能力仍有明显短板。
