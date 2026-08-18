---
title: 'StateM: Reaching 95.3% Raw Accuracy, or a \$15 Frontier Run, on Terminal-Bench
  2.1 via Harness Scaling'
title_zh: 《StateM：通过Harness Scaling大幅提升长程Agent性能并降低成本》
authors:
- Ziheng Qin
- Yaxin Lu
- Zhangyang Atlas Wang
- Kai Wang
arxiv_id: '2608.15089'
url: https://arxiv.org/abs/2608.15089
pdf_url: https://arxiv.org/pdf/2608.15089
published: '2026-08-14'
collected: '2026-08-18'
category: Agent
direction: 长程Agent · 状态化执行控制优化
tags:
- Agent Runtime
- Harness Scaling
- Long-horizon Agent
- Finite State Machine
- Runbook
one_liner: 提出Agent原生状态化运行时StateM，无需修改模型权重即可提升长程任务准确率并大幅降低成本
practical_value: '- 做电商导购Agent、工单处理Agent等长流程任务时，可复用StateM的YAML runbook状态机设计，把任务拆分为带入钩子、退出校验的阶段，避免Agent中途丢状态、提前终止，无需微调模型即可提升任务成功率

  - 复用harness scaling思路：当业务Agent的基础大模型能力足够完成单步骤但全链路成功率低时，优先优化执行控制层而非换更大模型/微调，可大幅降低落地成本，甚至用小模型加优化控制层对标大模型效果

  - 跨模型迁移时，通用执行框架、runbook结构、失败迭代规则可直接复用，仅需少量成本适配具体模型的行为差异，能快速把已验证的Agent流程迁移到成本更低的模型上

  - 可借鉴失败驱动的runbook迭代机制：把每次任务失败的根因转化为runbook的校验规则、状态边界，将流程类经验沉淀在外部控制层而非依赖模型记忆，提升Agent的可解释性与可运维性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长程Agent普遍存在单步骤能力足够但全链路执行失败的问题：丢失可变状态、遗忘过往执行经验、跳过必要流程、提前终止。业界通常通过升级大模型、微调、新增多Agent协作模块解决，成本高昂，而执行控制层（harness）缺陷导致的模型能力浪费长期被忽视，如何在不修改模型权重的前提下充分释放模型已有能力是核心痛点。

### 方法关键点
- 提出harness scaling范式：通过优化Agent外围执行控制层提升性能，无需改动模型权重，与模型scaling互补
- 设计StateM轻量运行时：基于YAML格式的共享runbook定义状态、合法转移、阶段本地上下文、钩子、校验规则、恢复逻辑，Agent和用户均可通过CLI操作、查看、编辑runbook
- 核心设计：每个状态是「上下文+契约」边界，进入时自动刷新当前阶段指令与进度，退出必须满足显式校验条件；运行时维护独立执行状态与转移历史，支持中断恢复；配套失败驱动的runbook迭代机制，将执行失败根因转化为runbook规则，沉淀到控制层

### 关键实验
- Terminal-Bench 2.1（89个终端任务，445次试跑）：GPT-5.5 xhigh搭配StateM准确率从83.1%提升至92.1%，超过GPT-5.6 Sol Ultra的91.9%；GPT-5.6 Sol xhigh搭配StateM准确率达95.3%，覆盖全部89个任务
- 跨模型迁移：GPT-5.5训练的runbook无修改迁移到GPT-5.6 Luna，准确率从76.7%提升至85.4%；适配DeepSeek-V4 Flash仅花38美元适配成本，最终达到和GPT-5.6 Sol Max相当的88.8%准确率，最终评测API成本仅15美元，比GPT参考方案低38倍
- BusinessBench上，流程匹配的任务家族准确率最高提升10.04个百分点

### 核心结论
Agent性能瓶颈很多时候不在模型本身，优化执行控制层的投入产出比远高于单纯升级模型
