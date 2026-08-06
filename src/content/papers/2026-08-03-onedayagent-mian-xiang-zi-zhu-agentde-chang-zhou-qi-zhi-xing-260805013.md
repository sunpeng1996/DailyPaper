---
title: 'OneDayAgent: Towards a Long-Horizon Harness for Autonomous Agents'
title_zh: OneDayAgent：面向自主Agent的长周期执行管控框架
authors:
- Jingsheng Zheng
- Xinyuan Fang
- Jintian Zhang
- Zhengke Gui
- Huajun Chen
- Ningyu Zhang
affiliations:
- Zhejiang University
- Ant Group
- Independent Researcher
arxiv_id: '2608.05013'
url: https://arxiv.org/abs/2608.05013
pdf_url: https://arxiv.org/pdf/2608.05013
published: '2026-08-03'
collected: '2026-08-06'
category: Agent
direction: 长周期Agent · 通用执行管控框架
tags:
- LLM-Agent
- Long-Horizon
- Task-Decomposition
- Memory-Management
- Verification-Repair
one_liner: 提出跨LLM后端通用的长周期Agent执行框架，融合三大核心能力，刷新AgentIF-OneDay基准SOTA
practical_value: '- 长周期Agent任务可复用「任务拆分+子任务状态checkpoint+全局校验修复」流水线，适配电商智能客服处理跨环节退换货诉求、运营Agent自动生成带素材的商品详情页等场景，大幅降低目标漂移、状态丢失问题

  - 上下文压缩方案可直接落地：工具返回的大体积内容（如爬虫结果、商品评价语料）做摘要截断，子任务间仅传关键状态而非全量trace，可降低长链路Agent的上下文占用，减少KV
  cache开销

  - 业务对延迟敏感时可仅开启全局校验修复模块，ablation显示仅开启该模块比仅开启任务拆分模块latency低60%、得分相当，适合电商实时营销话术生成、售前问题解答等场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent处理长周期、跨环境、多模态任务时普遍存在目标漂移、中间状态丢失、上下文溢出问题，现有方案多仅解决单点故障，缺乏跨后端通用的执行管控框架，难以适配真实场景中跨工具、长链路的用户诉求。

### 方法关键点
- 任务分解：将复杂请求拆分为最多6个有界子任务，每个子任务独立执行ReAct逻辑，子任务间仅传递关键结果而非全量交互trace，降低上下文压力
- 全局校验与修复：所有子任务完成后，将产出与原始请求逐点校验，发现缺陷后仅针对问题部分做定向修复，无需重跑全链路
- 执行记忆：工具返回的大体积观测结果自动做摘要截断，对话上下文超过后端窗口90%时自动压缩历史交互，同时保留系统提示、原始任务和最近动作轮次
- 统一工具接口：封装网页访问、文件操作、多模态处理、代码执行等通用工具，支持跨环境交互

### 关键实验
在AgentIF-OneDay基准的104个日常长周期任务上测试，搭配GLM-5.2后端时整体得分0.821，刷新SOTA，比此前最优基线高2.2pp；同一框架无需微调即可适配5款不同厂商、不同参数量的LLM后端，得分区间0.613-0.821；ablation显示同时开启拆分和校验模块得分最高，仅开启校验模块时性价比最优，延迟仅比无管控方案高2.2分钟，得分提升3.3pp。

### 核心结论
长周期Agent的性能上限不仅取决于后端LLM的能力，执行管控框架的优化可在不微调模型的情况下实现跨模型通用的性能提升，且不同模型在同一框架下会呈现显著的执行风格差异
