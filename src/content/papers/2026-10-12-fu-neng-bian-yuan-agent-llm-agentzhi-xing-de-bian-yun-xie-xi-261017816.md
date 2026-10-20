---
title: 'Empowering Edge Agents: A Systematic Analysis of Edge-Cloud Collaboration
  in LLM Agent Execution'
title_zh: 赋能边缘Agent：LLM Agent执行的边云协同系统性分析
authors:
- Pengcheng Huang
- Zhenghao Liu
- Shixin Ren
- Shi Yu
- Sijia Yao
- Yukun Yan
- Chaojun Xiao
- Maosong Sun
affiliations:
- Northeastern University
- Tsinghua University
- China Mobile Online Services Co., Ltd.
arxiv_id: '2610.17816'
url: https://arxiv.org/abs/2610.17816
pdf_url: https://arxiv.org/pdf/2610.17816
published: '2026-10-12'
collected: '2026-10-20'
category: Agent
direction: 边缘Agent · 边云协同架构优化
tags:
- EdgeAgent
- Edge-Cloud Collaboration
- LLM Agent
- Benchmark
- Privacy Preserving
one_liner: 提出EC²-Bench基准，系统分析长周期LLM Agent边云协同的性能、成本与隐私权衡
practical_value: '- 端侧Agent（如电商购物助手、本地推荐助手）落地可直接复用四类协同策略：端侧模型<10B时优先用步级外部路由策略，端侧模型≥27B时切换为边控云顾问模式，平衡性能、成本与用户隐私

  - 成本优化可参考量化结论：边云协同相比纯云执行最高节省77.3%的云调用成本，隐私暴露相比纯云最高降低84.3%，适合处理用户本地敏感行为数据的推荐/广告场景

  - 端侧小模型微调可优先优化两个核心能力：云调用时机决策能力、云侧指导指令遵循能力，可直接提升边云协同任务完成率3~4个百分点

  - 自研边云协同Agent评估体系可复用EC²-Bench的三维评估框架：任务性能、资源开销、隐私暴露，减少重复设计成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有边云LLM协同研究大多聚焦单Query的单次路由决策，而长周期Agent执行的云调用交错在完整执行轨迹中，会带来轨迹级的性能波动、资源开销累计、敏感数据泄露风险，此前缺乏统一的评估基准和系统性分析框架，相关规律认知不足。
### 方法关键点
- 构建EC²-Bench基准：包含128个可执行的数字工作区长周期Agent任务，覆盖工具调用、多步规划等典型场景，其中100个任务标注细粒度敏感信息单元
- 统一三维评估维度：任务性能（任务完成率、Pass3鲁棒性）、资源开销（云token成本、端侧FLOPs）、隐私暴露（上传至云的敏感信息占比）
- 覆盖四类主流协同策略：查询级路由、步级路由、边控云委托、边控云顾问
### 关键结果
用Qwen 2B/9B/27B/Plus作为端侧模型，GLM-5.3作为云模型，对比纯端、纯云基线：边云协同对比纯端最高提升27.22%任务完成率，对比纯云最高节省77.3%云成本，隐私暴露最高降低84.3%；端侧模型能力越强，不同协同策略的性能差从25.22%缩小至3.67%，但隐私暴露差仍高达66.23%；弱端模型更适合外部路由+直接云执行模式，强端模型更适合边控调用+云顾问模式。
### 核心结论
边云协同是长周期端侧Agent落地的最优路径，策略选择需随端侧模型能力迭代动态调整，隐私保护是不同协同策略的核心差异化指标
