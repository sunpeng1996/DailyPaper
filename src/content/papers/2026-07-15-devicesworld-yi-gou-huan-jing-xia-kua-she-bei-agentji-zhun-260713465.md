---
title: 'DevicesWorld: Benchmarking Cross-Device Agents in Heterogeneous Environments'
title_zh: 《DevicesWorld：异构环境下跨设备Agent基准测试套件》
authors:
- Huatao Li
- Xinwei Geng
- Yuheng Wang
- Yutong Li
- Runde Yang
- Hantao Chen
- Shu Yao
- Jingru Fan
- Xuhui Ren
- Yuanyuan Zhao
affiliations:
- Shanghai Jiao Tong University
- Honor Device Co., Ltd
arxiv_id: '2607.13465'
url: https://arxiv.org/abs/2607.13465
pdf_url: https://arxiv.org/pdf/2607.13465
published: '2026-07-15'
collected: '2026-07-16'
category: Agent
direction: 跨设备Agent协作能力基准评测
tags:
- Cross-Device-Agent
- Agent-Benchmark
- LLM-Agent
- Heterogeneous-Environment
- Task-Execution
one_liner: 提出覆盖移动端、桌面端、IoT三类设备的6140个可执行跨设备Agent任务基准及统一评测框架
practical_value: '- 跨端/跨场景Agent评测可复用这套多阶段任务构建+规则化状态核验的设计思路，比如电商跨App（淘宝/支付宝/闲鱼）、跨端（手机/PC/智能音箱）导购Agent的评测，直接套用任务定义、环境初始化、动作路由、状态校验的全流程即可落地。

  - 跨端Agent的问题排查可复用其两类终止模式+8种错误分类的归因维度，快速定位问题是源信息获取失败、设备角色混淆、子目标遗漏还是全局校验缺失，大幅降低调试成本。

  - 跨多系统Agent架构设计必须显式维护全局任务状态（各设备角色、已获取信息来源、已完成子目标、待满足全端校验条件），不能仅依赖对话历史上下文，可有效减少写错设备、漏任务的问题。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent基准均聚焦单设备场景（手机/桌面/智能家居单独评测），但真实用户任务往往需要跨异构设备流转，比如从手机取验证码、电脑填表单、IoT设备执行控制，当前没有可复现、可自动校验的跨设备Agent评测基准，无法系统性评估模型跨设备信息整合、任务调度的能力。

### 方法关键点
- 统一适配三类异构设备环境：基于AndroidWorld实现移动端交互、基于OSWorld实现桌面端交互、自研智能家居IoT仿真环境，支持设备状态初始化、动作路由、状态更新、结果自动校验、环境重置全流程；
- 构建6140个可执行跨设备任务，覆盖单类设备内跨实例、两类设备跨端、三类设备联合任务，单任务最多涉及4个设备实例，所有任务经过多阶段设计、语义审核、运行时测试、校验对齐，符合真实用户需求且可自动核验；
- 定义两级评估指标：严格任务成功率（所有校验条件全部满足才计数）、平均得分（按满足的校验点比例计算），同时支持轨迹级失败归因分析。

### 关键实验
在分层抽样的固定评测集上对比5个前沿Agent方案：GPT-5.5、Qwen3.7-Plus、Gemini-3.1-Pro-Preview、Claude Opus 4.8、UFO3，最优方案UFO3的成功率仅12.5%，28.7%的失败任务满足至少1个校验条件但未完成全任务，涉及三类设备联合的任务无一个方案能成功完成。

**最值得记住的一句话**：跨设备Agent的核心瓶颈不是单设备操作能力，而是能否持续维护全局任务状态，局部操作成功不代表端到端跨设备任务完成。
