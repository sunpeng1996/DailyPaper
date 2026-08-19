---
title: 'HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety'
title_zh: HarnessRisk：面向全生命周期的Agent执行框架安全基准测试集
authors:
- Yajing Bai
- Jinhao Duan
- Jie Peng
- Xianfeng Wu
- Sijia Liu
- Song Wang
- Tianlong Chen
affiliations:
- University of North Carolina at Chapel Hill
- University of Central Florida
- Michigan State University
arxiv_id: '2608.17597'
url: https://arxiv.org/abs/2608.17597
pdf_url: https://arxiv.org/pdf/2608.17597
published: '2026-08-17'
collected: '2026-08-19'
category: Agent
direction: Agent执行框架 · 全生命周期安全评测
tags:
- Agent Safety
- Benchmark
- Agent Harness
- Lifecycle Evaluation
- LLM Agent
one_liner: 构建覆盖Agent执行框架6个生命周期的128个沙箱用例，量化模型+框架组合的安全表现
practical_value: '- 搭建电商导购、运营自动化类Agent时，优先加固Harness Configuration阶段的参数校验，对第三方工作流传入的权限配置、webhook地址等敏感参数强制做白名单校验，该阶段是所有框架共性最脆弱点

  - Agent上线前不能仅以任务完成率作为验收标准，哪怕Utility达到95%以上仍可能存在30%+的攻击成功率，需按照生命周期分阶段做安全专项测试

  - 风险检测模块必须配套拦截处置逻辑，实验显示部分配置风险检测率超90%但仍有30%+的攻击成功率，检测到风险后需同步阻断危险操作、清理持久化状态，不能仅告警不处置

  - 选型Agent执行框架时必须与绑定的LLM做联合安全评测，同一模型在不同框架下攻击成功率最大差可达4.3倍，不能单独依赖模型安全评级上线'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent安全基准大多仅覆盖单一攻击机制或有限运行场景，未针对Agent执行框架（Harness）的全生命周期风险做统一评测，无法对比不同Harness职责下的安全失效模式，也无法量化真实部署中模型+框架联合配置的真实安全水平。

### 方法关键点
- 提出Agent Harness的6个生命周期阶段划分：配置、能力扩展、运行时操作、状态持久化、动作控制、事件恢复，覆盖从初始化到故障处置的全流程风险点
- 构建128个沙箱化评测用例，每个用例将对抗指令嵌入正常工作流的非信任工件中，同时保留合法用户任务目标，实现任务效用和安全表现的独立评估
- 设计4项核心评测指标：Utility（任务完成率，越高越好）、Attack Success Rate（ASR，攻击成功率，越低越好）、Persistence（对抗影响持久化率，越低越好）、Detection（风险识别率，越高越好）

### 关键结果
在3款主流Agent Harness、6款大模型、14种模型+框架配置上测试，攻击成功率范围12.6%~80.9%，任务效用范围75.0%~97.6%；Harness Configuration是所有框架最脆弱的阶段，攻击成功率远高于其他阶段；部分配置风险检测率超90%仍存在30%+的攻击成功率，同一模型在不同框架下ASR最大差达4.3倍。

> 最值得记住的结论：Agent安全是模型和执行框架的联合属性，高任务完成率不代表高安全性，必须对部署的完整配置做全生命周期的安全评测。
