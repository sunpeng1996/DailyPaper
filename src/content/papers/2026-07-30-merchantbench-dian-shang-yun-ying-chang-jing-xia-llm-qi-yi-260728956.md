---
title: 'MerchantBench: Benchmarking LLM Agents for Long-Term Coherence in E-Commerce
  Operations'
title_zh: MerchantBench：电商运营场景下LLM Agent长期一致性评测基准
authors:
- Qiming Shi
- Yulong Tao
- Linbo Jin
- Zhaolu Kang
- Yibo Dou
- Jiawen Zhu
- Tianjun Pan
- Shaokang Fu
- Chengyu Wang
- Siyue Li
affiliations:
- Alibaba Group
- Zhejiang University
- Peking University
- Fudan University
arxiv_id: '2607.28956'
url: https://arxiv.org/abs/2607.28956
pdf_url: https://arxiv.org/pdf/2607.28956
published: '2026-07-30'
collected: '2026-08-05'
category: Agent
direction: Agent评测 · 电商长周期决策
tags:
- LLM Agent
- Benchmark
- E-commerce
- Long-Horizon
- Decision Coherence
one_liner: 基于98843条真实电商商品数据构建365天粒度的卖家Agent长期决策一致性评测基准
practical_value: '- 做电商商家运营类Agent的团队可直接复用MerchantBench的26个工具定义、365天订单级仿真框架，快速完成Agent迭代验证，无需从零搭建模拟环境

  - 长周期决策Agent设计可重点优化三个核心模块：长期目标对齐、延迟反馈归因、动态资源分配，避免出现操作活跃度衰减、策略漂移问题

  - 可复用Benchmark的三维评估体系：从业务绩效、店铺可靠性、长周期活跃度三个维度构建Agent离线评估指标，降低线上试错成本'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent评测大多聚焦短周期、有明确终止条件的任务，而真实电商卖家运营需要跨长周期的连贯决策，前期动作会约束后期选择、反馈延迟不均，现有基准无法评测这类长期一致性能力。

### 方法关键点
- 基于1688平台98843条真实商品的365天需求数据，构建订单粒度的365天仿真环境，包含上游供应商事件、下游订单全生命周期模拟，反馈分为即时供应商事件和延迟订单结果两类；
- 定义选品、上架定价、现金流管理、混合延迟反馈适配4类核心决策模块，开放26个工具接口；
- 从业务绩效、店铺可靠性、长周期活跃度三个维度设计评测指标。

### 关键实验结果
评测8款主流LLM在ReAct、Hermes两种Agent框架下的表现，共48次365天模拟运行：最优LLM配置（Hermes+Qwen3.7-Max）的最终净资产仅为人类运营者均值的27.3%；带记忆、代码执行能力的Hermes框架比纯ReAct平均净资产高53.3%。

**最值得记住的结论**：当前LLM Agent在长周期连贯决策上和人类的差距远大于短任务，核心瓶颈是操作连贯性衰减与策略随时间漂移。
