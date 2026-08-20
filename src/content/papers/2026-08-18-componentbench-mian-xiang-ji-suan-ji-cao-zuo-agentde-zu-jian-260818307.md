---
title: 'ComponentBench: Diagnosing Component-Level Failures in Computer-Use Agents'
title_zh: ComponentBench：面向计算机操作Agent的组件级故障诊断基准
authors:
- Tianchen Guan
- Xinlei Lin
- Royce Cheng-Yue
- Xiangjun Wang
- Shuyan Zhou
affiliations:
- Duke University
- Amazon AGI SF Lab
arxiv_id: '2608.18307'
url: https://arxiv.org/abs/2608.18307
pdf_url: https://arxiv.org/pdf/2608.18307
published: '2026-08-18'
collected: '2026-08-20'
category: Agent
direction: 计算机操作Agent 评测基准
tags:
- Agent-Evaluation
- Computer-Use-Agent
- UI-Interaction
- Benchmark
- Failure-Diagnosis
one_liner: 构建覆盖97种UI组件的2910个任务基准，可诊断Web UI下操作Agent的组件级失效原因
practical_value: '- 电商自研导购Agent、运营自动化Agent可复用该基准的组件级测试方法，针对常见UI控件（日期选择器、多选框、滑块等）做专项能力验证，提前发现交互故障

  - 操作Agent的架构选型可参考结论：弱视觉能力模型优先用Set-of-Marks/AX-tree观察空间降本提效，强视觉模型可直接用Pixel空间避免SoM标记的额外开销

  - 可复用基准的「预期难度-实际难度」对齐方法，基于人类交互轨迹校准任务难度，减少Agent评测的任务设计偏差

  - 操作Agent的优化优先级可参考失效归因：优先解决连续校准错误、瞬态状态丢失、提交动作缺失三类高频故障，能快速提升交互效率和成功率'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有计算机操作Agent评测要么侧重长流程端到端任务（故障归因难），要么侧重单步UI定位（无法覆盖多步组件交互），中间缺失组件级的细粒度评测层：长流程任务的可靠性下限由其中最脆弱的组件交互决定，仅5个80%成功率的组件交互就会导致端到端成功率降到33%，同时现有评测普遍缺乏对交互效率的量化评估，无法满足落地的延迟、成本要求。

### 方法关键点
- 构建覆盖97种通用UI组件、14个交互族、24种任务模板的组件本体，跨Ant Design、MUI、Mantine三大UI库生成2910个可程序化校验的任务，配套人类参考交互轨迹，同时蒸馏出912个难例组成的Core基准子集用于压力测试
- 支持AX-tree、Set-of-Marks、Pixel、Browser-Use四种观察/动作空间，可对比不同输入输出范式对Agent性能的影响
- 提出分层诊断pipeline，通过人类轨迹重放测量任务实际难度，可结构化归因组件级失效原因

### 关键实验
在7个主流多模态模型上测试：观察/动作空间对同模型的成功率影响超过30%（GPT-5 mini在AX-tree空间下成功率83.1%，在Pixel空间下仅48.9%）；效率差距显著，即使最优配置的Agent完成任务耗时也是人类的3.7倍，最弱配置达21.5倍；人类1-2步就能完成的空间操作组件（滑块、拖拽列表、分割器等），所有Agent平均成功率不足60%。

操作Agent的性能由模型能力和交互范式共同决定，组件级评测可暴露长流程评测和单步定位评测都无法发现的失效模式。
