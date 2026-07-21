---
title: Environment-free Synthetic Data Generation for API-Calling Agents
title_zh: 无需真实环境的API调用智能体合成数据生成方法
authors:
- Seanie Lee
- Sanjoy Chowdhury
- Chao Jiang
- Cheng-Yu Hsieh
- Ting-Yao Hu
- Alexander T Toshev
- Oncel Tuzel
- Raviteja Vemulapalli
affiliations:
- Apple
arxiv_id: '2607.16900'
url: https://arxiv.org/abs/2607.16900
pdf_url: https://arxiv.org/pdf/2607.16900
published: '2026-07-17'
collected: '2026-07-21'
category: Agent
direction: API调用Agent · 无环境合成数据生成
tags:
- Agent
- Synthetic Data
- API Calling
- LLM Simulator
- SFT
one_liner: 仅需API规范即可生成高质量多步调用轨迹，训练的API调用智能体效果优于真实环境数据训练方案
practical_value: '- 电商/推荐场景的工具调用Agent训练可直接复用这套pipeline，无需搭建完整API执行环境和数据库，仅靠内部API的OpenAPI规范即可生成训练数据，大幅降低冷启动成本

  - 任务生成的分桶采样+逆频率采样策略可迁移到其他合成数据生成场景，保证不同难度、类型的API覆盖度均衡，避免数据塌缩到高频API

  - LLM模拟API响应的4条规则（数据一致性/多样性/真实性/schema合规）+ 多层校验（参数校验→schema校验→历史一致性校验），可复用在内部API模拟服务，用于Agent离线测试和数据生成

  - 结论可复用：纯合成数据训练的4B-8B小模型即可达到甚至超过GPT-4o等大模型的API调用效果，适合端侧/低延迟场景的Agent部署'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
训练API调用LLM Agent需要大量包含多步交互的高质量轨迹数据，现有合成数据方案依赖真实可执行的API环境和预填充的后端数据库，搭建环境、填充数据的成本极高，是Agent规模化落地的核心瓶颈。

### 方法关键点
- 三阶段ESAT pipeline：仅输入API规范即可生成训练数据，分为任务合成、轨迹合成、轨迹过滤三个核心模块
- 任务合成：按难度、动作类型、涉及APP数等维度分桶生成任务，搭配逆频率采样保证API覆盖度，再经LLM校验、改写为符合真实用户习惯的自然请求
- 轨迹合成：教师Agent与LLM API模拟器迭代交互，模拟器基于任务、交互历史、API规范生成响应，内置数据一致性、多样性、真实性、schema合规4条规则，搭配多层校验（参数校验→schema校验→历史一致性校验）保证响应质量
- 轨迹过滤：用LLM judge多轮评估，仅保留多数投票为正确的高质量轨迹

### 关键实验
在AppWorld、OfficeBench两个行业通用Agent基准上测试，覆盖1.7B到27B参数的全规模模型：SFT后模型性能最高提升50.5%（AppWorld）、60.5%（OfficeBench）；纯合成数据训练的模型效果超过用真实AppWorld环境数据训练的同规模模型；4B-8B小模型经ESAT数据训练后，性能超过GPT-4o、Nemotron-120B等大模型的零-shot效果。

最值得记住的一句话：仅靠API规范生成的纯合成数据，就能训练出效果优于真实环境数据训练的API调用Agent，大幅降低Agent落地的冷启动成本。
