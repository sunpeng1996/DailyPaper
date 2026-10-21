---
title: 'The Token-Energy Law of LLM Decode: Active Bytes and Realized Time Account
  for Joules per Token'
title_zh: LLM解码的Token-能耗定律：活跃字节与实际时间决定单Token能耗
authors:
- Chenxu Niu
- Batuhan Sencer
- Wei Zhang
- Yong Chen
affiliations:
- NVIDIA Corporation
- Texas Tech University
- Texas Advanced Computing Center
arxiv_id: '2610.28576'
url: https://arxiv.org/abs/2610.28576
pdf_url: https://arxiv.org/pdf/2610.28576
published: '2026-10-20'
collected: '2026-10-21'
category: LLM
direction: LLM推理 · 能耗建模优化
tags:
- LLM inference
- energy efficiency
- KV cache
- GPU serving
- decode optimization
one_liner: 提出跨配置通用的LLM解码单Token能耗预测模型，最高预测误差仅3.73%
practical_value: '- 部署LLM驱动的Agent、生成式推荐、智能客服等业务时，可复用该模型框架快速估算不同batch size、用户对话/历史长度下的单token能耗，做服务成本的定量评估与优化

  - KV cache优化是长上下文场景降本核心：私有KV活跃字节随context长度线性增长，长用户历史的生成服务可优先落地KV量化、历史截断、前缀缓存等优化手段

  - 调度侧优先拉高适批大小：在满足服务延迟SLA的前提下，尽可能提高有效batch size，可降低单token能耗33%~47%，大幅提升GPU利用率和服务成本竞争力'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM部署规模爆发式增长，谷歌2026年5月单月处理token量达3.2千万亿，推理累计能耗已可匹敌训练能耗；现有能耗测算多为场景化实测，缺乏跨模型、硬件、部署配置的通用可解释模型，无法支撑能效优化的定量决策。
### 方法关键点
- 定义两个核心可观测维度：活跃字节（迭代内共享权重摊薄到单token的访问量、每个请求私有的KV cache读写量）、实际解码时间（单token平均耗时）
- 构建仿射形式的Token-能耗定律，仅需针对每个模型+硬件+运行时配置校准一次系数，即可跨batch、context长度、请求动态上下线场景做能耗预测
- 变量设计适配真实服务场景：有效batch size、token加权平均历史长度均可从调度trace直接提取，无需修改推理引擎
### 关键结果
实验覆盖Qwen2.5-7B/14B、Mistral-7B三个稠密模型，在NVIDIA GH200、GB300 GPU上测试，包含双GPU张量并行场景：
- 固定系数下，374组held-out测试的平均能耗预测误差最高仅3.73%
- 相比仅用时间、仅用字节的baseline，预测误差降低90%以上
- 同配置下，最大batch比最小batch单token能耗低33.2%~46.8%；context长度从6k升到14k，单token能耗接近翻倍
### 核心结论
LLM解码单token能耗由共享权重摊销、私有KV访问、执行时间三个独立维度共同决定，仅靠参数规模、算力无法准确估算能耗
