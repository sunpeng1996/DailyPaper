---
title: 'GTAGym: Real AAA Game Tasks Environment for Evaluation and Reinforcement Learning'
title_zh: GTAGym：基于GTA V真实AAA游戏任务的智能体评估与RL环境
authors:
- Jiajun Chen
- Shicheng Fang
- Jiahao Lu
- Yuxin Wang
- Xipeng Qiu
affiliations:
- Shanghai Innovation Institute
- Fudan University
arxiv_id: '2611.13028'
url: https://arxiv.org/abs/2611.13028
pdf_url: https://arxiv.org/pdf/2611.13028
published: '2026-11-08'
collected: '2026-11-12'
category: Agent
direction: 多模态智能体 · 游戏场景评估与RL训练
tags:
- Embodied Agent
- Benchmark
- Reinforcement Learning
- Multimodal LLM
- LoRA
one_liner: 开源GTA V衍生的AAA游戏任务基准与环境，支持多模态智能体自动评估与强化学习训练
practical_value: '- 复杂交互任务自动评估方案可迁移至电商导购/客服Agent：将任务成功条件拆解为可量化的状态谓词，无需人工标注即可自动校验任务完成度，大幅降低评测成本

  - 模板化批量任务生成思路可复用：固定场景规则+采样可变参数批量生成训练/测试样本，可用于推荐系统冷启动样本构造、Agent仿真测试用例批量生成

  - LoRA RL低成本迭代方案可参考：在同领域生成样本上做LoRA微调，不仅提升域内效果还可跨域迁移到原生业务任务，避免全量微调的高成本

  - 动态交互任务延迟优化结论可落地：推理延迟超过任务响应窗口会导致效果暴跌，可指导实时交互Agent（如直播助手、实时导购）的工程优化，优先保障响应速度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有AAA游戏场景的智能体评估多依赖人工标注，缺乏自动任务结果校验能力，也没有可批量生成的标准化RL训练环境，无法支撑多模态具身智能体的能力迭代与横向效果对比。

### 方法关键点
- 构建GTAVBench基准，包含103个3D交互任务（覆盖导航、载具控制、动态交互9大类）+47个图像类射击狙击任务，共150个真实GTA V主线衍生任务
- 支持两种评估模式：普通模式提供文本指令，GTAVBench-AGI模式仅在首屏截图展示指令，自动压缩交互上下文，更贴近真实场景交互逻辑
- 内置模板化RL环境生成器，支持用户自定义参数范围批量生成带自动reward与终止信号的训练任务
- 统一键鼠+截图交互接口，支持并行测试，直接通过引擎状态自动校验任务结果，无需人工标注

### 关键结果
- 测试6款前沿多模态大模型，最优配置（GPT-6-Astra+Codex harness）在GTAVBench-AGI上总体准确率达70.9%，较人类水平89.8%低18.9个百分点，空中导航、规避、拦截类任务仍存在明显瓶颈
- 基于生成的步行导航任务对Qwen3.8-27B做LoRA RL微调，域内准确率从54.2%提升至72.9%，跨域任务准确率从31.8%升至34.8%，原生GTA V任务准确率从15%升至23%

### 核心结论
动态交互任务的核心瓶颈不是感知或规划能力，而是动作校准与持续调节能力，推理延迟超过任务响应窗口会直接导致效果暴跌。
