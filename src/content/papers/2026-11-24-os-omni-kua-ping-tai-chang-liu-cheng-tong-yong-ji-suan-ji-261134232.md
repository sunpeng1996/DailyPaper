---
title: 'OS-Omni: Benchmarking Generalist Computer-Using Agents on Long-Horizon Workflows
  Across Platforms'
title_zh: OS-Omni：跨平台长流程通用计算机操作Agent基准
authors:
- Hui Shen
- Yunta Hsieh
- Jianing Ma
- Zhuoran Yin
- Zhuhan Bao
- Ziyuan Liu
- Qi Han
- Xiuqi Xu
- Xianbang Wang
- Wenhao Chai
affiliations:
- University of Michigan
- University of Pennsylvania
- Touchstone AI
- OpenAI
- Massachusetts Institute of Technology
arxiv_id: '2611.34232'
url: https://arxiv.org/abs/2611.34232
pdf_url: https://arxiv.org/pdf/2611.34232
published: '2026-11-24'
collected: '2026-11-27'
category: Agent
direction: Agent 跨平台操作基准评测
tags:
- GUI Agent
- Agent Benchmark
- Cross-Platform
- Long-Horizon Task
- Computer Use Agent
one_liner: 推出覆盖6大主流平台与跨端长流程的通用计算机操作Agent可复现评测基准
practical_value: '- 开发跨端GUI Agent（如电商多端操作Agent、用户行为模拟Agent）时，可复用双动作层设计：上层用统一PyAutoGUI风格动作语义，下层映射到各平台原生执行后端，大幅降低跨端适配成本

  - 长流程Agent任务验收可参考最终状态校验逻辑：不考核中间轨迹相似性，直接校验最终持久化状态（如电商加购后直接查后台购物车数据而非页面截图），提升评测准确率

  - 搭建内部Agent能力benchmark时，可复用五级任务标注管线：经验设计→独立审核→跨场景难度校准→Oracle校验→失败用例测试，保证任务集合理性与可复现性

  - 多设备联动Agent场景（如PC端选品后同步到手机端购物车）可参考单屏跨端交互方案：通过scrcpy将手机投屏到桌面，用统一键鼠操作完成跨端流程，无需多端分别对接'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有计算机操作Agent基准多孤立覆盖Web、移动、桌面单一场景，无法验证单个通用Agent能否完成跨多系统、带持久化状态的长流程任务，也无法统一对比不同模型的跨平台泛化能力。

### 方法关键点
- 覆盖Windows、Ubuntu、macOS、iOS、Android、Web 6大主流平台，v1版本共300个任务：单平台各48个，另含12个桌面+Android跨端长流程任务，平均交互步数67.54，是此前OSWorld基准的4.5倍
- 自研18个可控Open系列应用（覆盖电商、银行、出行、办公等场景），避免依赖第三方商业服务，支持可复现初始化、全轨迹日志、最终状态自动校验
- 设计双层动作空间：上层为平台无关的PyAutoGUI风格通用操作（点击、输入、滚动等），下层映射到各平台原生执行后端，保证Agent交互接口统一

### 关键结果
- 评测9款模型+人类基线，最强Claude Opus 5.5平均成功率68.5%，比人类基线77.3%低8.8个点；GPT-6-Astra为66.1%，Gemini 4 Argon为58.6%，7B级小模型如Qwen 3.8 9B成功率为0
- 平台性能差异极大：前沿模型在Linux上超过人类成功率，但在iOS、macOS上分别比人类低33.5、25.6个点

### 核心结论
通用计算机操作Agent的核心能力不仅是单界面操作熟练度，更需要在长交互中持续跟踪状态、适配不同系统交互规则、最终验证操作的持久化效果
