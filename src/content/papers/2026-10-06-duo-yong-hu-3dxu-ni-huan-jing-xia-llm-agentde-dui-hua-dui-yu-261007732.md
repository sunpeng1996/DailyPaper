---
title: Who Is Talking to the Agent? LLMs in Multi-User 3D Virtual Environments
title_zh: 多用户3D虚拟环境下LLM Agent的对话对象识别与隐私风险研究
authors:
- Mohammad Al-Ratrout
- Shayla Sharmin
- Roghayeh Leila Barmaki
affiliations:
- University of Delaware
arxiv_id: '2610.07732'
url: https://arxiv.org/abs/2610.07732
pdf_url: https://arxiv.org/pdf/2610.07732
published: '2026-10-06'
collected: '2026-10-07'
category: Agent
direction: 多用户Agent · 3D环境交互优化
tags:
- Multi-User Agent
- Addressee Detection
- Spatial Cue
- Privacy Leakage
- LLM
one_liner: 构建LOOKAWAY受控语料库，揭示多用户场景下LLM Agent对空间信号的过度依赖与隐私泄露风险
practical_value: '- 电商虚拟直播间、多人在线导购场景的共享Agent可引入用户朝向、空间距离信号替代部分唤醒词触发逻辑，降低用户交互成本

  - 多用户场景下给Agent传入用户profile时需做分层隔离：仅用户在公开会话中主动披露的属性允许被用于回答其他用户的询问，避免未公开的偏好、隐私信息泄露

  - 空间朝向信号不能作为对话对象判定的唯一依据，需叠加会话关键词、上下文相关性做加权决策，可参考论文的提示词优化方案降低对不可靠空间信号的过度依赖

  - 多用户交互Agent的评测可复用LOOKAWAY的受控变量设计，独立控制信号一致性、信息可见性等维度，快速定位系统缺陷'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
LLM Agent已广泛应用于XR、虚拟直播间等共享3D环境，但现有方案存在两个核心痛点：一是多用户对话时无法精准判断用户是否在和自己说话，空间朝向这类易得信号的可靠性未知；二是Agent获取多用户profile后容易泄露用户未公开的隐私信息，此前缺乏同时控制对话对象、空间信号、profile可见性的受控评测语料，无法系统性验证上述问题。

### 方法关键点
- 构建LOOKAWAY受控语料库：包含40组双用户会话共1200轮对话，覆盖80个独立persona，每个persona设4个公开会话属性+4个仅profile可见的隐式属性，独立控制每轮对话的说话人朝向（与目标对象一致/冲突）、Agent可见的profile范围
- 设计5组对照实验：从无profile无空间信息的基线，到同时提供双用户profile+空间信息，测试3款开源LLM（Qwen3.6 27B、Mistral Small3.2 24B、Nemotron3 33B）共18000次决策
- 核心评测指标：对话对象识别准确率、跨用户询问的回答正确率、未公开属性泄露率

### 关键结果数字
- 加入与对话目标对齐的朝向信号后，对话对象识别准确率从56%提升至99.5%；但当朝向与目标冲突时，两款表现合格的模型85%以上的决策会跟随朝向信号，即便提前警告朝向可能不可靠，仅能将该比例降低不到10%
- 给Agent同时提供双用户profile时，跨用户询问的正确回答率从14%提升至56.2%，但未公开属性泄露率也从3.3%飙升至45.3%；添加通用隐私提示可将泄露率降至24.4%，而过严的隐私规则会导致60%以上的公开信息问题被拒绝回答

### 核心结论
多用户共享LLM Agent不能仅靠增加上下文提升效果，必须同时设计信号加权规则与信息权限控制机制，否则会同时出现误响应和隐私泄露问题
