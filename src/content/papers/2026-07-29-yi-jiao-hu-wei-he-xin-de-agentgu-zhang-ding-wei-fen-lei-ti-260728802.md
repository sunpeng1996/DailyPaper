---
title: Model or Harness? An Interaction-Centric Taxonomy for Localizing Agent Failures
title_zh: 以交互为核心的Agent故障定位分类体系，精准定位故障责任组件
authors:
- Harsh Raj
- Vipul Gupta
- Anas Mahmoud
- Razvan-Gabriel Dumitru
- Darvin Yi
- Aakash Sabharwal
- Yunzhong He
affiliations:
- Scale AI
arxiv_id: '2607.28802'
url: https://arxiv.org/abs/2607.28802
pdf_url: https://arxiv.org/pdf/2607.28802
published: '2026-07-29'
collected: '2026-08-05'
category: Agent
direction: Agent故障定位 · 根因归因分类体系
tags:
- Agent Failure
- Fault Localization
- Taxonomy
- LLM-as-a-Judge
- Root Cause Analysis
one_liner: 提出覆盖41种故障模式的交互中心Agent故障分类法，可自动定位故障责任组件
practical_value: '- 搭建业务Agent故障排查体系时，可直接复用该分类法的9类核心组件（模型、harness、工具、环境等）定义和「边+故障侧」的归因逻辑，快速判断问题需要优化LLM微调还是harness工程

  - 故障归因时采用「回溯最早不可恢复故障」的规则，避免将下游症状误判为根因，大幅降低业务Agent排障的错误率

  - 可复用论文的Agent-as-a-Judge+多模型投票的故障自动标注方案，3票一致时分类精度可达0.83、覆盖率90%，降低人工标注故障的成本

  - 业务Agent迭代时，可参考分类法区分模型侧/非模型侧故障，避免盲目投入资源优化LLM却无法解决harness或环境导致的问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent故障评估多停留在系统结果层面，相同的故障表现可能由模型微调、harness工程、环境重构、基准修复等完全不同的干预方式解决，传统分类法要么绑定特定基准，要么无法明确责任组件，导致排障效率极低。

### 方法关键点
- 将Agent系统拆分为9类核心组件，以组件间的交互边为分析单元，每个故障标记为「组件1-组件2·fault:责任方」的格式，覆盖41种细分故障模式
- 故障归因采用根因回溯规则：从最终故障反向追溯，标记最早的不可恢复故障，而非下游继发错误
- 采用Agent-as-a-Judge框架验证分类一致性：法官仅依据分类定义和故障原始轨迹，经过证据重构、故障分类、歧义校验三步输出标签，通过多模型投票提升精度

### 关键结果
用4款前沿大模型作为法官，在40个公开故障示例上验证，GPT-5.5与人工标注的Cohen's κ达0.76，多法官3票一致时分类精度0.83、覆盖率90%，4票全一致时精度达0.96、覆盖率68%。

### 最值得记住的一句话
相同的Agent故障表现，可能需要完全不同的干预方案，仅优化模型无法解决harness、环境或评估体系导致的非模型侧故障。
