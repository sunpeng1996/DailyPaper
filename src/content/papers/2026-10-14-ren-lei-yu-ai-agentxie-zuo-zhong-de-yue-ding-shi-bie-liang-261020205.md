---
title: What and Where in Identifying and Quantifying Conventions in Humans and AI
  Agents
title_zh: 人类与AI Agent协作中的约定识别、量化及内容与位置分析
authors:
- Makoto Fukushima
- Tim Puphal
affiliations:
- Honda Research Institute Japan
- Honda Research Institute Europe
arxiv_id: '2610.20205'
url: https://arxiv.org/abs/2610.20205
pdf_url: https://arxiv.org/pdf/2610.20205
published: '2026-10-14'
collected: '2026-10-17'
category: Agent
direction: 人机协作Agent 约定识别与量化
tags:
- Human-AI Collaboration
- Convention Quantification
- Off-Belief Learning
- Multi-Agent
- Hanabi
one_liner: 提出convention gap量化框架对比人与AI协作约定，定位差异并验证多约定阻断的超加性成本
practical_value: '- 挖掘用户和推荐/搜索系统的隐式交互约定（如搜索query省略规律、推荐卡片点击偏好）可复用convention gap思路：基于显性规则计算行为基线概率，用实际行为和基线的差值量化隐式约定，无需标注即可挖掘用户未明确表达的交互习惯

  - 设计电商导购Agent、智能客服等人机交互系统时，可借鉴分层干预结论：修改单个隐式交互规则的效果通常有限，用户会自动路由到其他替代约定，要优化交互效率需同时调整多个关联约定

  - 多Agent协同的广告/推荐系统做策略迭代时，不要仅通过单变量消融判断规则价值，需做多规则联合消融，单个规则的观测贡献度会因替代路由被低估，联合消融才能得到真实业务影响'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
过往人机协作场景的隐式约定仅能通过更换协作伙伴后的分数下降间接证明存在，无法量化约定的具体内容、适用场景、实际价值，也难以系统对比人类与AI Agent的约定差异，无法指导优化Agent的人机协作适配能力。

### 方法关键点
- 定义**convention gap**：由仅依赖规则的字面观察者基于公开规则信息计算动作失败概率，减去实际动作失败率，差值即为隐式约定带来的收益，单位为pp
- 采用Off-Belief Learning（OBL）训练的1-5层Agent作为分层基准，层级越高模型越有能力利用非字面的隐式约定
- 构建六维上下文分类体系拆分gap的分布场景，设计频率匹配的随机阻断作为控制组，通过干预实验验证约定的实际业务价值

### 关键结果
- 数据集：两个独立人类Hanabi游戏语料（hanab.live 425局、AH2AC2 1858局），OBL各层级Agent各1000局自玩数据
- 人类群体的convention gap达26.16pp，高于OBL最高层级Level 5的21.68pp；人群独有间接提示约定（提示指向非触碰卡片）的gap达61.3pp，OBL5同场景仅为13.7pp
- 阻断单个高gap约定的超额损失仅0.12分（大部分为随机干扰损失），同时阻断8个高gap约定总损失达1.84分，远超过单个阻断损失之和0.77分，验证约定阻断成本的超加性

### 核心结论
单个隐式约定的观测贡献度不等于其实际价值，隐式约定会通过路由到其他替代场景大幅降低单规则修改的影响，仅多规则联合干预才能有效改变协作效率
