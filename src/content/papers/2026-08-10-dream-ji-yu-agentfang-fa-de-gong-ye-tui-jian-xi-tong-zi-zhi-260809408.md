---
title: DREAM Technical Report
title_zh: DREAM：基于Agent方法的工业推荐系统自治优化控制架构技术报告
authors:
- Bin Zhang
- Bowen Zheng
- Chao Yi
- Chengyu Lai
- Dian Chen
- Dimin Wang
- Gaoyang Guo
- Jialin Zhu
- Jian Wu
- Jing Yu
affiliations:
- Taobao
- DREAM Team
arxiv_id: '2608.09408'
url: https://arxiv.org/abs/2608.09408
pdf_url: https://arxiv.org/pdf/2608.09408
published: '2026-08-10'
collected: '2026-08-11'
category: Agent
direction: Agent 推荐系统全链路自治优化
tags:
- Agentic RecSys
- Intent Understanding
- Edge-cloud Collaboration
- Closed-loop Optimization
- Pipeline Orchestration
one_liner: 在工业级级联推荐Pipeline上叠加Agent化控制层，无侵入式实现全链路策略自治优化
practical_value: '- 存量推荐系统改造无需替换原有模块，可采用「全局控制层+原有Pipeline参数下发+默认兜底」的无侵入架构，避免稳定性风险，快速拿到业务收益

  - 端云联动的用户意图感知方案可直接复用：端侧做轻量GRU变点检测过滤85%无效上报，云侧仅处理8.7%的高价值行为信号，大幅降低LLM推理成本

  - Agent策略迭代可采用离线模拟+在线反馈的双奖励闭环，离线先做策略空间探索降低线上试错风险，在线反馈沉淀到策略记忆持续优化

  - 工业场景下LLM推理可结合用户分层、时段动态阈值做调用频率控制，优先给高价值用户、高意图变更场景分配推理资源，性价比最优'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业级推荐系统普遍采用召回、排序、重排的级联Pipeline，存在模块间信息碎片化、优化目标分散、策略依赖人工调优、实时意图感知弱四大痛点，现有Agent化推荐方案要么仅做单品选择，要么仅做架构编排，未端到端覆盖意图感知、策略生成、执行反馈全链路，无法落地大规模工业场景。

### 方法关键点
- 架构无侵入：在原有Pipeline上层叠加控制层，不替换任何存量模块，保障服务稳定性
- 三层Intent Engine：端云联动F1-F4流量漏斗过滤无效信号，仅8.7%行为触发云端推理，输出L0（物理属性）/L1（需求）/L2（偏好）三层结构化意图，配套夜间Dreaming机制整合全天行为更新长期意图
- Meta Engine：基于Qwen3做M1意图总结、M2策略规划（复用策略记忆）、M3参数翻译三层推理，输出的可执行参数经统一出口带安全护栏下发到下游模块
- 双奖励闭环：离线环做模拟探索训练策略，在线环采集真实用户反馈沉淀到策略记忆，实现全链路自迭代

### 关键实验
在淘宝首页feed做大规模A/B测试，仅控制重排时IPV提升2.06%、核心IPV提升2.39%、GMV提升0.88%；扩展到控制精排后，对应收益提升到2.71%、3.06%、1.31%，PV稳定提升超1%。

最值得记住的一句话：Agent化推荐落地的最优路径不是重构原有系统，而是做存量Pipeline之上的自治控制层，用最小侵入成本拿到业务收益。
