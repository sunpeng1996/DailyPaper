---
title: 'Think Short, Defer Smart, Act, and Repeat: Calibrated Reasoning and Uncertainty-Aware
  Deferral for Edge LLM Agents'
title_zh: 面向边缘LLM Agent的校准推理与不确定性感知云边协同框架
authors:
- Amirmohammad Farzaneh
- Osvaldo Simeone
affiliations:
- Northeastern University London
- Institute for Intelligent Networked Systems (INSI)
arxiv_id: '2607.26865'
url: https://arxiv.org/abs/2607.26865
pdf_url: https://arxiv.org/pdf/2607.26865
published: '2026-07-29'
collected: '2026-07-30'
category: Agent
direction: 边缘LLM Agent · 云边协同推理优化
tags:
- LLM Agent
- Edge Deployment
- Uncertainty Quantification
- Calibration
- Cloud-Edge Collaboration
one_liner: 融合思考收敛探测与不确定性云降级的边缘LLM Agent框架，提供效果与成本的可证保障
practical_value: '- 端侧交互Agent（如电商导购、端搜推荐意图理解Agent）可接入轻量收敛探针，无需等待全量思考链生成即可输出动作，大幅降低端侧推理延迟，提升用户交互体验

  - 云边分级LLM服务部署可复用PPL作为不确定性阈值规则，仅将高不确定请求转发至云端大模型，在保障业务效果的同时降低云端算力成本；可通过LTT校准流程为业务SLA提供可量化的统计保障

  - 多步交互Agent（如电商客服、导购Agent）应避免不必要的长思考链，过长推理会导致模型对错误决策过度自信，反而抑制降级机制触发；提前截断得到的不确定性信号更能反映真实决策风险'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
边缘LLM Agent落地面临三重核心矛盾：端侧算力、内存、功耗有限，但ReAct范式的思考链生成占推理成本的大头；端侧小模型效果不稳定容易出错，但全量请求转云端会带来过高的延迟、带宽和成本；过度推理还会让模型对错误动作过度自信，干扰不确定性降级机制的判断，亟需同时优化推理效率、效果可靠性和云调用成本。
### 方法关键点
- 设计轻量EMA收敛探针，监控边缘LLM推理过程的隐层状态，当探测到动作决策已经收敛时立即截断思考链，避免冗余计算
- 采用生成动作的PPL作为不确定性评分，超过阈值则将该步请求降级到云端大模型处理，避免端侧错误传递累积
- 通过多目标Learn-Then-Test（LTT）流程联合校准截断阈值和降级阈值，提供有限样本下的期望奖励、云调用率的可证保证，最终选择满足约束下推理成本最低的参数组合
### 关键结果
在GSM8K、HotpotQA、MBPP、家庭机器人四个ReAct基准测试上验证，对比仅思考校准、仅校准降级等基线：TSDS在HotpotQA、MBPP、家庭机器人任务上比仅降级基线减少43%~73%的单轮思考计算量，同时满足预设的奖励下限和云调用率上限；MBPP任务下相比全推理降级基线减少64%的思考token，云调用率仅为后者的一半。
### 核心洞见
思考校准和云降级是高度协同的，过早截断会提升不必要的云调用，过度推理会让模型过度自信掩盖真实不确定性，联合校准才能在效果和成本间拿到最优平衡。
