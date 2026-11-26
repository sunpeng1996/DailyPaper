---
title: Welfare-Enhancing Mechanism Design for Agent Ecosystems
title_zh: 面向Agent生态的福利提升机制设计
authors:
- Zitian Guo
- Chen Xu
- Beibei Li
- Chenyan Xiong
affiliations:
- University of California, San Diego
- Carnegie Mellon University
arxiv_id: '2611.33627'
url: https://arxiv.org/abs/2611.33627
pdf_url: https://arxiv.org/pdf/2611.33627
published: '2026-11-25'
collected: '2026-11-26'
category: MultiAgent
direction: 多Agent生态 · 机制设计优化
tags:
- Multi-Agent System
- Mechanism Design
- Agentic Web
- Simulation Benchmark
- Ecosystem Optimization
one_liner: 构建多Agent生态仿真基准WILDREGISTRY，提出DEC机制解决内容Agent竞争导致的生态恶化问题
practical_value: '- 电商/搜索平台的多服务商竞争场景可复用DEC奖惩逻辑：用历史交付数据给优质服务商加权，对多次入选但无转化的服务商限流，平衡供需双方收益

  - Agent服务市场/工具调用路由团队可直接复用WILDREGISTRY仿真框架，提前测试不同策略的长期生态稳定性，避免线下试错成本

  - 生成式推荐/Agentic搜索场景可将交付证据动态补充到服务商/商品profile，减少信息不对称导致的匹配质量下降'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
Agentic Web场景下，内容Agent通过优化自身profile竞争用户Agent的入选机会，现有研究仅关注单主体内容优化，未覆盖多主体长期博弈的生态影响。无干预的竞争最终会使服务商曝光提升48.6%，但用户侧站点选择质量下降1.25个百分点，陷入有害稳定平衡。
### 方法关键点
- 构建WILDREGISTRY仿真基准：基于真实Agent搜索请求流、100个站点的去中心化服务市场，模拟内容Agent迭代profile、用户Agent选站的长期动态博弈
- 提出DEC（Delivery-Evidence Credit）平台侧机制：①Credit：将历史相似请求下的成功交付记录作为证据附加到对应站点profile，提升优质站点入选概率；②Withhold：对修改过profile且多次入选但无成功交付的站点剥夺入选机会，空位由有交付记录的候补站点补位
### 关键结果
基于DeepResearchGym 6个月真实搜索流量、AgentWebBench的100站点语料实验，对比Profile Adaptation、VCR、Keyword Scrub等基线，60天长期实验下DEC实现福利增益+2.01，站点选择质量W-nDCG@5比Profile Adaptation高2.14，同时保留89.7%的服务商曝光增益，无依据的profile占比下降43.8%。

**值得记住的一句话**：站点选择不仅分配当前机会，还决定未来供需双方的学习证据，是引导Agent生态向健康方向演化的核心机制杠杆。
