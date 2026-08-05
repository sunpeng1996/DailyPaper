---
title: Attacking and Defending Multi-Agent Collaborative Filtering Systems Through
  Connectivity
title_zh: 基于连接性的多智能体协同过滤系统攻防机制研究
authors:
- Anjun Hu
- Hanting Xie
- Saranya Govindan
- Jas Kandola
- Kurt Cutajar
affiliations:
- University of Oxford
- Amazon
arxiv_id: '2608.03272'
url: https://arxiv.org/abs/2608.03272
pdf_url: https://arxiv.org/pdf/2608.03272
published: '2026-08-04'
collected: '2026-08-05'
category: Agent
direction: 多智能体推荐 攻防机制与安全优化
tags:
- Multi-Agent
- Collaborative Filtering
- Adversarial Attack
- Defense
- Recommendation Safety
- LLM4Rec
one_liner: 揭示多智能体协同过滤系统连接性对攻防的调控规律，适配通用MAS攻防方法到推荐场景
practical_value: '- 多智能体推荐架构设计时，可将单轮用户交互候选数k控制在2以内，在几乎不损失推荐效率的前提下，将攻击稳态ASR降低20%以上

  - 安全检测需区分用户/商品agent的不对称性：用户侧污染优先用G-Safeguard，高商品集中度（ρ>1）的电商场景优先用BlindGuard检测商品侧攻击

  - 语义注入攻击比传统词汇扰动攻击留存率高35%以上，商品内容审核需增加语义层面的恶意检测，不能仅依赖关键词匹配

  - 评估智能体推荐鲁棒性时需分别统计 transient 阶段和稳态的ASR，单一时间点的指标无法反映系统真实安全水平'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
多智能体协同过滤（CF）系统通过LLM驱动的用户、商品agent交互优化推荐效果，但同时继承了数据驱动模型和多智能体通信的双重安全漏洞，现有通用多智能体系统（MAS）的攻防结论无法直接迁移到二部图结构的CF场景，连接性对漏洞传播的调控机制尚不明确，亟需系统性研究支撑鲁棒的智能体推荐系统设计。
### 方法关键点
- 定义两个连接性核心调控轴：单轮用户交互候选数k（推理侧配置，取值1/2/3）、商品目录集中度ρ（历史交互密度，ρ=用户数/商品数，取值0.5/1/2）
- 适配6类通用MAS攻击（传播类CORBA/NetSafe、提取类MAMA/MASLeak、双向TOMA/MASTER）和4类防御方法（G-Safeguard/BlindGuard/T-Guard/M-Guard）到二部图CF场景
- 基于AgentCF框架搭建评估pipeline，采用LLM judge分用户/商品侧统计攻击成功率（ASR），区分 transient 阶段增长斜率和稳态均值两类指标
### 关键结果
实验基于MovieLens-100K数据集，控制100个用户、25%的agent被攻陷的攻击场景：
1. 候选数k≥2时，传播类攻击稳态ASR比k=1高20%-40%；提取类攻击k=2与k=3的稳态泄漏率相当，均比k=1高30%以上
2. G-Safeguard可将用户侧平均ASR从31.6%降至3.3%，商品侧高ρ场景下的防御增益比低ρ场景高25%
3. 语义注入攻击比传统词汇扰动攻击的成功率高35%以上

多智能体推荐系统的攻防效果存在显著的角色不对称性和时间阶段异质性，连接性配置是平衡推荐效率与安全的核心可调参数
