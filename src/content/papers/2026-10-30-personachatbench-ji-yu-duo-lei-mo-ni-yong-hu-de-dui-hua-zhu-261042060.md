---
title: 'PersonaChatBench: Evaluating Chat Assistants with Diverse Simulated Users'
title_zh: PersonaChatBench：基于多类模拟用户的对话助手评估框架
authors:
- Zheyuan Deng
- Taoran Li
- Jingwen Zhang
- Yuante Li
- Dachuan Zhao
- Fulei Zhang
- Yunkai Zhang
- Zhikun Xu
- Yajie Liao
- Haichao Zhang
affiliations:
- Brown University
- Texas A&M University
- Harvard University
- Carnegie Mellon University
- Columbia University
arxiv_id: '2610.42060'
url: https://arxiv.org/abs/2610.42060
pdf_url: https://arxiv.org/pdf/2610.42060
published: '2026-10-30'
collected: '2026-11-02'
category: Eval
direction: 对话Agent · 多用户群体适配评估
tags:
- LLM Evaluation
- Conversational Agent
- Persona Simulation
- Benchmark
- User Experience
one_liner: 提出固定任务、切换带私有人设模拟用户的对话助手多维度评估框架
practical_value: '- 电商智能导购/客服Agent评估可复用「固定任务+切换用户人设」范式，替代单一测试用例，挖掘不同用户群体的服务体验盲区，避免总指标掩盖的细分体验问题

  - 可基于该框架构建电商场景专属用户persona模拟集，测试推荐/导购Agent对不同消费偏好、交互习惯用户的需求满足率，定向优化弱势用户群体的服务效果

  - 优化LLM导购模型时可参考核心结论：不能仅用任务完成率作为核心指标，需单独增加个性化需求满足度评估，跨品类场景需做针对性适配调优'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有对话助手评估多基于单一协作型用户设定，无法有效衡量模型对不同背景、偏好、交互风格用户的服务适配性，聚合得分易掩盖细分用户群体的体验缺陷。

### 方法关键点
推出PersonaChatBench评估框架，固定同一底层任务，搭配多个绑定私人设卡的模拟用户，人设卡明确定义不同用户的专属需求、偏好、交互行为，从原生任务完成结果、用户人设需求满足度、模拟器保真度三个维度开展独立评估。

### 关键结果
跨6个领域测试20款LLM，发现任务表现与需求满足度在不同人设、领域间差异显著；强任务完成能力不必然对应个性化需求满足效果，模型的需求满足相对优势跨领域不具备一致性，框架可精准定位不同用户群体的服务缺口。
