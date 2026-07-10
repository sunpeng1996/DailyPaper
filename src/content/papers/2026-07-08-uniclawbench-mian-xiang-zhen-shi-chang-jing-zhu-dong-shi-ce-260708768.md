---
title: 'UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks'
title_zh: UniClawBench：面向真实场景主动式Agent的通用评测基准
authors:
- Zhekai Chen
- Chengqi Duan
- Kaiyue Sun
- Bohao Li
- Yuqing Wang
- Manyuan Zhang
- Xihui Liu
affiliations:
- HKU MMLab
- Meituan
arxiv_id: '2607.08768'
url: https://arxiv.org/abs/2607.08768
pdf_url: https://arxiv.org/pdf/2607.08768
published: '2026-07-08'
collected: '2026-07-10'
category: Agent
direction: 主动Agent · 多维度能力评测
tags:
- Proactive Agent
- Agent Benchmark
- Closed-loop Evaluation
- Real-world Task
- Capability-driven
one_liner: 首个能力驱动的主动Agent评测基准，含400个双语真实任务与三角色闭环评测框架
practical_value: '- 开发电商跨平台主动Agent（如智能比价、订单履约助手）时，可直接复用三角色闭环评测框架：隐藏Supervisor负责精准打分、User
  Simulator仅输出粗粒度自然反馈，既贴合真实用户多轮交互场景，又避免泄露评测规则导致过拟合。

  - Agent架构选型可直接参考实验结论：追求高任务完成率选OpenClaw这类集中式单Agent框架，上下文信息损失最小；对成本敏感的简单高频场景选Nanobot轻量架构，token消耗可降低50%；EDICT多Agent架构目前存在严重协调摩擦，暂不推荐长链路复杂业务场景。

  - 电商Agent能力优化优先级：先打磨已相对成熟的Skill Usage与Exploration能力（ROI最高），再重点攻坚长上下文信息留存、多模态商品理解、跨平台状态同步三大核心瓶颈。

  - 内部Agent评测体系建设可参考能力维度拆分方法，将任务按核心瓶颈归类，无需大量人工标注即可快速定位Agent失败根因，避免盲目迭代基础模型。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前主动式Agent已能操作浏览器、办公软件等工具处理真实任务，但现有评测基准普遍依赖沙箱环境、单轮评测范式，且按应用场景分类任务，无法区分失败根因是基础模型能力不足还是Agent架构设计缺陷，也无法模拟真实多轮用户交互，与落地场景差距极大。
### 方法关键点
- 按5个核心能力维度拆分任务：Skill Usage、Exploration、Long Context、Multimodal、Cross-Platform，每个任务对应单一核心瓶颈，共设计400个中英双语真实场景任务，覆盖电商、办公、科研等12个领域。
- 提出三角色闭环评测架构：Executor Agent在独立Docker容器的真实环境（含浏览器、本地工具、网络）中执行任务；隐藏Supervisor基于细粒度step checkpoint打分，抛弃静态标准答案适配真实环境动态变化；User Simulator仅接收粗粒度进度信号生成自然反馈，信息隔离避免泄露评测规则，支持多轮交互。
### 关键实验结果
对比10款SOTA大模型、3款主流Agent框架（OpenClaw/EDICT/Nanobot）：① SOTA模型最高整体通过率仅47.5%，Long Context、Multimodal、Cross-Platform三类任务通过率普遍低于25%，是核心瓶颈；② Agent框架选择对性能的影响远大于模型选择，OpenClaw通过率最高，EDICT token消耗是OpenClaw的1.5~2倍但通过率低7~13pct，Nanobot token消耗降低50%但通过率低10~15pct；③ 多轮用户反馈可将整体通过率从23.8%提升至31.7%。
### 核心结论
主动Agent落地的核心瓶颈往往不是基础模型能力，而是Agent框架的上下文管理与架构设计，以及长上下文、多模态、跨平台协同的能力短板。
