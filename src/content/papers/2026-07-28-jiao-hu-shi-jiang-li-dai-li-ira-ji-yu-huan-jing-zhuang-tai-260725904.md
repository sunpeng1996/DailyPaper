---
title: 'Interactive Reward Agent: GUI Task Evaluation via Environment-State Verification'
title_zh: 交互式奖励代理IRA：基于环境状态验证的GUI任务评估方法
authors:
- Chenrui Shi
- Yuwei Wu
- Yang Liu
- Ruining Feng
- Zirui Shang
- Zhi Gao
- Lifeng Fan
- Che Sun
affiliations:
- Beijing Institute of Technology
- Beijing Institute of General Artificial Intelligence (BIGAI)
- Shenzhen MSU-BIT University
- Tsinghua University
arxiv_id: '2607.25904'
url: https://arxiv.org/abs/2607.25904
pdf_url: https://arxiv.org/pdf/2607.25904
published: '2026-07-28'
collected: '2026-07-29'
category: Agent
direction: GUI Agent 评估与自动化奖励生成
tags:
- GUI Agent
- Reward Modeling
- Task Evaluation
- Propose-then-Verify
- Tool-Augmented LLM
one_liner: 提出基于propose-then-verify的交互式奖励代理，实现高准确率GUI任务评估并可作为RL训练奖励信号
practical_value: '- 做电商/运营类GUI Agent（比如后台批量改价、广告campaign创建Agent）的效果评估时，可复用propose-then-verify框架：先拆解原子化完成条件，再用工具主动校验后台数据、配置变更、生成文件等非可视化状态，避免纯VLM仅看截图的误判。

  - 给Agent RL训练做自动奖励标注时，可参考IRA的设计，把奖励判断从纯模型推理改成「条件拆解+跨源证据校验」，不需要为每个任务手工编写校验脚本，大幅降低规模化训练的标注成本。

  - 电商/广告后台的自动化任务巡检场景可直接复用分层工具设计：优先用命令执行、文件读取等结构化工具校验，最后才用GUI交互，兼顾评估准确率和执行效率。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有GUI任务评估方案存在明显缺陷：脚本式评估需要为每个任务人工编写校验规则，规模化成本极高；纯VLM评估仅能基于截图判断可视化状态，无法感知系统配置、文件内容、应用设置等隐藏状态，评估准确率低，无法作为可靠奖励信号支撑GUI Agent的规模化训练。

### 方法关键点
- 采用propose-then-verify框架：先基于任务指令和初始/最终截图，用VLM拆解成原子化的任务完成条件，不直接输出成败结论；
- 为每个条件设计ReAct风格的工具交互校验流程，配备三类工具：系统工具（读文件、执行命令、查配置）、应用专用工具（校验Office文档、浏览器配置等）、GUI交互工具，优先选择高可靠的结构化工具，GUI工具作为兜底；
- 所有条件校验完成后，按满足比例输出0~1的奖励值，超过0.8则判定为任务成功。

### 关键实验
- 构建了含321条Ubuntu桌面GUI任务轨迹的GUI-RewardBench，覆盖可见状态、隐藏状态、生成文件校验三类场景；
- 对比WebRL、ZeroGUI等4种纯VLM评估基线，IRA搭配GPT-5.5时准确率达86.9%，领先最强纯VLM基线8.1个百分点；
- 用IRA替代人工脚本作为RL训练的奖励信号，在OS-World上GUI Agent成功率达34.0%，仅比人工脚本方案的34.9%低0.9个百分点，可支撑无标注脚本的自动生成任务训练。

### 最值得记住的一句话
可靠的GUI奖励建模本质是证据校验问题，而非单纯的视觉分类问题。
