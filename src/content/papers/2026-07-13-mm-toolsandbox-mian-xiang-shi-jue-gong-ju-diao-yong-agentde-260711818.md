---
title: 'MM-ToolSandBox: A Unified Framework for Evaluating Visual Tool-Calling Agents'
title_zh: MM-ToolSandBox：面向视觉工具调用Agent的统一评估框架
authors:
- Kaixin Ma
- Di Feng
- Alexander Metz
- Jiarui Lu
- Eshan Verma
- Afshin Dehghan
affiliations:
- Apple
arxiv_id: '2607.11818'
url: https://arxiv.org/abs/2607.11818
pdf_url: https://arxiv.org/pdf/2607.11818
published: '2026-07-13'
collected: '2026-07-14'
category: Agent
direction: 多模态Agent · 工具调用能力评估
tags:
- MultiModal Agent
- Tool Calling
- Benchmark
- Evaluation
- Visual Grounding
one_liner: 推出支持多图多轮、500+工具的视觉工具调用Agent benchmark，揭示不同规模模型的差异化瓶颈
practical_value: '- 电商多模态导购Agent可复用该框架的测试场景，比如用户发商品截图查价、加购的多轮交互场景，快速验证自家Agent的视觉工具调用能力

  - 失败分析结论可直接指导Agent优化：小模型优先做规划链路的Prompt工程/微调，大模型优先优化视觉信息提取精度，尤其是长对话中早期图像的记忆召回能力

  - 工具调用的Code-Execution/Tool-Use两种模式无统一最优，可根据底座模型偏好选择，工具集粒度也可按需调整，无需盲目追求大而全的工具库

  - 做Agent自动化测试可复用其信息流引导的场景生成流水线，大幅降低人工标注成本，仅需最后做人工抽检'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有工具调用Agent评估框架大多为文本中心化，仅有的多模态Benchmark要么是单轮交互、工具集规模小，要么仅支持静态图像输入，无法模拟真实场景下用户发截图/照片、多轮交互、目标变更、多工具协同的复杂需求，缺乏统一的视觉工具调用能力评估体系。

### 方法关键点
- 框架层：提供有状态执行环境，覆盖16个应用域的511个工具，支持多图多轮交互，兼容结构化Tool-Use和自由Code-Execution两种执行模式，内置三层安全沙箱保障代码执行安全
- 基准构建：通过信息流引导规划、多阶段质量过滤的自动化场景生成流水线，产出258个人工验证的标准场景+50个交互式UI场景，覆盖7种信息流类型、4种对话挑战、4种图像到达模式
- 评估体系：结合状态校验（对比环境实体变更）和双LLM裁判（Agent裁判评任务完成度，用户裁判评对话合理性），与人类标注一致性达88%

### 关键结果
评估12个SOTA模型（从4B开源到前沿闭源）：① 最优模型Claude 4.5 Opus的任务成功率仅48.8%，视觉工具调用能力远未成熟；② 超过50%的失败来自视觉信息提取错误，而非规划错误；③ 小模型（<27B）主要失败在规划能力，大模型主要失败在视觉感知精度，存在规划-精度的能力交叉点；④ 多图工作记忆是核心瓶颈，图像全部前置给出的场景比渐进式给出的成功率低20%。

**最值得记住的一句话**：不同规模多模态工具调用Agent的优化方向完全不同，小模型优先补规划，大模型优先补视觉感知精度。
