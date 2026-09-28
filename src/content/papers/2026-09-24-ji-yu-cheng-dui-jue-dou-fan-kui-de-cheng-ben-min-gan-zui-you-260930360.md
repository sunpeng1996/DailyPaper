---
title: Cost-Aware Best-LLM Identification using Dueling Feedback
title_zh: 基于成对决斗反馈的成本敏感最优LLM识别算法
authors:
- Sarvesh Gharat
- Nikhil Karamchandani
- Jayakrishnan Nair
affiliations:
- Indian Institute of Technology Bombay
arxiv_id: '2609.30360'
url: https://arxiv.org/abs/2609.30360
pdf_url: https://arxiv.org/pdf/2609.30360
published: '2026-09-24'
collected: '2026-09-28'
category: LLM
direction: LLM选型 · 成本感知决斗多臂老虎机
tags:
- Dueling Bandit
- Cost-aware LLM Selection
- Best Arm Identification
- Condorcet Winner
- Track-and-Stop
one_liner: 提出成本感知的决斗土匪DCTAS算法，渐近最优，LLM选型成本较无感知基线最高降6%
practical_value: '- 电商多LLM Agent调度场景：可复用DCTAS框架做LLM选型，仅需少量成对偏好反馈就能识别性价比最优的LLM，较无成本感知的评估方案最高降6%推理成本

  - 推荐/搜索多模型A/B测试：将不同模型看作异构成本臂，用决斗反馈替代绝对值评估，用户偏好判断更准确，同时可降低测试流量占用和算力开销

  - 多召回源择优场景：可借鉴WeightPullAllocation的流量分配策略，优先给性价比最高的对比对分配测试流量，较轮询方式评估效率提升2~4倍'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
当前LLM选型广泛采用成对偏好评估（如Chatbot Arena的两两对比），相比绝对值评分更贴合人类判断逻辑，但不同规模LLM的查询成本差异可达数十倍，现有决斗多臂土匪算法默认采样成本一致，导致评估总开销极高。同时经验证，真实LLM偏好数据普遍满足Condorcet Winner假设（存在一个模型对其他所有模型的胜率均超过50%），现有算法未利用该弱假设优化成本效率。
### 方法关键点
- 首次将异构采样成本引入固定置信度决斗土匪框架，以识别Condorcet Winner为目标，最小化总采样成本
- 提出DCTAS算法：① 初始化阶段每对模型对比1次得到初始偏好估计；② 采样阶段通过WeightPullAllocation计算最优拉取比例，优先拉取与目标分配差距最大的模型对，对采样次数不足√t的对强制探索保证收敛；③ 停止阶段采用GLR统计量做动态阈值判断，严格满足δ-PC（错误率≤δ）的置信度要求
- 理论证明当误差δ趋近于0时，算法几乎必然达到信息论下界的渐近最优成本
### 关键实验
在合成数据集+Chatbot Arena的4类真实LLM对比数据集（T2I、T2T、Vision、Search）上实验，对比无成本感知TAS、成本感知CRR/DPCA等基线：DCTAS较无成本感知的TAS最高降低5.9%的总评估成本，比CRR、DPCA等基线的成本低2~6倍；搭配置信区间停止规则的DCTAC变种可进一步降低40%左右的总成本。
### 核心结论
在存在Condorcet Winner的成对偏好选型场景中，成本感知的自适应采样策略可在不损失评估准确率的前提下，大幅降低整体评估与推理开销。
