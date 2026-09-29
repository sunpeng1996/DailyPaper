---
title: 'BaRe-Mem: Bayesian Reliability Memory for Robust and Adaptive Agent Consultation'
title_zh: 面向鲁棒自适应多智能体咨询的贝叶斯可靠性记忆框架BaRe-Mem
authors:
- Peilin Feng
- Zhengyang Huang
- Soujanya Poria
affiliations:
- Nanyang Technological University
- Peking University
arxiv_id: '2609.35551'
url: https://arxiv.org/abs/2609.35551
pdf_url: https://arxiv.org/pdf/2609.35551
published: '2026-09-27'
collected: '2026-09-29'
category: MultiAgent
direction: 多智能体协作 · 可靠性记忆
tags:
- Multi-Agent
- Bayesian Regression
- Reliability Estimation
- Attention Modulation
- Task Routing
one_liner: 提出贝叶斯在线可靠性记忆，解决多智能体咨询的误导信息鲁棒性问题
practical_value: '- 可复用贝叶斯线性回归+Kalman增益的在线更新机制，用于电商多Agent导购/客服场景的外部信息（商家回答、工具返回结果）可靠性动态打分，无需全量重训，适配流式数据

  - 注意力logits加偏置的trick可直接用于RAG+推荐场景，对不同可信度的召回片段/广告素材做注意力降权，无需修改LLM结构，无额外训练成本

  - 「是否咨询外部信息」的阈值判断逻辑可迁移到搜索推荐多源结果融合场景，当自主排序结果置信度足够高时，直接截断低可信外部召回结果，降低坏case率

  - 稀疏反馈下的有效学习特性可用于标注成本高的业务场景，仅需1%左右的标注即可得到可用的可靠性估计，大幅降低标注开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多智能体咨询中Advisor能力随任务异构性差异极大，误导信息会导致中心模型放弃原本正确的判断，表现反而低于自主推理；现有方法仅存储历史交互，无法动态评估外部来源的任务级可靠性，也无法判断何时应该放弃咨询、优先自主推理，高能力模型甚至会出现协作负增益。

### 方法关键点
- 基于中心LLM的隐层表示建模问题共享信念与答案专属信念，结合来源one-hot编码生成候选表示，用贝叶斯线性回归建模候选正确性，支持Kalman增益的在线秩一更新，无需全量重算后验
- 用可靠性估计值修改注意力logits偏置，动态降权低可靠Advisor的响应，无额外可训练参数，不修改原有模型结构
- 建模咨询能力与自主推理能力的线性插值公式，动态判断当前任务应该咨询外部还是自主推理，阈值随中心模型自主能力自适应调整

### 关键实验
在9个基准（GSM8K、MMLU、MuSiQue等）、6个中心模型上验证，对比辩论、多数投票等baseline：100%误导信息的能力挑战任务集上，Qwen3-14B精度达68.6%，比无咨询基线高2.1pp，比普通咨询基线高18pp；仅需1%左右的标注反馈即可获得显著性能增益；在MuSiQue多智能体路由场景下，比历史成功率路由的任务完成率高3.4pp，能更早识别高能力worker。

**最值得记住的一句话**：多智能体协作不仅要判断该信谁，更要判断什么时候不需要信别人，自主推理反而效果更好。
