---
title: 'Bridging Exploration and Persona: Information-Directed Dueling for Test-Time
  Agent Personalization'
title_zh: 面向LLM Agent测试时个性化的信息导向对决框架ID-TAP
authors:
- Jie Mao
- Pingchen Lu
- Xiangyi Wang
- Hengquan Huang
- Shuang Qiu
- Min Zhang
- Zhongxiang Dai
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- University of Copenhagen
- City University of Hong Kong
- East China Normal University
arxiv_id: '2610.24385'
url: https://arxiv.org/abs/2610.24385
pdf_url: https://arxiv.org/pdf/2610.24385
published: '2026-10-16'
collected: '2026-10-24'
category: Agent
direction: Agent测试时个性化 · 偏好反馈优化
tags:
- LLM Agent
- Test-Time Adaptation
- Dueling Bandit
- Preference Feedback
- Persona Optimization
one_liner: 提出双系统ID-TAP框架，仅需少量二元偏好反馈即可实现Agent测试阶段高效个性化适配
practical_value: '- 电商导购/客服Agent的实时个性化可直接复用ID-TAP框架：无需微调LLM权重，仅通过用户对2个响应的二元选择反馈，10轮内即可适配用户偏好，最终响应胜率比现有方案高4-7个百分点

  - 双系统架构设计可迁移到生成式推荐场景：全局神经效用模型复用跨query的历史偏好数据，轻量本地BT模型负责高效探索，算法更新仅占端到端延迟的7%-22%，完全满足实时交互要求

  - 跨query相似度加权warm start trick可直接用于搜索推荐冷启动：新query/新用户到来时，用历史相似query的偏好数据初始化统计模型，可将超过基线效果的反馈轮次从10轮压缩到4轮，大幅降低探索成本

  - Persona候选池构建方法可复用：从用户历史生成基础人设后，通过有限变异重扩增生成K个候选，既保证语义区分度又不偏离核心人设，近冗余率低于0.2%'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent个性化多依赖预设prompt或静态历史上下文，测试时无法快速适配用户当前query的动态偏好；用户偏好隐含噪声大，且persona候选空间大，传统bandit探索效率低，亟需无需微调LLM权重、仅用少量交互即可完成的测试时适配方案。
### 方法关键点
- 离线-在线架构：离线从用户历史生成K个persona候选池，在线每轮仅需用户对两个响应的二元偏好反馈，不改动LLM权重
- 双系统设计：全局query-conditioned神经效用模型学习跨query的persona效用得分，选出当前最优champion；query本地轻量Bradley-Terry(BT)统计模型计算候选挑战者的熵减增益，平衡探索与利用
- 信息导向挑战者选择：以「效用差平方/熵减增益」为指标选挑战者，同时偏好效用损失小、信息增益大的候选
- 跨query知识迁移：新query到来时，按与历史query的embedding相似度加权继承BT统计量做warm start，降低冷启动成本
### 关键结果
在7个基准数据集（LaMP/ LongLaMP/ PrefEval/ UltraChat）上对比PersonaAgent、POHF、PDO Sampling三类基线，10轮反馈限制下，平均归一化ROUGE-L达0.919（第二名0.852），平均响应胜率达83.6%（第二名79.3%）；仅需4轮反馈即可超过所有基线的最终效果，K=400候选时每轮算法更新仅需0.065-0.571s。
### 核心结论
测试时个性化无需微调LLM，结合对决bandit的双系统架构+跨query知识迁移，仅用少量二元偏好反馈即可实现远超现有方案的效果，同时满足实时性要求
