---
title: 'J-Comm: Jacobian-Guided Latent Communication between LLM Agents'
title_zh: J-Comm：Jacobian引导的LLM Agent间隐式通信框架
authors:
- Xiangwei Wang
- Wei Wang
- Sachith Seneviratne
- Ken Chen
- Yu Xia
- Peng Wang
- Saman Halgamuge
affiliations:
- The University of Melbourne
- Shanghai Jiao Tong University
arxiv_id: '2610.32871'
url: https://arxiv.org/abs/2610.32871
pdf_url: https://arxiv.org/pdf/2610.32871
published: '2026-10-23'
collected: '2026-10-26'
category: Agent
direction: 多智体隐式通信框架优化
tags:
- MultiAgent
- Latent Communication
- Jacobian Lens
- LLM
- Communication Protocol
one_liner: 提出免训练Jacobian引导双信道LLM多智体隐式通信框架，性能更优且大幅降低生成token量
practical_value: '- 双信道隐式通信架构可直接迁移到电商多Agent系统，比如用户意图理解Agent和推荐排序Agent之间直接传递中间特征，避免文本转译的信息损耗和时延，适配不同大小的模型部署

  - GEAR的候选几何加权思路可复用在query改写、生成式推荐的候选token排序环节，基于embedding相似度+预测概率重加权，无需额外训练即可提升候选合理性

  - 跨模型通信的Jacobian锚点重构方法无需对齐模型隐层宽度、无需共享KV cache，可降低业务多Agent系统的架构约束，支持异构模型协作'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM多智体系统多采用文本通信，生成token开销大、推理链路长；隐式通信方案普遍要求对齐模型结构、共享KV cache，异构模型适配性差，且连续推理阶段未考虑候选token的语义空间一致性，推理质量不稳定。

### 方法关键点
- 免训练GEAR连续推理模块：基于候选token embedding的余弦相似度计算几何支持度，与预测概率相乘重加权，单调优化候选集的空间一致性，无需额外训练或反馈模块。
- H+J双信道通信接口：H信道传递发送端反馈分布权重，在接收端用自身embedding表重构输入；J信道基于Jacobian lens提取发送端中间状态的Top-P token锚点特征，接收端用自身Jacobian字典重构后在prefill阶段注入中间层，无需对齐模型隐层宽度、无需共享KV cache。

### 关键结果
在Qwen3-8B→Qwen3-4B跨大小模型通信场景下，7个基准测试均取得最优结果：MATH500准确率94.80%、GPQA-Diamond准确率54.55%、AIME2024+2025准确率73.33%、ALFWorld成功率62.93%；相比TextMAS基线，性能提升1.29~8.59pp，生成token量降低19.2%~74.8%；跨模型家族（Qwen3-8B→Llama-3.2-3B）场景也优于文本通信基线。

最值得记住的一句话：异构LLM多智体的隐式通信无需对齐模型结构，基于共享token对应的特征锚点即可实现高效信息传递，同时兼顾效果提升与推理降本。
