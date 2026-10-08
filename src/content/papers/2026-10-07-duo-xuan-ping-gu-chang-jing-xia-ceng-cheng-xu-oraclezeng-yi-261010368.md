---
title: Input-Blind Controls Produce Substantial Oracle Headroom for Layer Programs
  in Multiple-Choice Evaluation
title_zh: 多选评估场景下层程序Oracle增益存在大量输入盲对照可实现的余量
authors:
- Yibei Guo
- Rui Liu
affiliations:
- Kent State University
arxiv_id: '2610.10368'
url: https://arxiv.org/abs/2610.10368
pdf_url: https://arxiv.org/pdf/2610.10368
published: '2026-10-07'
collected: '2026-10-08'
category: Eval
direction: LLM自适应计算 · Oracle评估偏差验证
tags:
- Adaptive Computation
- Oracle Evaluation
- Layer Skipping
- LLM Inference
- Multiple-Choice Evaluation
one_liner: 验证LLM自适应层计算的Oracle评估增益大多来自非计算特异性因素而非层编辑本身
practical_value: '- 做LLM多选类效果评估（如RAG/Agent答案校验、推荐query意图分类测试）时，必须加选项旋转校验，避免选项顺序/字母偏好带来的虚高增益，确保评估结论可靠

  - 业务侧落地自适应层跳过/重复的推理优化时，不能直接用Oracle选的层程序作为训练标签，需先做输入盲对照基准测试，过滤非计算特异性的伪增益，减少无效研发迭代

  - 做算法方案上限预估（如搜索推荐排序策略的Oracle上限、大模型优化空间测算）时，加入输入无关的随机扰动对照组，避免高估优化空间，浪费研发资源'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM自适应层计算（跳层/重复层推理优化）的Oracle评估常使用已知答案选择最优层程序，直接将增益归因于层编辑的计算价值，但无法区分增益是来自计算本身还是评估流程、数据集的偏差，容易误导后续研发方向。
### 方法关键点
- 构建两类对照层程序集合：32种真实跳层/重复层操作、输入盲对照程序（在相同层位置注入与输入无关的固定随机增量，校准到与真实程序相同的答案改变率）
- 采用跨Prompt评估范式：同一问题搭配两组不同few-shot示例的Prompt，固定选项顺序时测量增益的跨Prompt留存，旋转选项顺序时测试增益对选项结构的依赖
- 量化headroom为Oracle最优策略相对最优静态策略的增益，对比真实与对照程序的headroom差值
### 关键结果
- 测试数据集为MMLU-Pro、BBH、ARC-Challenge共4413道多选题，覆盖Qwen3-4B-Base、Llama-3.1-8B两个模型
- 固定选项顺序时，输入盲对照的跨Prompt headroom在Qwen3上达11.8pp、Llama上达15.6pp，均超过真实程序的9.0pp、10.1pp
- 旋转选项后两类headroom均大幅下降，真实程序仅比对照高1.4~4.5pp；补充生成式数学题测试中，问题对应最优层程序改写后准确率比其他程序高26.0pp，未做安慰剂对照
### 核心结论
在字母打分的多选评估中，选项顺序固定时的大幅Oracle增益本身不足以证明层编辑的计算特异性价值，必须加入输入盲对照和选项旋转校验
