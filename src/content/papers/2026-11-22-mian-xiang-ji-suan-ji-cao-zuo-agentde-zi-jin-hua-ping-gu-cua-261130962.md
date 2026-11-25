---
title: Self-Evolving Evaluation Environments for Computer-Use Agents
title_zh: 面向计算机操作Agent的自进化评估环境CUA-SEE
authors:
- Wenhao Wang
- Panrong Tong
- Quyu Kong
- Pengxiang Li
- Haowen Yang
- chenglin Cai
- Siheng Chen
- Yue Wang
affiliations:
- Alibaba Group
- Zhejiang University
- Shanghai Jiao Tong University
arxiv_id: '2611.30962'
url: https://arxiv.org/abs/2611.30962
pdf_url: https://arxiv.org/pdf/2611.30962
published: '2026-11-22'
collected: '2026-11-25'
category: Agent
direction: Agent 自进化评估框架设计
tags:
- Agent-Evaluation
- Self-Evolving-Benchmark
- Computer-Use-Agent
- Dynamic-Verification
- Closed-Loop-Eval
one_liner: 提出与计算机操作Agent能力协同进化的闭环评估框架，解决静态benchmark鉴别力不足问题
practical_value: '- 电商导购Agent、店铺运营Agent的评估可复用这套闭环进化逻辑：先基于现有任务集跑Agent轨迹，用群体表现校准任务难度，再动态生成边界探针任务，避免静态用例快速饱和导致评估失效

  - 可直接复用验证器进化的工程方案：将评估任务拆解为原子可验证checkpoint，通过pass agent与verifier agent的对抗交叉校验提升自动判分准确率，比人工编写评估规则效率提升数倍，且能适配动态迭代的任务集

  - 做Agent/生成式推荐能力迭代的团队可复用7维能力量化rubric（Scale Consistency、Precision Control等），拆解模型薄弱项，比单一通过率指标更能精准定位迭代方向，解决A/B测区分度不足的问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前计算机操作Agent（CUA）迭代速度极快，但主流评估benchmark均为静态人工构造，存在三大核心缺陷：难度天花板固定，Agent能力达标后分数饱和无法区分进阶差异；功能覆盖有限，现有OSWorld任务仅覆盖不到20%的软件功能；缺乏动态诊断能力，无法主动定位Agent新增的能力边界与泛化缺陷，亟需与Agent能力同步进化的评估体系。

### 方法关键点
- 闭环三模块协同进化架构：基准任务进化基于多Agent群体表现校准难度，同时扩展软件功能覆盖，保持任务普适性不偏向单个Agent的缺陷；
- 单Agent诊断模块：针对单个Agent的历史表现，在7维能力维度上自适应探测能力边界，大幅提升评估分辨率；
- 验证器动态进化：将动态任务拆解为基于软件原生状态的可执行checkpoint，通过pass agent与verifier agent的对抗交叉校验提升判分精度，避免静态校验规则失效。

### 关键实验结果
基于OSWorld的8个核心桌面应用，对比静态benchmark，CUA-SEE经过4轮进化后：5款SOTA CUA平均得分从60.6降至47.5，任务平均交互步长从27.4升至39.3，软件功能覆盖提升3.65倍，自动验证器与人工判分的一致性达84%，可精准定位不同Agent的能力差异。

> 最值得记住的一句话：静态评估体系永远追不上快速迭代的Agent能力，将任务、验证器、Agent轨迹形成闭环协同进化，是长期保持评估鉴别力的核心路径
