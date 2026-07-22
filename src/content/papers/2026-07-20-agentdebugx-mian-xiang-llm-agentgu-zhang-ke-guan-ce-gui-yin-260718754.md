---
title: 'AgentDebugX: An Open-Source Toolkit for Failure Observability, Attribution,
  and Recovery in LLM Agents'
title_zh: AgentDebugX：面向LLM Agent故障可观测、归因与恢复的开源工具包
authors:
- Kunlun Zhu
- Xuyan Ye
- Zhiguang Han
- Yuchen Zhao
- Bingxuan Li
- Weijia Zhang
- Muxin Tian
- Xiangru Tang
- Pan Lu
- James Zou
affiliations:
- University of Illinois Urbana-Champaign
- University of Toronto
- Google
- Stanford University
arxiv_id: '2607.18754'
url: https://arxiv.org/abs/2607.18754
pdf_url: https://arxiv.org/pdf/2607.18754
published: '2026-07-20'
collected: '2026-07-22'
category: Agent
direction: Agent 故障诊断与自动恢复
tags:
- LLM Agent
- Debugging
- Root Cause Analysis
- Observability
- Self-Correction
one_liner: 开源LLM Agent闭环调试框架，实现故障检测-根因定位-修复-重跑全链路，修复效率是基线2-3倍
practical_value: '- 电商导购Agent、多Agent推荐系统可直接接入AgentDebugX的Detect-Attribute-Recover-Rerun闭环，快速定位Agent执行失败根因（如工具调用错误、促销规则理解偏差、用户意图匹配错误），大幅降低线上故障排查成本

  - DeepDebug的多轮根因定位策略（全局读+结构引导探测+交叉校验）可迁移到长链路推荐/搜索的badcase根因定位场景：替代逐阶段人工排查多阶段召回、排序链路的badcase根因，提升排查效率

  - Error Hub的脱敏故障共享机制可借鉴到团队内部的Agent故障知识库搭建：沉淀电商Agent常见错误模式和修复方案，复用历史调试经验，持续优化Agent性能

  - 成本感知的归因策略路由可直接复用：根据业务 latency 和成本要求，在准确率和推理开销之间做tradeoff，适合线上高并发Agent场景，避免不必要的多轮推理开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent故障通常在执行下游才暴露，根因却隐藏在更早的决策步骤，现有可观测工具仅支持execution trace回放，缺少根因定位和自动修复能力，无法形成调试闭环，导致Agent落地排查成本极高，尤其电商/推荐场景下的多Agent导购、长链路决策场景，故障会直接影响用户转化和体验。
### 方法关键点
- 整体采用Detect→Attribute→Recover→Rerun的闭环调试流程，支持LangGraph、CrewAI、OpenAI Agents SDK等主流框架的trace统一接入，与底层Agent框架解耦
- 核心DeepDebug诊断模块采用4步多轮归因：1. 全局扫描全轨迹输出初始根因候选；2. 结构引导探测（多Agent场景回溯交互链路、单Agent场景二分排查步骤）输出第二候选；3. 交叉校验两个候选，选择因果性更强的根因步骤；4. 输出带证据、修复建议的结构化报告
- 配套可选Error Hub，支持脱敏后的故障-诊断-修复bundle共享，可作为调试记忆复用；内置19种预置故障分类，支持自动扩展新故障模式
### 关键结果
- 归因任务在Who&When基准测试，基于qwen3.5-9b时，DeepDebug的严格根因（Agent+ exact step）准确率达28.8%，比最强单轮基线高7.1个百分点；长链路（>40步）场景下准确率优势更显著
- 端到端修复在GAIA基准测试，原始Agent准确率55.8%，加入DeepDebug后单次重跑修复13/73个失败任务，整体准确率提升到63.6%，修复数量是Reflexion、CRITIC等自校正基线的2~3倍，推理开销仅为单轮扫描的1.6倍

LLM的自校正效率在给定明确错误位置时会大幅提升，根因定位的精度比泛化的自校正策略对修复效果的影响更大
