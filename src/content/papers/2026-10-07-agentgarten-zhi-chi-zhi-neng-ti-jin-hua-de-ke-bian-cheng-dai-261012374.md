---
title: 'AgentGarten: Code Worlds for Evolving Agents'
title_zh: AgentGarten：支持智能体进化的可编程代码世界框架
authors:
- Jiawei Chi
- Shangchen Miao
- Zhiyuan Shi
- Kailu Wu
- Hanyang Wang
- Weiliang Chen
- Qiyu Dai
- Jinshan Ren
- Jun Gao
- Mingsheng Long
affiliations:
- MirroS
- Tsinghua University
- Peking University
arxiv_id: '2610.12374'
url: https://arxiv.org/abs/2610.12374
pdf_url: https://arxiv.org/pdf/2610.12374
published: '2026-10-07'
collected: '2026-10-09'
category: Agent
direction: Agent 交互式进化环境构建
tags:
- Agent_Evolution
- Neural_Rendering
- Interactive_Environment
- Playbook_Learning
- Adversarial_Forcing
one_liner: 结合仿真引擎与神经渲染器构建可编程代码世界，支撑预训练Agent快速迭代交互能力
practical_value: '- 做Agent交互式训练的业务可复用playbook迭代范式：将每轮交互经验沉淀为结构化Markdown技能文档，新Agent直接继承复用，大幅降低重复探索成本，适合导购Agent、客服Agent的场景化能力迭代

  - 多模态生成场景可借鉴Adversarial Forcing训练方法：通过精确重放保留历史梯度、加入真实数据对抗监督，解决长序列生成的画质退化问题，可迁移到商品短视频生成、虚拟直播间渲染等业务

  - 工程侧可复用低延迟推理优化方案：自定义Triton核融合算子、CUDA图捕获重放、轻量蒸馏解码器组合，将单GPU端到端视频生成延迟压到400ms级，适合实时交互类生成业务落地'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent训练环境存在核心权衡：仿真/游戏引擎状态可控、规则可编程，但3D资产制作成本高，新场景定制门槛高；视频世界模型能生成丰富视觉输出，但状态与规则隐式化，无法直接编辑调试，难以支撑Agent长期稳定进化，亟需同时兼顾状态保真、视觉真实、可灵活扩展的环境框架。

### 方法关键点
- 框架分层解耦：上层可编程仿真引擎维护世界状态、执行交互规则，仅输出深度/表面法向量等结构化几何条件；下层共享神经渲染器统一将几何条件、外观参考、文本描述转换为Agent视觉观测，新场景仅需编写逻辑代码无需定制视觉资产
- 提出Adversarial Forcing蒸馏策略：块级精确重放实现历史编码梯度回传，避免全差分rollout内存开销；加入真实数据对抗损失与免双反向的精确R1/R2正则，解决长序列渲染画质退化问题
- Agent迭代范式：Agent仅通过视觉观测感知环境，每轮交互后将经验沉淀为playbook技能文档，后续轮次Agent直接继承优化，无需从零训练

### 关键结果
- 渲染性能：单H100 GPU实现480×832分辨率36.5帧/秒实时渲染，端到端每16帧块延迟仅438.8ms；块级重放对比SGF方案相对L2误差降至0（比特级一致），前向速度提升5.4%
- Agent效率：躲猫猫任务中仅4轮迭代出现搭建掩体策略，10轮出现坡道使用策略，对比传统自play RL的2500万、1亿轮次训练成本下降6个数量级；另外4个测试场景经过4轮迭代后性能均提升30%以上

**最值得记住的一句话**：Agent的能力上限由其训练环境的边界决定，将环境状态与渲染解耦的可编程代码世界，是支撑预训练Agent持续闭环进化的关键基础设施
