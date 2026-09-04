---
title: 'FiMI Banking: A Sovereign Model for Indian Retail Banking'
title_zh: 面向印度零售银行的可控主权级对话Agent模型FiMI Banking
authors:
- NPCI AI Research Team
- Aman Kumar
- Asit Desai
- Chandra Bhushan
- Harsh Sharma
- Harshit Bhushan
- Hrithik Kadam
- Keyur Doshi
- Kolisetty Sai Kapardheeswar
- Krishanu Adhikary
affiliations:
- NPCI AI Research Team
arxiv_id: '2609.03960'
url: https://arxiv.org/abs/2609.03960
pdf_url: https://arxiv.org/pdf/2609.03960
published: '2026-09-03'
collected: '2026-09-04'
category: Agent
direction: 垂直领域Agent 小参数安全对齐训练
tags:
- Agent
- DPO
- GRPO
- Tool Use
- Synthetic Data
- Vertical LLM
one_liner: 结合DPO偏好优化与可验证奖励RL训练4.5B银行专用Agent，满足监管与操作约束
practical_value: '- 做垂直场景（如电商客服、广告投放工具Agent）可复用「基于模型自身失败构造DPO偏好对」的方法，不用依赖外部大模型生成偏好样本，避免模型学习长度、格式等表面特征，优化效果更稳定

  - 多轮工具调用类任务的奖励可拆分为分层可验证模块（工具序列、状态校验、信息触达、人工校验），80%以上的奖励可通过程序自动计算，大幅降低标注成本同时避免reward
  hacking

  - 小参数垂直模型对齐可采用双阶段方案：单轮安全行为（如拒答超范围请求、合规话术）用DPO优化，多轮工具编排与流程执行用可验证奖励RL优化，两者互补，效果可追平数倍参数的通用大模型

  - 涉及用户敏感数据的场景可全流程用合成数据+仿真环境训练验证，完全不触碰真实用户数据，满足合规要求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
通用大模型无法满足银行等强监管垂直场景的三大核心要求：一是输出必须严格grounding于官方规则与用户真实数据，不能虚构信息；二是工具调用必须严格遵循操作流程，顺序错误会导致资损；三是必须严格拒绝超范围请求，防范安全风险，同时银行需要完全可控、可本地化部署的模型，不能依赖外部公有大模型。
### 方法关键点
- 构建覆盖5类印度零售银行业务的全仿真可复现环境，所有训练数据、用户背景、账户状态均为合成生成，完全无真实用户数据，满足合规要求
- 单轮行为优化阶段：基于基模型偏离金标准对话的失败样例构造DPO偏好对，优先优化安全拒答、事实对齐、合规话术等单轮行为
- 多轮工具调用优化阶段：采用GRPO强化学习算法，奖励拆分为4层可验证指标（工具序列正确性40%、最终账户状态25%、核心信息触达用户15%、自然语言合理性20%），80%以上的奖励可通过程序自动校验
### 关键结果
- DPO优化后，超范围请求拒答率从52%提升至80%，社会工程攻击防御率从42%提升至84%，安全类指标持平26B~31B通用大模型
- RL优化后，边缘场景任务得分从0.509提升至0.718，顺序敏感任务得分从0.590提升至0.679，生成token量减少29%，仅4.5B参数的小模型效果追平接近3倍参数的12B通用大模型
### 核心结论
垂直领域Agent对齐不需要盲目堆叠参数，DPO优化单轮安全行为+可验证奖励RL优化多轮工具执行的组合方案，可让小参数模型在满足合规要求的前提下达到甚至超过大模型的效果
