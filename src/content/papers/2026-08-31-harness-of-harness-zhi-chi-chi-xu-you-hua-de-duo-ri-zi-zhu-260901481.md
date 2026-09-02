---
title: 'Harness-of-Harness: Multi-Day Autonomous Software Development with Continual
  Improvement'
title_zh: Harness-of-Harness：支持持续优化的多日自主软件开发框架
authors:
- Haoyang Yan
- Min-le Su
- Hangfan Zhang
- Zhanhao Li
- Chen Zhang
- Shao Zhang
- Yang Chen
- Lei Bai
- Shuyue Hu
affiliations:
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2609.01481'
url: https://arxiv.org/abs/2609.01481
pdf_url: https://arxiv.org/pdf/2609.01481
published: '2026-08-31'
collected: '2026-09-02'
category: Agent
direction: Agent 长周期任务迭代优化框架
tags:
- Agent Orchestration
- Autonomous Software Development
- Iterative Optimization
- Multi-Role Agent
- LLM4Code
one_liner: 基于现有编码Agent Harness构建迭代规划-编码-测试闭环，大幅提升长周期软件开发质量
practical_value: '- 电商/推荐领域的多Agent迭代任务（如素材自动生成、推荐策略迭代、大促活动页自动开发）可复用HoH三角色框架：规划（定小范围可验证的迭代目标）→开发（落地策略/素材/代码）→独立QA（验效果），避免大范围改动引入不可控风险

  - 长周期Agent任务（如全链路自动运营、用户生命周期自动运营）可参考其双状态管理方案：分别维护当前产物状态（已上线的策略/素材）和证据状态（已验证的效果、未解决的问题），避免迭代中丢失历史信息、重复踩坑

  - Agent任务的验收环节可参考其独立QA+黑白盒验证设计：开发者自测仅做预校验，最终效果由独立角色通过外部可观测指标（黑盒）+内部逻辑校验（白盒）双重验证，避免自嗨式验收'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有编码Agent大多仅支持单轮、人在环的辅助开发，长周期自主开发场景下易出现历史需求遗忘、局部修改引入全局冲突、陷入无效重复修复等问题，无法持续迭代产出完整可用的复杂软件系统。

### 方法关键点
- 兼容现有编码Agent Harness，无需修改底层实现，外层编排为「项目规划-开发-独立QA测试」的迭代闭环
- 跨轮双状态管理：分别维护**artifact状态**（代码、资源、配置等产物）和**证据状态**（已验证功能、未解决问题、历史测试报告），避免迭代过程信息丢失
- 增量迭代约束：每轮仅规划小范围、可独立验证的功能增量，仅约束各角色输出的结构化格式，不限制Agent内部推理、工具调用流程，平衡可控性与灵活性
- 分层测试机制：开发环节嵌入左移测试快速修复局部问题，QA环节做独立的黑白盒联合验证，覆盖功能、可用性、性能等多维度，测试结果作为下一轮规划的输入

### 关键结果
在GameCraft-Bench、FrontierSWE、ProgramBench三个基准测试集上，对比Codex+GPT-5.5、OpenCode+DeepSeek-V4-Pro、Pi+MiniMax-M3共3组基础配置，3轮迭代后平均相对提升52.25%，最高相对提升82.86%；FrontierSWE任务上10轮迭代后准确率从22%提升至72.67%；70+轮迭代可自主开发出完整可玩的FPS游戏，包含连贯剧情、核心战斗机制、音视频效果。

> 核心洞见：长周期Agent任务的核心竞争力不是单次执行能力，而是通过结构化迭代闭环、跨轮状态留存和独立验证机制实现的持续优化能力
