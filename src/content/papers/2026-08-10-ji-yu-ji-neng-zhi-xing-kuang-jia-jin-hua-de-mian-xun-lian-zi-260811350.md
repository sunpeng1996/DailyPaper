---
title: Self-Evolving Embodied Agents via Skill-Harness Evolution
title_zh: 基于技能-执行框架进化的免训练自进化具身Agent系统SHAPER
authors:
- Peidong Wang
- Zhiming Ma
- Ying Chang
- Xufang Luo
- Xiaocui Yang
- Shi Feng
- Yuqing Yang
- Dongsheng Li
affiliations:
- Northeastern University
- Microsoft Research
arxiv_id: '2608.11350'
url: https://arxiv.org/abs/2608.11350
pdf_url: https://arxiv.org/pdf/2608.11350
published: '2026-08-10'
collected: '2026-08-13'
category: Agent
direction: 具身Agent · 免训练自进化优化
tags:
- Embodied Agent
- Train-Free Adaptation
- Skill Evolution
- Harness Optimization
- Self-Evolving
one_liner: 冻结模型参数前提下通过进化文本技能与上下文代码框架提升具身Agent性能
practical_value: '- 对于无法微调大模型的电商/推荐业务场景，可复用「文本技能+上下文代码框架」的非参数优化思路，无需修改模型权重就能适配特定业务规则，提升导购/客服Agent、召回排序模块的效果

  - 可借鉴分层诊断+文本梯度的优化流程：用大模型本身作为judger分析错误轨迹，输出可落地的技能/框架修改意见，降低人工运营prompt、上下文规则的成本

  - 二阶段进化策略可直接复用：先优化prompt级的任务执行规范（对应电商客服话术/导购规则、推荐的多样性约束），再优化上下文拼接逻辑（对应用户行为历史压缩/关键信息提取规则），分阶段迭代降低试错成本

  - 进化后的技能和框架是一次性投入可复用的，比test-time scaling（多轮采样投票）成本低，适合高并发的电商/推荐业务场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
具身Agent性能不仅由模型权重决定，还受外围技能、上下文构造、执行封装等非参数组件影响；传统SFT、RL适配方案需要大量标注数据、算力支持，且要求模型权重可访问，现有免训练方案又高度依赖可编程API，在固定接口场景下无法落地，亟需低成本、通用的免调参适配方案。

### 方法关键点
- 将Agent拆解为**冻结VLM规划器、冻结执行器、可优化文本技能（任务分解、故障恢复等规则）、可优化上下文代码框架（轨迹历史选择与格式化逻辑）**四个组件，仅优化非参数部分实现适配
- 分层生成文本梯度：先逐轮对比动作前后观测生成局部批评，再聚合轨迹元数据、批评、最终结果生成可执行的优化反馈，避免直接处理长多模态轨迹
- 二阶段进化策略：复用同一冻结大模型作为优化器，先固定框架优化文本技能，再固定最优技能优化上下文框架；生成的代码框架需经过沙箱校验，通过beam search保留Top-K候选

### 关键结果
- 在VLABench上仅用15条训练轨迹进化，SHAPER成功率达34.5%，较种子Agent提升6.25pp，较同数据SFT提升10.5pp
- 在ESI-Bench上仅用10条训练轨迹进化，SHAPER微准确率达49.8%，较种子Agent提升17.3pp，宏观准确率42.9%超过GPT-5被动单视图基准的40.3%
- 进化成本极低，单轮进化API成本仅约2~3美元，进化后的技能与框架可直接复用，无test-time scaling的额外推理成本

> 最值得记住的结论：大模型权重不可修改或微调成本过高时，优先优化外围非参数化的技能与上下文框架，是提升Agent性能的高性价比路径
