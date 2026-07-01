---
title: 'TraceLab: Characterizing Coding Agent Workloads for LLM Serving'
title_zh: TraceLab：面向LLM服务的编码Agent工作负载特征分析
authors:
- Kan Zhu
- Mathew Jacob
- Chenxi Ma
- Yi Pan
- Stephanie Wang
- Arvind Krishnamurthy
- Baris Kasikci
affiliations:
- University of Washington
- Wuhan University of Technology
- Shanghai Jiao Tong University
arxiv_id: '2606.30560'
url: https://arxiv.org/abs/2606.30560
pdf_url: https://arxiv.org/pdf/2606.30560
published: '2026-06-29'
collected: '2026-06-30'
category: Agent
direction: Agent工作负载 · LLM服务优化
tags:
- Coding Agent
- LLM Serving
- KV cache
- Workload Analysis
- Tool Calling
one_liner: 发布跨厂商4300+真实编码Agent会话Trace，分析负载特征并给出LLM服务优化方向
practical_value: '- 做电商/广告场景多轮Agent服务（如导购Agent、投放优化Agent）时，可参考本文KV cache优化策略：针对用户思考间隔>5分钟的会话做缓存预取/主动保活，可减少45%左右冗余prefill，降低10%+API成本

  - 设计多步工具调用类Agent架构时，可复用观测结论：单步LLM输出短、工具调用长尾特征明显，优先实现多工具批量调用、低开销工具调用通路，可有效降低端到端时延

  - 若自研Agent服务引擎，可参考本文成本结构：prefix缓存读取占总开销近60%，针对性落地KV压缩、稀疏attention方案的降本投入产出比远高于优化生成环节'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
编码Agent已成为Agent LLM的核心落地场景，GitHub Copilot等产品用户量已突破千万级，但现有公开LLM服务Trace多聚焦单轮聊天、代码补全场景，未覆盖编码Agent特有的长会话、多步工具调用、人机间隔等特征，无法支撑LLM服务系统的针对性优化，行业缺乏真实场景的负载数据指导工程落地。
### 方法关键点
- 收集8个月内43名开发者的Claude Code、Codex两类主流编码Agent使用日志，覆盖23个模型版本，经格式归一化、隐私匿名化处理后，开源Trace数据集、采集与分析pipeline
- 从会话层、单步LLM调用层、工具调用层、prefix缓存层四个维度拆解工作负载特征，量化各环节的时延、token消耗、成本分布，挖掘优化空间
### 关键结果
- 数据集包含4265个有效会话，累计35.7万次LLM调用、43.2万次工具调用，对应API成本约4万美元
- 核心负载特征：单会话平均完成1个用户请求需要8.8次LLM调用、10.8次工具调用；prefix缓存读取占总输入token的95%，贡献了59.5%的总API成本；单步LLM平均输出仅214token，远低于输入长度；全局prefix缓存命中率达95.7%，但用户思考间隔超过5分钟后命中率大幅下降，实际冗余prefill是理想无驱逐缓存的5.3倍
- 基于观测特征的优化方案可降低12.8%的总服务成本，减少45.9%的冗余prefill token
### 核心结论
多步工具调用类Agent的服务成本核心来自重复的上下文读取，而非生成环节，针对性优化缓存策略的投入产出比远高于优化生成性能
