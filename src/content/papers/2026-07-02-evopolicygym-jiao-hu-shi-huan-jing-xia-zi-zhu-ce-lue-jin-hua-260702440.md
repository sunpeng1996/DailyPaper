---
title: 'EvoPolicyGym: Evaluating Autonomous Policy Evolution in Interactive Environments'
title_zh: EvoPolicyGym：交互式环境下自主策略进化评估基准
authors:
- Zhilin Wang
- Han Song
- Runzhe Zhan
- Jusen Du
- Jiacheng Chen
- Tianle Li
- Qingyu Yin
- Yulun Wu
- Zhennan Shen
- Tong Zhu
affiliations:
- University of Science and Technology of China
- The Chinese University of Hong Kong
- University of Macau
- Tsinghua University
- Shanghai Jiao Tong University
arxiv_id: '2607.02440'
url: https://arxiv.org/abs/2607.02440
pdf_url: https://arxiv.org/pdf/2607.02440
published: '2026-07-02'
collected: '2026-07-03'
category: Agent
direction: Agent 自主策略进化评估基准
tags:
- Autonomous Agent
- Policy Evolution
- Benchmark
- Reinforcement Learning
- LLM Agent
one_liner: 推出面向自主进化Agent的受控评估基准EvoPolicyGym，支持轨迹级诊断与跨环境能力评测
practical_value: '- 做Agent迭代优化评估时，可参考其「固定交互预算+可见训练反馈+隐藏验证/测试集」的评估范式，避免过拟合可见反馈、优化过程不可追溯的问题

  - 针对电商推荐/广告策略的自主迭代场景，可复用其「结构合成+参数调优」的二分诊断框架，区分策略优化是缺合适结构还是参数调优不到位，定位迭代瓶颈

  - 开发自进化推荐Agent时，可借鉴其轨迹级分析方法，追踪每轮交互反馈到策略修改的链路，量化预算分配效率，减少无效迭代消耗'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有自主Agent评估大多仅输出最终得分，无法区分盲目重试、过拟合可见反馈、未做验证等轨迹级失效模式，开放式工程任务又存在规格迭代、代码维护等干扰变量，缺少受控环境来单独衡量Agent将有限环境反馈转化为可泛化可执行策略的核心能力。
### 方法关键点
- 提出「自主策略进化」评估范式：Agent在固定交互预算约束下反复编辑可执行策略系统，仅能获取训练阶段的沙箱rollout反馈，验证、测试集完全对Agent隐藏，最终以隐藏验证集选出的最优checkpoint在测试集的表现作为最终得分
- 推出EvoPolicyGym基准：内置Core16环境集，覆盖控制、导航、驾驶、机器人4大类16个Gymnasium兼容场景，支持全轨迹记录，可诊断Agent的反馈利用率、预算分配效率、泛化能力
- 设计双维度分析框架：区分结构合成（新增感知、规划、记忆等控制逻辑）和参数调优（调整常量、阈值）两种优化模式，可定位Agent进化的核心瓶颈
### 关键结果
在128 episode固定交互预算下，对比4款主流大模型Agent的表现：GPT-5.5以0.891的综合排名得分位列第一，拿下9个场景第一、全部16个场景前二；Claude Opus 4.7综合得分0.750位列第二，在MiniGrid类符号规划场景表现最优；其余两款Agent仅各拿下1个场景第一，跨场景稳定性远低于头部模型。
最值得记住的一句话：强自主策略进化能力不仅要求单任务获胜，更需要能发掘适配任务的机制、在有限反馈下持续迭代优化出可泛化的策略。
