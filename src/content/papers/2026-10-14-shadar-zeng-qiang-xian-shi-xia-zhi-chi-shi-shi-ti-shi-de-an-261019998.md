---
title: 'ShadAR: Real-time Prompting On-demand Visual Augmentation in Augmented Reality'
title_zh: ShadAR：增强现实下支持实时提示的按需视觉增强系统
authors:
- Yanni Mei
- Samuel Hartenstein
- Jonas Wombacher
- Florian Mueller
- Jan Gugenheimer
affiliations:
- TU Darmstadt
arxiv_id: '2610.19998'
url: https://arxiv.org/abs/2610.19998
pdf_url: https://arxiv.org/pdf/2610.19998
published: '2026-10-14'
collected: '2026-10-18'
category: Other
direction: AR视觉增强 · 自然语言交互
tags:
- AR
- LLM
- Object Detection
- Shader Generation
- Natural Language Interaction
one_liner: 提出支持自然语言指令实时生成AR视觉增强效果的ShadAR系统，总结两类用户提示范式
practical_value: '- 自然语言意图理解+目标检测+规则生成的端到端链路可复用在AR电商场景：比如用户说「放大这个口红的色号」，自动识别商品+生成视觉增强效果，提升AR试穿/试妆交互体验

  - 过程式/目标式两类用户提示的分类框架可用于优化交互系统的意图识别逻辑，针对目标式提示设计多链路fallback策略降低不可控性

  - 实时shader注入的低延迟视觉修改方法可迁移到直播/短视频实时特效生成场景，支持用户自定义特效指令'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有AR视觉增强效果均由专家预编程实现，静态固化缺乏灵活性，无法响应用户按需自定义实时视觉效果的需求。
### 方法关键点
通过shader注入实现AR画面的实时图形操控，收到用户自然语言prompt后：1. 调用LLM（GPT5.2）解析用户意图；2. 用YOLOv26目标检测分析当前视野内容；3. 自动生成像素shader并应用到目标区域。
### 关键结果
21名HCI研究者的用户研究共识别出4类适用场景（设计、健康、生产力、社交互动），总结得到两类用户提示范式：明确修改对象与操作的过程式提示，仅表达期望状态的目标式提示。
