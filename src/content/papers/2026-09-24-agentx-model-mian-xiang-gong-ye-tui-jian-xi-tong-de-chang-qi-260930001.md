---
title: 'Advancing Model Research in AgentX: Long-Horizon Autonomy for Industrial Recommender
  Systems'
title_zh: AgentX-Model：面向工业推荐系统的长周期自主模型研究框架
authors:
- Shuang Yang
- Zijie Zhuang
- Changxin Lao
- Pengbo Xu
- Hanwen Xu
- Yusheng Huang
- Han Gao
- Guanchen Wang
- Tianbao Ma
- Linxun Chen
affiliations:
- Kuaishou
arxiv_id: '2609.30001'
url: https://arxiv.org/abs/2609.30001
pdf_url: https://arxiv.org/pdf/2609.30001
published: '2026-09-24'
collected: '2026-09-27'
category: Agent
direction: Agent 工业推荐模型迭代优化
tags:
- Dual-Agent
- Industrial RecSys
- Autonomous Research
- Long-Horizon Iteration
- Knowledge Transfer
one_liner: 提出双Agent架构实现工业推荐模型长周期自主迭代，提升实验效率与业务增益
practical_value: '- 可直接复用双Agent分工架构：将实验规划（对齐论文/业务、生成提案）和落地执行（编码/调参/实验）拆分给两个独立Agent，通过标准化提案格式交互，大幅降低推荐模型迭代的人工干预成本

  - 四类研究动作的分类框架可直接套用到团队的推荐迭代流程：Reproduce/Follow-up/Composition/Diagnose边界清晰，能帮助梳理实验优先级、减少无效试错，即使不接入Agent也能提升人工研发效率

  - 工程落地经验可直接复用：每轮实验必须留存最优版本代码而非最终版本；跨业务场景的已有实验经验迁移，比直接复现顶会论文方法的提效概率高30%以上，资源有限的团队可优先落地跨场景迁移

  - 调度策略选择结论：当Agent已具备自主筛选实验候选能力时，固定动作类型轮换+Agent选候选的组合，性价比远高于复杂的自适应调度策略，无需过度投入调度算法优化'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐模型迭代高度依赖人工完成实验规划、代码开发、效果分析全流程，效率低且历史经验难以沉淀；现有Agent辅助研发方案仅支持单轮实验，无法基于历史结果自主推进长周期迭代，也难以对齐校准、算力约束等业务要求。
### 方法关键点
- 双Agent分工架构：Research Agent对接外部论文、业务反馈、历史实验库，生成并独立审核标准化实验提案；Model Agent负责多轮代码实现、训练、验证，返回代码、指标、待解决问题
- 四类标准化研究动作：定义Reproduce（复现外部方法）、Follow-up（优化已有实验）、Composition（组合多有效方案）、Diagnose（定位业务问题根因），覆盖全场景研发需求
- 实验全链路留存机制：每轮实验留存轮次级代码、指标、上下文，分别基于业务基线、直接父实验、历史最优祖先计算增益，避免迭代过程中有效方案丢失
### 关键结果
在快手多个业务生产环境验证：25天完成636次模型迭代，其中560次AUC超过业务基线；5次线上A/B测试获10~15%拉新效率提升、15~20%定向广告花费提升、0.3~0.8%观看时长提升，观看时长模型参数量与FLOPs降低10%；跨场景知识迁移实验33.3%超基线，远高于直接复现论文的0%。

工业推荐模型自主迭代的核心不是追求复杂调度策略，而是通过明确分工、标准化动作、可复用经验，在业务约束下持续逼近最优效果。
