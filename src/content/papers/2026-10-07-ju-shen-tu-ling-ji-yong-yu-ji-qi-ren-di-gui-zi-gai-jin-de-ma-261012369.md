---
title: 'Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement'
title_zh: 具身图灵机：用于机器人递归自改进的有状态代码范式
authors:
- Kairui Hu
- Siyuan Hu
- Fangzhou Hong
- Zhaoxi Chen
- Ziwei Liu
affiliations:
- Nanyang Technological University
- Ropedia
arxiv_id: '2610.12369'
url: https://arxiv.org/abs/2610.12369
pdf_url: https://arxiv.org/pdf/2610.12369
published: '2026-10-07'
collected: '2026-10-10'
category: Agent
direction: 具身Agent · 纯代码策略范式
tags:
- EmbodiedAgent
- CodeAsPolicy
- RecursiveSelfImprovement
- TuringMachine
- Robotics
one_liner: 提出纯代码作为策略的COAP范式，无需运行时VLM/VLA，支持机器人任务递归自改进
practical_value: '- Agent 系统设计可借鉴 COAP 的显式状态管理思路，将用户、环境、任务状态用结构化变量存储，替代LLM上下文记忆，降低推理成本与幻觉概率

  - 多任务 Agent 能力沉淀可复用共享代码库机制，通用能力封装为可调用工具函数，新任务直接继承扩展，无需从零训练或Prompt调试

  - 业务策略迭代可参考COAP的递归自改进闭环：线上运行→异常校验→逻辑更新→回归验证，可控性远高于端到端微调模型'
score: 6
source: huggingface-daily
depth: abstract
---

## 动机
现有机器人策略运行时需调用VLM/VLA决策，存在可控性弱、推理成本高、跨任务能力难沉淀的问题，难以实现可控的递归自改进。
## 方法关键点
1. 提出具身图灵机抽象：将机器人与环境状态作为磁带、策略作为执行规则，状态可精准表征时无需大模型介入控制循环；
2. 设计纯代码策略范式COAP：代码从图像、本体感知数据中显式跟踪机器人、环境、任务三类状态，直接输出决策；
3. 支持多任务能力复用与递归自改进：不同任务共享通用代码库，新任务可复用、继承、扩展已有能力，编码Agent可闭环迭代更新代码库。
## 关键结果
在RoboDojo 42项双手操作任务上，测试阶段无模型介入的COAP成功率达70.24%，远高于VLA方案的33.95%与Agent Harness方案的36.27%，同时具备执行速度快、成本低、故障恢复灵活的优势。
