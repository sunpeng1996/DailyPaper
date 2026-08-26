---
title: 'CAFE: Self-Improving Search Agents Need Co-Evolving Feedback'
title_zh: CAFE：自进化搜索智能体需要协同进化的反馈机制
authors:
- Boyang Liu
- Senjie Jin
- Peixin Wang
- Zhangyue Yin
- Yibo Wang
- Yuhao Zhou
- Xinbing Liang
- Shizheng Zhu
- Yuhui Wang
- Jingqi Tong
affiliations:
- Fudan University
- Tencent
arxiv_id: '2608.24794'
url: https://arxiv.org/abs/2608.24794
pdf_url: https://arxiv.org/pdf/2608.24794
published: '2026-08-24'
collected: '2026-08-26'
category: Agent
direction: 搜索Agent · 自进化反馈协同优化
tags:
- SearchAgent
- Co-Evolution
- ReinforcementLearning
- DPO
- FeedbackMechanism
one_liner: 提出共享参数的Agent-反馈协同进化框架，提升搜索智能体性能并降低答案幻觉
practical_value: '- 电商导购/商品搜索Agent可直接复用CFE+反馈感知优势重塑的RL训练逻辑，让Agent主动识别搜索路径错误并请求反馈，降低长链路复杂查询（如多属性商品筛选）的失效概率

  - 共享参数的Agent-Critic双角色设计可复用，无需单独训练反馈模型降低工程成本；RDPO从实时业务rollout中挖掘前缀匹配的正负反馈对，让反馈机制随业务数据迭代，避免静态反馈过时

  - 失败轨迹保留错误前缀+插入反馈+成功续跑的SFT数据构造方法可直接复用，无需大量人工标注纠错样本，用线上失败case即可训练Agent的错误修复能力

  - 交替在线Agent RL优化、离线Critic更新的协同迭代策略，比单独优化任意一方收益更高，适合业务中需持续迭代的Agent系统'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有结果监督的搜索Agent仅靠终端奖励无法定位中间步骤错误，长链路搜索中早期错误会持续累积导致最终失效；静态反馈机制无法适配Agent进化后变化的错误分布，最终会出现性能瓶颈，同时结果 hallucination 问题难以缓解。

### 方法关键点
- 共享参数双角色模型：同一模型通过角色标识切换Agent和Critic功能，Agent动作空间新增`<request_feedback>`触发动作，Critic基于当前轨迹生成纠错反馈
- 初始化SFT数据构造：收集Base Agent失败轨迹，保留错误前缀，插入反馈请求、教师生成的纠错反馈和成功续跑路径，训练基础的反馈请求/生成/使用能力
- 在线RL优化：① 对比反馈估计（CFE）：同Prompt下对比请求/不请求反馈的成功率差，给请求动作分配额外奖励，惩罚重复请求；② 反馈感知优势重塑：将轨迹按首次反馈请求切分，降低错误前缀奖励权重，提升反馈后正确续跑的奖励权重，解决credit分配错位问题
- 离线迭代优化：Rollout-derived DPO（RDPO）：从最新在线轨迹中挖掘前缀匹配的成功/失败反馈对，用DPO更新Critic，每次迭代交替做在线Agent优化和离线Critic更新，实现两者协同进化

### 关键实验
在7个SearchQA基准（含6个跨域数据集）上测试，7B Qwen2.5 backbone下平均EM 52.5、F1 60.7，比最强RL基线IGPO高2.1 EM、1.3 F1，跨域收益稳定；答案级幻觉率从GRPO的17.6%降至12.6%；3B参数版本性能追平部分7B搜索模型。

### 核心结论
自进化智能体的反馈机制必须和其策略同步进化，固定的监督器无法适配Agent变化的错误分布。
