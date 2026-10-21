---
title: Which Model for Which Role? Cost-Efficient Pareto Recommendation for LLM Agentic
  Workflows
title_zh: 面向LLM Agent工作流的成本高效帕累托模型分配推荐方法
authors:
- Qian Xie
- Wenyue Hua
- Yueli He
- Sripad Karne
- Armaan Agrawal
- Nikos Pagonas
- Eugene Wu
- Kostis Kaffes
- Tianyi Peng
- Nairen Cao
affiliations:
- Columbia University
- Cornell University
- Microsoft
- New York University
- Shanghai University of Finance and Economics
arxiv_id: '2610.26676'
url: https://arxiv.org/abs/2610.26676
pdf_url: https://arxiv.org/pdf/2610.26676
published: '2026-10-19'
collected: '2026-10-21'
category: Agent
direction: Agent 多角色模型分配帕累托优化
tags:
- LLM-Agent
- Pareto-Optimization
- Cost-Efficiency
- Gittins-Index
- Model-Allocation
one_liner: 提出CC-GITTINS方法，以10%穷举成本恢复Agent多角色模型分配帕累托前沿
practical_value: '- 多角色Agent（如电商客服Agent的意图识别、回答生成、合规校验链路）选型时，可复用双控制器交替搜索的思路，无需穷举所有模型组合，将选型评估成本降低70%以上

  - 帕累托推荐环节可直接复用LCB质量下界+UCB成本上界的过滤规则，避免将效果不稳定、成本波动大的候选纳入推荐集，降低线上效果风险

  - 需兼顾多目标的业务场景（如推荐系统的效果/算力成本/响应延迟、Agent的回答质量/调用成本/latency），可扩展多控制器设计，每个控制器独立优化一个目标维度，共享观测数据避免重复评估'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM Agent工作流常拆分规划、求解、验证等多个专业角色，全用高能力大模型会导致部署成本过高，而不同角色的模型组合效果无法通过单模型孤立评估推导，穷举所有组合的端到端评估成本极高；现有方法要么固定权重优化单目标，要么需要提前指定效果阈值，无法灵活提供质量-成本的全量trade-off选项供业务按需选择。
### 方法关键点
- 核心利用「部署成本越高的模型组合，评估成本也越高」的天然耦合特性，设计CC-GITTINS多目标搜索框架，设置质量、成本两个独立控制器，交替选择候选组合进行评估，共享观测数据避免重复计算
- 每个控制器基于成本感知的Gittins指数排序待评估候选，当某一方向搜索收敛时独立下调评估价格权重，继续探索更优trade-off，无需提前指定搜索预算或偏好权重
- 推荐阶段采用保守帕累托过滤规则，用质量下置信界(LCB)、成本上置信界(UCB)计算支配关系，仅返回非支配的候选组合，可随时终止搜索获取当前最优推荐集
### 关键实验
在8个覆盖2-5个Agent角色、最多1681种候选组合的基准数据集上测试，对比EGE-SH、qNEHVI等5种基线方法：仅用10%的穷举评估成本即可恢复大部分真实帕累托前沿，平均召回88.75%、精度100%；30%成本下可覆盖绝大多数前沿点，几乎无假阳性。新增latency作为第三优化目标时仍保持优异表现。
### 核心结论
多角色Agent模型选型无需穷举，利用评估-部署成本耦合特性的帕累托搜索，可将选型成本降低90%以上
