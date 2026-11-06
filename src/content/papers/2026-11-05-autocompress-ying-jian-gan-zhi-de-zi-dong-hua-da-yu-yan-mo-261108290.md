---
title: 'AutoCompress: Automated Hardware-Guided Model Compression'
title_zh: AutoCompress：硬件感知的自动化大语言模型压缩框架
authors:
- Sheldon Liang
- Ali Taghibakhshi
- Saurav Muralidharan
- Sharath Turuvekere Sreenivas
- Ashwath Aithal
- Pavlo Molchanov
- Nima Tajbakhsh
affiliations:
- NVIDIA
arxiv_id: '2611.08290'
url: https://arxiv.org/abs/2611.08290
pdf_url: https://arxiv.org/pdf/2611.08290
published: '2026-11-05'
collected: '2026-11-06'
category: Training
direction: LLM压缩 · 硬件感知可微结构搜索
tags:
- LLM Pruning
- Differentiable NAS
- Hardware-aware
- Model Compression
- Knowledge Distillation
one_liner: 将硬件与服务引擎约束嵌入可微结构搜索，自动生成效果最优的异质性压缩LLM
practical_value: '- 端侧/边缘部署电商导购Agent、小流量LLM服务的团队，可直接复用该框架的端到端流程，输入硬件、延迟、内存约束即可自动生成适配的压缩模型，省去大量人工调优成本

  - 采用MoE架构的大推荐/大广告模型团队，可复用per-layer异质性裁剪思路，无需所有层保持统一宽度，相同吞吐量/内存约束下可提升模型效果0.5+个百分点

  - 做LLM部署成本评估时，可复用其服务引擎级的内存/延迟建模方法，纳入KV cache、运行时缓冲区、CUDA上下文等易遗漏开销，避免预估偏差导致上线故障

  - 用可微NAS做结构搜索的团队，可直接应用两个优化trick：router输出层零初始化并去掉warmup、MoE专家掩码加在选择后而非前，可降低10%+的蒸馏损失'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM剪枝框架大多针对参数量优化，但参数量与实际部署的延迟、吞吐量、内存占用无直接对应关系，后者受模型架构、业务负载、硬件、服务引擎共同影响。从业者需要手动反复调整压缩参数匹配部署约束，效率极低，且强制所有层采用统一维度的裁剪方式会浪费大量模型容量，难以在约束下取得最优效果。

### 方法关键点
- 四步自动化压缩流程：先针对目标硬件+服务引擎+业务负载构建延迟/内存代价模型，再基于激活重要性排序父模型权重初始化超网，然后联合训练结构router和超网，通过蒸馏损失+资源约束损失优化，最后提取最优结构再做蒸馏恢复精度
- 搜索空间同时覆盖全局维度（隐层大小、Mamba头数）和per-layer维度（专家数、FFN宽度、层删除开关），允许生成异质性架构，最大化有限容量的利用效率
- 代价模型直接从服务引擎的实际trace中提取每层latency、内存开销，纳入KV cache、运行时缓冲区、CUDA上下文等之前被忽略的开销，端到端预估误差低于3%

### 关键实验
在三类场景对比改进版Minitron++基线：RTX 5070端侧游戏NPC场景平均精度提升6.57个百分点，搜索token消耗减少2倍；RTX 5080本地编码Agent场景精度提升2.35个百分点，搜索token消耗减少3倍；H100数据中心场景精度提升0.57个百分点，搜索token消耗减少3.3倍。120B参数的Nemotron 3.5 Super可压缩到74B，单块B200即可支持128K上下文BF16推理，保留95%的基准测试分数。

**最值得记住的一句话**：参数量是模型部署成本的极差代理指标，相同参数量的模型在消费级GPU上延迟差可达35%，相同吞吐量的模型参数量差可达2.2倍。
