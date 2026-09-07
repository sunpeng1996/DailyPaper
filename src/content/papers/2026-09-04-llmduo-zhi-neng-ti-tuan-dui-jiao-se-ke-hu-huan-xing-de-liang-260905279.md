---
title: Testing Interchangeability in LLM Agent Teams
title_zh: LLM多智能体团队角色可互换性的量化测试研究
authors:
- Jianxin Gao
- Tianyi Yu
- Linna Deng
- Runze Li
- Zining Wang
affiliations:
- China Agricultural University
- Tianjin University of Finance and Economics
- Jilin University
- Tianjin University of Science and Technology
arxiv_id: '2609.05279'
url: https://arxiv.org/abs/2609.05279
pdf_url: https://arxiv.org/pdf/2609.05279
published: '2026-09-04'
collected: '2026-09-07'
category: MultiAgent
direction: 多智能体协作 · 可互换性测试
tags:
- Multi-Agent
- LLM Agent
- Coordination Efficiency
- Interchangeability
- Agent Evaluation
one_liner: 量化LLM多智能体团队角色互换的影响，提出带安慰剂对照的swap测试框架，明确任务表现与协调成本的分离效应
practical_value: '- 多Agent生产系统做角色扩容/故障转移时，不要仅监控任务成功率，需新增单位进度交互成本的埋点，避免表面正常但实际运行效率下降

  - Agent换入新团队时，直接清空其原有的partner notes记忆段，可减少16%~43%的swap penalty，效果优于保留全部历史记忆

  - 若系统需要频繁轮换Agent，优先选择greedy decoding（temperature=0），可把互换损失降低近一半，同时还能小幅提升任务完成率

  - 对高耦合多Agent场景（如电商客服工单流转、广告投放策略多Agent协同优化），尽量减少核心调度角色的轮换，其互换损失是普通执行角色的2~3倍'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前生产级多Agent系统默认相同角色的Agent可无成本互换，是故障转移、负载均衡、版本迭代的核心假设，但长期协作的LLM Agent会形成专属协作惯例，替换的实际影响从未被量化；现有研究未控制模型、角色、经验变量，无法分离能力差距与协作惯例不匹配的影响。
### 方法关键点
- 设计带安慰剂对照的swap测试框架：用同一基座模型生成多组独立团队，经历10轮形成期，Agent维护分为task notes（通用任务知识）和partner notes（专属协作知识）的私有notebook
- 设置6组对照条件：Intact（原团队）、Placebo（移除再放回同个Agent，控制人员变动通知的干扰）、Swap（跨团队换同角色Agent）、Swap cleared（换入Agent清空partner notes）、Amnesia（原团队删某Agent的partner notes）、Naive（换全新无经验Agent）
- 核心指标：归一化任务得分T、单位进度协调成本C，衡量协作专属价值占比的ρ系数
### 关键结果
在低耦合/高耦合Collab-Overcooked、Hanabi三个基准测试：
- 角色互换对任务得分影响极小，仅为新手替换损失的18%~44%；但协调成本大幅提升16%（低耦合）、51%（高耦合）、63%（Hanabi），Hanabi场景换有经验的异队Agent比换纯新手的协调成本还高11%
- 清空换入Agent的partner notes可降低16%~43%的互换损失，核心调度角色互换的损失是普通角色的2~3倍，70%的额外通信来自留任Agent
- 消融验证：greedy decoding比temperature=0.7的互换损失低48%，团队协作20轮后的互换损失是10轮的1.56倍

> 最值得记住的结论：LLM多智能体团队换人的影响全部藏在大家不看的协调成本里，任务成功率先恢复，沟通效率要慢一倍才能回到原有水平
