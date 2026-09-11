---
title: 'COBRA-Skills: Contextual Bandit-Guided Evolution for Agent Skill Optimization'
title_zh: COBRA-Skills：上下文老虎机引导进化的Agent技能优化框架
authors:
- Pingchen Lu
- Xiangyi Wang
- Xiang Li
- Jie Mao
- Zikun Qu
- Junfeng Luo
- Yao Shu
- Bryan Kian Hsiang Low
- Zhongxiang Dai
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Tianjin University
- The Hong Kong University of Science and Technology (Guangzhou)
- National University of Singapore
arxiv_id: '2609.11682'
url: https://arxiv.org/abs/2609.11682
pdf_url: https://arxiv.org/pdf/2609.11682
published: '2026-09-10'
collected: '2026-09-11'
category: Agent
direction: Agent技能优化 · 上下文老虎机
tags:
- LLM Agent
- Contextual Bandit
- Skill Optimization
- Evolutionary Algorithm
- Sample Efficiency
one_liner: 结合上下文老虎机与证据驱动进化，低成本优化Agent可复用技能，较基准降本55%以上
practical_value: '- 电商导购/客服Agent技能优化场景可直接复用该框架，将技能语义embedding作为Contextual Bandit的臂特征，用MLP+LinearUCB做优先级打分，优先评测高价值候选，大幅降低LLM调用成本

  - 推荐系统的prompt优化、商品文案迭代场景可复用三个进化算子（再生/滚动突变/交叉），基于历史落地反馈做证据迭代，避免无依据的修改，提升迭代效率

  - 中小业务场景可采用自训练模式（用目标Agent本身作为教学模型优化技能），无需依赖强外部大模型，成本降低近半且效果损失极小'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM Agent的可复用技能优化依赖大量执行评测和任务数据，反复调用LLM分析轨迹、修改技能成本极高，有限预算下难以高效筛选高价值技能，亟需兼顾效果和成本的技能优化范式。

### 方法关键点
- 将技能优化建模为动态候选空间的预算约束序列优化问题，每个技能对应Contextual Bandit的一个臂，技能语义embedding作为臂特征
- 优先级打分融合轻量两层MLP预测的技能reward + LinearUCB不确定性bonus，优先评测高潜力或未充分探索的技能，避免无效成本
- 定期执行证据驱动的技能进化：用再生算子引入新技能方向、滚动突变算子基于当前技能执行轨迹局部优化、交叉算子融合强弱技能的正负证据，淘汰低优先级技能更新候选池

### 关键实验
在6个异质Agent benchmark（开放域QA、表格处理、文档VQA、数学推理、社交推理、具身决策）、3款目标LLM上验证，对比SkillOpt等4个基准：
1. 平均性能较无技能基线分别提升13.1、26.9、22.5个百分点，全场景性能最优
2. 总优化成本较SkillOpt降低55%~58%，每提升1点性能的成本降低60%~69%，仅需每个基准50个优化样本
3. 跨Agent框架、自训练场景下效果稳定，优化后的技能可跨模型迁移，34/36跨模场景较基线有明显提升

**最值得记住的一句话**：Contextual Bandit优先级调度+证据驱动小步进化，是有限预算下优化Agent技能、prompt等文本候选的高性价比范式。
