---
title: Why Are GUI Agents Correct but Late? Decode on the Decision-Time Critical Path,
  Tested with Pre-Compiled Policy Trees
title_zh: 自适应预期策略树：消除GUI Agent决策关键路径的解码延迟
authors:
- Zihan Dong
- Rui Qian
- Qishi Zhan
- Dongshen Peng
- Kaixin Li
- Yu Li
affiliations:
- Georgia Institute of Technology
- Fudan University
- Marquette University
- University of North Carolina at Chapel Hill
- National University of Singapore
arxiv_id: '2607.28399'
url: https://arxiv.org/abs/2607.28399
pdf_url: https://arxiv.org/pdf/2607.28399
published: '2026-07-30'
collected: '2026-07-31'
category: Agent
direction: GUI Agent 低延迟决策优化
tags:
- GUI Agent
- Low Latency
- Policy Tree
- Critical Path Optimization
- Pre-compilation
one_liner: 通过空闲期预编译条件策略树，无模型修改将GUI Agent短窗口成功率从0.5提升到0.79
practical_value: '- 电商/广告端的短生命周期交互场景（比如限时弹窗、直播互动提示、自动消失的优惠提醒）可复用预编译思路：提前枚举所有候选响应动作，事件触发时仅做轻量特征匹配，避免关键路径调用大模型，大幅降低响应延迟

  - 工程层面可复用关键路径拆分逻辑：将大模型的重计算任务（如动作生成、规则推导）移到用户行为空闲期（如商品浏览间隙、页面加载期）预执行，仅将最低成本的匹配/分类逻辑留在请求关键路径

  - 预生成动作的校验逻辑可直接复用：给预生成动作加生效有效期、置信度阈值、动作白名单三层校验，匹配失败自动fallback到常规响应流程，完全避免错误动作'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有GUI Agent采用感知-推理-执行闭环，事件触发后才调用多模态大模型做自回归解码，推理延迟通常达数百毫秒，经常错过仅存在数百毫秒的短窗口交互场景（如自动消失的弹窗、临时验证请求、短时效交互提示），现有提前预测方案依然将大模型推理放在决策关键路径上，无法从根源解决延迟问题。

### 方法关键点
- 提出Adaptive Anticipatory Policy Trees (AAPT)，无需修改底座模型，仅在界面空闲期用同一冻结多模态模型预编译扁平结构的条件策略树，每个分支包含可观测触发条件、预授权动作、有效期、置信度，树的大小刚好覆盖模型自身的解码延迟
- 事件触发时仅运行轻量观察者模块，将变化帧和预存分支的触发条件做匹配，直接执行对应预授权动作，决策关键路径无大模型生成逻辑
- 匹配失败、超时、置信度不足时自动fallback到常规重推理流程，避免产生错误动作

### 关键结果
在毫秒级可控的短窗口GUI基准上对比反应式、开环、预测重规划三类baseline，600-650ms竞争窗口下，AAPT将成功率从反应式baseline的0.50提升到0.79（p=1.8×10^-3），全程无错误动作；跨通用多模态模型的126组验证实验中，成功率从0.341提升到0.778（p=4.9×10^-13）；外部基准测试显示AAPT仅在候选动作可提前枚举的场景下有优势，和反应式方案能力互补。

### 核心结论
Agent的响应失败很多时候是调度问题而非推理能力问题，把大模型生成逻辑从决策关键路径移走，能在不提升模型能力的前提下大幅提升短窗口场景的成功率。
