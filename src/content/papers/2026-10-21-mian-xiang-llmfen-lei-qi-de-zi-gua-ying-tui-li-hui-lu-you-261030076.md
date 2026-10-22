---
title: Circuits of LLM Classifiers
title_zh: 面向LLM分类器的自适应推理回路优化框架
authors:
- Hadi Khalaf
- Sajani Vithana
- Kunal Talreja
- Haewon Jeong
- Viveck R. Cadambe
- Flavio Calmon
affiliations:
- Harvard University
- Georgia Institute of Technology
- University of California Santa Barbara
- Flatiron Institute
- Kempner Institute
arxiv_id: '2610.30076'
url: https://arxiv.org/abs/2610.30076
pdf_url: https://arxiv.org/pdf/2610.30076
published: '2026-10-21'
collected: '2026-10-22'
category: LLM
direction: LLM推理优化 · 多模型成本精度权衡
tags:
- LLM-classifier
- cost-accuracy-tradeoff
- dynamic-programming
- sequential-decision
- model-orchestration
one_liner: 提出动态规划驱动的多LLM分类器组合框架，全局最优优化成本-精度权衡
practical_value: '- 电商/推荐场景的LLM-as-judge任务（评论审核、内容合规、Agent工具调用校验）可直接复用LMCircuit框架，仅需少量标注数据训练概率模型+动态规划，比现有级联、路由方案在同等成本下精度更高，同等精度下成本低30%+

  - 模型池选型可复用论文贪心策略：优先选择单位成本条件信息增益最高的模型，无需盲目堆叠大模型，一般2-3个互补模型即可逼近全池最优效果，大幅降低推理成本

  - 低预算场景可直接复用零成本预测方案：基于prompt embedding先做初筛，高置信样本直接输出结果，低置信样本再调用LLM，可比调用最便宜单模型的成本再降30%以上'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM作为分类器/评审器（内容审核、标注、Agent正确性校验等）部署简单，但单模型输出不稳定、成本与精度难以平衡，现有多模型组合方案（路由、级联、多数投票）均为静态策略，无法根据样本难度自适应调整调用逻辑，也无全局最优性理论保证。

### 方法关键点
- 提出分类回路（Circuit）通用框架，将所有多LLM分类器组合策略统一为贝叶斯序贯决策问题，以「错误率+λ*调用成本」为优化目标，最优解可通过动态规划精确求解
- 落地分为两步：先用带标注训练样本拟合prompt embedding、标签、各模型输出的联合概率模型；推理时针对每个样本，通过动态规划决策下一个调用的模型、以及何时停止输出结果
- 理论证明最优回路性能上下界：零调用时的贝叶斯误差为下限，全模型调用的贝叶斯误差为上限，同时给出模型池扩容的信息增益评估标准，以及误差随成本的缩放定律

### 关键实验
在7个任务（安全审核、Agent工具调用校验、医疗评估、人类偏好分类等）上测试，对比RouteLLM、FrugalGPT、级联路由、多数投票等10+基线，LMCircuit在所有预算点上均Pareto占优，训练时间仅1-3分钟，比基线快10-100倍；高置信样本上零调用预测可在比单模型低38%-86%成本下达到相当精度，低置信样本上精度提升5%-44%。

### 核心结论
多LLM组合的收益不来自单个模型的绝对精度，而来自不同模型提供的互补信息，自适应调用策略的收益远高于静态的级联、路由或投票方案。
