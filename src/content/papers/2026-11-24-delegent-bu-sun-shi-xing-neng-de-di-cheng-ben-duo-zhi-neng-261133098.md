---
title: 'Delegent: A Multi-Agent Harness That Reduces Cost without Sacrificing Performance'
title_zh: Delegent：不损失性能的低成本多智能体调度框架
authors:
- Lingwei Gu
- Jimmy Lin
affiliations:
- University of Waterloo
arxiv_id: '2611.33098'
url: https://arxiv.org/abs/2611.33098
pdf_url: https://arxiv.org/pdf/2611.33098
published: '2026-11-24'
collected: '2026-11-25'
category: Agent
direction: 多智能体调度 · LLM降本优化
tags:
- Multi-Agent
- Cost Reduction
- SLM
- Agent Harness
- Zero Training
- LLM Delegation
one_liner: 无训练多智能体调度框架，大模型主导核心任务，本地SLM执行简单子任务，实现降本且性能无损
practical_value: '- 业务Agent系统可复用「大模型主控+本地SLM跑工具密集型子任务」的分工模式，把搜索召回、信息核对、日志排查等简单劳动切给开源SLM执行，无需训练路由模型，大模型和SLM可自由替换，大幅降低API成本。

  - 可复用引导大模型主动委托的prompt设计：明确告知大模型委托范围、输出格式要求，无需修改原有Agent架构，仅加短指令即可先降低大模型自循环的冗余成本。

  - 长周期任务降本收益更高：电商场景的商品信息抽取、用户评论聚类、售后工单处理等长流程任务，用该分工模式的降本效果远好于短交互任务，任务越长成本下降幅度越大。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
基于前沿大模型的Agent系统成本极高，每轮推理都要重读全量上下文，哪怕是代码查找、信息检索、跑测试这类简单体力活也全部用大模型执行，长周期任务按token计费的成本高到难以落地；而之前的模型级联、路由方案都是让小模型跑全量任务，小模型能力不足容易掉点，还需要额外训练路由模块，模型替换不灵活。

### 方法关键点
- 按角色路由的无训练调度：主循环的规划、最终输出、核心决策全部交给前沿大模型，子Agent的工具调用、信息检索、事实核对等简单子任务全转发给本地部署的SLM执行，无需训练任何模型或路由组件，大模型和SLM可随时替换。
- 短指令引导大模型主动委托：给大模型添加简单prompt，明确要求把工具密集型的调查、验证类子任务交给SLM，自身仅做核心决策和最终输出，同时要求SLM返回带证据的短报告，方便大模型快速校验。
- 分层缓存优化：大模型侧每轮请求带固定缓存Key复用KV cache，SLM侧用vLLM做单GPU实例绑定，复用子任务上下文缓存，进一步降低两边的推理成本和延迟。

### 关键结果
实验覆盖3个编码任务集（SWE-bench Verified、SWE-bench Pro、DeepSWE）和5个搜索任务集（共694条搜索问题），baseline为纯前沿大模型跑相同任务的效果。用27B FP8 SLM时，长周期编码任务前沿大模型成本降67%，智能搜索任务成本降59%，任务成功率完全持平；哪怕用笔记本可跑的2B SLM，编码任务成本也能降66%，性能无损失；超过200轮大模型调用的长任务成本可降至原来的26%。

**最值得记住的一句话**：无需训练任何模块，仅通过大模型与SLM的任务分工，即可在性能无损的前提下将前沿大模型成本降低超50%，长周期任务收益更高。
