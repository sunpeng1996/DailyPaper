---
title: 'StreamVibe: Proactive Video Agents for Evolving User Intent'
title_zh: StreamVibe：面向动态演化用户意图的主动视频交互智能体
authors:
- Chengzhi Liu
- Yuxiang Lai
- Yuzhe Yang
- Yanqing Liu
- Jiheng Hou
- Yue Cao
- Haonan Wang
- Ruixi Fan
- Lan Wang
- Sheng Liu
affiliations:
- Google
- University of California Santa Barbara
- University of California Santa Cruz
- Stanford University
- University of Oxford
arxiv_id: '2610.34662'
url: https://arxiv.org/abs/2610.34662
pdf_url: https://arxiv.org/pdf/2610.34662
published: '2026-10-25'
collected: '2026-10-27'
category: Agent
direction: Agent主动交互 · 用户意图动态追踪
tags:
- Proactive Agent
- User Intent Tracking
- Multimodal LLM
- Streaming Video
- Hierarchical Memory
one_liner: 提出覆盖显式/隐式/动态用户意图的主动交互基准、流式模型与状态框架，响应质量较基线提升10.7%
practical_value: '- 电商直播/短视频带货场景可复用分层记忆+意图生命周期管理方案，追踪用户浏览/互动行为的隐式意图，触发精准推荐弹窗/智能助理响应，平衡转化效率和用户体验

  - 主动交互类Agent可借鉴自适应流式SFT+局部轨迹RL的训练范式，调整沉默/响应的权重平衡，降低误触发率，避免过度打扰用户

  - 多轮动态需求场景可复用显式交互状态维护方案，独立跟踪用户修订/新增/中断的多意图，避免长交互中的意图漂移和响应过时'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有主动交互多模态模型仅支持显式用户请求，无法推理用户隐式意图、跟踪动态变更的需求，长交互中易出现重复、过时、遗漏响应，无法适配电商直播、实时客服、内容推荐等需感知用户动态意图的业务场景。
### 方法关键点
- 构建StreamVibe-Bench：包含85K训练样本、4.1K评测样本，覆盖显式、隐式、动态三类用户意图，支持点式（单步决策）和轨迹（全流程交互）双维度评估
- StreamVibe-VL流式模型：先用自适应流式SFT调整沉默/响应token的权重，平衡两类任务的学习效果；再用局部轨迹RL仅优化关键交互片段，避免全轨迹优化的信用分配模糊问题，同时提升响应时机准确性和内容质量
- StreamVibe-Harness状态框架：显式维护活跃意图、任务进度、历史响应三类交互状态，每个意图独立管理生命周期；分层记忆压缩旧信息、按需检索相关上下文，降低长交互的上下文冗余
### 关键实验结果
对比Gemini 3.8 Flash、GPT-Realtime 2.1、Qwen3-VL等10+基线模型，StreamVibe-VL较开源基线的响应时机+质量综合得分提升10.7%，叠加StreamVibe-Harness后主动交互效果再提升12.3%，同时不损失通用视频理解能力。
### 最值得记住的结论
主动交互的核心不是越快响应越好，而是精准感知用户隐式需求、动态追踪意图变更，在正确的时机提供正确的帮助。
