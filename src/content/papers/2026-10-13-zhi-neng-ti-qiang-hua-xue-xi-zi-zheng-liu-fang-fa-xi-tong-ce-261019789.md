---
title: More Methods, Better Agents? A Reality Check on Self-Distillation in Agentic
  Reinforcement Learning
title_zh: 智能体强化学习自蒸馏方法系统性评测：无通用最优方案
authors:
- Linhao Zhong
- Bozhen Fang
- Xuehao Wang
- Duochao Shi
- Zekai Luo
- Guangming Yao
- Yi Yuan
- Hao Chen
- Jingdong Chen
- Chunhua Shen
affiliations:
- Zhejiang University
- Ant Group
arxiv_id: '2610.19789'
url: https://arxiv.org/abs/2610.19789
pdf_url: https://arxiv.org/pdf/2610.19789
published: '2026-10-13'
collected: '2026-10-15'
category: Agent
direction: Agent训练 · 自蒸馏方法评测
tags:
- LLM Agent
- Self-Distillation
- Reinforcement Learning
- GRPO
- Benchmark
one_liner: 在4个基准3种模型尺度下对比10种自蒸馏方法与GRPO，明确自蒸馏效果、稳定性与成本tradeoff
practical_value: '- 业务落地Agent训练时优先以GRPO为baseline验证效果，不要盲追最新自蒸馏方法：仅2种自蒸馏方法平均性能略超GRPO，多数方法在特定场景会出现性能崩溃，比如ICSD在电商WebShop场景4B模型下成功率直接归零，上线前必须做单场景小范围验证

  - 评估Agent训练方案不要只看最终得分，必须监测训练全程稳定性：部分方法最终得分高但中间存在长时间性能崩溃，工业场景训练时需设置多步checkpoint与回滚机制，避免不稳定训练浪费算力资源

  - 做算力ROI评估时需纳入自蒸馏的额外训练成本：主流自蒸馏方法比GRPO多消耗17%~19%的训练时间，但多数无法获得对应性能收益，算力预算有限的场景直接使用GRPO即可满足需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent强化学习自蒸馏方法层出不穷，但多数论文对比时复用不同实验条件下的基线得分，未系统对比同期方法，也极少关注训练稳定性和算力成本，导致从业者难以判断哪些方法真正具备落地价值，且Agent训练成本极高，亟需公平的系统性对比来指导方法选择。

### 方法关键点
- 以主流GRPO算法为基线，对比10种代表性自蒸馏方法，覆盖辅助损失、优势调制、奖励塑形、环境验证教师续接4类技术机制
- 实验覆盖3种模型尺度（Qwen3.5-2B/4B/9B）、4个典型Agent基准（ALFWorld、ScienceWorld、Search-QA、电商购物场景WebShop）
- 统一实验协议，所有方法在相同环境下训练100步，每5步验证，用8个rollout种子重复评估，同时统计训练耗时、GPU资源消耗

### 关键结果
总计132次训练，消耗12124.4 H800 GPU小时：仅2种自蒸馏方法（PCSD、AgentOPSD）在12个场景平均得分超过GRPO，分别高4.58、1.66分，其余8种均低于GRPO；无任何自蒸馏方法能在所有场景下稳定超过GRPO，部分方法存在严重场景崩溃问题，如ICSD在4B尺度WebShop场景下成功率为0；9次训练最终得分比训练峰值低20分以上，高最终得分可能隐藏严重的训练不稳定；超过半数的自蒸馏方法比GRPO训练耗时更长但性能更低。

**最值得记住的一句话：没有通用最优的自蒸馏方法，方法选择必须结合场景、稳定性要求与算力预算综合判断，不要脱离baseline谈单点收益**
