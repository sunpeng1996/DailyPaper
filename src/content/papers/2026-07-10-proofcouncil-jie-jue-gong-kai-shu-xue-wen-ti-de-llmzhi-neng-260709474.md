---
title: 'ProofCouncil: An LLM Agent for Solving Open Mathematical Problems'
title_zh: 《ProofCouncil：解决公开数学问题的LLM智能体》
authors:
- Johannes Schmitt
- Tim Gehrunger
- Jasper Dekoninck
- Gergely Bérczi
- Uri Kreitner
- Liam Price
- David Holmes
affiliations:
- ETH Zurich
- Aarhus University
- Independent Researcher
- Leiden University
arxiv_id: '2607.09474'
url: https://arxiv.org/abs/2607.09474
pdf_url: https://arxiv.org/pdf/2607.09474
published: '2026-07-10'
collected: '2026-07-13'
category: Agent
direction: LLM Agent · 复杂任务推理求解
tags:
- LLM Agent
- Author-Critic Architecture
- Reasoning
- Open Source
- Mathematical Reasoning
one_liner: 提出采用作者-评论家架构的数学求解Agent，在FirstProof竞赛取得最优成绩并开源配套Agent构建库
practical_value: '- 作者-评论家架构可复用在推荐/广告文案生成、内容审核链路，生成模块输出候选，评论家模块做质量校验与瑕疵修正，降低badcase率

  - 多轮核验的Agent工作流设计思路，可迁移到大促商品选品、广告投放策略自动迭代等需要多轮验证的业务场景

  - 开源的Agent构建库可直接二次开发，适配业务侧规则推理、效果核验类自动化任务'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有LLM在公开数学问题求解领域已取得一定进展，但缺乏适配真实科研实践的Agent工作流，整体性能仍有较大提升空间。
### 方法关键点
设计ProofCouncil数学求解Agent，采用作者-评论家双模块架构：作者模块负责生成解题思路与完整证明过程，评论家模块负责验证推导逻辑正确性、指出漏洞并给出修正方向，全程可自主运行无需人工介入，同时开源配套通用Agent构建库。
### 关键结果数字
在FirstProof挑战赛10道无公开解的真实数学题中，6道题的解法经评审仅需少量修正即可通过，成绩位列所有参赛队伍第一；在30道来自科研人员的公开数学题测试集上，21份获得人类反馈的解法中，5份完全正确、2份待验证即具备潜力、8份包含有效部分进展。
