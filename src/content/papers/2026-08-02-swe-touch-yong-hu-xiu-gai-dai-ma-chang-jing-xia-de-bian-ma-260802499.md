---
title: 'SWE-Touch: Benchmarking Coding Agents When Users Touch the Code'
title_zh: SWE-Touch：用户修改代码场景下的编码Agent基准测试框架
authors:
- Yuqiao Tan
- Jinxiang Meng
- Fangyu Lei
- Minzheng Wang
- Shizhu He
- Jun Zhao
- Kang Liu
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
arxiv_id: '2608.02499'
url: https://arxiv.org/abs/2608.02499
pdf_url: https://arxiv.org/pdf/2608.02499
published: '2026-08-02'
collected: '2026-08-05'
category: Agent
direction: 编码Agent 共享工作空间协作能力评测
tags:
- Coding Agent
- Benchmark
- Shared Workspace
- Counter Edit
- State Awareness
one_liner: 提出SWE-Touch基准框架，测试共享工作空间下编码Agent对用户代码修改的适配能力
practical_value: '- 开发人在回路的业务Agent（如选品Agent、文案协作Agent）时，需新增工作空间变更检测、冲突修改校验、执行结果重验证模块，避免人工介入后Agent适配失效

  - 做业务Agent性能评测时，可复用Counter-Edit对抗性测试思路，注入合理的人为修改干扰，评估Agent的动态环境感知能力，降低上线后效果落差

  - 长周期任务Agent的训练目标需新增状态感知相关约束，不能仅优化纯自主执行的效果，需覆盖动态变更场景下的自适应能力'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有编码Agent基准仅测试纯自主执行场景，用户交互仅支持消息输入，未覆盖真实开发中用户会直接修改共享工作空间代码的场景，无法评估Agent对动态环境变更的适配能力。
### 方法关键点
1. 提出SWE-Touch评测框架，从多轮代码修复轨迹中挖掘任务关键区域，通过独立的User Patch Generator生成合理的、会干扰任务完成的Counter-Edit（反事实编辑）；
2. 在Agent执行到相关代码节点时，注入编辑内容和上下文用户消息，模拟真实共享 workspace 交互逻辑。
### 关键结果
在SWE-bench Verified测试集上，Counter-Edit使9个编码模型的平均任务解决率下降7.7个百分点，长周期任务上性能下降同样显著；失效核心原因是Agent环境状态感知能力不足，未重新校验代码库或验证修改后效果。
