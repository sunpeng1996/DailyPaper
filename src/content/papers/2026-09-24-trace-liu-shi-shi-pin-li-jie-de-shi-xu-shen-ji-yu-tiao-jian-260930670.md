---
title: 'TRACE: Temporal Audit and Condition-aware Evaluation of Streaming Video Understanding'
title_zh: TRACE：流式视频理解的时序审计与条件感知评估
authors:
- Yibo Ma
- Qianqian Zhang
- Peng Liu
- Tiancheng Zhao
affiliations:
- Om AI Research
arxiv_id: '2609.30670'
url: https://arxiv.org/abs/2609.30670
pdf_url: https://arxiv.org/pdf/2609.30670
published: '2026-09-24'
collected: '2026-09-28'
category: Eval
direction: 多模态模型 · 流式视频理解评估
tags:
- Streaming Video Understanding
- MLLM
- Evaluation Benchmark
- Causal Protocol
- Temporal Processing
one_liner: 提出流式视频理解的条件感知评估框架TRACE，挖掘单指标掩盖的系统运行行为差异
practical_value: '- 直播/短视频信息流推荐的多模态模型评估可借鉴多维度指标设计，除准确率外加入时延、误触发率、完成度等业务相关指标，避免单指标误导选型

  - 实时流式输入的Agent系统（如直播审核、实时内容理解）可复用Core-Adapter协议架构，控制信息可见性同时记录处理事件，便于归因模型运行时行为

  - 直播场景的触发类任务（如商品弹窗时机、互动文案触发）可参考证据时序+触发条件标注方案，优化触发准确率与时延的tradeoff'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有流式视频理解评估仅输出单任务分数，未明确证据生效时间、视觉历史维护、响应触发逻辑，相似分数背后的系统实际workload、故障模式、运行行为差异被掩盖，离线与流式模型无法公平对比。
### 方法关键点
1. 构建带证据时序、指令依赖触发标注的时序审计视觉任务库；
2. 设计统一因果Core-Adapter协议，控制信息可见性同时记录历史处理、响应事件；
3. 输出覆盖答案质量、时延、响应选择行为、workload、完成度、可靠性的多维度报告。
### 关键结果
在517条视频的1240条记录上评测8个公开模型/8种配置，发现近乎相同的QA准确率下，完成度、答案有效性、生成workload差异显著，同时可拆分出响应质量、时延、误报、漏报四个主动性能维度。
