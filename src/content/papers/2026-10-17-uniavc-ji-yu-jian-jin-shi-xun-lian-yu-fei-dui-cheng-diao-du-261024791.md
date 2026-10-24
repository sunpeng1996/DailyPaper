---
title: 'UniAVC: Unified Audio-Video Creation via Progressive Training and Asymmetric
  Scheduling'
title_zh: UniAVC：基于渐进式训练与非对称调度的统一音视频生成编辑
authors:
- Kien T. Pham
- Yuhao Liu
- Chong Hou Choi
- Zhenqi He
- Yanghao Wang
- Chenyang Lei
- Rui Liu
- Qifeng Chen
- Long Chen
affiliations:
- HKUST
- Huawei Research
arxiv_id: '2610.24791'
url: https://arxiv.org/abs/2610.24791
pdf_url: https://arxiv.org/pdf/2610.24791
published: '2026-10-17'
collected: '2026-10-24'
category: Multimodal
direction: 多模态音视频生成 · 跨模态耦合优化
tags:
- Multimodal Generation
- Diffusion Model
- Progressive Training
- Cross-Modal Learning
- Scheduling Optimization
one_liner: 提出渐进式训练+模态解耦非对称调度的统一音视频生成编辑框架，无需任务专属适配器
practical_value: '- 电商多模态素材生成场景可复用渐进式训练范式：先用足量单模态数据训练单分支基础能力，再用稀缺的跨模态配对数据优化耦合关系，大幅降低配对数据需求量

  - 跨模态生成调度可参考模态解耦非对称策略：针对信息密度差异大的模态（如视频/音频、图文）独立配置噪声/生成步长，兼顾生成质量与效率

  - 电商素材局部修改场景可复用「固定单模态约束另一模态」的编辑方案：比如固定商品实拍视频批量生成匹配旁白/配乐，或固定口播音频生成对应商品展示视频，无需全量重生成降本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有统一音视频生成编辑方法高度依赖稀缺的跨模态配对语料，大量算力浪费在单模态基础能力学习而非跨模态耦合；且共享噪声调度忽略模态间信息密度差异，也无法支持非对称跨模态生成/编辑任务。

### 方法关键点
1. 两阶段渐进式训练：先用单模态数据训练各模态分支的生成、编辑全能力，再用配对数据仅优化跨模态对应关系；
2. 模态解耦非对称调度：各模态基于共享时间步独立适配噪声调度，同时加入单模态为输入的子任务监督非对称配置，支持固定单模态编辑另一模态、推理后单分支自优化。

### 关键结果
单组权重即可覆盖文本引导联合生成、双向跨模态生成、指令引导编辑等多任务，各运行模式下性能均达到同期可比水平，无额外任务适配器开销
