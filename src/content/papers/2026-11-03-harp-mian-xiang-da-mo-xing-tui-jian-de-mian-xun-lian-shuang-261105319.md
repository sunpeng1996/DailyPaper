---
title: 'HARP: Training-Free Dual-Profile Agentic Communication for LLM-Based Recommendation'
title_zh: HARP：面向大模型推荐的免训练双Profile智能体通信框架
authors:
- Zhen Tao
- Xun Zhou
- Xuhui Chen
- Ziyue Qiao
- Qingqiang Sun
affiliations:
- 哈尔滨工业大学（深圳）
- 大湾区大学
- 深圳湾区研究院
arxiv_id: '2611.05319'
url: https://arxiv.org/abs/2611.05319
pdf_url: https://arxiv.org/pdf/2611.05319
published: '2026-11-03'
collected: '2026-11-04'
category: Agent
direction: 智能体推荐 · 免训练双Profile通信
tags:
- AgenticRecommendation
- LLM4Rec
- TrainingFree
- Homophily
- DualProfile
one_liner: 提出免训练双Profile同质性门控的智能体推荐框架，Hit@1较SOTA最高提升24%
practical_value: '- 可直接复用双Profile设计：用户侧用LLM生成多维度结构化画像，物品侧通过规则抽取同schema画像，零额外LLM调用成本，适配电商/内容推荐大规模落地需求

  - 画像匹配信号优先接入召回阶段做加权，不要全部堆在精排prompt挤占上下文token，该设计经ablation验证可降低精排上下文饱和带来的效果损失

  - 用户画像迭代可采用单轮反射+保守规则校验方案，无需微调LLM即可实现in-context画像更新，适合冷启用户快速优化画像准确度

  - 跨域召回场景可借鉴通道可分解的同质性计算方法，分维度加权匹配用户与物品特征，兼顾推荐效果与可解释性'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前主流记忆增强型LLM推荐框架存在三个结构性缺陷：仅用户侧有结构化画像，物品侧无对齐schema的对等描述；画像信号全部注入精排prompt，挤占有限上下文带宽，无法作用于召回阶段前置筛选；用户画像预热后固定，无基于交互反馈的迭代规则，效果天花板明显。
### 方法关键点
将LLM推荐抽象为用户/物品智能体四阶段通信过程（BUILD/TRANSMIT/UNDERSTAND/SYNC），基于该框架设计三个免训练算子，无需改动LLM backbone：
1. BUILD：用户侧通过单轮LLM调用生成四通道（偏好/质量/场景/受众）结构化画像，物品侧通过规则抽取同schema画像，零额外LLM成本
2. UNDERSTAND：定义通道可分解的画像同质性匹配分，在召回阶段对协同得分做加权门控，不占用精排prompt token
3. SYNC：基于用户交互反馈做单轮反射式画像更新，加保守校验规则，无需梯度更新即可实现画像迭代
### 关键实验
在Yelp、Amazon Books、MovieTV、Goodreads四个公开基准测试，对比最强记忆增强基线MemRec，Hit@1提升6.9%~24.0%，所有提升统计显著性p<1e-9；消融实验显示召回侧同质性门控贡献了70%以上的效果增益，仅将画像注入精排prompt对效果无显著提升。
### 核心结论
结构化画像信号在召回阶段使用的收益远高于注入精排prompt，免训练的对称双Profile设计是LLM推荐降本提效的高可行性路径
