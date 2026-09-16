---
title: 'Emergence World: Adversarial Stress-Testing of Long-Horizon Multi-Agent Systems'
title_zh: Emergence World：面向长周期多智能体系统的对抗压力测试平台
authors:
- Deepak Akkil
- Tamer Abuelsaad
- Karthik Vikram
- Matthew Pace
- Aditya Vempaty
- Saahir Beotra
- Ravi Kokku
- Satya Nitta
affiliations:
- Emergence AI
arxiv_id: '2609.17320'
url: https://arxiv.org/abs/2609.17320
pdf_url: https://arxiv.org/pdf/2609.17320
published: '2026-09-14'
collected: '2026-09-16'
category: MultiAgent
direction: 多智能体系统鲁棒性 · 对抗压力测试
tags:
- Multi-Agent System
- Adversarial Testing
- Long-Horizon Agent
- Safety Evaluation
- Agent Simulation
one_liner: 构建持续运行的多智能体仿真环境，测试长周期下系统对三类对抗压力事件的响应韧性
practical_value: '- 多Agent系统上线前可参考本文三类压力事件（indirect prompt injection、虚假信息、内存泄露）设计鲁棒性测试用例，提前发现跨Agent传播的长周期风险

  - 部署长期运行的Agent集群时，不能仅做单Agent对齐，需额外增加系统层风险隔离机制，避免单个Agent故障通过记忆、工具调用、跨Agent通信扩散

  - 可复用本文分层工具设计（核心/补充/上下文门控），控制Agent工具调用权限范围，同时避免工具列表过长降低LLM tool call准确率

  - 业务涉及多Agent协作时，可参考Agent World Indicators设计系统级健康度监测指标，替代单Agent任务完成率指标，及时发现群体级异常（如目标漂移、集体不作为）'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
单Agent、短会话的安全评估无法覆盖长周期多智能体系统的风险：故障会通过记忆、工具调用、跨Agent交互、环境状态长期传播，企业级Agent工作流、具身AI等落地场景已面临这类风险，现有仿真环境不支持长周期、自治理、对抗事件注入的系统级测试。

### 方法关键点
- 搭建持续运行的多智能体仿真平台，支持120+分层工具调用、自主代码生成与工具扩展、民主治理机制、三层自主可控记忆架构，兼容不同厂商LLM作为Agent底座；
- 设计三类真实攻击场景的压力事件：多轮钓鱼（indirect prompt injection）、虚假信息投放、隐私内存泄露，通过Agent常规交互通道注入，无提前通知；
- 提出5个系统级Agent World Indicators，从群体健康、公共秩序、治理一致性、社会结构、经济活动多维度评估系统状态，避免单一指标局限性。

### 关键结果
8个并行世界（7个同构单模型世界、1个混合模型世界）共80个Agent，最长运行21天，累计85万+ LLM调用、近500亿token。所有世界均未通过三类压力事件的全resilience测试：即使Agent识别到威胁，仍有概率将敌对内容写入持久记忆，最长46小时后仍执行相关操作；单模型同构世界易出现「社会谄媚」效应，即使Agent私下不认同也会从众投票，混合模型世界该效应明显减弱。

单Agent对齐不具备组合性，当AI走向持久化、互联化，安全的前沿已经从模型对齐转向工程化的自治系统韧性建设。
