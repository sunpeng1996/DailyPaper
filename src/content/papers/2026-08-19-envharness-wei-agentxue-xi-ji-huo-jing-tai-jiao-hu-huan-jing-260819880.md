---
title: 'EnvHarness: Awakening Static Worlds for Agent Learning'
title_zh: EnvHarness：为Agent学习激活静态交互环境
authors:
- Chengsong Huang
- Zifeng Wang
- Rujun Han
- Jun Yan
- Yanfei Chen
- Zoey CuiZhu
- Ke Jiang
- Peng Xia
- Han Yu
- Yufan Zhuang
affiliations:
- Washington University in St. Louis
- Google Cloud AI Research
- Google Cloud
- University of North Carolina at Chapel Hill
arxiv_id: '2608.19880'
url: https://arxiv.org/abs/2608.19880
pdf_url: https://arxiv.org/pdf/2608.19880
published: '2026-08-19'
collected: '2026-08-21'
category: Agent
direction: Agent学习 · 动态适配训练环境生成
tags:
- EnvHarness
- Agent Learning
- Environment Customization
- Black-box Policy
- Co-evolution
one_liner: 提出静态环境可编程封装层EnvHarness，自动生成适配Agent弱点的定制训练环境
practical_value: '- 可复用EnvHarness的插件化封装思路，无需改动现有电商推荐/搜索仿真环境内核，快速生成针对模型弱点的定制训练场景（如针对推荐Agent长序列决策、冷门商品匹配短板调整初始状态、交互规则），大幅降低环境改造工程成本。

  - 可借鉴EnvRigger的黑盒诊断逻辑，无需获取LLM/推荐模型内部权重，仅通过轨迹分析即可定位模型缺陷、自动生成训练信号，适配业务中大量黑盒模型（第三方大模型、已上线排序模型）的迭代优化需求。

  - 电商Agent的RL训练可直接复用该框架的环境-策略共进化逻辑，相比盲目扩充训练样本，针对性调整环境难度可获得更高效率提升，实测减少9.8%交互步数即可取得更优效果，显著节约训练成本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent依赖交互环境获取训练信号，但现有环境多为人工构建的静态版本，无法适配Agent的能力变化，既不能针对性暴露Agent弱点，也会在Agent能力达标后失去训练价值；而现有自动环境生成方法要么领域绑定，要么生成的环境/验证器可靠性低，落地成本高。

### 方法关键点
- 提出EnvHarness可编程封装层，完全通过标准`reset/step`接口改造静态环境，不改动底层逻辑，保留原生验证器，包含三类可组合插件：Stage（调整任务初始状态）、Contract（修改动作/观测/转移规则）、Chain（拼接多环境实现长horizon任务）。
- 配套EnvRigger自动化流程，将目标策略视为黑盒，通过「观测执行轨迹→诊断缺陷→生成候选插件→新轨迹验证」的循环，自动生成适配当前策略弱点的定制化EnvHarness组件。

### 关键结果
在4个领域5个基准（ALFWorld、WebArena、SWE-bench Verified、OfficeQA、SpreadsheetBench）上验证，对比原生环境、领域专属环境生成基线：技能学习场景下OOD任务最高提升9.0个点，交互步数减少9.8%；RL场景下最高提升6.5个点；相同环境预算下，EnvHarness的策略-环境共进化效果远优于原生/生成环境的扩容效果，300个环境时SWE-bench上比原生环境高2.66个点，且仍保持增长趋势。

### 核心结论
与其从零构建新环境，不如通过标准化插件层封装现有静态环境，低成本实现环境与策略的共进化，是Agent训练提效的更优路径。
