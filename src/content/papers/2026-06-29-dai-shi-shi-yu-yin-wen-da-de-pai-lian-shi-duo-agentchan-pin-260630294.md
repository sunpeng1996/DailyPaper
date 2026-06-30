---
title: Rehearsed Multi-Agent Live Product Demonstrations with Real-Time Voice Question
  Answering
title_zh: 带实时语音问答的排练式多Agent产品直播演示系统
authors:
- Rahul Khedar
- Mayank Malhotra
- Avinash Karn
- Mouli V
- Prakhar Mehrotra
affiliations:
- PayPal AI
arxiv_id: '2606.30294'
url: https://arxiv.org/abs/2606.30294
pdf_url: https://arxiv.org/pdf/2606.30294
published: '2026-06-29'
collected: '2026-06-30'
category: MultiAgent
direction: 多Agent 自动化产品演示落地
tags:
- MultiAgent
- BrowserAgent
- SpeechQA
- WebAutomation
- TTS
one_liner: 提出RHETOR多Agent系统，自动生成支持实时语音问答的可交互Web产品直播演示
practical_value: '- 可复用「预排练+优雅降阶」架构：将Agent执行失败面从线上转移到离线预演阶段，失败操作自动降级为纯旁白，避免电商AI主播、自动化商品演示等场景出现线上事故

  - 复用6级语义定位器优先级策略：按role+name→text→label→placeholder→test-id→CSS顺序尝试元素定位，抗页面DOM结构变更能力远高于直接用CSS选择器，适合电商频繁迭代的运营页、商品页自动化交互场景

  - 采用语音-动作段同步握手机制：等旁白音频播放完成后再触发对应交互动作，彻底解决TTS延迟波动导致的语音与操作不同步问题，可直接迁移到AI直播、数字人演示场景'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有Web产品演示要么依赖人工，人力成本高且内容随产品迭代快速失效；要么是预录固定视频，无法支持实时交互问答，界面漂移后直接失效；通用浏览器Agent仅能完成指令式任务，不具备演示所需的叙事编排和语音交互能力。

### 方法关键点
- 五阶段pipeline：并行执行UI爬虫探索+源码分析，跨模态合并生成带HERO/SUPP/MENTION三级优先级的功能标签，生成动作严格绑定探索到的UI元素的演示脚本，多轮排练修复定位失败的元素，最终输出带同步旁白、支持实时问答的直播演示
- 6级优先级定位器策略，失败后LLM自动生成新定位器左序插入重试，最多3轮排练，无法修复的动作降级为纯旁白，保证演示流程完整性
- 运行时采用段同步握手协议，每段旁白播完再触发对应操作，实现零漂移；实时语音QA用RAG检索预先生成的跨模态知识文档，同时支持UI交互类和架构类问题回答

### 关键结果
在4个上线Web应用（包括开源白板Excalidraw）上完成6轮测试，147个脚本动作的定位成功率范围0.31~1.00；53个动作的复杂场景下定位成功率达0.92；Excalidraw场景下2轮排练后定位成功率达100%；排练耗时主要由浏览器操作决定，单轮仅10~41秒，LLM开销占比极低。

### 最值得记住的一句话
Agent落地优先把不确定性转移到离线可控阶段，用明确的降级规则替代强依赖模型能力的在线推理，可靠性提升远高于模型参数规模的增加
