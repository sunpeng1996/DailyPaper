---
title: 'ControlAnything: Generative UI and On-Demand Device Integration for Mixed-Reality
  Hand Interaction by a Coding Agent'
title_zh: ControlAnything：编码Agent驱动的MR生成式UI与按需设备集成
authors:
- Bektur Ryskeldiev
affiliations:
- Independent Researcher, Tokyo, Japan
arxiv_id: '2611.08321'
url: https://arxiv.org/abs/2611.08321
pdf_url: https://arxiv.org/pdf/2611.08321
published: '2026-11-05'
collected: '2026-11-07'
category: Agent
direction: 编码Agent · 混合现实按需设备集成
tags:
- CodingAgent
- GenerativeUI
- MixedReality
- HandGesture
- IoTIntegration
one_liner: 基于编码Agent的MR系统，可按需生成设备适配代码与AR手势交互界面
practical_value: '- 做工具调用类Agent时，可复用其带边界限制的运行机制：预设最大调用轮次、token量、超时时间，生成代码先经沙箱dry run校验合法性再上线，可用于电商营销自动化Agent、RAG工具调用Agent的安全管控，降低故障概率

  - 大模型高频调用场景可复用其prompt缓存优化方案：固定系统提示词、工具Schema等公共前缀存入缓存，实测输入token命中率达91.7%，可大幅降低调用成本与延迟，适合搜索推荐的query理解、个性化文案生成等场景

  - 生成式系统可参考其分层设计思路：通用基础能力（如本文的传输层、安全校验逻辑）由开发者预实现，上层个性化逻辑（设备映射、交互UI）由Agent生成，平衡灵活性与可控性，可迁移到生成式推荐的个性化交互组件生成、多Agent协作框架设计'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有混合现实（MR）系统操控物理设备需提前编写硬件适配代码、手势映射逻辑与交互UI，无法支持用户按需操控陌生设备；现有编码Agent多用于开发阶段，未集成到实时MR交互链路中，无法满足端侧交互的低延迟、高安全要求。
### 方法关键点
- 三层架构设计：Meta Quest 3头显负责SAM 3.1物体分割、手势跟踪与AR渲染，笔记本端运行Node服务与Muse Spark编码Agent，预实现MIDI、蓝牙、按键三类通用传输层，无需提前适配特定设备
- Agent带边界管控的工具调用链路：预设最大24轮调用、300s超时、60万token上限，生成的设备连接器代码需经测试拿到传输层确认回执后再返回结果，避免无效逻辑上线
- 低延迟交互设计：生成的交互输出分为AR控件、逐帧运行的手势映射JS代码两类，后者经沙箱预校验单帧耗时<2ms，头显端本地运行无需调用大模型，确保交互实时性
### 关键结果
单用户10次请求测试，覆盖5类目标设备（合成器、DJI云台、浏览器等），9/10请求成功就绪，中位就绪时间32.5s，其中89.9%耗时为顺序模型调用，prompt缓存命中率达91.7%，生成后交互单帧耗时<4ms
### 核心结论
基础通用能力预实现、上层个性化逻辑由Agent生成的分层架构，是平衡生成式系统灵活性与可控性的可行路径
