---
title: 'EnvOS: Auditing Computer-Use Agents When the World Moves On : Phenomenon-Based
  Task Construction, Certification, and Evidence-Based Evaluation'
title_zh: EnvOS：动态环境下计算机使用Agent的可审计评估框架
authors:
- Ankush Kadu
- Athira Gopal
- Niharika Singh
- Arpit Jain
- Aswanth Krishnan
affiliations:
- QpiAI, Bangalore, India
arxiv_id: '2610.40246'
url: https://arxiv.org/abs/2610.40246
pdf_url: https://arxiv.org/pdf/2610.40246
published: '2026-10-29'
collected: '2026-10-30'
category: Agent
direction: Agent 动态环境可审计评估
tags:
- Agent Evaluation
- Dynamic Environment
- Audit
- LLM Agent
- Benchmark
one_liner: 提出面向动态环境的Agent评估框架EnvOS，覆盖任务构建、预认证、可审计全流程
practical_value: '- 电商/广告场景的自动化Agent（客服工单处理、活动规则执行、库存调整Agent）评估时，可直接复用EnvOS的预认证流程，先验证环境变更的有效性、任务可解性，避免把环境配置错误、规则未生效等问题归因到Agent决策能力上

  - 对于需要感知实时数据变化的业务Agent（价格调整后的下单Agent、优惠券发放规则变更后的审核Agent），可采用「环境状态变更与观测通道分离」的设计，避免把系统提示和真实数据变更混淆，同时在决策前主动透出最新状态数据，可大幅提升Agent准确率（实验中最高提升93.75%）

  - 做Agent效果评估或RL训练奖励校验时，可复用EnvOS的全链路日志留存+独立校验机制，单独开发两套校验逻辑对结果做交叉验证，避免评估偏差或错误奖励信号影响训练效果

  - 业务侧的规则变更效果实验可借鉴其配对对照设计，保持真实规则变更一致，仅调整给Agent/运营人员的提示信息，可精准量化提示策略对决策效果的提升幅度'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前LLM驱动的计算机使用Agent运行在持续变化的软件环境中，预约调整、政策更新、库存变动等事件随时可能发生，而现有评估体系默认环境状态在任务周期内固定，一旦Agent出现失败，无法准确归因是Agent决策能力不足、环境变更未按预期触发、Agent未收到更新通知，还是评分逻辑出错；若将这类有偏评估数据用于RL训练，还会直接产生错误奖励信号，影响Agent训练效果。

### 方法关键点
- 现象-扰动抽象设计：将独立于应用的环境状态变更（现象）和给Agent的观测披露通道完全分离，扰动实例包含状态操作符、触发条件、观测披露规则、单次触发保障四个模块，避免将给Agent的通知等同于真实环境变更
- 预运行认证机制：Agent执行前先对候选任务做5项校验：环境变更触发符合预期、观测披露与真实状态一致、任务存在可解路径、可区分正确/错误行为、评分器可准确识别正负例，仅通过校验的任务才可进入评估
- 可审计评估流程：全链路留存环境事件、Agent侧观测、动作序列、最终提交状态，执行后先校验单轮episode的有效性，再基于权威状态评分，支持独立代码二次校验结果，同时支持故意篡改数据的对抗挑战测试

### 关键实验
基于诊所预约、保险理赔两个业务场景测试，对比不同信息披露策略下的Agent表现：①诊所预约场景，Claude Opus 5无额外信息时准确率0/16，仅给出校验提醒+源链接时2/16，直接展示更新后地址时准确率升至15/16，提升统计显著（p=0.00293）；②保险理赔场景，Claude Sonnet 5无额外政策提示时准确率1/10，决策前重新展示当前政策时升至9/10；③评估器鲁棒性测试中，EnvOS对26个故意篡改的无效episode全部识别，对外来39个问题样本识别出25个错误，远高于简单日志校验的4个。

### 核心结论
Agent评估的可信度不止来自最终结果的正确性，更依赖环境变更、观测传递、评分逻辑全链路的可验证性，任何一环的漏洞都会导致结果归因完全失效。
