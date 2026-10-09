---
title: 'From Traces to Agentic Worlds: Agentic Language World Models for Interactive
  Environment Simulation'
title_zh: 基于交互轨迹构建智能体仿真环境的语言世界模型Trace2Env
authors:
- Quanyu Long
- Xiao Chen
- Jianda Chen
- Haozhen Zhang
- Qisheng Hu
- Jianzhu Bao
- Wenya Wang
affiliations:
- Nanyang Technological University
- The Hong Kong Polytechnic University
arxiv_id: '2610.06100'
url: https://arxiv.org/abs/2610.06100
pdf_url: https://arxiv.org/pdf/2610.06100
published: '2026-10-04'
collected: '2026-10-09'
category: Agent
direction: Agent 环境仿真 · 语言世界模型
tags:
- Agent
- World Model
- Environment Simulation
- Trajectory Mining
- LLM Agent
one_liner: 无训练框架将历史交互轨迹转化为结构化世界书，实现高保真有状态环境仿真，无需复现原系统
practical_value: '- 电商/业务Agent训练评测可复用该无训练方案：仅需历史交互日志即可构建仿真环境，无需复现复杂业务系统，大幅降低Agent落地的测试成本

  - 可借鉴世界书分层知识设计：将历史日志拆解为接口Schema、落地证据、行为规则三类知识，比直接RAG召回原始日志的仿真准确度高2~6个百分点，适配业务环境一致性需求

  - 多轮交互场景可复用「全局静态知识+会话级动态状态+交互记忆」的分层状态管理方案，解决长流程状态幻觉问题，比如导购Agent多轮状态追踪、下单流程仿真'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent的训练、评测依赖真实环境交互，但电商/企业内部系统往往无法开放或低成本复现；传统Prompt驱动的语言世界模型长轮次仿真一致性差，容易出现状态幻觉，导致训练出的Agent无法迁移到真实环境。

### 方法关键点
- 离线无训练构建结构化世界书：从历史交互轨迹中提取环境动作/状态Schema、原始交互证据、归纳的通用行为规则、来源溯源四个模块，跨会话复用
- 在线双Agent架构：世界模型Agent作为任务Agent的仿真环境，结合静态世界书、当前会话动态状态、历史交互记忆三类信息，预测动作的观测结果和状态变更
- 双层门控校验：适用性门控区分召回知识的适用范围（支持性/不确定/仅格式用），验证门控校验状态变更合法性，避免错误状态扩散

### 关键结果
在9个环境（含电商购物、员工福利系统等业务场景）测试，对比直接Prompt、Trace RAG Prompt等baseline：
1. 单步观测预测平均分比直接Prompt高6.4~7.0分（0~100分制），所有环境的事实性和一致性均显著提升
2. 长轮次交互的W2R（仿真生成的动作序列在真实环境重放的成功率），ALFWorld场景从3%提升到85%，一致性CR从0.032提升到0.914；SciWorld场景W2R从45%提升到60%，CR从0.529提升到0.706

> 最值得记住的结论：长轮次环境仿真的核心指标不是仿真环境内的成功率，而是仿真中生成的行为能否迁移回真实环境
