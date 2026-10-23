---
title: 'Hidden Messages Between Diffusion Language Model Agents: Causal Evidence for
  Latent Communication'
title_zh: 扩散语言模型智能体间的隐式消息：潜层通信的因果证据与时序优化
authors:
- Alan-Barsag Gazzaev
- Alexey Gavrilov
- Sergey Muravyov
- Ilya Makarov
affiliations:
- ITMO University
- HSE University
arxiv_id: '2610.28905'
url: https://arxiv.org/abs/2610.28905
pdf_url: https://arxiv.org/pdf/2610.28905
published: '2026-10-19'
collected: '2026-10-23'
category: MultiAgent
direction: 多智能体隐通信 · 扩散LM时序优化
tags:
- Multi-Agent Communication
- Diffusion LM
- Causal Audit
- Latent Communication
- Agent Collaboration
one_liner: 验证扩散LM智能体可通过压缩隐状态传递有效信息，且传输时机比交互次数更重要
practical_value: '- 多智能体协作场景可复用轻量适配器通信方案，冻结大模型backbone仅训练task-specific的消息编解码模块，大幅降低训练成本，适合电商导购/推荐多Agent分工（如用户理解Agent、召回Agent、内容生成Agent协作）场景

  - 可借鉴因果审计方法验证隐通信有效性，通过替换/移除消息的对照实验排除通用激活等干扰，确保Agent间传递的是任务相关信息，避免伪收益

  - 多Agent交互时序设计可参考任务依赖匹配规则：若各Agent可独立处理自有数据（如召回/排序/冷启动分模块并行处理），采用单次晚融合方案比多轮交互效率、精度双高，适合推荐系统多模块协作降本提效

  - 仅当任务存在强顺序依赖（如用户query理解→召回→重排链路，上游结果直接影响下游计算）时，才需要多轮早期交互，避免盲目增加交互轮次浪费算力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Diffusion LM多智能体系统仅在生成结果解码为文本后才进行通信，丢弃了生成过程中丰富的连续隐状态信息；同时此前的隐通信研究缺乏严格因果验证，无法区分性能提升来自有效信息传递还是通用激活、额外算力等干扰因素，无法确认隐信道的实际价值。

### 方法关键点
- 设计HIDDENMESSAGES通信框架：发送端将扩散去噪隐状态压缩为4个128维带符号稠密向量作为传输消息，接收端通过残差融合（小模型）或虚拟前缀（7B大模型）接入，全程保留各智能体独立上下文、生成轨迹与随机种子，不共享生成画布
- 仅训练轻量任务专属通信适配器，冻结Diffusion LM主干，训练成本极低；引入因果审计机制：通过移除消息、替换为其他样本的消息两种干预，分别验证信道存在价值与消息内容的有效性
- 对比两种交互时序：多轮循环交互、仅决策前单次晚传输，验证传输时机对效果的影响

### 关键结果
三个测试场景覆盖合成推理、跨依赖任务、自然科学问答：Tiny-A2D合成任务上匹配消息比乱序消息准确率高63.6个百分点；Dream-7B跨依赖任务上匹配消息准确率达100%，乱序消息为0；QASC分布式问答上单轮晚传输准确率达87.8%，比4轮循环交互高7个百分点，错配消息比无通信准确率低25.8个百分点。

最值得记住的结论：多智能体交互的传输时机比交互次数更重要，匹配任务依赖结构的时序设计比盲目增加交互轮次效果更好
