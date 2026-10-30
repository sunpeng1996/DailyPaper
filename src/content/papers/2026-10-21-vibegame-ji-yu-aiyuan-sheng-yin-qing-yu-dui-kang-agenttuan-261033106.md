---
title: 'VibeGame: Prompt-to-Game Development with AI-Native Engine and Self-Evolving
  Adversarial Agent Team'
title_zh: VibeGame：基于AI原生引擎与对抗Agent团队的提示词生成游戏框架
authors:
- Wenbo Hu
- Ken Li
- Jiazhe Wei
- Yukang Cao
- Weiyi Hong
- Jiayi Dai
- Chenjun Bai
- Jiajun Liang
- Yucheng Liao
- Ruichuan An
affiliations:
- PRLab, Nanjing University
- S-Lab, Nanyang Technological University
- Liblib.ai
arxiv_id: '2610.33106'
url: https://arxiv.org/abs/2610.33106
pdf_url: https://arxiv.org/pdf/2610.33106
published: '2026-10-21'
collected: '2026-10-30'
category: MultiAgent
direction: 多智体协作 · 生成式产品开发
tags:
- MultiAgent
- LLM Agent
- Prompt-to-Product
- Self-Evolution
- Agent Collaboration
one_liner: 提出端到端提示词生成可运行2D游戏的框架，融合AI原生引擎、多角色对抗Agent团队与无训练自进化机制
practical_value: '- 多角色对抗Agent架构可直接迁移到电商广告素材、活动页、营销文案的自动生成场景，拆分生产、审核、测试角色，通过多轮校验降低逻辑错误、视觉不符、合规问题的发生率

  - 无训练自进化机制可复用到推荐系统、广告系统的策略开发流程，将验证通过的特征工程模板、排序策略、AB测试流程沉淀为通用骨架、模块与协作合约，大幅降低重复开发成本

  - AI原生系统设计思路可用于搭建业务侧Agent的操作接口，将商品、订单、用户、活动等业务状态全部结构化暴露，提供可调试的运行时控制接口，避免Agent适配GUI的高成本与不稳定问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent做软件开发大多无法覆盖游戏这类需要协调代码、资产、动画、物理逻辑的复杂场景，传统游戏引擎依赖GUI操作，Agent无法统一管控项目状态、调试运行时问题，且开发经验无法复用，导致端到端提示词生成可运行游戏的效果差、错误率高。

### 方法关键点
- 设计AI原生2D游戏引擎：全项目状态用结构化JSON存储，无GUI依赖，支持帧同步的运行时控制，Agent可直接暂停、步进、注入操作、校验运行时效果，引擎源代码随项目打包，避免文档不一致问题
- 搭建8角色Adversarial Agent Team：拆分设计、美术、架构、开发、审计、测试、评审、调度角色，开发和校验分离，通过多轮对抗评审修复逻辑、视觉、玩法问题，直到满足需求
- 无训练自进化机制：把验证通过的项目沉淀成三类可复用资产：游戏类型骨架（保留架构、调优参数、美术生成规则）、通用功能模块（可直接挂载的行为脚本）、协作合约（特定功能的角色协作流程、验收标准）

### 关键实验
在GameCraft-Bench的30个2D游戏任务上测试，对比Codex、OpenGame等主流Agent框架：用GPT-5.6-Luna时，VibeGame（P2G模式）总体得分49.99，领先最强基线11.7分；用GPT-6.1-Sol时，总体得分72.99，领先最强基线4.19分，用户调研平均胜率达72.7%。 ablation实验显示移除AI原生引擎或对抗Agent团队，得分分别下降10.33、4.63分，强模型沉淀的经验可提升弱模型得分2.92分。

### 核心结论
复杂多模态产品的Agent自动生成系统，需要统一的结构化状态层、角色分离的校验机制、可复用的经验沉淀三者紧密结合，才能大幅超越通用Agent的效果。
