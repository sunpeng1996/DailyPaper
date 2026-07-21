---
title: 'Sidekick: Designing Communication for Effective Multitasking with Computer
  Use Agents'
title_zh: Sidekick：面向计算机操作Agent多任务协作的交互通信设计
authors:
- Ruei-Che Chang
- Wenqian Xu
- Dingzeyu Li
- Bryan Wang
- Anhong Guo
affiliations:
- UMich
- Adobe Research
arxiv_id: '2607.17527'
url: https://arxiv.org/abs/2607.17527
pdf_url: https://arxiv.org/pdf/2607.17527
published: '2026-07-20'
collected: '2026-07-21'
category: Agent
direction: 人机协作 · Agent多任务交互反馈设计
tags:
- Computer Use Agent
- Multimodal Feedback
- Human-Agent Collaboration
- Ambient Display
- Multitasking
one_liner: 提出分交互阶段的多模态反馈系统Sidekick，提升人与计算机操作Agent的多任务协作效率
practical_value: '- 后台运行的Agent可复用色彩编码+精简摘要的弱打扰反馈设计，无需用户频繁切页查看进度，适配推荐/运营类后台自动化任务（比如批量素材生成、商品上架校验）的监控需求

  - Agent任务交互恢复阶段可复用多模态摘要（语音+操作高亮回放）的设计，降低用户切换回Agent任务时的上下文恢复成本，适合Agent处理长周期复杂任务（比如大促活动页搭建、用户分层运营）的场景

  - 前台运行的Agent可复用推理过程可视化+语音同步播报的设计，提升Agent操作的透明度，增强用户对Agent执行结果的信任，适合高风险场景（比如广告投放预算调整、敏感用户信息操作）的Agent交互'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
计算机操作Agent（CUA）可自主执行GUI多步骤任务，支持用户并行多任务，但现有反馈多为纯文本，用户需耗费精力监控进度，回溯GUI交互轨迹难度大：前台运行时决策过程不透明，后台运行时状态信号缺失，恢复交互时上下文重建成本高，严重限制人机协作效率。

### 方法关键点
- 分三个交互阶段设计分层反馈，不修改原有CUA逻辑，仅作为通信层部署：
  1. 后台运行阶段：常驻浮窗提供色彩编码状态信号（绿=正常、黄=少量错误、橙=错误累积、红=卡住暂停）+ 精简文本摘要+缩略图，支持用户余光感知进度
  2. 交互恢复阶段：生成语音+操作高亮回放的多模态摘要，对齐操作轨迹与截图，用色彩梯度标记操作新旧，帮助用户快速恢复上下文
  3. 前台运行阶段：实时语音播报Agent推理过程，同步可视化操作（点击位置标注、键盘输入展示、GUI元素高亮），搭配对应操作拟音，提升透明度
- 技术上用VLM做动作正确性校验，SSML标注对齐语音与视觉反馈，实现多模态信号同步

### 关键实验
30名被试参与对照实验，主任务为算术题，次任务为CUA辅助的表格填充，对比4组条件：纯手动（MN）、纯聊天文本反馈（BL）、浮窗纯文本反馈（PT）、Sidekick（SK）。核心结果：SK组总分比PT高17.1%，比BL高9.6%；次任务错误数比BL低47.8%、比PT低43.5%；监控耗时比BL低32.5%、比PT低17.4%，主任务性能无显著下降。

> 最值得记住的结论：人机协作的效率增益不仅取决于Agent自身能力，更取决于是否能在不干扰用户主任务的前提下，提供分场景的轻量化、高信息密度反馈，降低用户的监控与上下文恢复成本。
