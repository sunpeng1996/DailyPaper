---
title: 'Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement
  and Recursive Self-Improvement'
title_zh: 通用智能体迭代（GAI）：迭代策略优化与递归自改进统一框架
authors:
- Hongyao Tang
- Yi Ma
- Pengyi Li
- Yifu Yuan
affiliations:
- Tianjin University
- Shanxi University
arxiv_id: '2609.13406'
url: https://arxiv.org/abs/2609.13406
pdf_url: https://arxiv.org/pdf/2609.13406
published: '2026-09-10'
collected: '2026-09-17'
category: Agent
direction: Agent 递归自改进（RSI）形式化建模
tags:
- Agent
- Recursive Self-Improvement
- GPI
- Formal Framework
- Self-Evolving Agent
one_liner: 提出双维度可调的通用智能体迭代框架，统一经典策略迭代与递归自改进两类学习范式
practical_value: '- 设计电商/推荐场景的自优化Agent时，优先落地Anchored类RSI方案，将业务核心指标固定为不可修改的外部评估基准，从机制上避免自改进过程的目标漂移

  - 可参考GAI的组件划分规则，将自改进Agent的底层模型权重、合规校验逻辑等不可修改部分剥离到Agent外部，降低自优化的失控风险

  - 评估业务Agent的进化等级时，可先落地固定外层迭代逻辑的GPI类方案（比如固定的A/B测试流程+策略迭代），验证效果后再逐步开放改进机制的修改权限'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有递归自改进（RSI）领域研究缺乏统一形式化框架，经典广义策略迭代（GPI）仅能覆盖改进机制、评价基准均外置的迭代优化场景，无法适配当前大量支持自修改、自评估的Agent类系统，不同RSI方案的边界、风险、适用性也无法横向对比，亟需统一框架打通两类范式的关联，为自进化Agent的设计提供理论指导。
### 方法关键点
- 定义通用智能体迭代（GAI）核心循环为「Agent评估-Agent改进」两步迭代，明确系统由策略π、动作评论家V、修改器m、修改评论家U、评估基准ρ五大组件构成，将Agent定义为系统中所有可修改组件的集合
- 提出两个核心调控旋钮：旋钮1为改进机制（修改器m）是否属于Agent可修改范围，以此区分经典GPI（m外置）与RSI（m内置）两类范式；旋钮2为评估基准ρ是否外置且不可修改，将RSI划分为Anchored（基准固定外置）、Goal Drift（基准可被Agent修改）、完全自指（无外部基准）三类极性
- 梳理出4类RSI的固有缺陷，每类缺陷对应一条经典GPI的假设违背，可直接用于自改进系统的风险评估
### 关键结果
论文无新增实验，引用已有RSIBench-Data基准测试结论：58.33%的固定外部评估的自改进场景首次尝试即可获得效果提升，但78.26%的持续搜索场景最终效果低于历史最优值，验证了自改进步骤的非单调性缺陷。
### 核心结论
所有面向业务落地的自改进Agent都应优先选择Anchored极性，将对齐业务目标的评估基准固定在Agent可修改范围之外，是避免自优化漂移、保证效果可控的核心前提。
