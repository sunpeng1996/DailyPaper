---
title: 'LEASH: Stay Safe in Agentic Robotics'
title_zh: LEASH：具身智能机器人Agent安全防护框架与RoboRisk评测基准
authors:
- Qinfeng Zhu
- Weiguang Zhao
- Ke Sun
- Xihao Guo
- Yunxi Jiang
- Rui Zhang
- Lei Fan
- Kaizhu Huang
affiliations:
- Xi'an Jiaotong-Liverpool University
- Duke Kunshan University
- University of Liverpool
- National University of Singapore
- CNRS
arxiv_id: '2611.14115'
url: https://arxiv.org/abs/2611.14115
pdf_url: https://arxiv.org/pdf/2611.14115
published: '2026-11-09'
collected: '2026-11-12'
category: Agent
direction: 具身Agent 安全防护与评测
tags:
- Agent Safety
- Embodied AI
- Benchmark
- Safety Gate
- Foundation Model
one_liner: 推出覆盖5类安全场景的RoboRisk评测基准，以及兼容主流Agent架构的LEASH安全防护框架降低具身Agent危害率
practical_value: '- 电商智能导购/仓储AGV/自动直播等业务Agent可复用LEASH三级门控架构：分别在任务接收、动作生成、不可逆操作提交三个环节做安全校验，可适配任意现有Agent架构

  - Agent安全评测可借鉴RoboRisk的5类场景划分逻辑，覆盖任务拒识、计划修复、执行风险、Prompt注入、记忆篡改全链路风险点

  - 安全校验逻辑可复用「统一安全策略+上下文感知决策模型」的设计，在几乎不损失核心任务完成率的前提下降低额外开销'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前大模型驱动的具身机器人Agent缺乏系统性安全评测方案，已有的基准覆盖场景不足2类，多仅校验文本输出，大模型控制机器人存在极高危害风险。
### 方法关键点
1. 构建RoboRisk基准，覆盖任务拒识、计划修复、执行风险、Prompt注入、序列记忆5大类安全场景，含92个仿真任务+13个实体机器人任务，全部闭环执行；
2. 提出LEASH安全框架，适配任意Agent架构，基于统一安全策略设置任务门、动作门、提交门三级校验，分别校验任务合法性、单步动作安全性、不可逆操作风险。
### 关键结果数字
在6款主流大模型、2款机器人API上验证，LEASH可将实体机器人场景下4款大模型的危害率降至0%，几乎不损失任务完成率，额外时间和token开销极低。
