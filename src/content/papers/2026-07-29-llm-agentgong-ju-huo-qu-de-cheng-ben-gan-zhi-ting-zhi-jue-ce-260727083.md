---
title: 'Scores Are Not Decisions: Cost-Aware Stopping for Tool Acquisition in LLM
  Agents'
title_zh: LLM Agent工具获取的成本感知停止决策框架CAM-DF
authors:
- Yicheng Feng
- Yan Zhang
- Yan Cheng
- Wei Qi
affiliations:
- Peking University
- McGill University
- Shanghai University of Finance and Economics
- Tsinghua University
arxiv_id: '2607.27083'
url: https://arxiv.org/abs/2607.27083
pdf_url: https://arxiv.org/pdf/2607.27083
published: '2026-07-29'
collected: '2026-07-30'
category: Agent
direction: LLM Agent · 工具调用成本优化
tags:
- LLM Agent
- Tool Calling
- Cost Optimization
- Stopping Policy
- Decision-Focused Learning
one_liner: 提出预执行成本感知工具停止插件CAM-DF，无需微调LLM即可降本同时保障任务效果
practical_value: '- 可直接复用CAM-DF作为现有Agent工具排序链路的前置插件，无需修改上游ranker和下游LLM，快速落地成本管控能力，适配电商导购Agent、RAG问答等场景

  - 工具选择决策不要仅依赖排序得分，需引入工具边际收益/成本比、成本压力λ等特征，在API调用成本差异大、算力预算紧张的场景收益更显著

  - 训练目标可直接基于「停止vs继续的收益差」做regret加权，不需要复杂建模，小样本即可拟合，适合业务侧快速迭代

  - 电商召回截断、RAG检索截断场景可直接迁移这套停止决策逻辑，平衡效果与带宽/算力成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM Agent依赖大量外部工具支撑任务，但调用过多工具会带来API成本上涨、上下文负载升高、隐私暴露风险增加等问题，现有工具排序框架仅输出相关性得分，无法结合异构工具成本决定最优调用数量，纯得分阈值规则在成本异构场景下被理论证明是次优的，行业缺少可直接复用的预执行成本控制层。

### 方法关键点
- 定义收益函数：$U(A,x) = 任务完成度 - \lambda \times 调用工具总成本$，其中$\lambda$为成本压力系数，量化成本与效果的换算关系
- 提出CAM-DF停止策略：离线训练时标注每个工具前缀停止的收益与后续最优收益的差值，用差值大小作为样本权重训练二分类器，判断当前前缀是否可以停止，理论证明该目标与贝叶斯最优停止对齐
- 推出轻量化可解释版本CAM-DF-lite，仅用10个理论驱动特征（前缀进度、下一个工具的得分/成本比等）即可达到接近全模型的效果
- 部署时作为预执行插件，虚拟遍历排序后的工具列表输出最优前缀，无需修改现有ranker和底层LLM

### 关键结果
在包含零售、航空、电信等5个领域共1343个任务上评测，对比固定top-k、得分阈值、预测再阈值等6种基线：
1. 在τ-bench零售场景，CAM-DF在均匀和异构成本下均取得可部署方法中的最高收益，10种成本+排序配置下全部超过预测再阈值基线
2. 端到端评测中，CAM-DF相比全工具访问减少37%工具调用量，同时任务成功率从0.58提升到0.67，无统计显著性差异
3. 在高成本压力、低排序质量、成本异构性高的场景下，CAM-DF相对基线的收益最大，最高比预测再阈值基线高0.21

**最值得记住的一句话**：工具排序的得分不等于最终决策，异构成本下必须将边际收益与成本的比值作为停止决策的核心依据
