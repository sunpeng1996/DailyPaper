---
title: 'ServerBench: How can your coding agents design specialized LLM serving systems?'
title_zh: ServerBench：编码Agent设计LLM推理服务系统能力评测基准
authors:
- Xinrui Zhong
- Zhiming Wang
- Yongqi Liu
- Zhaohui Wang
- Shanglin Yang
- Zikun Li
- Zhuoming Chen
- Beidi Chen
affiliations:
- Carnegie Mellon University
- University of Southern California
- InfiniAI Lab
arxiv_id: '2611.06841'
url: https://arxiv.org/abs/2611.06841
pdf_url: https://arxiv.org/pdf/2611.06841
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: Agent 编码能力评测 · LLM推理服务优化
tags:
- Coding Agent
- LLM Serving
- Benchmark
- Inference Optimization
- vLLM
one_liner: 提出首个面向编码Agent设计全链路LLM推理服务的评测基准，测得Claude Sonnet 5.5性能达vLLM的4.87倍
practical_value: '- 优化LLM服务的成本收益可直接复用「dollars per dollar」指标：统计符合延迟SLO的合格Token价值除以GPU成本，兼顾电商/推荐场景下的业务收益与算力投入，避免单纯追求吞吐量牺牲用户体验

  - 调优推理服务时需遵循「先优化容量再调并发」的策略：先完成引擎侧优化（如KV cache复用、投机解码、连续batching）再上调并发数，当新增会话导致TPOT恶化时及时限制负载，平衡吞吐量与延迟

  - 系统上线前的验证必须覆盖真实业务的请求特征：比如电商大促场景下的长短请求混合、多轮对话共享上下文、并发子请求等，孤立的短请求测试会遗漏长上下文卡顿、跨请求缓存崩溃等线上问题'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有编码Agent系统优化基准仅评测单个内核、代码补丁效果，存在三大缺陷：一是使用简化的独立请求负载，无法复现生产场景多轮会话、前缀共享、长短请求混合的真实特征；二是仅用吞吐量/加速比作为目标，忽略业务必须满足的延迟约束与GPU算力成本；三是仅做正确性校验，未覆盖真实负载下的尾延迟、会话完整执行等要求，无法支撑Agent设计完整可用的推理服务系统。

### 方法关键点
- 核心指标采用「dollars per dollar」：仅统计同时满足TTFT、TPOT延迟要求的Token价值，除以对应GPU运行成本，直接衡量单位算力投入的业务收益
- 采用真实编码Agent会话的状态回放机制，保留请求长度分布、多轮依赖、共享前缀、并行子任务分支等真实特征，请求进度直接受服务延迟影响
- 设计三重校验机制：除正确性外，额外校验完整请求执行、尾延迟达标、生成质量无损失，最终验证使用开发阶段未见过的会话种子，避免过拟合

### 关键实验
在3种模型+硬件部署场景（Gemma E4B/1×L40、Qwen3.5 9B/2×L40、Qwen3.8 27B INT4/2×L40）下，对比vLLM、SGLang两大工业界主流推理引擎基线，测试11款主流编码Agent：Claude Sonnet 5.5在Gemma E4B场景下得分达2.97，是vLLM基线的4.87倍；33次测试中22次产出可通过校验的系统，13次性能超过最强基线。

### 核心结论
高价值LLM推理服务优化必须同时完成三件事：协同容量提升与负载选择、基于真实业务workload采集实验反馈、针对优化引入的新执行路径做专项校验
