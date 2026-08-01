---
title: 'VideoCoCo: Code-as-CoT for Physically-Consistent Video Generation via an Agentic
  Dual-Engine System'
title_zh: VideoCoCo：基于代码级CoT的双引擎智能体物理一致性视频生成框架
authors:
- Haodong Li
- Tianfei Ren
- Xiaoxiao Ma
- Chunmei Qing
- Zhen Fang
- Sipeng He
- Ziyu Guo
- Haoyu Wu
- Juanxi Tian
- Yihang Zou
affiliations:
- CUHK
- USTC
- SCUT
- HKU
- NTU
arxiv_id: '2607.27380'
url: https://arxiv.org/abs/2607.27380
pdf_url: https://arxiv.org/pdf/2607.27380
published: '2026-07-28'
collected: '2026-08-01'
category: Agent
direction: 智能体文生视频 · 代码级CoT
tags:
- Agent
- Chain-of-Thought
- Text-to-Video
- Controllable Generation
- Code Generation
one_liner: 提出以可执行Blender代码为过程级CoT的双引擎智能体框架，提升文生视频的物理一致性
practical_value: '- 可复用「可执行代码作为过程级CoT」思路，在电商商品3D展示视频生成场景中，先输出Blender脚本控制商品运动/灯光参数，再生成高清视频，保证展示逻辑合规

  - 双引擎解耦架构可迁移到Agent任务拆分场景：将逻辑推理（如生成动作脚本）和效果生成（如渲染高清内容）分离，降低端到端生成的错误率

  - 针对特定领域生成任务，可构造「草稿-指令-目标」三元组微调生成模型，适配前置模拟输出的低质量草稿，提升最终生成效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有文生视频模型视觉质量已达较高水平，但物理一致性表现较差，传统CoT引入的中间表示多不可执行或时间稀疏，无法完整控制场景时空演化过程。
### 方法关键点
- 采用可执行Blender代码作为过程级CoT，双引擎架构解耦过程推理与高保真渲染
- 编码智能体根据文本prompt生成显式定义场景及时空演化的Blender程序，模拟引擎运行输出确定性时空草稿
- 生成式视频引擎基于草稿做条件编辑生成写实视频，配套构造VideoCoCo-3K三元组数据集适配该编辑任务
### 关键结果
PhyGenBench指标较OmniWeaving基线从0.475提升至0.558，VBench-2.0指标从52.18提升至77.88，两个基准均取得最优平均得分。
