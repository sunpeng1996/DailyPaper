---
title: 'EAU: Environment-Agent-User Co-evolution for Training User-Centric Agents'
title_zh: EAU：环境-智能体-用户协同进化的用户中心智能体训练框架
authors:
- Min Cai
- Dan Zhang
- Gao Xing
- Libin Ma
- Zhaohui Xu
- Xi Ye
affiliations:
- University of Alberta
- National University of Singapore
- Kuaishou Technology
- Alberta Machine Intelligence Institute
arxiv_id: '2610.16523'
url: https://arxiv.org/abs/2610.16523
pdf_url: https://arxiv.org/pdf/2610.16523
published: '2026-10-11'
collected: '2026-10-22'
category: Agent
direction: Agent 训练优化 · 协同进化
tags:
- Meta Agent
- Reinforcement Learning
- User-centric Agent
- Co-evolution
- LLM Agent
one_liner: 提出元代理框架EAU，实现环境/用户/智能体协同进化，大幅提升用户中心多轮RL效果
practical_value: '- 多轮交互Agent（如电商客服、导购Agent）训练可复用「符号规则+LLM混合用户模拟器」设计，通过可调混合系数平衡用户行为可控性和对话自然度，避免模拟器泄露信息、偏离人设等问题

  - 推荐/广告系统的RL训练可引入轻量元代理监控训练轨迹，自动识别奖励稀疏、策略停滞等问题，动态新增中间奖励、调整RL超参数，减少人工调参成本，提升训练效率

  - 可落地跨训练 run 的经验沉淀机制，将历史训练中验证有效的配置（如奖励权重、用户模拟器规则）存入经验池复用，避免后续训练从零开始试错，降低大模型训练的资源消耗

  - 训练流程设计支持热插拔修改，验证有效的配置无需重启训练即可生效，缩短迭代周期，适合需要长期调优的生产级Agent训练场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
用户中心LLM Agent的多轮RL训练通常依赖固定的用户模拟器与环境，存在LLM用户模拟器行为不稳定、易泄露信息，环境奖励稀疏、规则不完善，以及训练信号随策略优化逐渐失效等问题，仅靠下游奖励shaping等方法无法从根源解决训练不稳定、效果上限低的痛点。

### 方法关键点
- 引入元代理EAU，全程监控训练轨迹、工具调用日志、奖励、训练统计数据，自动诊断失效交互，针对性修改用户模拟器、环境规则、奖励函数、RL超参数
- 设计符号+LLM混合用户模拟器，通过可调混合系数平衡符号规则的可控性和LLM交互的自然度，元代理可动态调整符号规则、生成参数、混合比例
- 支持训练中热插拔修改（intra-run）和跨训练轮次经验复用（inter-run），验证有效的修改自动更新到训练流程，沉淀到经验池供后续训练复用
- 底层Agent固定采用带GAE的PPO算法训练，元代理仅调优可配置项，不改动核心训练算法

### 关键结果
在ColBench、UserGym、τ2-bench三个用户中心Agent基准上测试，对比InfoPO等SOTA RL方法，基于Qwen3-4B和Qwen2.5-7B两个backbone，整体得分相对提升14.7%~15.0%，ColBench任务成功率最高提升36.7%，4B参数模型效果超过Gemini-3-Flash、GPT-4.1等闭源模型。

**最值得记住的一句话**：用户中心Agent的训练不需要只盯着策略优化，同步自适应调整训练环境、用户模拟器和训练配置，能带来远超单纯策略优化的效果提升
