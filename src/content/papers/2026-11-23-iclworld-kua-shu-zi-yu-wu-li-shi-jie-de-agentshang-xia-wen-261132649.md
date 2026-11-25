---
title: 'ICLWorld: Benchmarking In-Context Learning of Agents from Digital to Physical
  Worlds'
title_zh: ICLWorld：跨数字与物理世界的Agent上下文学习基准
authors:
- Qingle Liu
- Jieming Li
- Pei-lin Li
- Shenghan Zheng
- Ruize Yang
- Sunqi Fan
- Deyao Hong
- Huan-ang Gao
- Meng-Hao Guo
- Shuojin Yang
affiliations:
- Tsinghua University
arxiv_id: '2611.32649'
url: https://arxiv.org/abs/2611.32649
pdf_url: https://arxiv.org/pdf/2611.32649
published: '2026-11-23'
collected: '2026-11-25'
category: Agent
direction: Agent 上下文学习能力评估
tags:
- ICL
- Agent Benchmark
- Embodied Agent
- Computer Use
- Robot Use
one_liner: 提出跨数字与物理世界的无泄漏Agent ICL基准与统一交互框架UIverse
practical_value: '- 电商/办公自定义规则类Agent开发时，可复用多版本反常识规则的测试方案，验证Agent是否真的遵循用户个性化需求，而非输出预训练先验的默认结果，降低指令违背风险

  - 跨数字/物理场景的Agent（如同时操作电商后台与线下仓储设备的履约Agent）可借鉴UIverse的统一GUI交互层设计，无需为不同域单独适配接口，降低多场景Agent的开发与适配成本

  - 评估Agent ICL能力时，不能仅测单规则、演示复现场景，需增加跨环境泛化、规则理解与执行对齐的测试维度，避免高估实际落地效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent In-Context Learning（ICL）基准多为离线设计，依赖文本/静态图像输入，易存在训练数据泄露问题，且无法区分Agent是遵循给定规则还是依赖预训练先验输出结果；同时缺乏统一框架同时评估数字域（计算机操作）与物理域（机器人操作）的Agent ICL能力，无法衡量ICL能力的跨域迁移效果。
### 方法关键点
- 构建160个无泄露任务，包含110个计算机操作任务、50个机器人桌面操作任务，每个任务配3个反常识规则版本，无规则时成功率极低，确保任务必须依赖上下文学习才能完成
- 配套UIverse统一交互层，将Web应用、操作系统桌面、机器人仿真环境都封装为图形界面，Agent通过统一的观察、操作、查看演示、结束四类工具和所有环境交互
- 评估维度覆盖3种规则模态（无规则/文本/视频）、3种泛化层级（复现演示/同环境新实例/跨环境迁移），新增规则QA环节区分规则理解与执行能力
### 关键实验
在6个前沿大模型（Claude Opus 5.5、GPT-6 Astra、Qwen3.8-Max等）上测试：最强模型Claude Opus 5.5数字域任务成功率82%，物理域仅27%；GPT-6 Astra物理域规则QA正确率达98%但对应任务成功率仅20%；弱模型依赖文本规则，演示复现场景的成功多为动作照搬，跨实例后视频规则成功率下降29.5个百分点。
### 核心结论
Agent识别规则的能力远不等于执行能力，物理域落地、跨环境泛化、多规则鲁棒性是当前Agent ICL落地的核心瓶颈。
