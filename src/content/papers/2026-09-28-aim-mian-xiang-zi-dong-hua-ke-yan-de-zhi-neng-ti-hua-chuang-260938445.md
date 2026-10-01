---
title: 'AIM: Agentic Idea Management for Automated Research'
title_zh: AIM：面向自动化科研的智能体化创意管理框架
authors:
- Hyeong Kyu Choi
- Bhavana Dalvi Mishra
- Jiefeng Chen
- Mihir Parmar
- Rui Meng
- Chun-Liang Li
- Xiangru Tang
- Sharon Li
- Jinsung Yoon
- Tomas Pfister
affiliations:
- Google Cloud AI Research
- University of Wisconsin-Madison
arxiv_id: '2609.38445'
url: https://arxiv.org/abs/2609.38445
pdf_url: https://arxiv.org/pdf/2609.38445
published: '2026-09-28'
collected: '2026-10-01'
category: Agent
direction: Agent 自动化科研创意管理
tags:
- LLM Agent
- Idea-driven Search
- Bayesian Optimization
- Autonomous Research
- Resource Allocation
one_liner: 提出idea驱动的智能体创意管理框架AIM，在自动化科研任务上实现性能与效率双重提升
practical_value: '- 创意分层聚类+explore/exploit权衡的设计，可直接迁移到推荐系统物料池/召回策略池管理：对同类语义的物料、召回策略做聚类，动态分配流量/计算预算，避免资源浪费在同质化方向

  - Solution Auditor的对齐校验机制，可复用在GenRec的创意生成链路：校验生成的商品文案、推荐理由是否匹配商品属性、用户偏好，过滤无效生成结果

  - 动态资源规划的思路，可用于多并行A/B测试场景：根据实时实验效果动态调整流量分配，给潜力方向倾斜更多资源，预期收敛速度可提升2-3倍

  - idea驱动与solution驱动的范式选择结论可指导Agent链路设计：任务可选路径多、优质方案稀疏时优先选idea驱动分层搜索；路径少、需精细调优时用solution驱动局部迭代'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有自动化科研Agent多为solution驱动，直接优化可执行代码，容易陷入局部优化、资源浪费在同质化方向；idea驱动的方法又缺乏结构化的创意管理、选择机制，且存在创意与实现不匹配的问题，导致实验效率低、结果不可靠。
### 方法关键点
- 参考Bayesian Optimization的代理-采集架构，设计Agentic Surrogate模块：对创意池做语义聚类，基于历史实验证据对聚类簇和单个创意做潜力排序
- Agentic Acquisition模块：分层做explore/exploit决策，簇级和创意级分别选择动作，实验后通过4种模式（分数引导优化、交叉融合、错误修复、新创意生成）扩展创意池
- Solution Auditor模块：校验实现是否符合原始创意、是否满足任务要求，修正不匹配的创意归属，避免错误反馈污染后续决策
- Resource Planner模块：根据剩余预算动态调整每轮并行实验的数量，平衡并行广度和迭代反馈速度
### 关键实验
在10个AutoLab基准任务上测试，对比ScientistOne等7个SOTA基线：系统优化任务上平均准确率67.0%，超最强基线1.6个百分点；长周期模型开发&CUDA任务上平均准确率55.8%，超最强基线4.9个百分点；达到SOTA基线的最优性能最快可快3.1×。
### 核心结论
当任务可选方向多、优质方案稀疏时，idea驱动的分层搜索能通过可控的语义覆盖大幅提升探索效率，反之则适合用solution驱动的局部优化
