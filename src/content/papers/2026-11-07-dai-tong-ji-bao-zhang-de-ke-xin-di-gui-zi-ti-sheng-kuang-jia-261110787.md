---
title: Trustworthy Recursive Self-Improvement with Statistical Guarantees
title_zh: 带统计保障的可信递归自提升框架
authors:
- Zihe Gao
- Zhengling Qi
- Yifan Cui
affiliations:
- Zhejiang University
- George Washington University
arxiv_id: '2611.10787'
url: https://arxiv.org/abs/2611.10787
pdf_url: https://arxiv.org/pdf/2611.10787
published: '2026-11-07'
collected: '2026-11-10'
category: Agent
direction: Agent 递归自提升安全控制
tags:
- Recursive Self-Improvement
- Statistical Testing
- LLM Agent
- FDR Control
- False Evolution Rate
one_liner: 提出TRUST统计检验框架，控制Agent递归自提升的错误更新率，兼顾安全与性能增益
practical_value: '- 做Agent/生成式推荐的迭代（如prompt、工作流、记忆模块更新）时，可替换纯greedy更新规则，借鉴TRUST的FER控制思路，将错误更新率控制在预设阈值内，避免线上性能回退，尤其适合对稳定性要求高的电商/广告场景

  - 迭代中验证样本不足需要复用时，可引入重叠校正技巧，给复用样本加权重校正偏置，降低过拟合风险，节省验证资源

  - 不用给所有候选更新分配相同验证资源，可先让LLM基于历史上下文评估候选更新的潜在收益，给高潜力候选分配更高的检验阈值，兼顾迭代效率与安全性

  - 框架参数可解释性强：可根据业务阶段调整FER预算、损失容忍度、重叠校正强度，大促期调严参数保稳定，常规迭代期调松参数拿收益'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前Agent递归自提升（RSI）无需重训LLM，仅通过优化prompt、工作流、记忆模块即可提升性能，但更新决策机制存在明显缺陷：greedy门限仅依据验证集分数接受更新，易受采样噪声、验证集复用过拟合影响，误接受劣化更新导致性能持续下跌；现有统计门限为控制单轮错误过于保守，大量拒绝有效更新，难以在有限验证资源下平衡性能增益与迭代安全。

### 方法关键点
- 定义False Evolution Rate（FER）为核心安全指标，指所有接受的更新中不可接受劣化更新的占比，将多轮更新决策转化为在线多重假设检验问题，从理论上证明全局FER不超过预设的误差预算q
- 引入LLM引导的误差预算分配：LLM基于历史上下文、候选更新内容预判其潜在价值，给高潜力候选分配更高的检验阈值，提升优质更新的通过率
- 加入非劣效检验模块，允许用户设置可容忍的小幅性能损失，提升统计检验功效；新增重叠校正机制，抵消多轮复用验证样本带来的乐观偏置
- 基于e-value构造序贯检验统计量，无需跑完所有验证样本，证据足够时可提前终止验证，节省算力成本

### 关键实验
在HotpotQA、DROP、APPS三个基准数据集上，使用DeepSeek-V4-Flash、Qwen-3.8-Flash两个模型测试，对比greedy、PACE、SGM等主流基线：平均FER0（所有非增益更新的接受率）从greedy的45.59%降至2.78%，平均最大性能回撤从4.963pp降至0.047pp，最终平均性能增益达24.84pp，优于所有统计类基线。

### 核心结论
Agent递归自提升的核心瓶颈不是生成候选更新的能力，而是如何在不引入不可接受性能退化的前提下，筛选出真正有效的更新。
