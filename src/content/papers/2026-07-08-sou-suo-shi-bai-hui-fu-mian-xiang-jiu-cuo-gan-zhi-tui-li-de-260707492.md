---
title: 'Search, Fail, Recover: A Training Framework for Correction-Aware Reasoning'
title_zh: 搜索-失败-恢复：面向纠错感知推理的Pyligent训练框架
authors:
- Dmitry Beresnev
- Vladimir Makharev
- Roman Khalikov
- Ivan Oseledets
- Petr Anokhin
affiliations:
- Innopolis University
- Lomonosov Moscow State University
- AXXX (Moscow)
arxiv_id: '2607.07492'
url: https://arxiv.org/abs/2607.07492
pdf_url: https://arxiv.org/pdf/2607.07492
published: '2026-07-08'
collected: '2026-07-09'
category: Reasoning
direction: 纠错感知推理 · 显式回溯训练框架
tags:
- Reasoning
- Backtracking
- SFT
- LLM Training
- Search Planning
one_liner: 提出融合失败分支监督的Pyligent框架，让小参数LLM学会显式回溯纠错，大幅提升推理任务解决率
practical_value: '- 做电商导购Agent、营销活动规划、用户问题排查等需要路径推理的场景时，可复用`<backtrack>`动作设计，结合业务规则validator标注失败分支做SFT，无需仅依赖正确路径样本，大幅提升模型容错能力

  - 回溯后注入`<trace>`记录失败原因的trick可直接迁移到query改写、推荐路径纠错等场景，保留错误上下文避免重复踩坑，提升后续生成准确率

  - 反向课程学习的探索策略可复用在小模型推理训练中，先从近终点的短路径训练，再逐步延长推理路径，有效降低训练收敛难度'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有主流推理训练范式（如CoT）仅使用打磨后的成功路径作为监督信号，缺失失败尝试与错误恢复过程的标注，模型遇到延迟反馈类错误（如局部合规但全局不可行的决策）时无法有效回溯到正确决策点，导致搜索、规划类推理任务解决率极低，且容易在错误分支上浪费算力。

### 方法关键点
- 提出Pyligent训练推理框架，将推理建模为对部分解链的验证搜索，动作空间新增显式`<backtrack>`回溯动作，搭配`<node>`（新增推理步）、`<done>`（输出最终结果）动作，通过节点ID明确标记分支结构
- 训练分为三阶段：先SFT-A在黄金解链上训练基础动作格式；再通过任务专属validator引导探索，记录所有成功分支与失败叶子节点；最后SFT-B将搜索树转化为三类监督样本（继续、完成、回溯），可选注入`<trace>`记录失败分支摘要，避免模型重复犯同类错误
- 采用反向课程学习策略，探索先从黄金链近终点的短路径开始，逐步向根节点推进，降低长推理路径的训练难度

### 关键实验
在隐藏有向图、4×4数独（含推理trace版）、Blocksworld规划任务上验证，对比仅用黄金路径的SFT基线：隐藏有向图解决率提升72.7pp，混合难度/专家难度数独分别提升17pp/18pp，带推理trace的数独分别提升27pp/14pp，Blocksworld规划任务提升13pp。

### 核心结论
可靠的回溯能力无法仅从黄金解样本中自动涌现，需要在动作空间显式定义、探索阶段生成失败样本、事后验证标注后作为独立训练目标。
