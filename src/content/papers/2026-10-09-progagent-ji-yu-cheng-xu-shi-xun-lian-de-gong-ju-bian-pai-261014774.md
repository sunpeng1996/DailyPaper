---
title: 'ProgAgent: Learning Tool Orchestration through Programmatic Training'
title_zh: ProgAgent：基于程序式训练的工具编排Agent训练栈
authors:
- Hao Li
- Keqing He
- Longtao Zheng
- Junlong Li
- Weihao Zeng
- Qian Liu
- Yuzhen Huang
affiliations:
- Hong Kong University of Science and Technology
- Beijing University of Posts and Telecommunications
- Nanyang Technological University
arxiv_id: '2610.14774'
url: https://arxiv.org/abs/2610.14774
pdf_url: https://arxiv.org/pdf/2610.14774
published: '2026-10-09'
collected: '2026-10-15'
category: Agent
direction: Agent工具编排 · 程序式训练范式
tags:
- Tool Orchestration
- Programmatic Tool Calling
- Long-Horizon Agent
- Agent Training
- Reinforcement Learning
one_liner: 提出程序式工具调用训练范式，仅用数百级任务实现长周期工具编排能力超同规模基线
practical_value: '- 长链路电商导购/推荐Agent可复用PTC范式：工具调用逻辑用代码封装，中间结果存runtime变量不进上下文，大幅缓解长交互下的context
  rot，降低KV cache开销

  - 小样本训练工具能力可参考两阶段训练流程：先冷启动SFT喂优质教师轨迹，再用可验证的二进制reward做RL，仅用数百级任务就能训练出远超同规模基线的工具编排能力

  - 任务难度控制可复用环境缩放方案：固定任务逻辑/工具接口，仅缩放环境数据量制造难度梯度，训练出的Agent对大环境、长上下文的鲁棒性提升30%以上

  - 跨接口泛化结论可复用：PTC训练的Agent能力可迁移到DTC接口，不需要同时维护两种训练范式，降低训练侧复杂度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有基于Direct Tool Calling (DTC)的Agent执行长周期任务时，工具返回结果直接拼接进上下文，极易引发context rot导致编排失败；此前Programmatic Tool Calling (PTC)仅被用作推理优化，其训练价值未被挖掘，且缺少适配PTC的可验证长周期训练任务。

### 方法关键点
- 任务合成pipeline：覆盖23个领域的215个可验证长周期任务，固定任务逻辑、工具接口，仅缩放环境数据量生成4个难度梯度的任务变体，每个任务配套Python二进制验真器
- 轻量PTC runtime：基于持久化IPython内核的沙箱，工具调用通过代码执行，中间结果存runtime变量，仅打印的内容进入上下文，支持RL rollout的episode隔离
- 两阶段训练范式：第一阶段基于教师轨迹做冷启动SFT，第二阶段用验真器的二进制奖励做GSPO强化学习，支持DTC/PTC/混合三种训练范式的对比

### 关键实验
在MCPMark、Toolathlon-Verified、LOCA-bench、MCP-Atlas四个基准测试，对比同参数（8B/14B）开源基线、闭源模型：ProgAgent-14B在64k token环境的LOCA-bench上达到30.7%通过率，同规模基线得分为0；MCP-Atlas上达到45.6%，和Claude Sonnet-4.5 DTC水平相当；仅用215个原任务×4缩放变体，训练数据量远低于同类Agent训练方案。

### 核心结论
PTC不仅是推理优化手段，更是有效的训练范式，其训练得到的工具编排能力可跨接口迁移到DTC场景，用极小训练数据量即可实现能力跃升。
