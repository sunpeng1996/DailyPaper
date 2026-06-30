---
title: 'AgentOdyssey: Open-Ended Long-Horizon Text Game Generation for Test-Time Continual
  Learning Agents'
title_zh: AgentOdyssey：面向测试时持续学习Agent的开放长程文本评测框架
authors:
- Zheyuan Zhang
- Zehao Wen
- Alvin Zhang
- Andrew Wang
- Jianwen Xie
- Daniel Khashabi
- Tianmin Shu
affiliations:
- Johns Hopkins University
arxiv_id: '2606.24893'
url: https://arxiv.org/abs/2606.24893
pdf_url: https://arxiv.org/pdf/2606.24893
published: '2026-05-28'
collected: '2026-06-30'
category: Agent
direction: Agent 测试时持续学习能力评测
tags:
- LLM Agent
- Continual Learning
- Evaluation
- Benchmark
- Long Horizon
one_liner: 提出面向测试时持续学习Agent的开放式长程文本游戏评测基准
practical_value: '- 做长程交互类Agent（如电商会话推荐Agent、多轮购物Agent）时，需要设计「推理与学习 interleaved」的在线部署框架，测试时也允许Agent持续更新积累知识

  - 评估长程交互Agent不要只看最终任务指标，可借鉴多维度诊断方法，拆分知识获取、记忆保留、探索多样性等维度定位系统瓶颈

  - 验证了短期记忆对各类测试时学习Agent都有明确增益，开发交互Agent时可优先优化短期记忆模块，投入产出比更高'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有Agent评测大多遵循「测试阶段不更新学习」的传统机器学习假设，缺少适配测试时持续学习Agent的长程开放交互场景，无法有效衡量Agent探索、新知识获取、记忆保留、长程规划这些核心能力。
### 方法关键点
提出AgentOdyssey评测框架，通过过程式生成方式构建带有丰富实体、动态世界规则和长程任务的开放文本游戏，评测场景全程交错学习与推理，贴合真实部署中测试时持续学习的设定；同时设计多维度评测方案，除核心任务进度外，还包含世界知识获取、情景记忆、探索覆盖率、动作多样性、模型开销多个诊断维度。
### 关键结果
评测多种Agent范式发现：性能随基座模型能力提升而增长，但当前最强Agent性能仍远低于人类水平，仍有很大提升空间；验证了短期记忆对多种Agent范式都有正向增益，是测试时学习Agent的核心必要组件。
