---
title: 'Write, Execute, Refine: From Skill Followers to Skill Optimizers via Reinforcement
  Learning from Execution Feedback'
title_zh: 基于执行反馈强化学习的Agent技能迭代优化框架WER
authors:
- Kang Peng
- Zhiwei Zhang
- Yichen Zhang
- Zezhong Wang
- Yiming Du
- Geng Tu
- Baojun Wang
- Bin Liang
- Ruifeng Xu
- Kam-Fai Wong
affiliations:
- 哈尔滨工业大学（深圳）
- 香港中文大学
- 高可信软件技术教育部重点实验室
- 哈尔滨工业大学
- 华为技术有限公司
arxiv_id: '2608.17587'
url: https://arxiv.org/abs/2608.17587
pdf_url: https://arxiv.org/pdf/2608.17587
published: '2026-08-18'
collected: '2026-08-19'
category: Agent
direction: Agent 技能迭代优化
tags:
- Agent
- Skill Optimization
- Reinforcement Learning
- GRPO
- Execution Feedback
one_liner: 训练独立于冻结执行器的技能优化器，通过多阶段自举从执行反馈迭代优化Agent技能
practical_value: '- 可复用「冻结执行器+独立轻量优化器」架构，无需修改现有业务Agent核心权重，仅训练小模型优化prompt/规则，落地成本低，适配电商导购Agent、客服Agent的流程规则迭代

  - 借鉴「配对成败执行轨迹构造优化样本」的trick，无需人工标注失败原因，用相同上下文下的成败对比信号做优化，可迁移到推荐系统文案生成、query改写的效果迭代

  - 多阶段自举训练思路可用于生成式推荐的prompt优化：每轮保留效果中等的样本构造下一轮训练数据，逐步逼近最优prompt，避免过拟合'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent依赖专家编写的自然语言技能提升工具调用效果，但Agent自生成的技能比无技能基线效果差8-11个点；推理时的单次技能修复仅优化当前技能，不会提升模型的通用技能写作能力，通用LLM的反思能力不足以稳定将执行反馈转化为可复用的流程指导。

### 方法关键点
- 架构分离：冻结下游执行Agent，仅训练独立的轻量Skill Optimizer（4B参数），优化器仅输出自然语言技能，不直接与环境交互，训练成本极低
- 无偏奖励：用程序化验证器生成的组相对奖励做GRPO训练，奖励由格式合规、任务成功率、长度约束三部分构成，避免LLM打分的自确认偏差
- 多阶段自举训练：每轮保留执行结果好坏参半的中间技能，配对其成功/失败的执行轨迹构造下一轮优化样本，让优化器从自身输出的执行后果中迭代学习

### 关键结果
在BFCL v4多任务、τ2-bench两个工具调用基准上测试：相比无技能基线，Pass@1分别提升7.80、3.85个百分点；相比同架构未经过训练的优化器，Pass@1分别提升9.35、10.29个百分点；4B参数的训练后优化器在BFCL v4上Pass@1达76.63%，超过所有参评的通用大模型（包括GPT-5.5）。

**最值得记住的结论**：技能优化是独立于Agent执行能力的专用能力，小参数专用模型经针对性训练可超过通用大模型的技能优化效果
