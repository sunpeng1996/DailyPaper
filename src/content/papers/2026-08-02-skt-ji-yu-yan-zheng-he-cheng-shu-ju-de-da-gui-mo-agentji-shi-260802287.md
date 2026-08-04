---
title: 'SKT: Skill-Use Training at Scale via Verified Synthetic Data Generation'
title_zh: SKT：基于验证合成数据的大规模Agent技能使用训练框架
authors:
- Zelin Tan
- Yiqun Zhang
- Hao Li
- Zhiyao Cui
- Hejia Geng
- Shao Zhang
- Hangfan Zhang
- Yang Chen
- Xiaosong Wang
- Lilong Wang
affiliations:
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2608.02287'
url: https://arxiv.org/abs/2608.02287
pdf_url: https://arxiv.org/pdf/2608.02287
published: '2026-08-02'
collected: '2026-08-04'
category: Agent
direction: Agent技能调用能力优化
tags:
- Agent Skill
- Synthetic Data
- SFT
- Agent Evaluation
- Trajectory Synthesis
one_liner: 提出可验证的合成数据流水线，生成高质量技能使用训练数据，显著提升LLM Agent的技能调用与协作能力
practical_value: '- 电商/推荐业务Agent（如智能导购、运营决策Agent）的技能训练可直接复用SKT的验证流程：通过「有无技能对照实验」保证训练任务对指定技能的强依赖，避免无效数据导致的训练漂移

  - 做多Agent框架兼容的业务Agent时，可采用混合harness轨迹训练方案，无需为每个运行环境维护独立模型，单模型性能与专属模型差距小于2.71个点，大幅降低运维成本

  - 技能训练数据质量优先级远高于数量，轨迹层面必须增加校验环节，确保每段训练轨迹都真实、正确使用了所有指定技能，未校验的合成数据反而会降低模型的技能调用能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent Skill生态快速扩张，2025年10月以来公开技能已超60万个，但现有LLM普遍不具备有效识别、调用、协调多技能的能力，现有研究多聚焦技能检索、内化，缺乏高质量的技能使用训练数据，成为Agent落地的核心瓶颈。
### 方法关键点
- 三级流水线架构：先从公开技能库筛选可执行、可组合的技能，支持1~3种技能的单/多任务配置
- 任务合成带反馈修复：模板生成可执行任务包，经规则校验（完整性、可执行性）、LLM语义校验、技能依赖校验（有无技能的对照实验验证任务对技能的强依赖）、难度控制，失败任务返回修复，仅保留有效任务
- 轨迹双重校验：用强基座生成执行轨迹，经规则校验（执行成功、轨迹合法）+ LLM校验（所有指定技能均被实质性使用），仅保留合格轨迹用于SFT，训练时仅对Agent生成的推理、工具调用、回复token计算损失
### 关键实验
基于2000个公开技能生成4000个任务、27164条验证轨迹，训练Qwen3.5-9B、Gemma4 E4B-IT，在SkillsBench、SkillEval等4个基准上全部取得提升，绝对增益3.2~18.91个点；跨harness迁移可保留49%~58%的性能增益，混合harness训练的单模型与单harness专属模型的性能差距不超过2.71个点，性能随训练技能覆盖规模单调提升。
### 核心结论
高质量带全链路验证的技能使用合成数据，是低成本、可扩展提升Agent技能调用能力的最优路径，未校验的raw合成数据反而会损害模型性能。
