---
title: 'Blurring the Block Boundaries: Overlapping Block Denoising for Efficient Diffusion
  Language Models'
title_zh: 模糊块边界：面向扩散语言模型的重叠块去噪加速方法
authors:
- Amir Mann
- Jonathan Fhima
- Shaked Brody
- Or Avitan
- Asif Zamir
- Shahar Tsiper
- Niv Nayman
affiliations:
- Technion - Israel Institute of Technology
- Amazon Web Services
arxiv_id: '2611.14387'
url: https://arxiv.org/abs/2611.14387
pdf_url: https://arxiv.org/pdf/2611.14387
published: '2026-11-10'
collected: '2026-11-11'
category: LLM
direction: 扩散语言模型 · 推理加速优化
tags:
- Diffusion LLM
- Inference Acceleration
- Block Diffusion
- Training-free
- Hyperparameter-free
one_liner: 训练无超参的块重叠推理方法，为块扩散语言模型带来11.5-14.5%的生成提速且质量持平
practical_value: '- 业务中若使用块式扩散LLM做电商文案生成、推荐理由撰写，可直接集成B3，无需训练调参即可获得10%+推理提速，降本效果显著

  - 块边界算力浪费的分析思路可迁移到长文本生成、多轮Agent分块回复等场景，通过相邻块任务重叠并行提升GPU利用率

  - 动态自适应阈值设计可复用：无需针对不同任务/模型预调参数，通过在线统计生成过程的熵值自动校准触发条件，适配性强'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有块式扩散语言模型（DLM）的生成效率受块边界同步限制：每个块需等所有token收敛后才启动下一块，块收尾阶段40%的前向步骤仅产出17%的token，算力浪费严重；现有多块重叠优化方法需要针对模型/任务调超参，适配成本高。

### 方法关键点
- 推理阶段当前块收敛到一定程度时，提前初始化下一块，两个块共享同一次前向传播，注意力保持块因果性，不影响当前块预测结果
- 设计无超参的下一块触发条件：统计生成过程中生成边界推进时的前缀token最大熵，动态校准启动阈值，无需预调即可适配不同模型和任务
- 仅修改推理逻辑，无需重新训练模型，可无缝接入所有支持自编辑的块式DLM

### 关键实验结果
在DiffusionGemma 26B、LLaDA 2.1 mini 16B、LLaDA 2.1 flash 100B三个SOTA DLM上，覆盖10个数学、代码、推理类数据集，对比原生块解码、FlowBlock、MBD-LMs等基线：
1. 平均TPS提升11.5~14.5%，每轮前向传播产出token数提升15.9~19.4%，平均准确率波动仅为-0.4~+0.76pp，基本持平
2. 对比同类型多块重叠方法，在LLaDA 16B上比FlowBlock、MBD-LMs额外提效2%，准确率高1.7~2.1pp

### 核心结论
块式生成场景下的边界同步开销是易被忽略的算力浪费点，通过无超参的动态重叠调度可在无损质量前提下拿到可观的推理提速。
