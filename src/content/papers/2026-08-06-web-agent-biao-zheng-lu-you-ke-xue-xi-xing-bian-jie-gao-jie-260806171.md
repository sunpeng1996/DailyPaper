---
title: 'Routing Is Least Learnable Where It Is Most Valuable: Bounds on Representation
  Routing for Web Agents'
title_zh: Web Agent 表征路由可学习性边界：高价值场景下的路由难题
authors:
- Jiaming Wei
- Zekun Wu
- Adriano Koshiyama
- Maria Perez-Ortiz
affiliations:
- University College London
- Holistic AI
- UCL Centre for Artificial Intelligence
arxiv_id: '2608.06171'
url: https://arxiv.org/abs/2608.06171
pdf_url: https://arxiv.org/pdf/2608.06171
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: Web Agent 表征路由效率与效果优化
tags:
- Web Agent
- Representation Routing
- Cost Optimization
- Agent Efficiency
- Routing Bound
one_liner: 揭示Web Agent表征路由的收益上限与可学习性瓶颈，给出可落地的成本优化空间
practical_value: '- 做Agent路由优化前先测重跑噪声：同模式同任务重跑结果浮动12-14%，低于该区间的收益不要归因于路由策略，避免无效迭代

  - 可直接复用成本路由方案：将所有模式都无法解决的任务路由到最低成本模式，可在不降低成功率的前提下降低9.5-30.6%的推理成本

  - 低成功率Agent不要投入资源做表征路由：路由监督标签与Agent成功率正相关（ρ=0.95），成功率越低可学习的路由标签越少，投入产出比极低

  - 跨场景迁移Agent时不要直接复用表征选型：不同任务集下最优表征完全反转，必须基于自身业务场景实测选型'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前Web Agent普遍固定使用单种页面表征（纯文本DOM、带标注截图SoM、纯视觉截图等），学界普遍认为基于任务动态路由表征能大幅提升效果，但此前研究未量化运行噪声的干扰，也未明确路由的实际收益边界与可落地空间。
### 方法关键点
- 固定Agent执行框架、Prompt预算与动作空间，测试6种页面表征在8组「站点×Backbone」组合下的表现
- 引入同条件重跑噪声作为基准，排除随机波动对收益归因的干扰
- 对比5类路由策略（模式选择、成本分级、零成本规则、置信度级联、分层路由）的实际表现
### 关键实验
基于VisualWebArena、WebArena两个主流Web Agent基准测试：
- 表面上6种表征的Oracle路由成功率比最优单模式高7.1~51.9pp，但扣除重跑噪声后，新增不同表征带来的收益甚至低于重跑已有模式的收益
- 仅成本优化路由可稳定生效，在8组测试场景中均达到预期效果
- 所有可落地的路由策略均无法稳定超过固定选最优单模式的基线，仅在极低成功率的稀疏场景下存在例外
### 核心结论
路由监督标签的生成速度与Agent成功率高度相关，Agent越弱、路由价值越高的场景，反而越没有足够的标签训练路由模型
