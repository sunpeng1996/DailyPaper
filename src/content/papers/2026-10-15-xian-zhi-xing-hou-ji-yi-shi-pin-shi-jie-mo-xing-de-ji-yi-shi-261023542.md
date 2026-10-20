---
title: 'Execution Before Memory: Diagnosing Memory Failures in Video World Models'
title_zh: 先执行后记忆：视频世界模型的记忆失败问题诊断
authors:
- Weiyang Jin
- Jiwen Yu
- Sihan Xu
- Yuwei Niu
- Xihui Liu
affiliations:
- University of Hong Kong
- University of Michigan - Ann Arbor
- Peking University
arxiv_id: '2610.23542'
url: https://arxiv.org/abs/2610.23542
pdf_url: https://arxiv.org/pdf/2610.23542
published: '2026-10-15'
collected: '2026-10-20'
category: Agent
direction: Agent · 视频世界模型评估与测试时优化
tags:
- Video World Model
- Evaluation Framework
- Test-Time Optimization
- Prompt Revision
- Agent
one_liner: 提出MIST分阶段评估框架与M3-Agent，无需训练提升视频世界模型记忆测试表现
practical_value: '- 可复用测试时prompt优化思路：无需重新训练基座模型，通过诊断生成结果的失败点，仅改写指令的执行动作部分、保留核心约束，即可大幅提升生成内容符合度，可直接迁移到AI商品短视频生成、营销文案生成等电商场景

  - 评估拆解方法可复用：将生成任务拆分为场景搭建、动作执行、结果匹配多个独立可观测门限，替代单一总得分，可快速定位生成效果瓶颈，适用于所有生成式内容的效果归因

  - 多候选择优策略可复用：生成多候选结果时保留原始基准候选，避免改写损坏正确结果，用任务核心目标作为统一择优标准，可迁移到推荐系统多候选排序、生成内容最优选择场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有视频世界模型的记忆测试仅输出单一总得分，低分通常被误判为模型遗忘，但实际大量案例是指令要求的动作从未被执行，记忆阶段根本未被有效测试，无法定位真实瓶颈。
### 方法关键点
- MIST评估范式：将视频生成任务拆分为场景搭建、隐藏变化、结果揭示三个阶段，分别检测场景有效性、隐藏变化无泄露、执行动作触发、结果匹配四个独立门限，分开统计得分，彻底区分执行失败和记忆失败
- M3-Agent测试时优化流程：无需修改或训练基座模型，仅通过VLM诊断生成结果的失败模式，针对性改写指令的动作描述部分，保留核心目标、对象、时序约束不变，生成多个候选后基于任务目标选最优
### 关键结果数字
在自研MIST基准上，M3-Agent将reveal得分从基线0.147提升至0.492，提升超2倍；在公开WRBench基准上得分T从0.452升至0.570，涨幅26.1%；在公开MBench-T基准上得分U从0.292升至0.446，涨幅52.7%。
### 最值得记住的结论
视频世界模型的记忆测试低分往往不是模型记忆能力差，而是根本没有执行要求的动作，优先优化执行环节的性价比远高于新增记忆模块。
