---
title: 'Agentic University: Collaborative Agents for Personalized Learning'
title_zh: Agentic University：面向个性化学习的多智能体协作框架
authors:
- Jingru Fan
- Tianle Zhou
- Yunjie Zhou
- Zihao He
- Yixuan Zhou
- Kezhao Wu
- Xinyu Zheng
- Xiyuan Wang
- Yuheng Wang
- Zhi Li
affiliations:
- Shanghai Jiao Tong University
- Nanyang Technological University
- National University of Singapore
arxiv_id: '2610.40492'
url: https://arxiv.org/abs/2610.40492
pdf_url: https://arxiv.org/pdf/2610.40492
published: '2026-10-29'
collected: '2026-10-30'
category: MultiAgent
direction: 多智能体协作 · 人参与式自适应学习框架
tags:
- Multi-Agent System
- Human-in-the-loop
- Personalized Learning
- Adaptive System
- LLM Application
one_liner: 提出人类参与的多智能体组织框架，实现对齐目标、活动、评估的自适应个性化学习
practical_value: '- 可复用「人作为组织节点参与多智体协作」的架构设计，在电商个性化导购Agent中引入用户实时反馈作为核心状态输入，替代纯离线用户画像推断，大幅提升服务计划适配性

  - 可复用分层证据诊断+本地路径修订的迭代逻辑：在用户运营Agent中区分Learning-State Evidence（如点击、咨询）和Capability
  Evidence（如下单、复购），基于多Agent诊断结果动态调整后续触达策略，避免全局重排破坏用户体验一致性

  - 可复用「核心能力-阶段子目标-知识节点」的拆解范式，在内容/课程/商品套装推荐场景中基于用户目标生成结构化消费路径，搭配分层验证机制提升推荐路径的可解释性和转化完成率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM驱动的个性化学习系统仅能生成零散内容或单环节辅导，无法将目标、学习活动、评估形成对齐的连贯流程，也难以基于学习过程的动态证据持续适配学习者的需求变化，导致个性化支持的实际效果受限。
### 方法关键点
- 提出Human-Participatory Multi-Agent Organization框架，将学习者作为Human Node纳入多智体组织，与规划、辅导、评估、重规划四类专属Agent协作维护可迭代的Capability Program
- 设计分层评估机制：知识节点章节测试、阶段微项目、全流程企业仿真三层评估，区分Learning-State Evidence（交互、提问等过程数据）和Capability Evidence（评估得分），避免过度依赖辅助下的表现推断真实能力
- 重规划环节采用三Agent诊断（证据审计、过程观察、结果校验）+ 本地路径修订策略，修订结果需经过学习者确认后生效，既保证路径适配性又保留整体连贯性
### 关键实验结果
三个实验覆盖路径生成、修订、真人使用，对比baseline包括通用LLM、PLPP、SOTA系统GenMentor：
- 路径生成实验：96个模拟用户案例，AU的Assessment Validity得分比GenMentor高19.32分，Program Quality高10.52分
- 路径修订实验：128个匹配案例，AU的Program Improvement得分比GenMentor高8.01分，Revision Decision Appropriateness高5.78分
- 真人实验：32名参与者，AU组50分制测评得分平均提升12.19分，是对照组5.61分的2倍以上，用户认知支持评分显著更高
### 核心启示
人在回路的多智能体协作的核心不是让系统替代人做决策，而是通过共享结构化状态和明确的角色分工，让人的反馈成为系统迭代的核心锚点。
