---
title: 'MAPS: A Multi-Agent Personalized Script-Driven Video Advertising System Enhanced
  by Reinforcement Learning'
title_zh: MAPS：多智能体脚本驱动的强化学习增强个性化视频广告系统
authors:
- Zhongyu Wang
- Chen Zuo
- Qingxuan Sun
- Jiayang Qiao
- Qiuhao Qian
- Songyan Cui
- Guocheng Chen
affiliations:
- Beihang University
- Kuaishou Technology
arxiv_id: '2610.25748'
url: https://arxiv.org/abs/2610.25748
pdf_url: https://arxiv.org/pdf/2610.25748
published: '2026-10-19'
collected: '2026-10-20'
category: GenRec
direction: 生成式推荐 · 多智能体广告创意生成
tags:
- MultiAgent
- ReinforcementLearning
- VideoAdvertising
- GenerativeRecommendation
- GRPO
- LLM-as-Judge
one_liner: 构建四角色协作多智能体闭环框架，通过RL优化脚本生成，实现动态个性化视频广告生产
practical_value: '- 可直接复用四智能体分工的闭环架构：Profile/Scripter/Director/Reflector的角色拆分适配所有个性化创意生成场景，解决静态创意池容量不足、迭代慢的痛点

  - Scripter的两阶段训练范式可直接落地：SFT冷启动打结构基础+GRPO多维度奖励优化的方案，α=0.3/β=0.4/γ=0.3的奖励权重配比可直接参考，避免生成内容偏离业务目标

  - LLM-as-Judge的评估prompt可复用：论文设计的个性化匹配、产品信息对齐、创意融合质量等维度的评估规则，可替代80%以上的创意生成任务人工标注成本

  - 工业侧范式升级参考：从检索式创意匹配到生成式创意生产的升级，可带来ARPU近10%的增量，适合短视频、直播电商的广告场景优先试点'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前视频广告普遍采用检索式范式，依赖预生产的静态创意池，既无法匹配快速迭代的用户偏好，用户反馈也无法实时优化在投创意，导致个性化粒度不足、不同用户群效果差异大。随着定向、出价等传统优化手段进入性能瓶颈，创意侧优化已成为广告效果提升的核心抓手。
### 方法关键点
- 架构上设计4个协作Agent形成闭环：Profile Agent从用户历史交互和实时上下文提取结构化四维用户画像（兴趣主题/偏好风格/隐含需求/决策倾向）；Scripter Agent基于用户画像和产品信息生成结构化广告脚本；Director Agent基于脚本和产品素材合成视频；Reflector Agent归因用户反馈，输出最小化修订指令迭代更新上游模块。
- Scripter采用两阶段训练：SFT阶段在人工标注的广告脚本语料上微调，掌握结构化脚本生成能力；RL阶段基于GRPO算法，采用三维混合奖励（结构合规30%+个性化匹配40%+产品信息对齐30%）优化生成效果，兼顾格式正确性、用户偏好匹配度和产品信息准确性。
### 关键实验
离线在PCG-Bench、PCI-Bench两个创意生成基准上，所有指标全面优于SOTA；线上在快手广告场景A/B测试，相比检索式DLRM baseline，CTR提升4.88%、CVR提升4.01%、ARPU提升12.89%；相比生成式检索GRM baseline，CTR提升2.87%、CVR提升2.74%、ARPU提升9.85%。
### 核心结论
从检索固定创意池到动态生成个性化创意的范式升级，能够释放检索式系统无法触及的商业价值，是广告推荐系统下一个重要的增长来源
