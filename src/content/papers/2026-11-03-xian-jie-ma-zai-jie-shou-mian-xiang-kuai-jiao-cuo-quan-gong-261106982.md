---
title: 'Decode Before You Hear: Speculative Listening for Chunk-Interleaved Full-Duplex
  Speech Language Models'
title_zh: 先解码再接收：面向块交错全双工语音大模型的推测监听技术
authors:
- Yutong Bian
- Yanglin Zhang
- Yuxiang Wang
- Luoyuan Zhang
- Rongshen He
- Zihao Wang
- Junwen Qiu
- Jiaqi Li
- Zhizheng Wu
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Amphion Technology Co., Ltd.
arxiv_id: '2611.06982'
url: https://arxiv.org/abs/2611.06982
pdf_url: https://arxiv.org/pdf/2611.06982
published: '2026-11-03'
collected: '2026-11-06'
category: LLM
direction: LLM低延迟推理 · 推测解码优化
tags:
- Speculative Decoding
- Low Latency
- Full Duplex SLM
- Training Free
- Inference Optimization
one_liner: 提出无训练无损的推测监听框架，大幅降低全双工语音大模型的响应与工具调用延迟
practical_value: '- 实时交互Agent场景（如电商智能客服、直播AI助手）可复用该无训练推测思路，利用算力空闲窗口预生成候选结果，无需微调即可降低响应延迟

  - 工具调用类Agent任务可借鉴假设输入预生成+首token次优分支补充的方案，最高可实现二十余倍的工具调用速度提升

  - 流式生成场景可复用跨块候选池设计，平衡算力利用率与响应速度，将交互延迟控制在人类可接受范围'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
块交错全双工语音大模型存在算力负载不均问题：监听块等待音频时算力大量空闲，而发言、工具调用块的串行生成会带来高响应延迟，严重影响实时交互体验。
### 方法关键点
基于两个核心观测结论设计框架：1）95.3%的下一个音频块不会改变模型输出；2）88%的输出变更从首个token开始。提出无训练无损的Speculative Listening框架：空闲时段以静音为假设输入预生成下一块的候选结果，额外补充首token次优结果的分支候选，所有候选存入跨块假设池，真实音频到达后直接核验匹配的候选即可输出。
### 关键结果数字
在8任务基准TickTock-Bench上，发言块加速2.6-2.8x，工具调用块最高加速23.4x；响应前解码延迟平均降低73%至74-241ms，接近人类对话200ms的间隔gap，最大实时滞后降低94.4%
