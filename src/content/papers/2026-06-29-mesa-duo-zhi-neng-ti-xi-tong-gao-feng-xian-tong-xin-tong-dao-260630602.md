---
title: 'MESA: Prioritizing Vulnerable Communication Channels for Securing Multi-Agent
  Systems'
title_zh: MESA：多智能体系统高风险通信通道优先级排序框架
authors:
- Kunyang Li
- Kyle Domico
- Jonathan Gregory
- Patrick McDaniel
affiliations:
- University of Wisconsin–Madison
arxiv_id: '2606.30602'
url: https://arxiv.org/abs/2606.30602
pdf_url: https://arxiv.org/pdf/2606.30602
published: '2026-06-29'
collected: '2026-06-30'
category: MultiAgent
direction: 多智能体系统通信安全风险评估
tags:
- Multi-Agent System
- Communication Security
- Risk Ranking
- Graph Metric
- Proactive Defense
one_liner: 提出无标注MESA框架，主动排序多智能体通信边安全优先级，无需攻击轨迹标注
practical_value: '- 电商多Agent导购/售后系统可复用MESA的边排序逻辑，优先加固核心Agent间的通信通道，有限安全资源投入下可拦截3倍攻击

  - 可借鉴「图特征+动态探针（ablation/masking）」的无标注风险评估范式，不需要攻击样本即可识别系统脆弱点，适配业务冷启动安全需求

  - LangGraph开发的Agent工作流可直接对接MESA做前置风险排查，提前定位高风险通信边，降低恶意prompt注入等攻击的扩散影响'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
LLM驱动的多智能体系统（MAS）已落地多个高价值场景，但跨Agent通信通道的攻击面缺少可落地的评估方案，且不同通道攻击影响差异极大，单条被攻陷的通道最高可导致75%的攻击成功率，安全资源有限时无优先级的防护效率极低。
### 方法关键点
1. 提出无标注的MESA框架，无需攻击样本即可主动排序MAS中通信边的安全优先级
2. 融合6种图论指标+2种动态探针（ablation、masking），评估通信边被攻陷后对系统决策的影响程度
### 关键结果数字
- 跨3种MAS场景、8种网络拓扑、5款开源LLM（Qwen、Llama、Gemma系列）测试，MESA的通道风险排序与实际边攻击成功率的平均Spearman相关系数ρ=0.60，最高达0.73
- 资源受限场景下，监控MESA排序Top10%的通信边，拦截的成功攻击量是随机分配资源的3倍
