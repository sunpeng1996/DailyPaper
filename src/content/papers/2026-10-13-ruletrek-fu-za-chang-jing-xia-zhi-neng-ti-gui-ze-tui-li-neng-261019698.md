---
title: 'RuleTrek: Benchmarking Agentic Rule Reasoning in Complex Scenarios'
title_zh: RuleTrek：复杂场景下智能体规则推理能力评测基准
authors:
- Chenhao Yuan
- Bohan Yu
- Yinhao Xu
- Chao Yin
- Chenxi Zhou
- Zhaoxuan Wang
- Shuwen Xu
- Shaoping Huang
- Haolin Ren
- Jiaxiang Liu
affiliations:
- 中国科学院自动化研究所
- 中国科学院大学人工智能学院
- 北京人工智能研究院
arxiv_id: '2610.19698'
url: https://arxiv.org/abs/2610.19698
pdf_url: https://arxiv.org/pdf/2610.19698
published: '2026-10-13'
collected: '2026-10-15'
category: Agent
direction: Agent 规则推理能力评测
tags:
- Agent
- Benchmark
- Rule Reasoning
- LLM Evaluation
- Complex Scenario
one_liner: 提出覆盖6个领域的规则推理评测基准RuleTrek，系统评估智能体三类核心规则推理能力
practical_value: '- 构建电商/广告合规、营销活动校验类Agent时，可复用「规则图抽取→单规则子场景生成→依赖感知增量组合」的场景构建流程，每步做一致性校验，避免规则遗漏和场景冲突

  - 评估业务Agent规则处理能力时，可拆分规则识别、规则演绎、端到端推理三个维度单独评测，精准定位短板：规则识别错误占端到端失败案例的54.9%

  - 处理多文件分散的业务规则（如大促跨部门规则、售后政策）时，优先将规则结构化建模为依赖图，可显著降低Agent推理难度

  - 业务落地时尽量将规则图复杂度控制在3个节点以内、深度不超过2，规则节点≥14时Agent平均推理准确率会从76.5%骤降到23.6%，可通过规则拆解降低复杂度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有规则推理基准多采用简化的单文本场景，无法匹配真实业务中规则分散于多文档、场景信息跨多文件的复杂情况，也难以定位智能体在实际工作空间中的规则推理短板。

### 方法关键点
- 覆盖6个领域：税务、PostgreSQL、网络安全、软件政策、采购、游戏规则，共240个评测实例，规则库保留原始格式与组织结构
- 规则驱动的场景构建pipeline：第一步从真实规则库抽取结构化规则图并人工校验，节点为规则、边为规则依赖关系；第二步为每个规则生成对应子场景，确保子场景可通过该规则解决；第三步按照规则依赖增量组合子场景，每步都校验一致性和可解性
- 三类评测维度：Rule Identification（RI，从原始规则文档中定位适用规则及依赖）、Rule Deduction（RD，给定规则图后结合分散场景信息推理答案）、End-to-End Rule Reasoning（E2E，同时完成规则识别与演绎）

### 关键结果
测试11款前沿LLM，最高RI得分仅62.47%、最高RD得分仅60.43%，E2E得分区间为26.97%~55.29%；规则图节点≥14时11款模型平均E2E得分仅23.6%，规则图深度≥5时平均E2E得分仅26.4%。

### 核心结论
当前LLM智能体在复杂多文件场景下的规则推理能力仍有显著缺陷，规则识别和应用的双重瓶颈共同限制了端到端表现。
