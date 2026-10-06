---
title: 'ALoDLM: Adaptively Looped Diffusion Language Models'
title_zh: ALoDLM：自适应循环扩散语言模型
authors:
- Liancheng Fang
- Zhuowei Li
- Youngeun Kim
- Tianchen Zhao
- Rajat Koner
- Jiaye Wu
- Linghan Xu
- Xuanbai Chen
- Xiang Xu
- Zheng Zhang
affiliations:
- University of Illinois Chicago
- Amazon AGI
- Korea University
arxiv_id: '2610.04198'
url: https://arxiv.org/abs/2610.04198
pdf_url: https://arxiv.org/pdf/2610.04198
published: '2026-10-02'
collected: '2026-10-06'
category: LLM
direction: 扩散大语言模型 · 自适应推理加速
tags:
- Diffusion LLM
- Adaptive Computation
- Parallel Decoding
- Looped Transformer
- Inference Acceleration
one_liner: 在扩散语言模型中实现token级自适应循环计算，效果超同规模AR模型且吞吐量提升2.7倍
practical_value: '- 可复用token级自适应计算分配逻辑：在电商商品文案生成、搜索query改写场景中，给价格、规格、ID类高难度token分配更多计算资源，降低生成错误率

  - 参考深度感知KV cache优化方案：部署生成式推荐/Agent模型时，复用不同循环深度的KV缓存，降低推理延迟，提升高峰时段服务吞吐

  - 复用无预训练直接SFT的转换方案：快速将现有业务用自回归LLM改造为并行解码的扩散模型，降低生成模块的部署与训练成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
扩散语言模型（DLM）支持并行多token生成，推理速度显著优于自回归（AR）模型，但长期存在效果差于同规模AR模型的问题，核心原因是计算-难度不匹配：同一步去噪中不同token预测难度差异极大，但现有DLM给所有token分配相同的计算深度，算力浪费在易预测token上，难token得不到足够计算。
### 方法关键点
- 架构拆分：将Transformer拆分为Prelude（嵌入+前缀层）、Recurrent Core（中间循环层）、Coda（后缀层+双输出头：LMHead预测token分布、ExitGate输出停止概率）
- 内循环自适应计算：每步去噪中引入内循环，易预测token（熵低于阈值）提前提交为上下文，难token保留隐状态继续循环优化，通过ExitGate控制内循环停止时机
- 训练优化：将token退出深度作为隐变量推导条件NELBO目标，设计无偏梯度估计器与中间监督策略降低训练方差，无需继续预训练，直接基于Qwen3 backbone做SFT即可完成模型转换
### 关键结果
在11个涵盖推理、数学、代码的基准上测试，对比Qwen3 AR模型、LLaDA、WeDLM等SOTA DLM：1.7B版平均得分65.5，超过同规模AR的63.8；8B版平均得分80.3，超过同规模AR的78.5，比次优DLM WeDLM-8B高5.2分；GSM8K任务上，ALoDLM-8B精度与Qwen3-8B相当的情况下，吞吐量是vLLM部署Qwen3-8B的2.7倍，单token计算量比WeDLM-8B低13.6%，可通过调整阈值灵活平衡精度与速度。
### 核心结论
针对token粒度的计算资源动态分配，是同时提升扩散大语言模型效果与推理效率的核心可行路径
