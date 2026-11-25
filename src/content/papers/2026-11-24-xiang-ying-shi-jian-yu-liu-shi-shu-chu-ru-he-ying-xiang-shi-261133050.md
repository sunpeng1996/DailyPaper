---
title: Worth the Wait? How Response Time and Streaming Shape Judgments of Generative
  AI Answers and Chatbot Engagement
title_zh: 响应时间与流式输出如何影响生成式AI回答评价与用户交互意愿
authors:
- Zihan Chen
- Di Zhu
- Lei Nico Zheng
affiliations:
- Stevens Institute of Technology
- University of Massachusetts Boston
arxiv_id: '2611.33050'
url: https://arxiv.org/abs/2611.33050
pdf_url: https://arxiv.org/pdf/2611.33050
published: '2026-11-24'
collected: '2026-11-25'
category: LLM
direction: LLM 交互体验与服务优化
tags:
- LLM
- streaming
- response latency
- user engagement
- caching
- AI evaluation
one_liner: 通过三组大规模实测量化流式输出、响应速度对生成式AI用户偏好与交互意愿的影响
practical_value: '- 电商智能客服、导购Agent优先采用流式输出模式，相同回答内容下可大幅提升用户对回答质量的感知，无需额外优化模型即可提升满意度

  - 业务侧做LLM服务时延预算时，优先保障首包响应速度，避免首次交互过慢降低用户后续提问意愿，平衡流式输出增益与整体时延损失

  - 做LLM应用A/B测试或偏好评估时，需控制流式输出、响应速度变量，避免交付方式差异干扰对模型本身回答质量的判断'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前生成式AI服务的响应交付方式（流式输出/缓存直接返回）、响应速度差异大，盲测偏好排序默认仅与回答文本质量相关，未考虑交付环节的干扰，业界对响应时延的用户影响认知存在矛盾。
### 方法
开展三组真实场景随机对照实验：1）法国政府chatbot arena的同内容不同交付方式对照；2）32万+会话的拥塞导致流式响应变慢的影响分析；3）437万+WildChat真实ChatGPT会话的时延对留存的影响分析。
### 关键结果
相同内容下，流式输出比直接返回缓存内容的盲测胜率高25.8个百分点（流式胜率57% vs 缓存直接返回胜率29%），后者被认为更不完整、更肤浅、错误率更高；流式响应变慢不会影响用户对回答质量的投票，但首次交互过慢会显著降低用户后续提问意愿与继续对话概率
