---
title: 'SwarmWorld: Stigmergic technological evolution in societies of language-model
  agents'
title_zh: SwarmWorld：基于Stigmergy的LLM智能体群体技术演化框架
authors:
- Subhadeep Pal
- Fiona Y. Wang
- Markus J. Buehler
affiliations:
- Massachusetts Institute of Technology
arxiv_id: '2608.26081'
url: https://arxiv.org/abs/2608.26081
pdf_url: https://arxiv.org/pdf/2608.26081
published: '2026-08-26'
collected: '2026-08-27'
category: MultiAgent
direction: 多智能体 · 去中心化群体协作与演化
tags:
- Multi-Agent
- Stigmergy
- Decentralized Collaboration
- LLM Agent
- Collective Intelligence
one_liner: 设计无预设角色的去中心化LLM智能体环境，验证群体技术演化的边界优势
practical_value: '- 去中心化多Agent架构可复用：电商内容生成、智能客服、品类运营等Agent集群无需预设固定角色，通过共享知识库、用户反馈、操作记录（类stigmergy环境反馈）即可自发分化出探索、生产、维护类角色，大幅降低角色设计成本

  - 效果评估逻辑可迁移：多Agent系统评估不要仅看单实例最优效果，需同时覆盖整体服务鲁棒性、有效产出数量、能力复用率，尤其适合广告投放、推荐内容生产等需要抗扰动、多样化输出的场景

  - 长/短期任务资源分配策略参考：短期冲单指标最优适合用并行独立搜索方案，长期需要沉淀可复用资产的任务（如用户增长策略探索、商品知识体系搭建）适合引入群体协作、可执行资产继承机制'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多Agent系统大多依赖直接对话、预设角色或中心化工作流，无法验证去中心化无预设的LLM Agent群体能否自主演化出功能更优的技术体系，也无法区分群体能力提升是来自并行搜索还是真实协作增益。

### 方法关键点
- 搭建SwarmWorld模拟环境，所有初始Agent无角色、无预设技术库，可自主探索环境、加工资源、构建持久化可执行artifact、编写控制器程序，由环境独立判定所有动作的合法性与实际效果
- 设计4组对照实验：全文化（支持通信、代码继承、环境stigmergy）、无通信、无显性文化（仅保留环境stigmergy）、独立搜索（N个单Agent并行，取各端点最优结果作为强baseline）
- 评估维度覆盖单artifact性能、未知扰动下鲁棒性、技术组合韧性、有效发明数量

### 关键结果数字
- N=200时无显性文化组相比独立搜索baseline，发现前沿AUC提升0.069，验证发明数量增加6个，鲁棒性、技术组合韧性均显著高于baseline
- 3200tick长周期实验中，全文化组技术组合韧性比baseline高38%，有效发明数量是baseline的2倍以上，但独立搜索baseline的单最优artifact性能仍比全文化组高46%

### 核心结论
多智能体协作的核心优势是沉淀多样化、高韧性的能力生态，而非产出单维度最优的个体结果。
