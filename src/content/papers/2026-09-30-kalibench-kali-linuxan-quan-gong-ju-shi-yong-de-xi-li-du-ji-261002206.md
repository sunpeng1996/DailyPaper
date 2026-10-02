---
title: 'KaliBench: A Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux
  with Runtime-Free Verifiable Rewards'
title_zh: KaliBench：Kali Linux安全工具使用的细粒度基准，支持无运行时可验证奖励
authors:
- Pengfei Li
- Naufal Suryanto
- Sicheng Zhang
- Muzammal Naseer
affiliations:
- Khalifa University
- University of Western Australia
arxiv_id: '2610.02206'
url: https://arxiv.org/abs/2610.02206
pdf_url: https://arxiv.org/pdf/2610.02206
published: '2026-09-30'
collected: '2026-10-02'
category: Eval
direction: LLM工具调用 · 网络安全Benchmark
tags:
- Benchmark
- Cybersecurity
- Tool-Calling
- NL-to-CLI
- Reward-Engineering
- LLM-Evaluation
one_liner: 构建含8504条Kali工具查询-命令对的NL转CLI细粒度基准，支持无运行时奖励训练
practical_value: '- 多阶段数据校验pipeline（LLM校验+沙箱执行+人在回路+语义去重）可直接复用在业务领域工具调用/指令转操作数据集构建，比如电商运营指令转后台CLI、Agent调用内部接口数据集的质量管控

  - 无运行时可验证奖励的设计思路可迁移到高风险/高成本接口的Agent训练，把工具调用拆解为工具选择、可选参数、位置参数等可静态校验维度，无需实际执行就能生成RL奖励信号，避免错误执行带来的业务损失

  - 三级分层评估模式（无提示/候选工具提示/完整文档提示）可复用在业务Agent的能力拆解评估，精准定位故障点是工具选择错误还是参数生成错误，指导针对性优化

  - 8B小参数模型经过领域SFT+GRPO强化学习训练后性能可追平685B MoE模型，该结论可复用在垂直业务小模型优化，大幅降低推理成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有网络安全领域LLM评估要么聚焦知识问答，要么测端到端Agent任务，未直接评估自然语言转可执行CLI命令的能力；而安全操作对CLI语法精度要求极高，微小的参数顺序、flag拼写错误都会导致执行失败，同时现有工具调用基准均基于schema定义的API，不适用无schema的CLI场景。

### 方法关键点
- 基于Kali Linux官方工具文档生成27.7K初始查询-命令对，经过LLM校验、沙箱执行验证、人在回路优化、SemHash语义去重，最终得到8504条高质量标注对，覆盖1642个工具、23个能力维度、5个安全攻击生命周期阶段
- 设计三级评估模式：Unrestricted（仅输入查询）、Restricted（提供20个候选工具名）、Hinted（提供工具完整文档），拆分工具选择准确率、可选参数F1、位置参数F1、完全匹配准确率等细粒度指标，实现能力分层评估
- 支持无运行时可验证奖励，基于静态shell语法解析即可生成多维度奖励信号，可直接用于SFT和GRPO强化学习训练

### 关键实验
测试24种通用和安全垂域大模型，无提示模式下开源模型最高完全匹配准确率仅41.3%（GLM-5.2 753B）；基于8B参数RedSage模型用KaliBench做SFT+GRPO训练后，平均总分达79.2%，接近685B DeepSeek-V3.2的80.2%水平。

### 核心结论
工具选择和参数构造是完全独立的两个挑战，约束候选工具集几乎能解决所有工具选择错误，但可选参数生成的正确性才是无schema工具调用的核心瓶颈
