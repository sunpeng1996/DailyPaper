---
title: 'MetaStrategy: Generative Ranking with Executable LLM Strategies'
title_zh: MetaStrategy：基于可执行LLM策略的工业级生成式排序框架
authors:
- Chengyu Lai
- Jiuning Lin
- Zhibo Xiao
- Xiaodong Zhu
- Ruiquan Lan
- Bin Zhang
- Zihong Huang
- Wendong Zhang
- Chuxin Chen
- Yinjiang Cai
affiliations:
- Taobao & Tmall Group of Alibaba
- Wuhan University
- The University of Hong Kong
- University of Cambridge
arxiv_id: '2608.09440'
url: https://arxiv.org/abs/2608.09440
pdf_url: https://arxiv.org/pdf/2608.09440
published: '2026-08-10'
collected: '2026-08-11'
category: GenRec
direction: 生成式推荐 · LLM可执行排序策略
tags:
- Generative Ranking
- LLM4Rec
- Multi-Objective Ranking
- Reinforcement Learning
- Knowledge Distillation
one_liner: 让LLM生成结构化可执行排序策略，淘宝首页上线后交易金额提升2.83%
practical_value: '- LLM落地工业排序系统可优先采用「生成可执行参数而非直接生成item序列」的架构，LLM在异步近线生成结构化JSON配置，同步路径仅做参数lookup，完全不增加线上RT，兼容现有成熟排序链路无需重构

  - 训练LLM排序策略时可复用现有生产链路做离线replay，不需要暴露给用户流量，搭配「被选中+相对排名+基线提升」三类组合奖励做RL优化，避免直接对齐在线反馈的风险

  - 大模型蒸馏可采用Evaluator路由的奖励增强on-policy distillation：同请求下先对比多个Teacher生成的策略在Evaluator的得分，仅用最优Teacher指导小模型，0.8B小模型效果即可超过4B大模型

  - 可通过自竞争课程学习缓解RL训练的策略坍塌问题：把高频出现的有效策略冻结为新的Generator加入竞争池，迫使LLM学习更多样的请求适配策略'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业级推荐排序需要同时兼顾用户体验、商业转化、运营规则、合规护栏等多目标，现有生成式排序方案直接生成item序列，难以兼容成熟的预测模型、运营规则与风控体系，而人工配置的全局策略无法做到请求级个性化适配，多目标调优还易出现规则冲突问题。
### 方法关键点
- 采用Generator-Evaluator（GE）范式，LLM不直接生成item序列，而是输出符合固定schema的JSON格式可执行排序策略，包含目标权重、内容/品类偏好、体验约束、置顶策略5类参数，经校验编译后控制独立Generator，与现有生产Generator共同竞争，由全局列表级Evaluator选择最优排序结果
- 训练基于生产链路replay环境，重放历史请求的候选集、精排得分，执行全量生产重排链路获取反馈，无需占用用户流量；奖励由被Evaluator选中、相对排名、相对基线提升三类信号组合而成
- 引入自竞争课程学习，将高频有效策略冻结为新Generator加入竞争池，缓解RL训练的策略坍塌问题；采用Evaluator路由的奖励增强on-policy蒸馏，将多个4B Teacher的能力压缩到0.8B Student，降低推理成本
- 上线采用Diff触发的近线生成架构，仅当用户上下文变化超过阈值才触发LLM推理，同步路径仅读取预生成的策略，无额外RT开销
### 关键结果
在淘宝首页猜你喜欢场景开展7天随机A/B测试，对比生产基线，MetaStrategy拿下27.93%的GE调用选择权，点击PV提升2.11%，商品详情页PV提升3.12%，交易金额提升2.83%，无明显RT增加。
> 最值得记住的一句话：LLM落地工业推荐的最优路径不是替代现有成熟链路，而是作为策略层拓展现有系统的决策空间，兼顾灵活性和稳定性。
