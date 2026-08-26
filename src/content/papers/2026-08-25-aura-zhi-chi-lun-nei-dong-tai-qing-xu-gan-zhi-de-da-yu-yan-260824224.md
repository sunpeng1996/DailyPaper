---
title: 'Aura: Dynamic Intra-Turn Emotion-Aware Adaptation of Large Language Model
  Responses'
title_zh: Aura：支持轮内动态情绪感知的大语言模型响应适配框架
authors:
- Rachel Schuchert
- Christian Holz
affiliations:
- Department of Computer Science, ETH Zürich, Switzerland
arxiv_id: '2608.24224'
url: https://arxiv.org/abs/2608.24224
pdf_url: https://arxiv.org/pdf/2608.24224
published: '2026-08-25'
collected: '2026-08-26'
category: LLM
direction: 大语言模型 · 实时情绪感知响应适配
tags:
- LLM
- LoRA
- Emotion-Aware
- Human-AI Interaction
- Real-time Adaptation
one_liner: 提出Aura框架，通过感知用户实时面部情绪动态调整LLM轮内输出，提升人机交互效率
practical_value: '- 电商智能客服Agent可复用该框架逻辑，接入用户实时情绪信号（对话文本情绪、进线面捕情绪等），通过轻量LoRA切换响应风格，降低用户投诉率

  - 生成式推荐场景可借鉴轮内动态调整思路，输出商品介绍/种草文案时实时感知用户反馈（停留、点击、表情等），中途调整内容侧重，提升转化

  - 可复用概率信念模型做干预决策的设计，降低情绪感知误判导致的无效调整，平衡内容准确性与个性化适配效果'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有LLM采用静态prompt-响应交互模式，生成过程中无法感知用户即时反应，缺乏交互同步性，易导致信息过载、用户困惑无法实时解决。
### 方法关键点
提出Aura三层架构：
1. 感知模块：从用户面部表情持续估算实时情绪状态
2. 策略模块：基于概率信念模型选择最优干预策略
3. 生成模块：采用LoRA轻量适配实现响应生成过程中的轮内动态调整，输出上下文适配的定制化内容
### 关键结果
信息搜索任务用户实验（N=20）显示：相对GPT-4o、Llama-3基线，交互时间降低21%；感知学习收益显著高于Llama-3基线；事实准确性无明显下降，用户满意度显著提升。
