---
title: 'RiskChainBench: A Benchmark for Obfuscated Platform Message Restoration and
  Evidence-Grounded Web Investigation'
title_zh: RiskChainBench：混淆平台消息还原与证据驱动网页调查基准
authors:
- ZhuoXin Liu
- Zhiming Ma
- Ying Zhang
- Mengzheng Yang
- Yifan Wang
- Zhengqi Huang
- Yanhan Zhou
- Zekun Lin
- Jun Zhang
- Shun Zhang
affiliations:
- Baidu
- SmartFlowAI
- People's Public Security University of China
- Tsinghua University
- JD Technology
arxiv_id: '2609.16900'
url: https://arxiv.org/abs/2609.16900
pdf_url: https://arxiv.org/pdf/2609.16900
published: '2026-09-14'
collected: '2026-09-18'
category: Agent
direction: Agent 网页风险调查评测基准构建
tags:
- Benchmark
- WebAgent
- VLM
- RiskDetection
- TextRestoration
one_liner: 构建串联混淆文本还原与网页风险调查的评测基准，配套标注数据集与可重置沙箱
practical_value: '- 可复用混淆文本还原的任务设计思路，治理电商平台评论/私信内的隐晦引流、违规推广内容

  - 可参考「文本还原-网页验证」的两级风险判定链路，提升违规引流账号/内容的识别准确率

  - 可复用证据锚定的风险报告生成逻辑，降低风险判定的误召回，减少合规投诉'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有混淆文本、风险网页的评测基准相互独立，无法评估文本还原效果对下游风险取证的影响，不符合黑灰产引流全链路的实际治理场景。
### 方法关键点
1. 数据集包含3600条合成混淆文本还原样本、600组对应人工标注的本地网页环境
2. 设计两级串联任务：先还原混淆消息的意图与跳转目标，再用同一底座的VLM web agent访问目标站点生成带证据的风险报告，评测排除消息语义、域名信誉先验提示
3. 分别评测还原准确率、网页调查准确率，用跳转入口预测作为门控计算端到端效果
### 关键结果
10款测试模型的跳转入口Top-1准确率35.2%~95.2%，网页决策准确率26.3%~62.8%；web agent执行失败占网页任务错误的31.9%，是核心性能瓶颈，基准、评测协议与可重置本地沙箱已开源
