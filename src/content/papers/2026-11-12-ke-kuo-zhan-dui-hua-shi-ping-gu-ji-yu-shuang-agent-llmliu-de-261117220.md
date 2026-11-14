---
title: 'Scalable Conversational Assessment: Chat-Based Exams with a Two-Agent LLM
  Pipeline'
title_zh: 《可扩展对话式评估：基于双Agent LLM流水线的聊天式考试系统》
authors:
- Geoffrey Challen
- Craig Zilles
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2611.17220'
url: https://arxiv.org/abs/2611.17220
pdf_url: https://arxiv.org/pdf/2611.17220
published: '2026-11-12'
collected: '2026-11-14'
category: Agent
direction: 双Agent协作的对话式自动评估
tags:
- LLM Agent
- Multi-Agent
- Conversational Assessment
- Automated Evaluation
- Agent Architecture
one_liner: 提出双Agent分工的LLM流水线架构，实现可规模化的交互式对话类考试评估
practical_value: '- 双Agent权责拆分架构可复用在电商客服Agent、用户访谈Agent场景：前端交互Agent不接触核心规则/答案，从架构层面规避prompt注入、敏感信息泄露风险

  - 预设多类persona模拟不同特征/对抗策略用户做压测的方法，可直接复用在LLM驱动的业务系统上线前的鲁棒性测试

  - 虚构测试主题排除预训练知识干扰的评估思路，可借鉴来做LLM推荐系统的冷启动、无偏效果验证'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
线下口试可通过交互追问考察用户推理能力、澄清模糊回答，但规模化落地成本极高，现有自动化评估方案无法实现交互式深度测评。
### 方法关键点
1. 采用双Agent权责拆分架构：前端Interviewer Agent仅负责与用户交互、接收提问指令，不接触评分规则与参考答案；后端Hidden Evaluator Agent掌握全量评估目标，基于评分rubric跟踪用户表现，指导Interviewer选择追问或切换问题，从架构层面规避答案泄露风险。
2. 评测阶段先构造不同能力/对抗策略的LLM模拟用户persona（如prompt注入、编造答案、窃取答案等），引入虚构评估主题排除预训练知识干扰，再落地真实场景验证。
### 关键结果
已在AI通识选修课的形成性、总结性评估场景落地，经人工+AI复盘对话日志，验证架构可行性，同时识别出追问生成、用户贡献归因打分等优化方向
