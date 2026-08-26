---
title: 'Meta^n: Recursive Self-Improvement through Emergent Depth'
title_zh: 《Meta^n：通过涌现深度实现递归自改进的Agent框架》
authors:
- Zae Myung Kim
- Young-Jun Lee
- Seungyeon Jwa
- Dongyeop Kang
affiliations:
- University of Minnesota
- Seoul National University
arxiv_id: '2608.24735'
url: https://arxiv.org/abs/2608.24735
pdf_url: https://arxiv.org/pdf/2608.24735
published: '2026-08-24'
collected: '2026-08-26'
category: Agent
direction: 自改进Agent · 元递归架构设计
tags:
- Self-Improving Agent
- Meta-Recursion
- LLM Agent
- Evolutionary Archive
- Emergent Depth
one_liner: 固定通用元操作递归叠加输入生成层级Agent栈，稳定突破现有自改进Agent的元深度上限
practical_value: '- 可直接复用「固定元操作+递归输入」的稳定自改进架构，替代现有推荐/广告系统的策略迭代流程：固定一个分析全链路badcase、输出优化规则/通用工具的元prompt，递归叠加前序优化结果，自动迭代召回/排序/冷启动策略，完全避免修改迭代逻辑本身导致的系统稳定性问题

  - 进化存档多链搜索机制可迁移至多任务Agent场景：比如营销文案生成、商品标题优化、query改写等多任务场景，维护多个候选策略链存档，按单任务效果选最优策略，论文显示相比单链贪婪迭代可提升6%~7%的综合效果

  - 跨任务badcase提炼通用工具的思路可落地：做电商全场景的query理解、商品信息归一化等任务时，自动从多个任务的错误轨迹里抽取通用的实体识别、规格归一化工具函数，跨任务复用，减少重复开发量'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有自改进LLM Agent要么仅优化输出答案、不改进底层生成过程，要么修改自身代码时必须冻结部分驱动逻辑保证系统稳定，实际可实现的元深度最高仅约2.5，性能存在明显天花板，且递归修改改进逻辑本身极易引发系统崩溃。

### 方法关键点
- 固定通用元操作Ω，不对Ω本身做任何修改，递归将Ω的输出（前序层的运行轨迹+生成的代码栈）作为下一次Ω的输入，逐层生成包含策略前置处理逻辑+可调用工具库的元层，栈深度由收敛条件自动决定而非提前固定
- 运行时每层的前置处理逻辑会向下传递策略上下文，深层策略框架约束浅层执行逻辑，工具库逐层累加，深层同名函数覆盖浅层实现
- 配套进化存档搜索机制，维护多个候选层链种群，按得分+探索权重采样扩展，支持跨链的最优策略复用，还可开启零回归巩固模式，单任务优化时继承其余任务的最优结果

### 关键结果
在8类基准测试（组合优化、文本分类、终端Agent、数学推理等）上对比Gödel Agent、OpenEvolve两个SOTA自改进Agent，两个 backbone 下Meta^n在所有基准上均领先：ARC-AGI-2基准上仅Meta^n得分>0（达0.331），CO-Bench上比OpenEvolve最高领先0.168，递归本身带来的性能增益达0.131，其中72%的增益来自层间上下文传递，15%来自可调用工具库注入。

**最值得记住的一句话**：自改进的核心收益不一定来自修改改进逻辑本身，给固定的改进器输入更丰富的前序执行上下文和代码栈，就能实现稳定的多层级元改进，突破现有元深度上限。
