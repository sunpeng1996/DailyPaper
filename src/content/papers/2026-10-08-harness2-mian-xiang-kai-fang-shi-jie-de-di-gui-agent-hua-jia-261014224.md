---
title: 'Harness^2: Recursive Agent Harnessing for an Open World'
title_zh: Harness²：面向开放世界的递归Agent Harness优化框架
authors:
- Ruiyao Xu
- Yanfei Chen
- Zhongying CuiZhu
- Bhavana Dalvi Mishra
- Yifei Ming
- Han Yu
- Rujun Han
- Chen-Yu Lee
- Tomas Pfister
affiliations:
- Northwestern University
- Google Cloud AI Research
arxiv_id: '2610.14224'
url: https://arxiv.org/abs/2610.14224
pdf_url: https://arxiv.org/pdf/2610.14224
published: '2026-10-08'
collected: '2026-10-14'
category: Agent
direction: Agent 自适应优化 · 递归自进化
tags:
- Agent
- Recursive Self-Improvement
- Harness Optimization
- Open World
- Test-time Adaptation
one_liner: 提出双层级递归免标注Agent Harness优化框架，跨任务累积经验持续提升性能
practical_value: '- 电商/广告Agent场景（智能客服、选品、工单处理等）可直接复用Propose-Probe-Compose流程，无需标注即可在线优化prompt、工具调用逻辑等harness组件，无需修改模型权重

  - 双递归分层设计可直接迁移：任务级递归优化当前业务场景的执行harness，优化级递归将跨场景（促销、售后等）的优化经验沉淀到组件库，实现经验复用

  - 可复用「弱模型+优化harness」思路：业务侧无需盲目升级大模型，针对中小模型迭代harness即可追平甚至超过更大原生模型的效果，大幅降低推理成本

  - 无ground truth场景下可复用行为对比评估方法：相同任务相同配置下对比不同harness的执行轨迹差异，无需等业务指标回流即可判断harness迭代有效性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent效果同时依赖基础模型与执行harness（含prompt、工具、编排逻辑等组件），现有递归自优化方案要么依赖标注引导迭代，要么优化经验无法跨任务迁移，无法适配开放世界下新任务无标注、分布动态变化的场景。

### 方法关键点
- 双层级递归架构：分为任务级、优化级两层递归，任务级迭代当前任务的执行harness，优化级沉淀跨任务的改进规则与可复用组件到经验库，指导后续任务优化
- 无标注对比式优化流程：先生成通用+领域两类harness修改候选，在相同模型、环境配置下执行候选生成行为对比，再选择性合并验证有效的修改，无需ground truth标注
- 支持并行/序列两种任务级递归模式，可通过k值控制探索预算，优化效率灵活可调
- 经验库存储可复用harness组件与对应的生效场景、效果证据，后续任务可直接适配无需从零优化

### 关键结果
在WorkBuddy-Bench（办公任务）、JobBench（专业任务）、LAB（法律任务）三个基准，覆盖GLM-5、Gemini 3.5 Flash两个模型+OpenCode、Codex两个初始harness的4种配置下：单步优化比基准harness最高提11.5分（WorkBuddy-Bench）、4.5分（JobBench）、11.8个百分点（LAB通过率）；并行递归k=5时可额外带来2.9~6.7个百分点的增益，优化后的弱模型效果可超过未优化的强模型。

**最值得记住的一句话**：Agent性能优化的核心优先级不一定是更换更大的模型，持续迭代harness即可在不改动模型权重的前提下获得显著、可累积的性能收益。
