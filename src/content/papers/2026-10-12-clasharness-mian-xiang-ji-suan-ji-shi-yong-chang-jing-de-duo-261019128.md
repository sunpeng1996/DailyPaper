---
title: 'CLASHarness: Benchmarking Multi-Agent Conflict in Computer Use via a Controllable
  and Verifiable Generation Pipeline'
title_zh: CLASHarness：面向计算机使用场景的多智能体冲突基准框架
authors:
- Yuxiang Lai
- Jike Zhong
- Chengzhi Liu
- Ming Li
- Haonan Wang
- Xiaofeng Yang
- Liang Zhao
- Youbao Tang
- Ruixi Fan
affiliations:
- Google
- Emory University
- University of Southern California
- University of Florida
- University of Chicago
arxiv_id: '2610.19128'
url: https://arxiv.org/abs/2610.19128
pdf_url: https://arxiv.org/pdf/2610.19128
published: '2026-10-12'
collected: '2026-10-16'
category: MultiAgent
direction: 多智能体协作 · 冲突处理能力评测
tags:
- Multi-Agent
- Benchmark
- Conflict Resolution
- Computer Use
- VLM
one_liner: 提出可控可验证的多智能体冲突场景生成框架，配套600项任务基准，揭示3项核心能力瓶颈
practical_value: '- 电商/广告多Agent协作流程可强制加入「操作前校验系统状态+操作后释放共享锁/交接任务」的标准化步骤，可降低超58%的收尾操作失败率

  - 业务场景的Agent评测可复用8步微生成管道+参考轨迹编译打分器的设计，无需人工编写评测规则，保证生成任务100%可解，大幅降低评测集构建成本

  - 跨部门协同类Agent（如大促活动多角色Agent）可引入「系统/视觉证据优先级高于子Agent文本报告」的规则，避免弱模型盲目信任错误输出导致的资损'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多智能体基准默认协作环境信息一致，无法覆盖真实场景中子Agent输出过时状态、矛盾指令、争抢共享资源的冲突解决能力评测；手动构造任务成本高无法规模化，无约束LLM生成任务易出现叙事漂移、答案泄露、无解问题，亟需可扩展的可控冲突场景生成方案。
### 方法关键点
- 分层分阶段合成架构：拆解为全局多智能体世界构建、3-4轮分阶段规划+单轮8步微生成、生成后一致性校验三层，避免上下文溢出和叙事漂移
- 多模态预承诺机制：预先确定决定性事实后再渲染视觉资产，346项任务的关键事实仅出现在视觉内容中无文本泄露，强制Agent进行视觉校验
- 可验证打分机制：从执行的参考轨迹直接编译混合代码+语义打分器，保证所有任务100%可解；语义评测采用3样本自一致性投票，评委一致性达97.5%
### 关键结果
- 构建覆盖20个领域的600项多轮冲突任务基准，含7970个视觉资产、3760个混合校验器
- 测试15个前沿模型，最高GPT-6 Astra整体通过率仅28.7%；主动解决冲突相比仅检测冲突通过率下降17.1pp，所有模型收尾协调操作（释放锁、任务交接）失败率超58%
- 弱模型易盲目信任子Agent错误文本输出，强模型会主动校验视觉证据；增加测试时推理计算对冲突任务收益极低，甚至会导致模型陷入思考循环降低性能

多智能体系统的核心瓶颈不是冲突检测能力，而是冲突后的状态修复能力与标准化协调协议的执行能力
