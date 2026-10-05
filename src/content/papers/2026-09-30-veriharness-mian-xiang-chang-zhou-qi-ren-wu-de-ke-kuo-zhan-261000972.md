---
title: 'VeriHarness: Scaling Agentic Verification for Long-Horizon Tasks'
title_zh: VeriHarness：面向长周期任务的可扩展智能体验证框架
authors:
- Caiqi Zhang
- Rujun Han
- Zifeng Wang
- Zoey CuiZhu
- Nigel Collier
- Tomas Pfister
- Chen-Yu Lee
affiliations:
- University of Cambridge
- Google Cloud AI Research
arxiv_id: '2610.00972'
url: https://arxiv.org/abs/2610.00972
pdf_url: https://arxiv.org/pdf/2610.00972
published: '2026-09-30'
collected: '2026-10-05'
category: Agent
direction: 长周期智能体 · 验证框架优化
tags:
- LLM-Agent
- Verification
- Long-Horizon-Task
- Self-Evolution
- Test-Time-Scaling
one_liner: 基于同基座LLM的无训练验证框架，通过环境证据校验分歧、挑战共识提升长周期智能体输出质量
practical_value: '- 可直接复用「分歧校验+共识挑战」的双路验证结构，优化电商导购Agent、活动方案生成Agent的输出质量，无需更换更强基座，仅用现有模型即可降低幻觉错误率

  - 验证技能自进化机制可直接迁移到业务场景：将商品参数校验、活动权益计算等业务场景的失败反馈沉淀为可复用校验规则，无需微调模型即可持续提升验证准确率

  - 多rollout结果筛选不要仅依赖多数投票、best-of-N这类纯模型判断方案，结合业务环境数据（商品库、规则库、用户历史数据等）做证据校验，能大幅提升输出正确性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长周期LLM Agent输出错误率高，现有验证方法要么依赖更强裁判模型，要么仅基于多rollout投票、LLM-as-judge判断，未结合环境真实证据；且实验发现34%的共识结果存在错误，74%的分歧结果包含正确选项，需要在无参考答案、不升级基座的场景下提升验证能力。
### 方法关键点
- 采用与生成器完全相同的基座LLM作为验证器，无需训练，为即插即用的harness架构，包含工作空间、证据工具、验证协议、可复用技能库4个核心组件
- 双路验证逻辑：分歧解析器针对多rollout结果存在差异的claim，调用环境工具获取证据筛选错误选项；共识挑战器针对所有rollout一致的claim，主动假设错误场景，校验正确性、排查遗漏需求
- 裁决模块整合双路验证结果，选择最优基础rollout，基于证据生成修订方案输出最终结果；支持从失败反馈中自动迭代验证技能库，无需调整模型权重
### 关键结果
在5个长周期工作空间基准测试，用Gemini 3.5 Flash、Claude Opus 4.8分别作为生成和验证基座：VeriHarness（带证据修订）比单rollout平均得分分别高6.2、6.4个点；验证技能自进化后，在APEX-Agents基准上比人工编写的技能库再提升6.8个点，所有场景下均超过多数投票、LLM-as-Verifier等主流基线。
### 核心结论
验证能力不需要等待更强的基座模型，可以围绕现有模型，基于其生成的多rollout结构、环境中的证据、积累的失败经验搭建实现。
