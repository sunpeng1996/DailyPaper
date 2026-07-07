---
title: 'DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive
  Generation'
title_zh: DSpark：基于半自回归生成的置信度调度投机解码框架
authors:
- Xin Cheng
- Xingkai Yu
- Chenze Shao
- Jiashi Li
- Yunfan Xiong
- Yi Qian
- Jiaqi Zhu
- Shirong Ma
- Xiaokang Zhang
- Jiasheng Ye
affiliations:
- Peking University
- DeepSeek-AI
arxiv_id: '2607.05147'
url: https://arxiv.org/abs/2607.05147
pdf_url: https://arxiv.org/pdf/2607.05147
published: '2026-07-06'
collected: '2026-07-07'
category: LLM
direction: LLM推理优化 · 投机解码
tags:
- Speculative Decoding
- LLM Inference
- Serving Optimization
- Semi-Autoregressive
- Throughput Acceleration
one_liner: 提出半自回归+负载感知置信调度的投机解码框架，生产环境LLM生成提速60%-85%
practical_value: '- 电商Agent/LLM客服场景可直接复用DSpark的半自回归结构+置信调度策略，在不损失生成质量的前提下提升用户侧响应速度60%+，降低高并发时段的服务超时率

  - 生成式推荐（GenRec）场景的大规模LLM推理服务可借鉴其硬件感知调度逻辑：预压测得到不同batch下的SPS曲线后，动态裁剪低置信度生成后缀，同等GPU资源下提升系统整体吞吐30%以上

  - 可复用轻量序列头设计思路：在并行生成主干后追加低秩Markov/RNN头，仅增加<2%的推理延迟就能缓解并行生成的token依赖缺失问题，提升生成序列一致性'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有并行投机解码的draft模型缺少块内token依赖，接受率随序列长度快速衰减；同时固定长度的全量验证会浪费batch容量在高拒绝风险的token上，高并发场景下吞吐下降严重，是LLM生产服务（如电商客服、Agent、生成式推荐）的核心性能瓶颈。

### 方法关键点
- 半自回归生成架构：并行主干（基于DFlash）负责大部分计算，维持单次前向生成长块的低延迟优势；追加轻量低秩Markov/RNN序列头，注入块内token依赖，缓解后缀接受率衰减，额外延迟仅0.2%-1.3%
- 置信度调度验证：新增轻量置信头预测每个位置的前缀存活概率，通过Sequential Temperature Scaling校准后，结合硬件预压测的SPS（每秒步数）曲线，贪心分配验证预算给高预期收益的token，动态裁剪低置信后缀
- 训练策略：联合交叉熵、分布匹配、置信度三类损失，位置加权优先优化靠前token的预测精度，全程冻结目标大模型的嵌入和LM头

### 关键实验
离线覆盖数学推理、代码生成、日常聊天三类场景，对比Eagle3、DFlash等SOTA drafter，在Qwen3-4B/8B/14B上平均接受长度分别比Eagle3高30.9%/26.7%/30.0%，比DFlash高16.3%/18.4%/18.3%。线上部署在DeepSeek-V4生产环境，同等吞吐下用户侧生成速度提升60%-85%；严格SLA下避免吞吐骤降，拓展了服务的Pareto边界。

最值得记住的一句话：投机解码的优化不仅要提升draft本身的接受率，更要结合系统负载动态分配验证资源，才能在生产环境下实现真正的吞吐-延迟双优。
