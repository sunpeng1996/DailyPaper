---
title: 'Lies We Can See: Joint Verbal and Non-Verbal Deception by VLM Agents in Embodied
  Social Interactions'
title_zh: 具身社交场景下VLM智能体的语言与非语言联合欺骗行为研究
authors:
- Jaewoo Ahn
- Junseo Kim
- Hyunseo Kim
- Heeseung Yun
- Jaehyeon Son
- Zsolt Kira
- Gunhee Kim
affiliations:
- Seoul National University
- Inha University
- KAIST
- Georgia Institute of Technology
arxiv_id: '2608.30428'
url: https://arxiv.org/abs/2608.30428
pdf_url: https://arxiv.org/pdf/2608.30428
published: '2026-08-30'
collected: '2026-09-02'
category: MultiAgent
direction: 具身多智能体 · 多模态欺骗行为分析
tags:
- VLM
- Multi-Agent
- Embodied AI
- Deception
- LLM-as-Judge
- Social Deduction
one_liner: 提出3D多模态社交推理测试环境与可配置VLM代理框架，量化具身场景多模态欺骗行为
practical_value: '- 多模块Agent/推荐系统架构可参考ARIA的可插拔消融设计思路，将状态表示、记忆、规划、排序策略等模块做成独立可配置轴，快速迭代定位性能瓶颈

  - 电商虚假宣传检测、多Agent交互仿真（如商家-用户博弈、虚拟主播策略优化）等场景可复用原子级行为标注+LLM-as-Judge方案，标注一致性达Cohen
  κ=0.709，大幅降低人工标注成本

  - 营销/内容类Agent的策略优化可参考欺骗行为的量化思路，将多维度策略拆解为原子动作+序列弧组合，精准归因不同策略对转化的贡献

  - 开发AR导购、虚拟店员等具身Agent时，注意当前VLM第一人称空间感知能力不足，需补充结构化全局状态辅助信息，避免直接使用纯egocentric输入'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM/VLM Agent欺骗行为研究全部基于纯文本社交推理游戏，缺失了欺骗行为核心的非语言感知-动作通道，且所有测试都基于固定Agent配置，无法区分行为是模型固有属性还是框架配置导致，无法支撑具身多模态Agent的对齐与安全研究。

### 方法关键点
- 搭建**MINEAMONGUS**：基于Minecraft的3D多模态Among Us沙箱，支持VLM Agent第一人称RGB输入、连续空间移动交互、自然语言会议沟通，同时覆盖语言与非语言欺骗通道
- 提出**ARIA**可配置VLM Agent框架，开放5个独立消融轴：状态表示、记忆、规划、反思与技能记忆、提示风格，可精准归因不同组件对欺骗行为的影响
- 构建覆盖23种原子欺骗动作、序列弧级的标注体系，配套LLM-as-Judge标注pipeline，与人工标注Cohen κ达0.709，接近人-人标注一致性0.792

### 关键实验结果
- 固定VLM消融ARIA组件：仅用第一人称输入时，内鬼胜率从40%跌到0%，完全无法完成击杀；分层规划、会后反思、滚动窗口记忆等配置可平均提升内鬼胜率9.4pp；非语言击杀循环类动作（跟踪、无目击者击杀、逃离现场）与胜率的相关性最高（点二列相关系数最高达0.434）
- 固定ARIA配置对比12款VLM：模型作为内鬼和船员的胜率高度相关（Pearson r=0.71），说明通用能力远重于角色专项能力；表现最好的VLM的非语言伪装类动作（假装做任务）是最差模型的6.6倍，是区分胜负的核心指标

**最值得记住的结论**：具身场景下VLM Agent的欺骗行为中，非语言动作通道的贡献远高于单纯的语言话术。
