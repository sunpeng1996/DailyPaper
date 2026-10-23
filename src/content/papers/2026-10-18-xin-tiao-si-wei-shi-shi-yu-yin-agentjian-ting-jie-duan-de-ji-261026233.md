---
title: 'Heartbeat Thinking: Speculative Reasoning and Tool Execution While Listening
  in Realtime Voice Agents'
title_zh: 心跳思维：实时语音Agent监听阶段的投机推理与工具执行
authors:
- Zhenyu Zhang
- Kewei Fu
- Yongqi Tong
- Chenzhi Zheng
- Wei Wu
- Jiang-Ming Yang
- Jianshe Li
affiliations:
- Ant International
arxiv_id: '2610.26233'
url: https://arxiv.org/abs/2610.26233
pdf_url: https://arxiv.org/pdf/2610.26233
published: '2026-10-18'
collected: '2026-10-23'
category: Agent
direction: 语音Agent · 低延迟投机执行优化
tags:
- VoiceAgent
- SpeculativeReasoning
- ToolCalling
- LowLatency
- RealtimeSystem
one_liner: 提出异步心跳式投机执行机制，在用户语音输入阶段并行完成推理与工具调用，降低语音Agent响应延迟
practical_value: '- 电商语音导购/客服Agent可直接复用架构配置：默认500ms心跳周期+2并发Thinker的参数，在用户说话时提前触发商品搜索、订单查询等工具调用，实测可降低36%左右的响应延迟，显著提升用户体验

  - 架构设计可复用：将投机执行Thinker与最终响应Responder解耦，二者可独立选型模型，Thinker用小模型降推理成本，Responder用大模型保效果，无需共享模型内部状态，工程实现难度低

  - 状态管理trick：通过共享状态存储已完成的推理与工具结果，避免重复调用；语音结束时直接取消未完成的投机任务，无需等待pending任务，避免额外延迟

  - 搜索推荐场景可借鉴投机思路：用户输入query（打字/语音）过程中提前触发召回、粗排，输入完成后直接复用中间结果，降低全链路响应延迟'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有工具调用型语音Agent均需等用户说完话才启动推理与工具调用，用户等待时间长；此前的投机执行方案要么受语音chunk边界限制，要么会中断生成导致工具调用参数不完整，能提前完成的有效工作极少，无法充分利用用户说话的空窗时间。

### 方法关键点
- 双角色解耦架构：周期性触发的Thinker负责监听阶段的投机推理和工具调用，VAD检测到语音结束后触发的Responder负责基于完整请求与已完成准备工作生成最终响应，二者可独立选择模型
- 固定间隔Δ（默认500ms）异步启动Thinker调用，最多允许K（默认2）个并发，不中断正在执行的任务，所有已完成的推理、工具调用结果存入共享状态供后续调用复用
- 语音结束时直接取消所有未完成的投机任务，Responder仅使用当前已完成的有效结果，无需等待pending任务，避免额外延迟

### 关键实验
在SpeechFCEval、FDBench v3、AudioCRAG三个基准上对比SHANKS式窗口推理、Pipecat等基线；FDBench v3上投机工具覆盖率从34.67%提升至50.67%，最终响应延迟从6.90s降至4.39s，降幅36.4%，比最快的级联基线Pipecat还低45.7%；三个基准上的投机工具覆盖率分别比窗口基线高10.56、16、42.37个百分点。

### 核心结论
将语音监听时间转化为可复用的准备工作，是降低实时交互类Agent响应延迟、提升用户体验的核心可行路径。
