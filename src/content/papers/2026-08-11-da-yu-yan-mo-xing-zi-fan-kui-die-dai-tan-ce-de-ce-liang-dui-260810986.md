---
title: What Iterated Self-Feeding Probes of Language Models Measure, and a test that
  separates the construction from the model
title_zh: 大语言模型自反馈迭代探测的测量对象及构造与模型分离测试
authors:
- Nicolás Vera Zúñiga
affiliations:
- Independent Researcher, Chile
arxiv_id: '2608.10986'
url: https://arxiv.org/abs/2608.10986
pdf_url: https://arxiv.org/pdf/2608.10986
published: '2026-08-11'
collected: '2026-08-12'
category: LLM
direction: LLM自反馈/Agent loop 性能评估
tags:
- Self-Feedback
- Probing
- Agentic Loop
- Lyapunov Exponent
- Evaluation
one_liner: 区分LLM自反馈迭代探测中构造固有与模型专属的两类测量值，给出分离测试方法
practical_value: '- 搭建Agent自迭代、LLM自我修正模块时，先拆分观测指标属于loop构造固有属性还是模型能力，避免误判模型优化效果

  - 评估多轮自反馈链路性能时，可复用固定构造换模型、固定模型换构造的对照测试方法，筛除无效评估指标

  - 做迭代式生成（如商品文案润色、推荐理由优化）时，可参考损伤传播量化方法判断迭代收益拐点，减少无效计算消耗'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前自洽性推理、迭代内容优化、Agentic loop等LLM自反馈类方法的观测指标来源模糊，极易把链路构造的固有属性误判为模型本身的能力，导致优化方向走偏。
### 方法关键点
基于token序列Glauber动力学，用公共随机数耦合仅相差1个token的两个token环同步演化，实现损伤传播效应的可量化测量；提出分离测试范式：固定探测构造换模型、固定模型换探测构造，通过指标是否波动判断其归属。
### 关键结果
覆盖19个模型、70倍参数跨度的测试显示，token空间Lyapunov指数λ_ca(r)的半径缩放为模型不变量；λ_ca过零点可稳定对应模型训练阶段，吸引子份额可跨构造稳定排序模型；此前测得的3位精度相变效应实际属于探针构造而非模型，配套方法已打包开源。
