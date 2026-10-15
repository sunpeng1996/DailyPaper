---
title: 'AdCoEvo: A Co-Evolving Multi-Agent Advertising Delivery System'
title_zh: AdCoEvo：协同演化的多智能体广告投放系统
authors:
- Tianzhu Hu
- Hang Yu
- Zeyuan Zhao
- Zeyu Pan
- Huan Luo
- Chun Gan
- Mingzhe Cao
- Liubin Wang
- Mingming Li
- Jiao Dai
affiliations:
- Institute of Information Engineering, CAS
- University of Chinese Academy of Sciences
- The University of Sydney
- JD.COM
arxiv_id: '2610.19454'
url: https://arxiv.org/abs/2610.19454
pdf_url: https://arxiv.org/pdf/2610.19454
published: '2026-10-14'
collected: '2026-10-15'
category: MultiAgent
direction: 多Agent广告投放 · 协同演化
tags:
- MultiAgent
- AdDelivery
- CoEvolution
- ReinforcementLearning
- LoRA
- LLM4Ads
one_liner: 提出分角色协同演化的多智能体广告投放系统，较规则基线提ADV14.02%、降CPA7.07%
practical_value: '- 广告投放多角色分工可直接复用：将全链路投放拆分为预算规划、tCPA调价、周期诊断3个独立角色，分别用LoRA微调，大幅降低单Agent决策复杂度，输出非法率降为0，适合电商多账户规模化运营

  - 协同演化机制适配动态场景：每个周期轮询更新单个角色参数，其他角色固定，用业务结算后的真实反馈做RL优化，训练稳定性更高，可直接迁移到电商大促、流量波动等动态环境的策略迭代

  - 差异化回报设计解决长周期反馈问题：针对不同角色的影响范围和反馈时效设计reward，比如Inspector的reward用相邻周期业务指标变化加权计算，可复用在所有长周期决策的Agent系统

  - 小模型领域训练方案性价比极高：8B小模型加SFT+RL的效果超过GPT-5.6-Terra等通用大模型，单周期API成本仅0.235元，比最便宜的大模型低65%，适合大规模落地'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有广告投放仅实现出价、预算分配等单任务自动化，全链路决策仍高度依赖人工运营，难以支撑大规模账户管理，且人工经验难以沉淀为可复用能力，动态流量环境下策略迭代滞后，无法快速适配市场变化。
### 方法关键点
- 角色分工：拆分3个独立专业化角色，Planner负责账户级剩余预算分配，Optimizer负责广告单元tCPA实时调价，Inspector负责周期结算后的诊断输出，指导下周期决策，各角色独立维护LoRA参数，输出非法率为0
- 两阶段训练：第一阶段用运营专家轨迹做SFT，再用离线GSPO算法做RL优化各角色策略；第二阶段持续协同演化，每个周期轮询更新1个角色参数，用结算后的真实业务反馈做RL优化，其他角色固定，实现多角色共同适配环境变化
- 差异化回报构造：针对不同角色的影响范围和反馈时效设计reward，Planner/Optimizer的reward结合单账户和全局收益，Inspector的reward用相邻周期的业务指标变化计算，匹配各角色的反馈延迟特征
### 关键实验
基于AuctionNet仿真环境，对比规则基线、AdPilot单Agent系统、GPT-5.6-Terra等通用大模型：较规则基线，AdCoEvo提升ADV14.02%，降低CPA7.07%；较固定参数的多Agent系统，ADV提3.96%，CPA降1.24%；较GPT-5.6-Terra，ADV提3.73%，CPA降3.23%，单周期API成本仅0.235元，比最便宜的大模型低65%以上。
### 核心结论
多Agent系统的效果提升不仅来自合理的角色分工，更来自基于真实业务反馈的持续协同演化，小模型加领域专项训练的性价比远高于通用大模型。
