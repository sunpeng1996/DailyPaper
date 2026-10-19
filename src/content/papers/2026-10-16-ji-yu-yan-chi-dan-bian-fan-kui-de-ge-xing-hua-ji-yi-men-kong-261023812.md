---
title: Learning Personalized Memory Gating from Delayed One-Sided Feedback
title_zh: 基于延迟单边反馈的个性化记忆门控学习方法
authors:
- Kaixuan Ji
- Zixiang Chen
- Wenting Zhao
- Cheng Qian
- Heng Wang
- Weizhi Zhang
- Jielin Qiu
- Liangwei Yang
- Quanquan Gu
- Silvio Savarese
affiliations:
- Salesforce AI Research
- University of California, Los Angeles
- University of Illinois at Urbana-Champaign
- University of Illinois Chicago
arxiv_id: '2610.23812'
url: https://arxiv.org/abs/2610.23812
pdf_url: https://arxiv.org/pdf/2610.23812
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: Agent 个性化记忆门控优化
tags:
- MemoryGating
- ContextualBandit
- UCB
- DelayedFeedback
- LLMAgent
- Personalization
one_liner: 提出融合离线预训练与在线UCB适配的Warm-Start UCB，解决LLM Agent记忆门控的延迟单边反馈问题
practical_value: '- 记忆门控标注可复用检索+LLM校验的无人工标注流程，直接从用户交互的检索命中、响应生成环节自动生成事实效用标签，大幅降低标注成本

  - 电商/推荐场景的用户偏好记忆存储可直接复用Warm-Start UCB框架：先基于全量用户数据预训练通用门控基线，再通过在线单边延迟反馈做用户个性化适配，平衡冷启动与个性化效果

  - 资源受限场景（如用户端本地记忆、RAG有限token窗口）可借鉴这套门控逻辑，优先保留高复用概率的事实，相比通用LLM判断的门控策略，RHR最高可提升5pct以上

  - 延迟反馈的建模思路可迁移到电商转化延迟预估场景，比如用户点击后数天才下单的场景，用截断窗口方式处理未反馈样本，避免样本倾斜'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM Agent长时记忆系统受限于存储容量，现有全局通用的门控策略忽略用户个性化的事实复用规律，且记忆效用的反馈天然是单边的（只有存入的事实能观测到是否被后续检索使用，丢弃的无法获得反馈）、延迟的（事实存入后要过一段时间才会被用到），现有方法未适配这种反馈特性，效果天花板明显。

### 方法关键点
- 标注层：提出检索驱动的事实效用标注流水线，先对存入的事实判断后续是否被检索命中，再通过LLM校验是否实际用于响应生成，自动生成0/1效用标签，无需人工标注
- 问题建模：将个性化记忆门控抽象为带延迟单边反馈的contextual apple tasting问题，适配只有存入事实能获得反馈、反馈存在延迟的特性
- 算法层：提出Warm-Start UCB两阶段策略，第一阶段用其他用户的历史数据预训练通用门控参数做热启动，第二阶段在线交互时基于UCB算法结合延迟反馈做用户个性化适配，通过截断窗口处理未到期的延迟样本，理论上证明regret上界为$\tilde{O}(T\epsilon \wedge d\sqrt{T})$

### 关键实验
在PerMemBench-S/L两个长交互Agent记忆数据集上验证，对比Universal（全存）、LLM-based门控、冷启动UCB、固定预训练打分器等基线，Warm-Start UCB的检索命中保留率（RHR）相对全存基线最高提升5.37个百分点，在所有内存预算下均优于其他基线；预训练池越大效果越优，在线方法的F1分随交互时长增长持续提升。

最值得记住的一句话：个性化记忆门控的核心是平衡全局通用规律与用户个性化偏好，用检索反馈自动生成标注、结合延迟bandit在线适配的方案，效果远好于纯LLM启发式判断的门控策略
